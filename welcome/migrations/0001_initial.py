# Generated by Django 4.2.18 on 2025-01-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('contact_info', models.TextField()),
                ('is_valid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
