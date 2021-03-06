"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from Blog import settings
from myBlog import views
from django.views import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # 网站首页
    path('list-<int:lid>.html', views.list, name='list'),  # 列表页
    path('show-<int:sid>.html', views.show, name='show'),  # 内容页
    path('tag/<tag>', views.tag, name='tags'),  # 标签列表页
    path('s/', views.search, name='search'),  # 搜索列表页
    path('about/', views.about, name='about'),  # 联系我们单页
    path('accounts/', include('allauth.urls')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('deletecomment/', include('comment.deleteUrls', namespace='deletecomment')),
    path('404/', views.page_not_found, name='404'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
]
