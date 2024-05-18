# Generated by Django 4.1.13 on 2024-05-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_project_name_projects_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('picture', models.ImageField(blank=True, upload_to='images/about/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/projects/%Y/%m/%d'),
        ),
    ]