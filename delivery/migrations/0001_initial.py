# Generated by Django 4.1.3 on 2024-04-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackingNumber', models.CharField(max_length=10)),
                ('carrier', models.CharField(max_length=5)),
                ('senderStreet', models.CharField(max_length=10)),
                ('senderRegionalCode', models.CharField(max_length=10)),
                ('senderCity', models.CharField(max_length=255)),
                ('senderCountry', models.CharField(max_length=255)),
                ('receiverStreet', models.CharField(max_length=10)),
                ('receiverRegionalCode', models.CharField(max_length=10)),
                ('receiverCity', models.CharField(max_length=255)),
                ('receiverCountry', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('sku', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
