# Generated by Django 2.0.4 on 2018-06-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_menu_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='count',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tot_price',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
