# Generated by Django 4.0.4 on 2022-05-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_issu_id_returnbook_issuebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returnbook',
            name='issuebook',
            field=models.IntegerField(),
        ),
    ]
