# Generated by Django 4.0 on 2021-12-28 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rej_log', '0002_userprofile_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='profile_pic/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('surr_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rej_log.userprofile')),
            ],
        ),
    ]
