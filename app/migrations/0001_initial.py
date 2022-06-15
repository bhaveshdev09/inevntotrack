# Generated by Django 3.2.2 on 2022-06-09 06:49

import app.validators
import django.contrib.auth.password_validation
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SKUItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_name', models.CharField(default='', max_length=100, unique=True)),
                ('sku_qty', models.IntegerField(default=0)),
                ('sku_rate', models.FloatField(default=0.0)),
                ('sku_serial_no', models.CharField(blank=True, default='', max_length=200, null=True, unique=True)),
                ('sku_barcode_image', models.ImageField(default='backup/', upload_to='barcode/')),
                ('sku_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70, validators=[app.validators.validate_name])),
                ('email', models.EmailField(default='', max_length=70, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('contact', models.CharField(default='', max_length=10, unique=True, validators=[app.validators.validate_contact])),
                ('password', models.CharField(default='', max_length=200, validators=[django.contrib.auth.password_validation.validate_password])),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(default='', max_length=200)),
                ('invoice_party_name', models.CharField(default='', max_length=200)),
                ('invoice_sales_ledger', models.CharField(default='', max_length=200)),
                ('invoice_date', models.DateField(auto_now_add=True)),
                ('invoice_item_qty', models.IntegerField(default=0.0)),
                ('invoice_item_rate', models.FloatField(default=0.0)),
                ('invoice_item_amount', models.FloatField(default=0.0)),
                ('invoice_item_total_scan', models.IntegerField(default=0.0)),
                ('invoice_total_qty', models.IntegerField(default=0)),
                ('invoice_total_amount', models.FloatField(default=0.0)),
                ('invoice_item_scanned_status', models.BooleanField(default=False)),
                ('invoice_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.skuitems')),
            ],
        ),
        migrations.CreateModel(
            name='ByPassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bypass_datetime', models.DateTimeField(auto_now_add=True)),
                ('bypass_against_sku_name', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bypass_against_sku_name', to='app.skuitems')),
                ('bypass_invoice_no', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='app.invoice')),
                ('bypass_sku_name', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='app.skuitems')),
            ],
        ),
    ]
