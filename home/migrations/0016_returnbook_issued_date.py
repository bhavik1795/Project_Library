# Generated by Django 4.0.4 on 2022-05-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_issuebook_returnbook_issuebook_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnbook',
            name='issued_date',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='home.issuebook'),
            preserve_default=False,
        ),
    ]
