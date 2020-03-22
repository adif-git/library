# Generated by Django 3.0.4 on 2020-03-19 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_book', models.CharField(choices=[('Novel', 'Novel'), ('Documentation', 'Documentation'), ('Other', 'Other')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('date_published', models.DateField()),
                ('number_of_pages', models.IntegerField()),
                ('author', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_site.Author')),
                ('book_type', models.ManyToManyField(to='library_site.BookTypes')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]