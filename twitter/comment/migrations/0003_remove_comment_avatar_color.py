# Generated by Django 5.1.7 on 2025-03-15 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_avatar_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='avatar_color',
        ),
    ]
