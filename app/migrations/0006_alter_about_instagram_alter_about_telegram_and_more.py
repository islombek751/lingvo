# Generated by Django 4.0.1 on 2022-01-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_about_banner_contact_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='instagram',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='about',
            name='telegram',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='about',
            name='twitter',
            field=models.CharField(max_length=150),
        ),
    ]