# Generated by Django 4.0.4 on 2022-05-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_portfoliomodel_body_1_portfoliomodel_body_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='commit',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
