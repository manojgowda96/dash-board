# Generated by Django 5.0.6 on 2024-06-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0005_alter_data_added_alter_data_impact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sector',
            field=models.CharField(max_length=100),
        ),
    ]
