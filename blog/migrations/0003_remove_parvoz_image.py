# Generated by Django 5.0.6 on 2024-05-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_parvoz_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parvoz',
            name='image',
        ),
    ]