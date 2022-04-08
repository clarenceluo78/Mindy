from django.db import models

# models.Model类里面有所有的CRUD操作
class AbstractModel(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    # 关联表
    class Meta:
        abstract = True


# Create your models here.
# 继承下来的新类，可以对应后台的表
class CooperationMind(AbstractModel):
    """

    """
    coop_mind_name = models.CharField(verbose_name='脑图名称', max_length=64, null=False, blank=False)
    creator = models.BigIntegerField(verbose_name='创建人ID', null=False, blank=False)
    client_id = models.CharField(verbose_name='客户端ID', max_length=64, null=False, blank=False)
    snapshot_data = models.TextField(verbose_name='脑图数据', null=True, )
    log_id = models.BigIntegerField(verbose_name='data对应的操作日志(cooperation_mind_log)ID', null=True, )
    data_format = models.CharField(verbose_name='数据格式化类型', max_length=32, null=False, blank=False)

    class Meta:
        db_table = 'cooperation_mind'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['creator'])
        ]
        verbose_name = "脑图表"


class CooperationMindLog(AbstractModel):
    """
    操作日志表
    """
    coop_mind_id = models.BigIntegerField(verbose_name='脑图ID', null=False, blank=False)
    log_uuid = models.CharField(verbose_name='操作UUID', max_length=64, null=False, blank=False)
    log_content = models.CharField(verbose_name='操作内容', max_length=1024, null=False, blank=False)
    operator = models.BigIntegerField(verbose_name='操作人', null=True)
    operator_ip = models.CharField(verbose_name='操作人IP', null=False, max_length=32)
    client_id = models.CharField(verbose_name='客户端ID', max_length=64, null=False, blank=False)

    class Meta:
        db_table = 'cooperation_mind_log'
        ordering = ['id']
        unique_together = (("coop_mind_id", "log_uuid"),)
        indexes = [
            models.Index(fields=['coop_mind_id'], ),
            models.Index(fields=['operator'], )
        ]
        verbose_name = "操作日志表"


# Email confirm
class User(models.Model):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    created_time = models.DateField(auto_now=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = "User"
        verbose_name_plural = verbose_name


class Confirm_Message(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + ": " + self.code

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "Verification code"
        verbose_name_plural = verbose_name