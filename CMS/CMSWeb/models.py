from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class Groups(models.Model):
    group = models.CharField(
        max_length=200,
        default='-',
        verbose_name='Группа'
    )
    course = models.CharField(
        max_length=2,
        default='-',
        verbose_name='Курс'
    )
    direction = models.CharField(
        null=True,
        max_length=200,
        default='-',
        verbose_name='Специальность'
    )

    class Meta:
        verbose_name = 'Учебные группы'
        verbose_name_plural = 'Учебные группы'

    def __str__(self):
        return self.group


class Subject(models.Model):
    subject = models.CharField(
        max_length=300,
        verbose_name='Предмет'
    )
    teacher = models.CharField(
        max_length=200,
        verbose_name='Преподаватель'
    )
    course = models.IntegerField(
        verbose_name='Курс'
    )

    class Meta:
        verbose_name = 'Предметы'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.subject


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name='Телефон'
    )
    group = models.ForeignKey(
        Groups,
        on_delete=models.DO_NOTHING,
        verbose_name='Группа',
    )
    FIO = models.CharField(
        max_length=200,
        verbose_name='ФИО'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.FIO


class Performance(models.Model):
    FORMS = (
        ('Экзамен', 'Экзамен'),
        ('Зачет', 'Зачет')
    )
    FIO = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING,
        verbose_name='ФИО студента'
    )
    group = models.ForeignKey(
        Groups,
        on_delete=models.DO_NOTHING,
        verbose_name='Группа'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.DO_NOTHING,
        verbose_name='Предмет'
    )
    mark = models.CharField(
        max_length=3,
        verbose_name='Оценка'
    )
    reporting_form = models.CharField(
        max_length=20,
        choices=FORMS,
        verbose_name='Форма отчетности'
    )
    date = models.DateField(
        null=True,
        verbose_name='Дата'
    )

    class Meta:
        verbose_name = 'Успеваемость'
        verbose_name_plural = 'Успеваемость'

    def __str__(self):
        return str(self.FIO)
