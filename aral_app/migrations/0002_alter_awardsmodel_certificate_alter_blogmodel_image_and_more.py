# Generated by Django 5.0.4 on 2024-04-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aral_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardsmodel',
            name='certificate',
            field=models.ImageField(upload_to='award_images/'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='blog_photos/'),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='image',
            field=models.ImageField(upload_to='portfolio/'),
        ),
        migrations.AlterField(
            model_name='servicesmodel',
            name='icon',
            field=models.ImageField(upload_to='icons/'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='image',
            field=models.ImageField(upload_to='team_images/'),
        ),
    ]
