# Generated by Django 2.2.3 on 2021-06-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('nitrogen', models.IntegerField()),
                ('lk', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
    ]
