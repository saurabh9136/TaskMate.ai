# Generated by Django 5.0.6 on 2024-05-28 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AIResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ai_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(default='pending', max_length=10)),
                ('importance', models.CharField(default='veryHighg', max_length=50)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('ai_response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.airesponse')),
            ],
        ),
    ]