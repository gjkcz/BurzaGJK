# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 21:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_offer_will_be_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abstractoffer',
            options={'verbose_name': 'abstraktní nabídka', 'verbose_name_plural': 'abstraktní nabídky'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'kniha', 'verbose_name_plural': 'knihy'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': 'nabídka', 'verbose_name_plural': 'nabídky'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'uživatel', 'verbose_name_plural': 'uživatelé'},
        ),
        migrations.AddField(
            model_name='offer',
            name='buyer_complete',
            field=models.DateField(blank=True, null=True, verbose_name='Transakce Proběhla'),
        ),
        migrations.AddField(
            model_name='offer',
            name='vendor_complete',
            field=models.DateField(blank=True, null=True, verbose_name='Transakce Proběhla'),
        ),
        migrations.AlterField(
            model_name='abstractoffer',
            name='negotiable',
            field=models.BooleanField(verbose_name='smlouvatelné'),
        ),
        migrations.AlterField(
            model_name='abstractoffer',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='cena'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='obrázek'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name='název'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Book', verbose_name='kniha'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='stav'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='will_be_active',
            field=models.DateField(blank=True, null=True, verbose_name='k odebrání od'),
        ),
        migrations.AlterField(
            model_name='user',
            name='visited_class',
            field=models.CharField(choices=[('R1.A', 'R1.A'), ('R2.A', 'R2.A'), ('R3.A', 'R3.A'), ('R4.A', 'R4.A'), ('R5.A', 'R5.A'), ('R6.A', 'R6.A'), ('R7.A', 'R7.A'), ('R8.A', 'R8.A'), ('1.A', '1.A'), ('1.B', '1.B'), ('1.C', '1.C'), ('2.A', '2.A'), ('2.B', '2.B'), ('2.C', '2.C'), ('3.A', '3.A'), ('3.B', '3.B'), ('3.C', '3.C'), ('4.A', '4.A'), ('4.B', '4.B'), ('4.C', '4.C')], max_length=255),
        ),
    ]
