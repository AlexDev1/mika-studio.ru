# Generated by Django 3.1.7 on 2021-04-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_auto_20210412_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priceservices',
            options={'verbose_name': 'Прайс', 'verbose_name_plural': 'Прайсы'},
        ),
        migrations.AddField(
            model_name='priceservices',
            name='time',
            field=models.CharField(default='с 9.00 до 21.00', help_text='с 9.00 до 21.00', max_length=100, verbose_name='Время'),
        ),
    ]
