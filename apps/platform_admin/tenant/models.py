from django.db import models

from apps.core.models import BaseModel


class Tenant(BaseModel):
    STATUS_INACTIVE = 0
    STATUS_ACTIVE = 1

    STATUS_CHOICES = (
        (STATUS_INACTIVE, "禁用"),
        (STATUS_ACTIVE, "启用"),
    )

    name = models.CharField(max_length=128, verbose_name="租户名称")
    code = models.CharField(max_length=64, unique=True, verbose_name="租户编码")
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
        verbose_name="租户状态",
    )
    created_by = models.CharField(
        max_length=32, verbose_name="创建人用户名", default=""
    )
    updated_by = models.CharField(
        max_length=32, verbose_name="修改人用户名", default=""
    )

    class Meta:
        verbose_name = "租户"

    def __str__(self):
        return self.name
