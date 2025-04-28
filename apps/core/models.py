from django.db import models


class BaseManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._include_deleted_filtering = False

    def with_deleted_filtering(self, enable=True):
        self._include_deleted_filtering = not enable
        return self

    def get_queryset(self):
        if self._include_deleted_filtering:
            return super().get_queryset()

        return super().get_queryset().filter(is_delete=False)


class BaseModel(models.Model):
    """通用模型字段"""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")
    is_deleted = models.BooleanField(default=False, verbose_name="是否已删除")

    class Meta:
        abstract = True


class TenantBaseModel(BaseModel):
    """租户通用模型字段"""

    tenant_id = models.BigIntegerField(verbose_name="租户ID", db_index=True)

    class Meta:
        abstract = True


class ForeignKey(models.ForeignKey):
    def __init__(
        self,
        to,
        on_delete=models.SET_NULL,
        related_name=None,
        related_query_name=None,
        limit_choices_to=None,
        parent_link=False,
        to_field=None,
        db_constraint=False,
        **kwargs,
    ):
        kwargs["null"] = True
        super().__init__(
            to,
            on_delete,
            related_name,
            related_query_name,
            limit_choices_to,
            parent_link,
            to_field,
            db_constraint,
            **kwargs,
        )


class ManyToManyField(models.ManyToManyField):
    def __init__(
        self,
        to,
        related_name=None,
        related_query_name=None,
        limit_choices_to=None,
        symmetrical=None,
        through=None,
        through_fields=None,
        db_constraint=False,
        db_table=None,
        swappable=True,
        **kwargs,
    ):
        super().__init__(
            to,
            related_name,
            related_query_name,
            limit_choices_to,
            symmetrical,
            through,
            through_fields,
            db_constraint,
            db_table,
            swappable,
            **kwargs,
        )
