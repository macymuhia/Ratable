# Generated by Django 2.2.4 on 2019-11-19 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KPIs', '0002_remove_score_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KPIs.Area'),
        ),
    ]
