from django import forms
from myapp.models import Topic
from django.forms.widgets import RadioSelect, Textarea
class TopicForm(forms.ModelForm):
    class Meta:
        model= Topic
        fields=['subject', 'intro_course', 'time', 'avg_age']
        widgets={'time': RadioSelect}
        labels={
                'time': 'Preferred Time',
                'avg_age': 'What is your age',
                'intro_course':'This should be an introductory level course'
                }
class InterestForm(forms.Form):
    interested= forms.TypedChoiceField(widget=RadioSelect, coerce=int, choices= ((0, 'No '),(1, 'Yes')))
    age=forms.IntegerField(initial=20)
    comments=forms.CharField(widget=Textarea,label='Additional Comments',)