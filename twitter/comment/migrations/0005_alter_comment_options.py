# Generated by Django 5.1.7 on 2025-03-15 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-sent_date']},
        ),
    ]
