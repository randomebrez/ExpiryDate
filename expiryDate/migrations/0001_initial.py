# Generated by Django 3.0.5 on 2020-04-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField(verbose_name='Référence produit')),
                ('expiryDate', models.DateTimeField(verbose_name="Date d'expiration")),
            ],
            options={
                'verbose_name': 'reference',
                'ordering': ['expiryDate'],
            },
        ),
    ]
