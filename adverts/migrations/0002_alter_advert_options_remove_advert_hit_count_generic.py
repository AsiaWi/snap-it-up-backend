# Generated by Django 4.2.8 on 2023-12-13 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='advert',
            name='hit_count_generic',
        ),
    ]
