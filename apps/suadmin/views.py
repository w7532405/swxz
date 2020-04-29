from django.shortcuts import render
from apps.user.forms import RegisterForm
from apps.user.models import User
from django.views.generic import ListView
from .list import run_main
def create_user(request):
    if request.method=='POST':
        # telephone=request.POST.get('telephone')
        # name=request.POST.get('name')
        # sex=request.POST.get('sex')
        # id_card=request.POST.get('id_card')
        # email = request.POST.get('email1')
        # password=request.POST.get('password')
        # print(telephone,name,sex,id_card,email,password)
        form=RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            sex=form.cleaned_data.get('sex')
            id_card=form.cleaned_data.get('id_card')
            email = request.POST.get('email1')
            if email:
                user = User.objects.create_user(name=name, telephone=telephone, sex=sex, id_card=id_card,email=email,password=password)
            else:
                user = User.objects.create_user(name=name, telephone=telephone, sex=sex, id_card=id_card,password=password)
            user.save()
            errors=['添加成功！']
        else:
            errors=[]
            for value in form.get_errors().values():
                if value[0]=='This field is required.':
                    errors.append('必填项不能为空！')
                else:
                    errors.append(value[0])
            errors=set(errors)
        return render(request, 'detail/suadmin/cre_user.html',{'errors':list(errors)})
    else:
        return render(request, 'detail/suadmin/cre_user.html')

def create_users(request):
    # for i in range(100):
    #     list_a=run_main()
    #     name=list_a[0];telephone=list_a[1];id_card=list_a[2];sex=list_a[3]
    #     user=User.objects.create_user(telephone=telephone,password='123456',name=name,id_card=id_card,sex=sex)
    #     user.save()
    # print('生成成功！！！')
    return render(request, 'detail/suadmin/cre_users.html')
def change_user(request):
    return render(request, 'detail/suadmin/cha_user.html')
def delete_user(request):
    return render(request, 'detail/suadmin/del_user.html')
def show_user(request):

    return render(request, 'detail/suadmin/show_user.html')
class UserListView(ListView):
    model = User
    template_name = 'detail/suadmin/show_user.html'
    context_object_name = 'users'
    paginate_by = 9
    page_kwarg = 'p'
    ordering = 'name'
    def get_context_data(self, *, object_list=None, **kwargs):
        content=super(UserListView,self).get_context_data(*kwargs)
        paginator = content.get('paginator')
        page_obj = content.get('page_obj')
        pagination_data = self.get_paginate_data(paginator, page_obj)
        content.update(pagination_data)
        return content
    def get_paginate_data(self,paginator,page_obj,around_count=2):
        current_page=page_obj.number
        num_pages=paginator.num_pages
        left_has_more=False
        right_has_more=False
        if current_page<=around_count+2:
            left_pages=range(1,current_page)
        else:
            left_has_more=True
            left_pages=range(current_page-around_count,current_page)
        if current_page>=num_pages-around_count-1:
            right_pages=range(current_page+1,num_pages+1)
        else:
            right_has_more=True
            right_pages=range(current_page+1,current_page+around_count+1)
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'num_pages':num_pages,
        }