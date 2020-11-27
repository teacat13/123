# Generated by Django 3.1.3 on 2020-11-09 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, unique=True)),
                ('price', models.FloatField(blank=True)),
                ('discount', models.BooleanField(default=False)),
                ('price_discount', models.FloatField(blank=True)),
                ('type', models.CharField(blank=True, choices=[('1', 'fruit'), ('0', 'vegetables'), (None, 'Unknown')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(editable=False, max_length=50)),
                ('age', models.CharField(default=18, max_length=50)),
                ('sex', models.CharField(blank=True, choices=[('1', 'men'), ('0', 'women'), (None, 'Unknown')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.user')),
            ],
        ),
    ]
