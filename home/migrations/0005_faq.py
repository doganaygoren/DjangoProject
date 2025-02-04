# Generated by Django 3.0.3 on 2020-06-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.IntegerField()),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Active'), ('False', 'Inactive')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
