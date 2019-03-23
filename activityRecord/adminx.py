import xadmin
from django.contrib.auth.models import User,Group
from django.contrib import admin
from  activityRecord import models
from xadmin import views
from django.db.models import Q



@xadmin.sites.register(models.MemberInfo)
class memberAdmin(object):
    list_display = ('name','mem_id','post','sex','phoneNum','join_date','notice',)
    list_editable = ('notice',)
    list_per_page = 50
    ordering = ('-join_date',)
    list_filter = ('sex', 'join_date','post') #过滤器
    search_fields = ('name', 'mem_id')          #搜索字段
    date_hierarchy = 'join_date'        #详细时间分层筛选
    #model_icon="fa fa-user"
    model_icon="fa fa-user"


@xadmin.sites.register(models.actInfo)
class actAdmin(object):
    list_display = ('name','phone','notice')
    list_editable = ('notice',)


@xadmin.sites.register(models.actRecord)
class actRecordAdmin(object):
    list_display = ('act','member','score','address','start_time','duration','notice')
    list_editable = ('notice',)
    ordering = ('-start_time',)
    list_filter = ('member', 'act') #过滤器
    search_fields = ('act', )          #搜索字段
    date_hierarchy = 'start_time'        #详细时间分层筛选
    model_icon="fa fa-tag"


@xadmin.sites.register(models.allRecorddView)
class allRecorddViewAdmin(object):
    list_display = ('name','post',"mem_id","actname",'join_time',"score")
    ordering = ('post','mem_id','name')
    search_fields = ('name','actname' )
    list_filter = ('name', 'actname')
    model_icon = 'fa fa-envelope'

@xadmin.sites.register(models.allRecordSumView)
class allRecorddViewAdmin(object):
    list_display = ('name','post',"mem_id","score")
    ordering = ('post','mem_id','name')
    search_fields = ('name' )
    list_filter = ('name', )
    model_icon="fa fa-check"

admin.site.site_header = '社区党员积分系统'
admin.site.site_title='社区党员积分系统'
admin.site.index_title='社区党员积分系统'

@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True


@xadmin.sites.register(views.CommAdminView)
class GlobalSettings(object):
    site_title='社区党员积分系统'
    site_footer='社区党员积分系统'
    menu_style='according' #设置菜单收起功能
    site_header = '社区党员积分系统'
    index_title = '社区党员积分系统'