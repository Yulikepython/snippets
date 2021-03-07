from django.core.mail import send_mail

from hironish import settings

from .utils import random_string_generator, random_username


def activate_account(user, key):
    subject = 'アカウントを有効にしてください'
    message = """
                 アクティベーションキー：{}
                 アカウントを有効にするためにこちらにアクセスし、必要な情報を入力してください。
                 http://testaddress/{}
                                  """.format(key, user.pk)
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[user.email, settings.EMAIL_HOST_USER]
#    print(user, key)
    return send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,)
#    print(subject, message, from_email, recipient_list)

def reset_password(user):
    name = random_username(user)
    passw = random_string_generator(8)
    subject = 'パスワードをリセットしました'
    message = """
                 ユーザー名:{}
                 パスワード：{}
                 ユーザー名、パスワードをリセットしました。こちらでログインをして、再設定をしてください。
                 http://localhost:8000/login
                                  """.format(name, passw)
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[user.email, settings.EMAIL_HOST_USER]
    user.username=name
    user.set_password(passw)
    user.save()
#    print(user, key)
#    return send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,)
    print(subject, message, from_email, recipient_list)