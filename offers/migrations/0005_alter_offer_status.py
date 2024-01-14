# Generated by Django 4.2.8 on 2024-01-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_alter_offer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('SOLD', 'Sold')], default='PENDING', max_length=20),
        ),
    ]