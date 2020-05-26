from django.contrib.auth.models import User
from django.db import models

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
        verbose_name='Специальность'
    )

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'

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


class Users(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь'
    ),
    email = models.EmailField(
        max_length=200,
        verbose_name='Почта'
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name='Телефон'
    )
    group = models.ForeignKey(
        Groups,
        on_delete=models.DO_NOTHING,
        verbose_name='Группа'
    )
    FIO = models.CharField(
        max_length=200,
        verbose_name='ФИО'
    )

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.FIO


class Performance(models.Model):
    FORMS = (
        ('exam', 'Экзамен'),
        ('offset', 'Зачет')
    )

    FIO = models.ForeignKey(
        Users,
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
        return self.FIO