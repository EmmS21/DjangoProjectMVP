from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return "Profile of user{}".format(self.user)




class Mentor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(max_length=200,null=True,blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='media', default='default.jpg')
    address = models.CharField(max_length=500, null=True, blank=True)
    billing_name = models.CharField(max_length=200, null=False, blank=False)
    account_num = models.IntegerField(default=1234)
    bank_name = models.CharField(max_length=50, null=False)
    branch_code = models.IntegerField(default=1234)

    def __str__(self):
        return "Profile of user {}".format(self.user)


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE )
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, )