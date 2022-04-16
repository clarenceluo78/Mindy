from .models import SysSetting
from django.conf import settings

# 系统设置 - 上下文变量
def sys_setting(request):
    setting_dict = dict()
    # 设置网站版本
    setting_dict['mrdoc_version'] = settings.VERSIONS
    # 设置debug状态
    setting_dict['debug'] = settings.DEBUG
    # 获取系统设置状态
    datas = SysSetting.objects.filter(types__in=["basic","doc"])
    for data in datas:
        setting_dict[data.name] = data.value
    return setting_dict