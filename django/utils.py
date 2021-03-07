import random
import string

from django.conf import settings

from django.utils.text import slugify

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

DONT_USE = ['create']

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 8)

#from shortener.models import KirrURL

def random_string_generator(size=20, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_username(instance):
    chars=slugify(instance.email)
    Klass = instance.__class__
    username = ''.join(random.choice(chars) for _ in range(5))
    qs_exists = Klass.objects.filter(username=username).exists()
    
    while qs_exists == True:
        username = ''.join(random.choice(chars) for _ in range(5))
        qs_exists = Klass.objects.filter(username=username).exists()
    return username

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )

        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))

import random
import string

from django.utils.text import slugify
from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 35)

#from shortener.models import KirrURL

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

DONT_USE = ['create']

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )

        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
    
def random_username(instance):
    chars=slugify(instance.email)
    Klass = instance.__class__
    username = ''.join(random.choice(chars) for _ in range(5))
    qs_exists = Klass.objects.filter(username=username).exists()
    
    while qs_exists == True:
        username = ''.join(random.choice(chars) for _ in range(5))
        qs_exists = Klass.objects.filter(username=username).exists()
    return username