# Generated by Django 3.1.4 on 2021-03-26 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20210323_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprofile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='users/profile_pictures'),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('TM', 'Trans Male'), ('TF', 'Trans Female'), ('Q', 'Queer'), ('F', 'Genderfluid'), ('AT', 'Attack Helicopter'), ('D', 'Dog')], max_length=120),
        ),
        migrations.CreateModel(
            name='CreatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='default.jpg', upload_to='users/images')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
