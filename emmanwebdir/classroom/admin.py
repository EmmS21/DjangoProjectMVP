from django.contrib import admin

# Register your models here.
from .models import Answer,Mentor,Question,Quiz,Student,StudentAnswer,Subject,TakenQuiz

admin.site.register(Answer)
admin.site.register(Mentor)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Student)
admin.site.register(StudentAnswer)
admin.site.register(Subject)
admin.site.register(TakenQuiz)
