# Generated by Django 4.1.3 on 2022-12-05 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, verbose_name='Size')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Size',
            },
        ),
        migrations.RemoveField(
            model_name='product_s',
            name='quantity',
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_s')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
    ]
