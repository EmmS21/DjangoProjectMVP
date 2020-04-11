from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError

from django.forms import ModelForm, Textarea, TextInput
from django.core.files.images import get_image_dimensions
from allauth.account.views import SignupForm
from classroom.models import Mentor 
from classroom.models import (Answer, Question, Student, StudentAnswer,
                              Subject, Mentor)

from django.contrib.auth import get_user_model
User = get_user_model()



class TeacherSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    linkedin = forms.URLField(max_length=200)
    address = forms.CharField(max_length=500)
    billing_name = forms.CharField(max_length=200)
    account_num = forms.IntegerField()
    bank_name = forms.CharField(max_length=50)
    branch_code = forms.IntegerField()

    def save(self,request, commit=True):
        user = super(TeacherSignUpForm, self).save(request) 
        user.is_teacher = True
        user.is_active = True 
        user.is_allow = False #custom active function. you can play with it or is_active
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        try:
            user_Name = str(user.email).split('@')[0]
            user.username = user_Name
        except:
            user.username = user.first_name

        user.save()
        mentor = Mentor.objects.get_or_create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            linkedin=self.cleaned_data['linkedin'],
            address=self.cleaned_data['address'],
            billing_name=self.cleaned_data['billing_name'],
            account_num=self.cleaned_data['account_num'],
            bank_name=self.cleaned_data['bank_name'],
            branch_code=self.cleaned_data['branch_code'],
        )
        return user

class StudentSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    def save(self,request, commit=True):
        user = super(StudentSignUpForm, self).save(request) 
        user.is_student = True
        user.is_active = True 
        user.is_allow = False
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        try:
            user_Name = str(user.email).split('@')[0]
            user.username = user_Name
        except:
            user.username = user.first_name
        user.save()
        mentor = Mentor.objects.get_or_create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return user



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')


class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer',)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')


#basic form
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# edit mentor payment details
class MentorPaymentForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('address', 'billing_name', 'account_num', 'bank_name', 'branch_code')


# basic form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     # student.email.add(*self.cleaned_data.get('email'))
    #     # student.firstname.add(*self.cleaned_data.get('firstname'))
    #     # student.lastname.add(*self.cleaned_data.get('lastname'))
    #     # student.phone.add(*self.cleaned_data.get('phone'))
    #     student.interests.add(*self.cleaned_data.get('interests'))
    #     return user


# class StudentInterestsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('interests', )
#         widgets = {
#             'interests': forms.CheckboxSelectMultiple
#         }
#
#edit mentor payment details
# class MentorPaymentForm(forms.ModelForm):
#     class Meta:
#         model = Mentor
#         fields = ('address', 'country', 'invoice_name', 'account_num', 'bank_name', 'branch_code')
