# yqmap
首先在本地数据库中创建yq1数据库：  CREATE DATABASE yq1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
在mysite目录下使用命令 python manage.py makemigrations
再使用 python manage.py migrate
以上两步操作是把python写的对数据库中表的创建写成迁移文件，然后迁移到数据库，这样数据库中就生成了各个表
执行 python manage.py createsuperuser  创建超级管理员可以查看修改后台数据
执行 python manage.py runserver 后查看给定的本地端口连接并通过添加url admin/、index/、news/ 查看后台、地图和新闻 
最后记得关闭server