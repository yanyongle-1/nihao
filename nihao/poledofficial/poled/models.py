from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# 语言


class Language(models.Model):
    language_name = models.CharField('语言', max_length=50, editable=False)
    language_tag = models.CharField('语言代码', max_length=50, editable=False)

    def __str__(self):
        return '{}'.format(self.language_name)

    class Meta:
        verbose_name = '多语言'
        verbose_name_plural = verbose_name


# 分类
class Category(models.Model):
    select_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name='语言')
    CATEGORY_CHOICES = (('post', u'文章'), ('product', u'产品'), ('file', u'文件'))
    category_type = models.CharField(u"选择类型", choices=CATEGORY_CHOICES, max_length=32)
    category_name = models.CharField('分类', max_length=50)

    def __str__(self):
        return '{}'.format(self.category_name)

    class Meta:
        verbose_name = ' 分类'
        verbose_name_plural = verbose_name


# 文章
class PostArticle(models.Model):
    select_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name='语言')
    select_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='分类')
    title = models.CharField('标题', max_length=100)
    contents = RichTextUploadingField('内容')
    POST_CHOICES = (('published', u'发布'), ('draft', u'草稿'))
    post_status = models.CharField(u"状态", choices=POST_CHOICES, max_length=10)
    summary = models.CharField('摘要', max_length=200)
    author = models.ForeignKey(User, editable=False, null=True, blank=True
                               , on_delete=models.CASCADE, verbose_name='作者')
    time = models.DateTimeField('发布时间', editable=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    def shorten_title(self):
        if len(str(self.title)) > 22:
            return '{}......'.format(str(self.title)[0:22])
        else:
            return str(self.title)
    shorten_title.short_description = '标题'

    def shorten_contents(self):
        if len(str(self.contents)) > 65:
            return '{}......'.format(str(self.contents)[0:65])
        else:
            return str(self.contents)
    shorten_contents.short_description = '内容'

    class Meta:
        ordering = ['-time']
        verbose_name = '  文章'
        verbose_name_plural = verbose_name


#  产品
class Product(models.Model):
    select_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name='选择语言')
    select_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='分类')
    title = models.CharField('产品名', max_length=50)
    PRODUCT_CHOICES = (('up', u'上架'), ('down', u'下架'), ('oos', u'缺货'))
    product_status = models.CharField(u"产品状态", choices=PRODUCT_CHOICES, max_length=10)
    image = models.ImageField(verbose_name="上传产品图片", upload_to="up_image", blank=True)
    subtitle = models.TextField("摘要")
    description = RichTextUploadingField("描述")

    def __str__(self):
        return '{}'.format(self.title)

    def shorten_product_title(self):
        if len(str(self.title)) > 22:
            return '{}......'.format(str(self.title)[0:22])
        else:
            return str(self.title)
    shorten_product_title.short_description = '产品名'

    def shorten_product_description(self):
        if len(str(self.description)) > 65:
            return '{}......'.format(str(self.description)[0:65])
        else:
            return str(self.description)
    shorten_product_description.short_description = '描述'

    class Meta:
        verbose_name = ' 产品'
        verbose_name_plural = verbose_name
        ordering = ['-id']


@receiver(pre_delete, sender=Product)
def mymodel_delete(sender, instance, **kwargs):
    instance.image.delete(False)


# 上传文件
class UploadFile(models.Model):
    select_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name='选择语言')
    select_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='分类')
    name = models.CharField('文件名', max_length=100)
    image = models.ImageField(verbose_name="预览图片", upload_to="up_image", blank=True)
    file = models.FileField(verbose_name="上传文件", upload_to="up_file", blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['-id']
        verbose_name = '下载中心'
        verbose_name_plural = verbose_name


#  留言/反馈
class Poledfeedback(models.Model):
    name = models.CharField('姓名', max_length=50)
    email = models.EmailField('邮箱', max_length=50)
    qq = models.CharField('QQ号码', max_length=50)
    phone = models.CharField('手机号码', max_length=50)
    message = models.TextField('留言内容')

    def __str__(self):
        return '{}'.format(self.name)

    def shorten_product_message(self):
        if len(str(self.message)) > 65:
            return '{}......'.format(str(self.message)[0:65])
        else:
            return str(self.message)
    shorten_product_message.short_description = '描述'

    class Meta:
        verbose_name = ' 留言/反馈'
        verbose_name_plural = verbose_name


# 设置
class Option(models.Model):
    language_name = models.CharField('当前语言', max_length=8)
    # ========基本设置
    logo = models.ImageField(verbose_name="上传logo", upload_to="up_image", blank=True)
    site_name = models.CharField('网站名称', max_length=50)
    site_describe = models.CharField('网站描述', max_length=50)
    site_footer = models.CharField('页脚信息', max_length=50)
    record = models.CharField('备案信息', max_length=50)
    footer_left = RichTextUploadingField('页脚左部')
    footer_content = RichTextUploadingField('页脚中部')
    footer_right = RichTextUploadingField('页脚右部')
    keywords = models.TextField('关键词')
    # ========主页设置
    swiper01 = models.ImageField('轮播图1', upload_to="swiper_img", blank=True)
    swiper02 = models.ImageField('轮播图2', upload_to="swiper_img", blank=True)
    swiper03 = models.ImageField('轮播图3', upload_to="swiper_img", blank=True)
    product_card = models.ManyToManyField(Product, verbose_name='选择首页展示产品', blank=True)
    d = (('up', u'向上滚动'), ('down', u'向下滚动'))
    direction = models.CharField(u"滚动方向", choices=d, max_length=10)
    scrolling_text = RichTextUploadingField('滚动文本')
    # ========页面设置
    company_info = RichTextUploadingField('公司简介', null=True, blank=True)
    company_organization = RichTextUploadingField('组织机构', null=True, blank=True)
    company_environment = RichTextUploadingField('科研环境', null=True, blank=True)
    company_recruit = RichTextUploadingField('招聘职位', null=True, blank=True)
    contact_information = RichTextUploadingField('联系方式', null=True, blank=True)
    company_map = models.FileField(verbose_name="上传地图文件", upload_to="up_file", blank=True)
    qqgroup = models.TextField('QQ群')
    qqonline = models.TextField('QQ在线')

    def __str__(self):
        return '{}'.format(self.site_name)

    class Meta:
        verbose_name = '其它设置'
        verbose_name_plural = verbose_name
