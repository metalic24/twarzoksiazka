# Generated by Django 3.2.9 on 2021-12-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej_log', '0005_user_details_friends_alter_user_details_profile_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('send', 'send')], max_length=8),
        ),
    ]