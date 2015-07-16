'''
Created on Jun 2, 2015

'''
from django.conf.urls import patterns, url
from myapp import views
from myapp.models import Course
from django.conf.urls import patterns, url
from myapp.genviews import IndexView, CreateView, DetailView
from myapp import genviews
'''
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^detail/(?P<course_no>\d{3})$', views.detail, name='detail'),
        url(r'^topic/$',views.topics,name='topic'),
        url(r'^addtopic', views.addtopic, name='addtopic'),
        url(r'^topics/(?P<topic_id>\d+)$', views.topicdetail, name='topicdetail'),
        url(r'^user_logout', views.user_logout, name='user_logout'),
        url(r'^user_login', views.user_login, name='user_login'),
        url(r'^mycourses', views.mycourses, name='mycourses'),
        )
'''
urlpatterns = patterns('',
        url(r'^$', genviews.IndexView.as_view(),name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^(?P<course_no>\d{3})$', genviews.DetailView.as_view(), name='detail'),
        url(r'^topic/$',views.topics,name='topic'),
        url(r'^addtopic/$',genviews.CreateView.as_view(),name='addtopic'),
        #url(r'^addtopic', views.addtopic, name='addtopic'),
        url(r'^topics/(?P<topic_id>\d+)$', views.topicdetail, name='topicdetail'),
        url(r'^topicdetail/(?P<topic_id>\d+)$', views.topicdetail, name='topicdetail'),
        url(r'^detail/(?P<course_no>\d{3})$', DetailView.as_view(model = Course, template_name='myapp/detail.html')),
        url(r'^user_logout',views.user_logout,name='user_logout'),
        url(r'^user_login',views.user_login,name='user_login'),
        url(r'^mycourses',views.mycourses,name='mycourses'),
        )