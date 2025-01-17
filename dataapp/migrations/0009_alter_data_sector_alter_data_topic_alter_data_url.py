# Generated by Django 5.0.6 on 2024-06-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0008_alter_data_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sector',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='topic',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(),
        ),
    ]
