from django.core.management import BaseCommand

from poled.models import Option, Language, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Language.objects.create(
            language_name="中文",
            language_tag="cn"
        )
        Language.objects.create(
            language_name="英文",
            language_tag="en"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="post",
            category_name="员工天地"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="post",
            category_name="企业新闻"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="post",
            category_name="行业新闻"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="file",
            category_name="产品目录"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="file",
            category_name="文献解析"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="钙钛矿材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="电子与空穴传输材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="热延迟荧光材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="聚合物光电材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="有机荧光材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="有机磷光材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="有机光伏材料"
        )

        Category.objects.create(
            select_language_id="1",
            category_type="product",
            category_name="特种材料"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="post",
            category_name="trade news"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="post",
            category_name="Company News"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="post",
            category_name="Industry News"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="file",
            category_name="Product Catalog"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="file",
            category_name="Document Analysis"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Perovskite Materials"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="TADF Material"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Electron And Hole Transport Material"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Polymer Optoelectronic Materials"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Organic Phosphorescent Material"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Organic Fluorescent Material"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Organic Photovoltaic Material"
        )

        Category.objects.create(
            select_language_id="2",
            category_type="product",
            category_name="Special Materials"
        )

        Option.objects.create(language_name='中文设置'
                              , logo='up_image/cn_logo.png'
                              , swiper01='swiper_img/swiper1.jpg'
                              , swiper02='swiper_img/swiper2.jpg'
                              , swiper03='swiper_img/swiper3.jpg'
                              , site_name='西安宝莱特光电科技有限公司'
                              , site_describe='西安宝莱特光电科技有限公司'
                              , site_footer='© 西安宝莱特光电科技有限公司'
                              , record='陕ICP备19012968号-1'
                              , keywords='宝莱特,西安'
                              , footer_left='西安宝莱特光电科技有限公司由国家“千人计划”专家赵炜博士发起创立于2007年，注册资本5000万元。发改委批准依托该公司成立陕西省平板显示技术工程研究中心，工信厅和科技厅等给予重点支持。公司（中心）以推动有机发光二极管技术产业化为目标。'
                              , footer_content='所有产品展示'
                              , footer_right='地址: 陕西省西安市高新区定昆池三路1199号<br />电话：029-81101199<br />邮箱: info@p-oled.cn<br />传真:  +86-029-81101199<br />手机:  15702951000'
                              , direction='up'
                              , scrolling_text='西安宝莱特光电科技有限公司由国家“千人计划”专家赵炜博士发起创立于2007年，注册资本5000万元。发改委批准依托该公司成立陕西省平板显示技术工程研究中心，工信厅和科技厅等给予重点支持。公司（中心）以推动有机发光二极管技术产业化为目标。'
                              )

        Option.objects.create(language_name='英文设置'
                              , logo='up_image/en_logo.png'
                              , swiper01='swiper_img/swiper1.jpg'
                              , swiper02='swiper_img/swiper2.jpg'
                              , swiper03='swiper_img/swiper3.jpg'
                              , site_name="Xi'an Polymer Light Technology Corp."
                              , site_describe="Xi'an Polymer Light Technology Corp."
                              , site_footer="© Xi'an Polymer Light Technology Corp."
                              , record='陕ICP备19012968号-1'
                              , keywords='P-oled'
                              , footer_left='Xi’an Polymer Light Technology Corp. (PLT) was found in 2007 by Dr. Zhao Wei, a member of the （Recruitment Program of Global Experts of China）, with a 50,000,000 RMB (US$ 8,000,000) capitalization. The Shaanxi FPD Research & Engineering Center (the Center) was established within PLT by unrelenting support from the Shaanxi Provincial Development & Reform Committee, the Provincial Offices of Industry & Information and Science & Technology. Their objective is to make it feasible to produce organic light-emitting diodes industrially.'
                              , footer_content='所有产品展示'
                              , footer_right='Add: No. 1199, 3rd Dingkunchi Road, Hi-tech District, Xi’an<br />Tel: +86-029-81101199<br />Email: info@p-oled.cn<br />Fax:  +86-029-81101199<br />Mobile: +86-15702951000'
                              , direction='up'
                              , scrolling_text='Xi’an Polymer Light Technology Corp. (PLT) was found in 2007 by Dr. Zhao Wei, a member of the （Recruitment Program of Global Experts of China）, with a 50,000,000 RMB (US$ 8,000,000) capitalization. The Shaanxi FPD Research & Engineering Center (the Center) was established within PLT by unrelenting support from the Shaanxi Provincial Development & Reform Committee, the Provincial Offices of Industry & Information and Science & Technology. Their objective is to make it feasible to produce organic light-emitting diodes industrially.'
                              )

        # TODO use logging

        self.stdout.write('{}'.format('网站创建成功,您可以通过IP访问网站了'))
