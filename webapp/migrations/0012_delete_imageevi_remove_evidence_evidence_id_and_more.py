# Generated by Django 4.2.6 on 2023-12-01 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_evidence_imageevi_uploadedfile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageEvi',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='evidence_id',
        ),
        migrations.AddField(
            model_name='evidence',
            name='evidence_name',
            field=models.CharField(default='asff', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case', to='webapp.caseinfo'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='evidence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Evi', to='webapp.evidence'),
        ),
    ]