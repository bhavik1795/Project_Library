# Generated by Django 4.0.4 on 2022-05-20 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_returnbook_issued_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnbook',
            name='issued_date',
        ),
    ]
