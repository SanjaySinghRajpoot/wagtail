# Generated by Django 2.0 on 2018-02-15 10:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.tests.testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0028_headcountrelatedmodelusingpk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="streampage",
            name="body",
            field=wagtail.core.fields.StreamField(
                (
                    ("text", wagtail.core.blocks.CharBlock()),
                    ("rich_text", wagtail.core.blocks.RichTextBlock()),
                    ("image", wagtail.tests.testapp.models.ExtendedImageChooserBlock()),
                    (
                        "product",
                        wagtail.core.blocks.StructBlock(
                            (
                                ("name", wagtail.core.blocks.CharBlock()),
                                ("price", wagtail.core.blocks.CharBlock()),
                            )
                        ),
                    ),
                )
            ),
        ),
    ]
