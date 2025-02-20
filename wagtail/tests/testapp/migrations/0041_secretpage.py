# Generated by Django 2.1.4 on 2018-12-17 18:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.tests.testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("tests", "0040_customdocument_file_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecretPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("boring_data", models.TextField()),
                ("secret_data", models.TextField()),
            ],
            options={
                "abstract": False,
            },
            bases=(wagtail.tests.testapp.models.PerUserPageMixin, "wagtailcore.page"),
        ),
    ]
