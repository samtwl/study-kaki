# Generated by Django 4.0.2 on 2023-07-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docqueryapi', '0004_transcript'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='transcriptResponse',
            field=models.CharField(default='', max_length=150000),
            preserve_default=False,
        ),
    ]
