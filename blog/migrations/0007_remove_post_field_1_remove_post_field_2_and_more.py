# Generated by Django 4.2.13 on 2024-05-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_field_2_post_field_3_alter_post_field_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
    ]