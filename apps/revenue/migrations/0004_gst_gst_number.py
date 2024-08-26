# Generated by Django 4.2.14 on 2024-08-17 12:58

from django.db import migrations
from ..models import GST

def create(apps, schema_editor):
    GST.objects.create(percent=18)

class Migration(migrations.Migration):

    dependencies = [
        ("revenue", "0003_auto_20240816_2117"),
    ]

    operations = [migrations.RunPython(create)]