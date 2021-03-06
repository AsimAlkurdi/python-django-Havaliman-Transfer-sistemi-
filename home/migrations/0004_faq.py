# Generated by Django 3.2 on 2021-06-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=150)),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('True', 'YES'), ('False', 'NO')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
