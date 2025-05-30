# Generated by Django 5.2 on 2025-04-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tenant",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="更新时间"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="是否已删除"),
                ),
                ("name", models.CharField(max_length=128, verbose_name="租户名称")),
                (
                    "code",
                    models.CharField(
                        max_length=64, unique=True, verbose_name="租户编码"
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "禁用"), (1, "启用")],
                        default=1,
                        verbose_name="租户状态",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(
                        default="", max_length=32, verbose_name="创建人用户名"
                    ),
                ),
                (
                    "updated_by",
                    models.CharField(
                        default="", max_length=32, verbose_name="修改人用户名"
                    ),
                ),
            ],
            options={
                "verbose_name": "租户",
            },
        ),
    ]
