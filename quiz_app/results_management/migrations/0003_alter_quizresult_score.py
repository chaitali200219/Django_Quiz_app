# Generated by Django 4.2.3 on 2024-09-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results_management', '0002_alter_questionresult_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]