# Generated by Django 4.1.7 on 2023-03-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='Tour')),
                ('img', models.ImageField(upload_to='images', verbose_name='Tour Image')),
                ('price', models.PositiveBigIntegerField(verbose_name='Tour Price')),
            ],
        ),
        migrations.DeleteModel(
            name='Tours',
        ),
    ]