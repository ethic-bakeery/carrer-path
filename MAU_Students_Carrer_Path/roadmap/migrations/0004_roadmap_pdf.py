# Generated by Django 4.2.11 on 2024-09-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0003_roadmap_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmap',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='roadmaps/pdfs/'),
        ),
    ]
