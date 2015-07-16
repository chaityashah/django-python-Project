from django.contrib import admin
from myapp.models import Book, Author, Course, Topic, Instructor, Student
# Register your models here.
from myapp.models import Book, Author, Course, Topic, Student, Instructor

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'courses_using_book')

    def courses_using_book(self, obj):
        return ', '.join([course.title for course in obj.course_set.all()])

class AuthorAdmin(admin.ModelAdmin):
    fields = [('fname', 'lname'), 'birthday' ]
    list_display = ('fname', 'lname', 'country')

class CourseAdmin(admin.ModelAdmin):
    fields = [('course_no', 'title', 'textbook'), ('instructor', 'student') ]
    list_display = ('course_no', 'title', 'teacher')
     
    def teacher(self, obj):
        return ', '.join([instructor.user.first_name+ " "+instructor.user.last_name for instructor in Instructor.objects.filter(course=obj)])
        #return obj.course_set.all()

class CourseInline(admin.StackedInline):
    fields=[('course_no', 'title')]
    model=Course
    
class InstructorAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    list_display=('user', 'office')
    fieldsets=[
               ('Personal_Info',{'fields':['user']}), 
               ('Other Info', {'fields':['office', 'webpage']}),]


def change_level(modeladmin,request,queryset):
        queryset.update(level =3)
        change_level.shortDescription="Level Changed!!"
    
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'list_of_course')
    actions=[change_level]
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic)
admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
'''
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Student)
admin.site.register(Instructor)
'''