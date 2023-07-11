# Generated by Django 4.2.3 on 2023-07-11 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_alter_showing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='address',
            field=models.CharField(help_text='(Street, City, State, Zip)', max_length=100),
        ),
        migrations.AlterField(
            model_name='showing',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]