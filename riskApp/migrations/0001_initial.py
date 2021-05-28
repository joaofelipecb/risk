# Generated by Django 3.2.3 on 2021-05-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accountReceivable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=11)),
                ('probability', models.FloatField()),
                ('dueDate', models.DateTimeField()),
            ],
        ),
    ]
