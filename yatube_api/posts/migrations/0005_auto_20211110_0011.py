# Generated by Django 2.2.16 on 2021-11-09 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211110_0004'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_following',
        ),
    ]
