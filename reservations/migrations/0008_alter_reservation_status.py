# Generated by Django 3.2 on 2021-06-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20210620_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
    ]
