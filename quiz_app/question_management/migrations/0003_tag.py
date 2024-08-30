# Generated by Django 5.0.3 on 2024-08-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_management', '0002_questions_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('questions', models.ManyToManyField(related_name='tags', to='question_management.questions')),
            ],
        ),
    ]
