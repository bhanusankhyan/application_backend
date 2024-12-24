# Generated by Django 5.1.4 on 2024-12-23 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='App_Name',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='applications',
            name='App_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Application_Picture',
            field=models.BinaryField(blank=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apis.category'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Created_By',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apis.user'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Points',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Subcategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apis.subcategory'),
        ),
    ]
