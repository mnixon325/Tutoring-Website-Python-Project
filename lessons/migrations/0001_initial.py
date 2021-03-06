# Generated by Django 2.2.6 on 2019-12-18 03:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tutor', models.CharField(max_length=120)),
                ('student', models.CharField(max_length=120)),
                ('completed', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.CharField(blank=True, default='Python!', max_length=120)),
            ],
        ),
    ]
