# poled_Official

### 介绍
Python 3.7.2 + Django

### 安装教程

安装文件

    pip install -r requirements.txt  #
    
创建数据库(postgreSQL)

    CREATE DATABASE poledofficial ENCODING 'utf-8';
    CREATE USER poled WITH ENCRYPTED PASSWORD '19301bbb';    
    GRANT ALL PRIVILEGES ON DATABASE poledofficial TO poled;

初始化表

	python manage.py migrate

修改了model之后, 生成数据库修改脚本(放入git)

	python manage.py makemigrations

有新的修改脚本，应用到数据库表里

	python manage.py migrate

创建超级用户(admin)

	python manage.py createsuperuser
	
执行语句添加默认数据
    
    python manage.py default_data
        
然后启动项目即可使用
