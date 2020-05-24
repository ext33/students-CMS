# Generated by Django 3.0.6 on 2020-05-24 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=200, verbose_name='Группа')),
                ('course', models.IntegerField(null=True, verbose_name='Курс')),
                ('direction', models.CharField(max_length=200, null=True, verbose_name='Специальность')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300, verbose_name='Предмет')),
                ('teacher', models.CharField(max_length=200, verbose_name='Преподаватель')),
                ('course', models.IntegerField(verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, verbose_name='Почта')),
                ('telephone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('FIO', models.CharField(max_length=200, verbose_name='ФИО')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CMSWeb.Groups', verbose_name='Группа')),
            ],
        ),
    ]
