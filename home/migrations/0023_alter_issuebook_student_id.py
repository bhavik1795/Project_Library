# Generated by Django 4.0.4 on 2022-05-21 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_issuebook_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
