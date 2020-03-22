# Generated by Django 3.0.4 on 2020-03-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_site', '0005_auto_20200321_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='type_of_book',
            field=models.CharField(blank=True, choices=[('Novel', 'Novel'), ('Documentation', 'Documentation'), ('Other', 'Other')], max_length=255, null=True),
        ),
    ]
