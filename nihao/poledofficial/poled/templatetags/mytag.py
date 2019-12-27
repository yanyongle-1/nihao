from django import template
from pyquery import PyQuery as pq

register = template.Library()


@register.filter
def postArticles(x):
    html = pq(x)
    img_path = pq(html)('img').attr('src')
    if img_path:
        return img_path
    else:
        return '/media/swiper_img/d-img.bmp'


