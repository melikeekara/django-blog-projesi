from django import template
from bloge.models import KategoriModel

register = template.Library()

@register.simple_tag
def kategori_list():
    kategoriler = KategoriModel.objects.all()
    return kategoriler