from django.urls import include, path,re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users.views import (
            TeacherRegistrationView, 
            StudentRegistrationView, 
            SignUpView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignUpView.as_view(), name='account_signup'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'), #duplicate because in most templtes we use signup namespace
    path('accounts/signup/teacher/', TeacherRegistrationView.as_view(), name='teacher_signup'),
    path('accounts/signup/student/', StudentRegistrationView.as_view(), name='student_signup'),
    path('accounts/', include('allauth.urls')),
    path('', include('classroom.urls')),
]

admin.site.site_header = "TheGradientBoost"
admin.site.site_title = f"TheGradientBoost Admin Portal"
admin.site.index_title = f"Welcome to TheGradientBoost"


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)