# Generated by Django 3.2.5 on 2021-07-16 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('actor', 'Actor'), ('director', 'Director'), ('writer', 'Writer')], max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='person_profile_image')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
    ]
