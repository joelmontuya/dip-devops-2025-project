# Generated by Django 5.2.3 on 2025-07-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_remove_book_id_book_book_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="isbn",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="published_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
