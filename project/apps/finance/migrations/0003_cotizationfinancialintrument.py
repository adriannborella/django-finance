# Generated by Django 3.2.4 on 2021-07-02 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20210701_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='CotizationFinancialIntrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotization', models.FloatField()),
                ('date', models.DateField()),
                ('fin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.financialinstrument')),
            ],
        ),
    ]