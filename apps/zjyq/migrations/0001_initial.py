# Generated by Django 3.0.6 on 2020-06-13 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('de_addr', models.CharField(max_length=20)),
                ('hot', models.BooleanField()),
                ('danger_area', models.BooleanField()),
                ('cough', models.BooleanField()),
                ('other_cases', models.CharField(max_length=20, null=True)),
                ('refer_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]