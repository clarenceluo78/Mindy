from django.shortcuts import render,redirect
from django.http.response import JsonResponse,Http404,HttpResponseNotAllowed,HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required # 登录需求装饰器
from django.views.decorators.http import require_http_methods,require_GET,require_POST # 视图请求方法装饰器
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage # 后端分页
from django.core.exceptions import PermissionDenied,ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from app_doc.models import Project,Doc,DocTemp
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import transaction
from django.urls import reverse
from loguru import logger
from app_doc.report_utils import *
from app_admin.models import UserOptions,SysSetting
from app_admin.decorators import check_headers,allow_report_file
import datetime
import traceback
import re
import json
import random
import os.path
import base64
import hashlib


# 个人中心
@login_required()
def user_center(request):
    return render(request,'app_doc/user/user_center.html',locals())


# 个人中心菜单
def user_center_menu(request):
    menu_data = [
        {
            "id": 1,
            "title": _("Overview"),
            "type": 1,
            "icon": "layui-icon layui-icon-console",
            "href": reverse('manage_overview'),
        },
        {
            "id": "my_project",
            "title": _("My Project"),
            "icon": "layui-icon layui-icon-component",
            "type": 0,
            "href": "",
            "children": [
                {
                    "id": "manage_project",
                    "title": _("Management"),
                    "icon": "layui-icon layui-icon-console",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse('manage_project')
                },
                {
                    "id": "manage_colla_self",
                    "title": _("Collaboration"),
                    "icon": "layui-icon layui-icon-console",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse('manage_pro_colla_self')
                },
            ]
        },
        {
            "id": "my_doc",
            "title": _("My Documents"),
            "icon": "layui-icon layui-icon-file-b",
            "type": 0,
            "href": "",
            "children": [
                {
                    "id": "doc_manage",
                    "title": _("Management"),
                    "icon": "layui-icon layui-icon-face-smile",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse("manage_doc")
                },
                {
                    "id": "doc_template",
                    "title": _("Templates"),
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse("manage_doctemp")
                },
                # {
                #     "id": "doc_tag",
                #     "title": _("Labels"),
                #     "icon": "layui-icon layui-icon-face-cry",
                #     "type": 1,
                #     "openType": "_iframe",
                #     "href": reverse("manage_doc_tag")
                # },
                {
                    "id": "doc_share",
                    "title": _("My Share"),
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse("manage_doc_share")
                },
                {
                    "id": "doc_recycle",
                    "title": _("Recycle Bin"),
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse("doc_recycle")
                }
            ]
        },
        {
            "id": "my_fodder",
            "title": _("My Attachments"),
            "icon": "layui-icon layui-icon-upload-drag",
            "type": 0,
            "href": "",
            "children": [
                {
                    "id": "my_img",
                    "title": _("Pictures"),
                    "icon": "layui-icon layui-icon-face-smile",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse("manage_image")
                },
                {
                    "id": "my_attachment",
                    "title": _("Others"),
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": reverse("manage_attachment")
                },
            ]
        },
        {
            "id": "my_collect",
            "title": _("Collection"),
            "icon": "layui-icon layui-icon-star",
            "type": 1,
            "openType": "_iframe",
            "href": reverse("manage_collect")
        },
        {
            "id": "self_settings",
            "title": _("User Settings"),
            "icon": "layui-icon layui-icon-face-smile",
            "type": 1,
            "openType": "_iframe",
            "href": reverse("manage_self")
        },
    ]
    return JsonResponse(menu_data,safe=False)
