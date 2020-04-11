from django.contrib.auth.models import AbstractBaseUser,    BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.conf import settings
from django.db.models.signals import post_save, pre_save


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, default='abc', null=True, blank=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_allow = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
  
    def __unicode__(self):
      return u'%s' % self.email


    def get_absolute_url(self):
        return f"/users/{self.pk}/"




def post_save_receiver(sender, instance, created, **kwargs):
    if instance.username =='abc' or instance.username is None:
      user_Name = str(instance.email).split('@')[0]
      instance.username = user_Name

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)



def send_mail_toadmin(user):
    site_url = f'{settings.C_SITE_URL}/admin/users/user/{user.pk}/change/'
    subject = f'User signup request for approval | {user}'
    msg = f'Here is link: to approve user \n {site_url}'
    from_send = 'emmanuel@thegradientboost.com'
    to_send = ['emmanuel@thegradientboost.com']
    send_mail(subject, msg, from_send, to_send, fail_silently=False,)


@receiver(user_signed_up)
def registration_callback(user: User, **kwargs: dict) -> None:
    send_mail_toadmin(user)

