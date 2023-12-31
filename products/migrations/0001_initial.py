# Generated by Django 3.2.19 on 2023-07-01 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('model_name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True)),
                ('size', models.CharField(choices=[('4 x 6 inches', '4 x 6 inches'), ('5 x 7 inches', '5 x 7 inches'), ('8 x 10 inches', '8 x 10 inches'), ('8.5 x 11 inches', '8.5 x 11 inches')], default='4 x 6 inches', max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]
