# Generated by Django 3.0.3 on 2020-02-12 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=100)),
                ('on_sale', models.BooleanField(blank=True, null=True)),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('percent_off', models.DecimalField(blank=True, decimal_places=1, max_digits=30, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=0, max_digits=30, null=True)),
                ('bought_counter', models.DecimalField(decimal_places=0, default=0, max_digits=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]