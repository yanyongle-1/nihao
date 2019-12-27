from builtins import locals
from django.core.paginator import Paginator
from django.shortcuts import render
from poled.models import *
from django.http import FileResponse
from django.core.mail import send_mail


def index(request):
    site_url = request.path[0:3]
    if "/en" in site_url:
        post_article = PostArticle.objects.filter(select_language__language_tag="en")[:3]
    else:
        post_article = PostArticle.objects.filter(select_language__language_tag="cn")[:3]
    return render(request, 'index.html', locals())


def postarticle(request):
    p_article = request.GET.get('p-article', default='')
    post_article_detail = PostArticle.objects.get(title=p_article)
    return render(request, 'post.html', locals())


def produce_card(request):
    p_card = request.GET.get('p-card', default='')
    produce_card_detail = Product.objects.get(title=p_card)
    return render(request, 'product.html', locals())


def paging(modelsdate, number, page_num):
    paginator = Paginator(modelsdate, number)
    contacts = paginator.get_page(page_num)

    current_page_num = contacts.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    return contacts, page_range,


def post_list(request):
    page_num = request.GET.get('page', 1)
    p_card = request.GET.get('p-card', default='')
    post_article_list = PostArticle.objects.filter(select_category__category_name=p_card)
    pag = paging(post_article_list, 1, page_num)
    contacts_post = pag[0]
    page_range = pag[1]
    return render(request, 'PostList.html', locals())


def produce_list(request):
    page_num = request.GET.get('page', 1)
    pro_card = request.GET.get('pro-card', default='')
    post_produce_list = Product.objects.filter(select_category__category_name=pro_card).all()
    pag = paging(post_produce_list, 4, page_num)
    contacts_produce = pag[0]
    page_range_produce = pag[1]
    return render(request, 'ProductList.html', locals())


def option_detail(request):
    option_d = request.GET.get('opt-de', default='')
    opt_title = request.GET.get('opt-title', default='')
    site_url = request.path[0:3]
    if "/en" in site_url:
        option_details = Option.objects.values(option_d)[1]
    else:
        option_details = Option.objects.values(option_d)[0]
    return render(request, 'page.html', locals())


def download_list_read(request):
    page_num = request.GET.get('page', 1)
    download_card = request.GET.get('download-card', default='')
    download_file = UploadFile.objects.filter(select_category__category_name=download_card)
    pag = paging(download_file, 1, page_num)
    contacts_download = pag[0]
    page_range_download = pag[1]
    return render(request, 'download.html', locals())


def download_list(request):
    tests = request.GET.get('tests', default='')
    file = open('media/' + tests, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="example.tar.gz"'
    return response


def search_date(request):
    search_card = request.POST.get('search', default='')
    site_url = request.path[0:3]
    if "/en" in site_url:
        search_produce = Product.objects.filter(select_language__language_tag="en",
                                                title__contains=search_card)
    else:
        search_produce = Product.objects.filter(select_language__language_tag="cn",
                                                title__contains=search_card)
    return render(request, 'search.html', locals())


def feedback(request):
    site_url = request.path[0:3]
    if "/en" in site_url:
        feedbacck = 'Feedback'
    else:
        feedbacck = '留言&反馈'
    return render(request, 'feedback.html', locals())


def message(request):
    message_card = request.POST
    Poledfeedback.objects.create(name=message_card['name'], email=message_card['email'], qq=message_card['qq'],
                                 phone=message_card['phone'], message=message_card['message'])
    res = send_mail('留言反馈', message_card['message'], '458029484@qq.com', [message_card['email']], fail_silently=False)
    if res:
        return render(request, 'test.html')
