from poled.models import Option, Category


def base_page(request):
    site_url = request.path[0:3]

    if "/en" in site_url:
        language = "/en/"
        home = "<a href='/en' style='color: #000;'>Home</a>"
        language_change = "<a href='/' style='color: #000;'>中文</a>"
        about_us = "About Us"
        all_products = "All Products"
        download = "Download"
        news = "News"
        talent_idea = "Talent Idea"
        products_show = 'Products Show'
        online_chating = 'Online Chating'
        latest_news = 'Latest News'
        company_info = 'company profile'
        company_organization = 'Company Organization'
        company_environment = 'Research Environment'
        company_recruit = 'Job Vacancy'
        contact_information = 'Contact Way'
        company_map = 'Where We Are'
        company_activities = 'Company Activities'
        feed_back = "Feedback"
        qq_group = "QQ Group"
        customer_service = "QQ"
        back_top = "Back Top"
        f_name = 'Your Name :'
        f_name01 = 'Your Full Name'
        f_email = 'Your Email :'
        f_email01 = 'Valid Email Address'
        f_qq = 'QQ Number :'
        f_qq01 = 'Valid Your QQ Number'
        f_number = 'Phone Number :'
        f_number01 = 'Valid Your Phone Number'
        f_message = 'Message :'
        f_message01 = 'Your Message to Us'
        f_send = 'send'
        option = Option.objects.all()[1]
        produce_category = Category.objects.filter(category_type="product", select_language__language_tag="en")
        post_category = Category.objects.filter(category_type="post", select_language__language_tag="en").exclude(
            category_name="Company Activities")
        download_category = Category.objects.filter(category_type="file", select_language__language_tag="en")
    elif "/" in site_url:
        language = "/"
        home = "<a href='/' style='color: #000;'>首页</a>"
        language_change = "<a href='/en' style='color: #000;'>English</a>"
        about_us = "关于我们"
        all_products = "产品展示"
        download = "下载中心"
        news = "新闻中心"
        talent_idea = "人才理念"
        products_show = '展示产品'
        online_chating = '滚动文本'
        latest_news = '最新消息'
        company_info = '公司简介'
        company_organization = '组织机构'
        company_environment = '科研环境'
        company_recruit = '招聘职位'
        contact_information = '联系方式'
        company_map = '公司地图'
        company_activities = '员工天地'
        feed_back = "留言"
        qq_group = "QQ群"
        customer_service = "客服"
        back_top = "返回顶部"
        f_name = '姓名 :'
        f_name01 = '请告诉我们怎么称呼您'
        f_email = '邮箱 :'
        f_email01 = '您的电子邮箱'
        f_qq = 'QQ号码 :'
        f_qq01 = '您的QQ号码'
        f_number = '电话号码 :'
        f_number01 = '您的电话号码'
        f_message = '内容 :'
        f_send = '发送'

        option = Option.objects.all()[0]
        produce_category = Category.objects.filter(category_type="product", select_language__language_tag="cn")
        post_category = Category.objects.filter(category_type="post", select_language__language_tag="cn").exclude(
            category_name="员工天地")
        download_category = Category.objects.filter(category_type="file", select_language__language_tag="cn")
    return locals()
