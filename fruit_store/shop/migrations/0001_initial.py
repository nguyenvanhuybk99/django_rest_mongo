# Generated by Django 2.2 on 2021-05-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('quantity_in_stock', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
