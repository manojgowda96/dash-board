# Generated by Django 5.0.6 on 2024-05-24 15:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0002_alter_data_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='city',
        ),
        migrations.RemoveField(
            model_name='data',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='data',
            name='year',
        ),
        migrations.AddField(
            model_name='data',
            name='added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='data',
            name='end_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='impact',
            field=models.CharField(blank=True, default='N/A', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='insight',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='data',
            name='pestle',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='data',
            name='sector',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='source',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='start_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='title',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='data',
            name='topic',
            field=models.CharField(default='N/A', max_length=250),
        ),
        migrations.AddField(
            model_name='data',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='country',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='intensity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='likelihood',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='region',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='relevance',
            field=models.IntegerField(default=0),
        ),
    ]