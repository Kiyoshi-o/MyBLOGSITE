# Generated by Django 3.1.5 on 2021-01-18 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20210115_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userProfile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
