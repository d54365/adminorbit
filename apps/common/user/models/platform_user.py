from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from apps.core.models import BaseManager, BaseModel, ForeignKey


class PlatformUserManager(BaseUserManager, BaseManager):
    @staticmethod
    def create_superuser(username, name, email, phone, password):
        return PlatformUser.objects.create(
            username=username,
            name=name,
            email=email,
            phone=phone,
            password=make_password(password),
            is_super=True,
            updated_at=None,
        )


class PlatformUser(AbstractBaseUser, BaseModel):
    """平台运营后台用户"""

    username = models.CharField(max_length=32, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=128, verbose_name="密码")
    name = models.CharField(max_length=32, verbose_name="昵称", db_index=True)
    email = models.CharField(max_length=64, verbose_name="邮箱", db_index=True)
    phone = models.CharField(max_length=32, verbose_name="手机号码", db_index=True)
    avatar = models.CharField(max_length=128, verbose_name="头像", default="")
    created = ForeignKey(
        "self",
        verbose_name="创建人",
        related_name="platform_user_created",
    )
    created_name = models.CharField(max_length=32, verbose_name="创建人姓名")
    updated = ForeignKey(
        "self",
        verbose_name="上次修改人",
        related_name="platform_user_updated",
    )
    updated_name = models.CharField(
        max_length=32,
        verbose_name="上次修改人姓名",
        default="",
    )
    last_login_at = models.DateTimeField(verbose_name="上次登陆时间", null=True)
    is_active = models.BooleanField(default=True, verbose_name="是否激活")
    is_super = models.BooleanField(default=False, verbose_name="是否是管理员")

    objects = PlatformUserManager()

    REQUIRED_FIELDS = ["name", "email", "phone", "password"]
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
