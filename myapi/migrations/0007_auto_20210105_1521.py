# Generated by Django 3.1.5 on 2021-01-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20210105_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waifu',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='bloodType',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='bust',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='dateBirth',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='description',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='gender',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='hip',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='iid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='img',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='likeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='name',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='orName',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='placeOf',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='roName',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='serie',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='trash',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='trashCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='type',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='url',
            field=models.CharField(default='', max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='waist',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
