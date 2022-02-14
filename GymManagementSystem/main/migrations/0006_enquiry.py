# Generated by Django 4.0.1 on 2022-02-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('detail', models.TextField()),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]