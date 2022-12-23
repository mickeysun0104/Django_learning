# Generated by Django 4.1.4 on 2022-12-23 02:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20, verbose_name='姓名')),
                ('cSex', models.CharField(choices=[('M', '男'), ('F', '女')], default='', max_length=1, verbose_name='性別')),
                ('cBirthday', models.DateField(verbose_name='生日')),
                ('cEmail', models.EmailField(blank=True, default='', max_length=100, verbose_name='Email')),
                ('cPhone', models.CharField(blank=True, default='', max_length=15, verbose_name='手機')),
                ('cAddr', models.CharField(blank=True, default='', max_length=255, verbose_name='地址')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='最後修改日期')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
            ],
        ),
    ]
