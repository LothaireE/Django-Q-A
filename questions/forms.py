from django import forms
from django.contrib.auth import get_user_model
from .models import Question, Answer

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_passord(self):
        cl_data = self.cleaned_data
        if cl_data['password'] != cl_data['password2']:
            raise forms.ValidationError('Passwords do not match')

        return cl_data['password2']

class QuestionRegistrationForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body')

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('description',)


class QuestionUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ('title', 'body')

class AnswerUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ('description',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email')




