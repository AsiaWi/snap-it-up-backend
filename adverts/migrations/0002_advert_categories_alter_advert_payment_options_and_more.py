# Generated by Django 4.2.8 on 2023-12-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='categories',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Electronics', 'Electronics'), ('HomeDeco/Furniture', 'HomeDeco/Furniture'), ('Games', 'Games'), ('Books', 'Books'), ('Beauty/Personal Care', 'Beauty/Personal Care'), ('Home appliances', 'Home appliances'), ('Vintage', 'Vintage'), ('Baby', 'Baby'), ('Pets', 'Pets'), ('Sports', 'Sports'), ('Other', 'Other')], default='Clothing', max_length=100),
        ),
        migrations.AlterField(
            model_name='advert',
            name='payment_options',
            field=models.CharField(choices=[('Cash or Paypal', 'Cash or Paypal'), ('Cash only', 'Cash only'), ('PayPal only', 'PayPal only')], default='Cash or Paypal', max_length=20),
        ),
        migrations.AlterField(
            model_name='advert',
            name='shippment_options',
            field=models.CharField(choices=[('Collection or delivery', 'Collection or delivery'), ('Collection Only', 'Collection Only'), ('Delivery Only', 'Delivery Only')], default='Collection or delivery', max_length=50),
        ),
    ]