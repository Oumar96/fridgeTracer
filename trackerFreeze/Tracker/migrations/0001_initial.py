# Generated by Django 2.1.5 on 2019-01-27 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inside_Freeze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField()),
                ('amount', models.FloatField(default=None)),
                ('expire_date', models.DateTimeField()),
            ],
        ),
    ]
