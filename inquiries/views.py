from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView, TemplateView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Inquiry


#LoginRequiredMixin:ログインしていないのにページにアクセスが来たら，ログインページを表示させる

#自作したテンプレートを使う場合は'TemplateView'を用いる
class ContactView(TemplateView):
    template_name = 'contact.html'

#inquirys/url.py/でマッチしたら実行されるのがビュー

#subクラスで継承したいsuperクラスのimport順も重要
class InquiryListView(ListView):
    model = Inquiry
    #template_nameは表示させるwebページのテンプレートのファイル名.
    #template_nameはListViewクラスで使う変数だから，他の名前にするとかはできない．
    template_name = 'inquiry_list.html'



class InquiryDetailView(LoginRequiredMixin, DetailView):
    model = Inquiry
    template_name = 'inquiry_detail.html'
    login_url = 'login'

class InquiryUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Inquiry
    #fielsdにはinquiryの更新したいfieldを渡す．指定したfieldsがwebページ常に表記される
    #今回は，タイトルと本文を更新対象とするので，title, bodyとしている．
    #modelにはInquiryを使っていて，Inquiryはfieldsにtitle, author, body, dateを持っている．
    #つまり，fields = ('author','title','body') とすれば，authorも変更できる．
    # （authorを変更することは普通はないから，含めていない．）
    #'date'もfieldsとしてあるが，dateはnon-editable fieldsなので，含めることは不可
    fields = ('title','body',)
    template_name = 'inquiry_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class InquiryDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Inquiry
    template_name = 'inquiry_delete.html'
    #投稿を削除した後のページのurl_nameが'inquiry_list'
    success_url = reverse_lazy('inquiry_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class InquiryCreateView(LoginRequiredMixin,CreateView):
    model = Inquiry
    template_name = 'inquiry_new.html'
    fields = ('title','body',)
    #login_urlはログインしていない状態で，inquiries/new/にアクセスした場合にリダイレクトするurl_nameである．
    #ログインしていないのにinquirys/new/にアクセスして，新規投稿ができるのはおかしいから．
    login_url = 'login'

    #新規で投稿する場合，ログインしているユーザ名がauthorとなるようにしている．
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)