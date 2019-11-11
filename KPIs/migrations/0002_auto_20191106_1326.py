# Generated by Django 2.2.7 on 2019-11-06 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KPIs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Indicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KPIs.Area')),
            ],
        ),
    ]
