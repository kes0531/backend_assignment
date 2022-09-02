# Generated by Django 4.1 on 2022-09-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(primary_key=True, serialize=False)),
                ('order_user', models.CharField(max_length=20)),
                ('order_createdDate', models.DateTimeField(auto_now_add=True)),
                ('order_modifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.UUIDField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField(max_length=100)),
                ('product_createdDate', models.DateTimeField(auto_now_add=True)),
                ('product_modifiedDate', models.DateTimeField(auto_now=True)),
                ('product_image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=25)),
                ('member_pw', models.CharField(max_length=30)),
                ('member_name', models.CharField(max_length=20)),
                ('member_photo', models.ImageField(upload_to='%Y/%m/%d')),
            ],
        ),
    ]