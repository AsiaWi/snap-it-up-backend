# Generated by Django 4.2.8 on 2023-12-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_advert_categories_alter_advert_payment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.ImageField(default='../upload.png_t8qvp6', upload_to='images/'),
        ),
    ]
