from django.contrib import admin

from poled.models import Category, PostArticle, Language, Product, UploadFile, Poledfeedback, Option

admin.site.site_title = "P-oled后台管理"
admin.site.site_header = "P-oled"


@admin.register(PostArticle)
class PostArticleAdmin(admin.ModelAdmin):  # 文章
    list_display = ('shorten_title', 'shorten_contents', 'author', 'time', 'select_category', 'select_language', 'post_status')
    list_editable = ('select_category', 'select_language', 'post_status')
    search_fields = ('title', 'contents', 'select_category', 'post_status')

    fieldsets = (
        ('文章设置', {
            'fields': ('summary', 'select_language', 'select_category', 'post_status')
        }),
        ('编辑文章', {
            'fields': ('title', 'contents')
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        if db_field.name == "select_category":
            kwargs["queryset"] = Category.objects.filter(category_type="post")
            return db_field.formfield(**dict(**kwargs))
        else:
            kwargs["queryset"] = Language.objects.all()
            return db_field.formfield(**dict(**kwargs))

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # 产品
    list_display = ('shorten_product_title', 'shorten_product_description', 'select_category', 'select_language', 'product_status')
    list_editable = ('select_category', 'select_language', 'product_status')
    search_fields = ('title', 'description', 'select_category')

    fieldsets = (
        ('产品设置', {
            'fields': ('image', 'select_language', 'select_category', 'product_status')
        }),
        ('编辑产品', {
            'fields': ('title', 'subtitle', 'description')
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        if db_field.name == "select_category":
            kwargs["queryset"] = Category.objects.filter(category_type="product")
            return db_field.formfield(**dict(**kwargs))
        else:
            kwargs["queryset"] = Language.objects.all()
            return db_field.formfield(**dict(**kwargs))

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):  # 上传文件
    list_display = ('name', 'select_language',)

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        if db_field.name == "select_category":
            kwargs["queryset"] = Category.objects.filter(category_type="file")
            return db_field.formfield(**dict(**kwargs))
        else:
            kwargs["queryset"] = Language.objects.all()
            return db_field.formfield(**dict(**kwargs))


@admin.register(Poledfeedback)
class PoledfeedbackAdmin(admin.ModelAdmin):  # 留言反馈
    list_display = ('name', 'email', 'qq', 'phone', 'shorten_product_message')
    readonly_fields = ('name', 'email', 'qq', 'phone', 'message')

    def has_edit_permission(self, request):
        return False

    def has_add_permission(self, request):
        """
        返回当前用户是否有添加权限
        """
        return False

    def has_delete_permission(self, obj=None):
        """
        返回当前用户是否有删除权限
        """
        return True


@admin.register(Category)
class CategoryCnAdmin(admin.ModelAdmin):  # 分类
    list_display = ('category_name', 'category_type', 'select_language')
    list_editable = ('category_name', 'category_type', 'select_language')
    list_display_links = None


@admin.register(Option)
class OptionsAdmin(admin.ModelAdmin):  # 设置
    list_display = ('site_name', 'site_footer', 'record', 'keywords', 'language_name')
    readonly_fields = ('language_name',)
    style_fields = {'product_card': 'm2m_transfer'}

    fieldsets = (
        ('基本设置', {
            'fields': ('logo', 'site_name', 'site_describe', 'site_footer', 'record', 'footer_left', 'footer_content', 'footer_right')
        }),
        ('主页设置', {
            'fields': ('swiper01', 'swiper02', 'swiper03', 'product_card', 'direction', 'scrolling_text')
        }),
        ('页面设置', {
            'fields': ('company_info', 'company_organization', 'company_environment', 'company_recruit', 'contact_information', 'company_map')}),
        ('其他设置', {
            'fields': ('language_name', 'keywords', 'qqgroup', 'qqonline')}),
    )

    def has_add_permission(self, request):
        """
        返回当前用户是否有添加权限
        """
        return False
        # return True

    def has_delete_permission(self, request, obj=None):
        """
        返回当前用户是否有删除权限
        """
        return False