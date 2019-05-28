from django import template
from ..models import Classify
register = template.Library()


@register.simple_tag
def getchufang():
    """
    返回前7个厨房分类
    :return:
    """
    a=Classify.objects.get(id=1)
    return a.classify_set.all()[:7]

@register.simple_tag
def getchufang1():
    """
    返回后7个厨房分类
    :return:
    """
    a=Classify.objects.get(id=1)
    return a.classify_set.all()[7:14]

@register.simple_tag
def getjiating():
    """
    返回前7个家庭分类
    :return:
    """
    a=Classify.objects.get(id=2)
    return a.classify_set.all()[0:7]

@register.simple_tag
def getjiating1():
    """
    返回后7个家庭分类
    :return:
    """
    a=Classify.objects.get(id=2)
    return a.classify_set.all()[7:14]