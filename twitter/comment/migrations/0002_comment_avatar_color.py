# Generated by Django 5.1.7 on 2025-03-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar_color',
            field=models.CharField(blank=True, default='black', max_length=20, null=True),
        ),
    ]
