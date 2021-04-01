from django.db import models


class User(models.Model):
    nickname_text = models.CharField(max_length=50, verbose_name='昵称')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(null=True, default=None, verbose_name='最后修改时间')


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_text = models.CharField(max_length=50, verbose_name='国家')
    address_text = models.CharField(max_length=500, verbose_name='详细地址')
