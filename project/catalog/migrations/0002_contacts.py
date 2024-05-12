from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название контакта",
                        max_length=50,
                        verbose_name="Название контакта",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Введите номер контакта",
                        max_length=20,
                        verbose_name="Номер контакта",
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        blank=True,
                        help_text="Введите сообщение",
                        null=True,
                        verbose_name="Сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ["name", "phone"],
            },
        ),
    ]