# Generated by Django 4.0.2 on 2022-02-06 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('marcket', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='marcket.marcket')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('stock', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('product', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='marcket.product')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
