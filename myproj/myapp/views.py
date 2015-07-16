from django.shortcuts import render, get_object_or_404
# Import necessary classes
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from myapp.models import Course, Book, Author, Topic, Student, Instructor
from django.shortcuts import get_object_or_404
from myapp.forms import TopicForm, InterestForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.template import RequestContext 
from django.template import RequestContext 
from datetime import datetime

# Create your views here.
auth = User.objects.all()

def index(request):        
    # This is your index view function
    
    # Access db to get list of courses. limit 10
   courselist = Course.objects.all()[:10]        
   response = HttpResponse()        
   # Create empty response object
   
   #Send list of courses to template file
   return render_to_response('myapp/index.html', {'courselist': courselist,'auth':auth, 'user':request.user})

   # For each course, create a str to write to response
   '''
   for course in courselist:
        para = '<p>' + str(course) + '</p>'      
        # This is the new string response.write(para) # Add each str as a <p> to response obj
        response.write(para)
   #return response
    '''
'''
def about(request):
    return render_to_response('myapp/about.html', {'user':request.user})
    #return HttpResponse("This APP let you view and select courses to register in.")
'''
def about(request):
    '''
    request.session.set_test_cookie()
    '''
    c=RequestContext(request)
    visits = int(request.COOKIES.get('visits', '0'))
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            response =render_to_response('myapp/about.html',{'visits':visits+1},c)
            response.set_cookie('visits', visits+1)
            response.set_cookie('last_visit', datetime.now())
    else:
        response =render_to_response('myapp/about.html',{'visits':visits+1},c)
        response.set_cookie('visits', visits+1)
        response.set_cookie('last_visit', datetime.now())
    
    return response
@login_required
def detail(request,course_no):
    #courselist1=Course.objects.all()[:10]
    a = get_object_or_404(Course,course_no=course_no)
    #response=HttpResponse()
    '''
    for course in courselist1:
        if((int(course_no) == int(course.course_no))):
                   
            para = '</p>'+'<br>'+str(course.course_no)+'<br>'+str(course.title)+'<br>'+str(course.textbook)+'</p>'
            response.write(para)
    return response
    '''
    return render_to_response('myapp/detail.html', {'course':a,'auth':auth,'user':request.user})

def topics(request):
    topiclist = Topic.objects.all()[:10]
    return render(request, 'myapp/topic.html', {'topiclist':topiclist,'auth':auth,'user':request.user})

def addtopic(request):
    topiclist = Topic.objects.all()
    if request.method=='POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses=1
            topic.save()
            return HttpResponseRedirect(reverse('myapp:topic'))
    else:
        form=TopicForm()
    return render(request, 'myapp/addtopic.html', {'form':form, 'topiclist':topiclist,'auth':auth,'user':request.user})

def topicdetail(request, topic_id):
    topic= get_object_or_404(Topic, id=topic_id)
    if request.method=='POST':
        form= InterestForm(request.POST)
        
        if form.is_valid():
            if (form.cleaned_data['interested']== 1):
                print("hello!")
                a=form.cleaned_data['age']
                topic.avg_age=(topic.avg_age*topic.num_responses)
                topic.num_responses+=1
                topic.avg_age=(topic.avg_age+a)/topic.num_responses
                topic.save()
        return HttpResponseRedirect(reverse('myapp:topic'))
    else:
        form=InterestForm()
        return render(request, 'myapp/topicdetail.html', {'form':form, 'topic':topic,'auth':auth, 'user':request.user})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) 
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.') 
    else:
        return render(request, 'myapp/login.html', {'user':request.user})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:index')))
'''
@login_required
def mycourses(request):
    student=hasattr(request.user, 'student')
    if student:
        courselist = Course.objects.filter(student__user=request.user)
        response = HttpResponse()        # Create empty response object
        template='myapp/index.html'
        return render_to_response(template, {'courselist': courselist,'user':request.user},)
    for course in courselist:
        para = '<p>' + str(course) + '</p>'      # This is the new string         
        response.write(para) # Add each str as a <p> to response obj
        return response    
    else:
        return HttpResponse("You are not a student.")
'''
@login_required
def mycourses(request):
    stu=Student.objects.filter(user=request.user)
    
    try:
        courselist=Course.objects.filter(student=stu)
    except ValueError:
        print()
    
    message="You are not a student!"  
    
    return render(request,'myapp/mycourses.html' , {'user':request.user, 'courselist': courselist, 'message': message }, )