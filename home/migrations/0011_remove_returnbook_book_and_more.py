# Generated by Django 4.0.4 on 2022-05-20 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_returnbook_book_returnbook_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='returnbook',
            name='issuebook_id',
        ),
        migrations.RemoveField(
            model_name='returnbook',
            name='student_id',
        ),
        migrations.AddField(
            model_name='returnbook',
            name='issu_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='home.issuebook'),
            preserve_default=False,
        ),
    ]
