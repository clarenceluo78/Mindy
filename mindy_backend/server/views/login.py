from django.shortcuts import render, redirect
from .. import models
from .. import forms
import hashlib    # 加密密码
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return redirect("/server/")
    return render(request, 'users/index.html')


def login(request):
    if request.session.get('is_login', None):  #已登录，不可重复登陆
        return redirect(reverse('home_list'))
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')  #cleaned_data 字典只包含有效字段
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = 'The user does not exist'
                return render(request, 'users/login.html', locals())  #locals()函数返回所有的本地变量字典

            if not user.has_confirmed:
                message = 'User has not confirmed registration by email!'
                return render(request, 'users/login.html', locals())

            if user.password == encode(password):
                #往session字典内写入用户状态与数据
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect(reverse('home_list'))
            else:
                message = 'Incorrect password, please try again!'
                return render(request, 'users/login.html', locals())
        else:
            return render(request, 'users/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'users/login.html', locals())


def make_confirm_message(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = encode(user.name, now)
    models.Confirm_Message.objects.create(code=code, user=user,)
    return code


def send_email(email, code):
    subject = 'Verification email'

    text_content = '''Thanks for registration, this is the confirmation email！\
                    If you see this message, your email server does not provide HTML links, please contact the administrator！'''

    html_content = '''
                    <p>Thanks for registration!<a href="http://{}/confirm/?code={}" target=blank>Confirm</a></p>
                    <p>Please click the link to complete registration confirmation!</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def encode(s, salt='myweb'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def register(request):
    if request.session.get('is_login', None):
        return redirect('/server/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            username = register_form.cleaned_data.get('username')
            pwd1 = register_form.cleaned_data.get('pwd1')
            pwd2 = register_form.cleaned_data.get('pwd2')

            if pwd1 != pwd2:
                message = 'Two passwords should be consistent！'
                return render(request, 'users/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'The user name has been occupied!'
                    return render(request, 'users/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'This email has been registered！'
                    return render(request, 'users/register.html', locals())

                new_user = models.User()
                new_user.email = email
                new_user.name = username
                new_user.password = encode(pwd1)
                new_user.save()

                verify_code = make_confirm_message(new_user)
                send_email(email, verify_code)

                message = 'Please check your email for confirmation!'
                return render(request, 'server/users/register.html', locals())
        else:
            return render(request, 'users/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'users/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        #未登录
        return redirect("/server/")
    request.session.flush()
    return redirect("/server/")


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.Confirm_Message.objects.get(code=code)
    except:
        message = 'Invalid confirmation request!'
        return render(request, 'users/confirm.html', locals())

    c_time = confirm.created_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = 'Your verification mail has expired! Please register again!'
        return render(request, 'users/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = 'Thank you for your confirmation, please login with your account!  '
        return render(request, 'users/confirm.html', locals())