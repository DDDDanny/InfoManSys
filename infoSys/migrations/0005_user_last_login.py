# Generated by Django 2.1.3 on 2019-01-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoSys', '0004_auto_20181202_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, max_length=6, verbose_name='最后登录时间'),
        ),
    ]
