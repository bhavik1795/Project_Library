# Generated by Django 4.0.4 on 2022-05-19 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_issued_id_returnbook_issued_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnbook',
            name='issued_date',
        ),
        migrations.AlterField(
            model_name='returnbook',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.issuebook'),
        ),
    ]
