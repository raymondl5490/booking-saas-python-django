# Generated by Django 3.2.10 on 2022-01-11 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20220111_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectformdefault',
            name='multiple',
        ),
    ]
