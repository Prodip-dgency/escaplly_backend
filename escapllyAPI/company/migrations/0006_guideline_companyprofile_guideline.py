# Generated by Django 4.1 on 2022-10-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_companyprofile_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='guideline',
            field=models.ManyToManyField(blank=True, to='company.guideline'),
        ),
    ]