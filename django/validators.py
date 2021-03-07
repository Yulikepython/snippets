from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from .models import Profile

User = get_user_model()


def validate_key(value):
    qs = User.objects.filter(activation_key=value)
    if not qs.exists():
        raise ValidationError("アクティベーションキーが違います。")

def validate_email(value):
    qs = User.objects.filter(email=value)
    if qs.exists():
        raise forms.ValidationError("このアドレスはすでに登録済みです。")

def reset_email(value):
    qs = User.objects.filter(email=value)
    if not qs.exists():
        raise ValidationError("このアドレスで登録しているユーザーはいません。登録画面へおすすみください")

def validate_hiragana(value):
    hiragana = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'
    if value not in hiragana:
        raise ValidationError('ひらがなでご記入ください')


def validate_email(value):
    email = self.cleaned_data.get("email")
    if "edu" in email:
        raise ValidationError("We do not accept edu emails")


CATEGORIES = ['Mexican','Asian','American','Whatever']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{ value } not a valid category")