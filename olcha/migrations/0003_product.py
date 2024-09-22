# Generated by Django 5.1.1 on 2024-09-22 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0002_alter_category_options_category_slug_group_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d/')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='olcha.category')),
                ('groups', models.ManyToManyField(related_name='products', to='olcha.group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
