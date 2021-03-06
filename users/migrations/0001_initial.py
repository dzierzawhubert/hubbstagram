# Generated by Django 3.1.4 on 2021-03-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sec_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=120)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
    ]
