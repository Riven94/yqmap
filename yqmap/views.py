from django.shortcuts import render

# Create your views here.
from yqmap.models import NewsPost,User,City
def index(request):
    q = request.GET.get('q')
    # q='2021-5-24'
    if q:
        post_list = User.objects.filter(name=q)
        return render(request, 'indexx.html', {
            'post_list': post_list,
        })
    if not q:
        return render(request, 'indexx.html')

def new_index(request):
    new_list = NewsPost.objects.all()  # 获取所有数据
    return render(request,'index.html', {'new_list':new_list})   # 返回index.html页面