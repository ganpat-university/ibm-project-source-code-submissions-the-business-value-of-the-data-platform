# Generated by Django 4.0.1 on 2022-03-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_complaints_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='customer_disputed',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='customer_timely_responded',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]