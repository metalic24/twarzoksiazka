# Generated by Django 4.0 on 2021-12-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej_log', '0012_alter_user_details_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('send', 'send')], max_length=8),
        ),
    ]