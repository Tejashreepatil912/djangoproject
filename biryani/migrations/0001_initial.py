# Generated by Django 3.1.7 on 2021-04-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'biryani_contact',
            },
        ),
    ]
