from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser



class Profile(AbstractUser):
  email = models.EmailField(_('email address'), unique=True)

class Course(models.Model):
  name = models.CharField(max_length=250, verbose_name='Название курса')
  price = models.IntegerField(verbose_name='Цена', default=0)
  students = models.ManyToManyField(Profile, blank=True, related_name='courses')

  def __str__(self):
    return self.name

class CourseParagraph(models.Model):
  course = models.ForeignKey(Course, related_name='paragraphs', on_delete=models.CASCADE)
  text = models.CharField(max_length=255)

  def __str__(self):
    return self.text

"""
Доступ к соДержимому курсов
return qs.filter(students__in=[self.request.user])

related_name

"""


class ContactMessage(models.Model):
  KINDS = (
    ('t', 'Telegram'),
    ('i', 'Instagram'),
    ('w', 'WhatsUp'),
    ('m', 'Mail')
  )

  name = models.CharField(max_length=250, verbose_name='Имя')
  contact = models.CharField(max_length=1, choices=KINDS, default='t', verbose_name='Telegram/WhatsApp/Istagram/Mail')
  contact_name = models.CharField(max_length=250, verbose_name='nickname')
  message = models.TextField(verbose_name='Сообщение')
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'Message'
    ordering = ['-created']

  def __str__(self):
    return self.message

