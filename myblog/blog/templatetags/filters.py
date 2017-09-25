#coding=utf-8
#引入注册对象
from django.template import Library
register=Library()

#使用装饰器进行注册
@register.filter
#定义求余函数mod，将value对2求余
def mod(value):
    value += 1
    return int(value)
