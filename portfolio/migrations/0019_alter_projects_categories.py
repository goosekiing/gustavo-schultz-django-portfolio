# Generated by Django 4.1.13 on 2024-05-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_websiteinfo_contact_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='portfolio.category'),
        ),
    ]