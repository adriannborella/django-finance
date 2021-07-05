# Generated by Django 3.2.4 on 2021-07-02 23:45

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20210702_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('ARS', 'ARS $'), ('USD', 'U$D')], default='ARS', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='ARS', max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.FloatField(default=0, verbose_name='Qnt'),
        ),
    ]