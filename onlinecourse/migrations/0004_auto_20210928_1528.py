# Generated by Django 3.1.3 on 2021-09-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20210928_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
    ]
