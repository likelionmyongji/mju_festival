# Generated by Django 2.2.1 on 2019-05-11 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lost_property', '0006_auto_20190510_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]