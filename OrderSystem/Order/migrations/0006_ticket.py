# Generated by Django 2.0.4 on 2018-06-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_auto_20180620_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tot_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('o_id', models.ForeignKey(on_delete=True, to='Order.Order')),
            ],
        ),
    ]