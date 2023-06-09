# Generated by Django 4.1.7 on 2023-03-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='First Tour')),
                ('img', models.ImageField(upload_to='images', verbose_name='Tour Image')),
                ('price', models.PositiveBigIntegerField(verbose_name='Tour Price')),
            ],
        ),
    ]
