# Generated by Django 5.2.4 on 2025-07-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_book_isbn_book_published_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
