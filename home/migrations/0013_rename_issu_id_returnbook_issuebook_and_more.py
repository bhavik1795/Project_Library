# Generated by Django 4.0.4 on 2022-05-20 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_returnbook_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='returnbook',
            old_name='issu_id',
            new_name='issuebook',
        ),
        migrations.AddField(
            model_name='returnbook',
            name='student_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]