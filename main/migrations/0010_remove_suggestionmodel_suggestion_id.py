# Generated by Django 4.2.6 on 2023-10-31 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_suggestionmodel_suggestion_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestionmodel',
            name='suggestion_id',
        ),
    ]