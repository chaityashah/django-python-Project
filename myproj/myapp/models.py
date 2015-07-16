from django.db import models
from django.contrib.auth.models import User
#from _overlapped import NULL

# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    student_id = models.IntegerField() 
    UNDERGRAD = 1
    MSC = 2
    PHD = 3
    LEVEL_CHOICES = (
        (UNDERGRAD, 'Undergrad'),
        (MSC, 'Masters'),
        (PHD, 'PhD')
    )
    
    level = models.IntegerField(default=UNDERGRAD, choices=LEVEL_CHOICES)
    
    def list_of_course(self):
                return ', '.join([course.title for course in self.course_set.all()])
    def __str__(self):
                return '%s %s' % (self.user.first_name, self.user.last_name)
    '''
    level = models.IntegerField(default=UNDERGRAD, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
 #   def list_of_course(self):
    def __courselist__(self):
        return [course.title for course in course.object.all()] 
    def course(self):
        return Course.objects.filter(student=self)

    def course(self):
        return ourse.objects.filter(student=self)

    def list_of_course(self):
        return [course.title for course in course.objects.all()]
'''    
class Instructor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    webpage = models.URLField()
    office = models.CharField(max_length=50, default='EH120')
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name 

class Author(models.Model): 
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    #age = models.IntegerField( default = None)
    birthday = models.DateField(default = '1991-01-31')
    #city = models.CharField(max_length=20)
    country = models.CharField(max_length=20, default = 'Canada')
    
    def __str__(self):
        return self.fname

class Book(models.Model): 
    title = models.CharField(max_length=100)
    numpages = models.IntegerField()
    in_stock = models.BooleanField(default = 1)
    authors = models.ManyToManyField(Author)
    pubyear = models.IntegerField( default = None)
    def __str__(self):
        return self.title

class Course(models.Model):
    course_no = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    textbook = models.ForeignKey(Book)
    instructor=models.ForeignKey(Instructor, null=True)
    student=models.ManyToManyField(Student)
    
    def __str__(self):
        return str(self.course_no)

class Topic(models.Model):
    subject = models.CharField(max_length=100, unique=True)   
    intro_course = models.BooleanField(default=True)
    NO_PREFERENCE = 0
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    TIME_CHOICES = (
        (0, 'No preference'),
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Evening')
    )
    time = models.IntegerField(default=0, choices=TIME_CHOICES)
    num_responses = models.IntegerField(default=0)
    avg_age =models.IntegerField(default=20)
    
    def __str__(self):
        return self.subject
    