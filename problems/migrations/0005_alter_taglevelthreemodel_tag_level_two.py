# Generated by Django 3.2.1 on 2021-05-23 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20210523_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taglevelthreemodel',
            name='tag_level_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.tegleveltwomodel'),
        ),
    ]
