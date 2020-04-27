# Generated by Django 3.0.3 on 2020-04-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=25)),
                ('fax', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('smtpserver', models.CharField(max_length=50)),
                ('smtpemail', models.CharField(max_length=50)),
                ('smtppassword', models.CharField(max_length=50)),
                ('smtpport', models.CharField(max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('aboutus', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Active'), ('False', 'Inactive')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
