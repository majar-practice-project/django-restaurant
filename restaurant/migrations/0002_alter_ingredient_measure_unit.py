# Generated by Django 4.2.6 on 2023-10-31 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measure_unit',
            field=models.CharField(choices=[('tbsp', 'teaspoon (tbsp)'), ('lbs', 'pound (lbs)'), ('oz', 'ounce (oz)'), ('g', 'gram (g)'), ('na', 'N/A')], default='tbsp', max_length=5),
        ),
    ]
