# Generated by Django 4.2.6 on 2023-12-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_evidence_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]