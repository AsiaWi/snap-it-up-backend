# Generated by Django 4.2.8 on 2024-01-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_advert_contact_dets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='item_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]