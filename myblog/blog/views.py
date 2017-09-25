#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from django.core.paginator import Paginator, Page
from django import forms
# Create your views here.


def redir(request):
    return redirect('http://127.0.0.1:8000/index_1')

#博客首页
def index(request, page):
    # myblog1 =
    blog_list =MyblogModel.objects.order_by('-blog_date')
    #按一页一个开始分页
    p = Paginator(blog_list, 3)
    #如果没有传递分页信息那么当前页就为1
    if page == '':
        page = '1'
    #获取第page页的数据
    list_all = p.page(int(page))
    print(list_all)
    #获取所有的页数
    page_list = p.page_range
    content = {'title':'MiaoSen博客-首页','blog_list':blog_list, 'list_all':list_all, 'page_list':page_list, 'page':page}
    return render(request, 'blog/index.html', content)

#关于
def about(request):
    content = {'title':'MiaoSen博客-关于'}
    return render(request, 'blog/about.html', content)

#博客样式
def post(request):
    content = {'title':'MiaoSen博客-博客样式'}
    return render(request, 'blog/post.html', content)

#个人信息
def contact(request):
    content = {'title':'MiaoSen博客-作者信息'}
    return render(request, 'blog/contact.html', content)

def write_blog(request):
    content = {'title':'MiaoSen博客-写博客'}
    return render(request, 'blog/write_blog.html', content)

#获取博客内容加载到页面上面
def get_blog(request):
    myblog = MyblogModel()
    #获取博客标题
    blog_titles = request.POST.get('blog_biaoti')
    blog_text = request.POST.get('blog_text')
    myblog.blog_title = blog_titles
    myblog.blog_text = blog_text.encode('utf-8')
    myblog.save()

    image = request.FILES.get('file_img')
    img_path = './static/img/'
    with open(img_path + image.name, 'wb') as f:
        f.write(image.read())
    #保存到数据库
    blog_file = Blog_img()
    blog_file.blog_img_id = blog_titles
    blog_file.blog_img = img_path+image.name
    blog_file.save()

    return redirect('/index_1/')

#删除博客
def delete_blog(request):
    blog_id = request.POST.get('id')
    # 查询所有的博客列表
    blog = MyblogModel.objects.get(pk=blog_id)
    # 删除
    blog.delete()
    response = redirect('/index_1/')
    return response

#显示博客详细信息
def blog_detailed(request, pid):
    blog = MyblogModel.objects.get(pk=pid)
    try:
        img = Blog_img.objects.get(blog_img_id=blog.blog_title)
        content = {'blog': blog, 'image': img}
        return render(request, 'blog/blog_detailed.html', content)
    except:
        img = ''
        content = {'blog': blog, 'image': img}
        return render(request, 'blog/blog_detailed.html', content)

#删除验证
def blog_validation(request, pid):
    content = {'pid':pid}
    return render(request, 'blog/blog_validation.html', content)

def delete_validation(request, pid):
    del_pswd = request.POST.get('pswd_del')
    if del_pswd=='weige521':
        # 查询所有的博客列表
        blog = MyblogModel.objects.get(pk=pid)
        # 删除
        blog.delete()
        response = redirect('/index_1/')
    else:
        response = redirect('/blog_validation'+pid+'/')
    return response

#搜索
def search(request):
    q = request.GET.get('q')
    blog_obj = MyblogModel.objects.filter(blog_title=q)
    content = {'blog_obj':blog_obj, 'title':'MiaoSen博客-搜索信息'}
    return render(request,'blog/search.html', content)









