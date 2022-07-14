from asyncio.log import logger
import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import InquiryForm, PersonalForm
from .models import Sample
from config.settings import *
import shutil
import os

logger = logging.getLogger(__name__)

class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = PersonalForm

    # postメソッドをオーバーライドする
    def post(self, request, *args, **kwargs):
        form = PersonalForm(request.POST)

        # フォームから受け取ったデータをmodelのフィールドに格納
        sample = Sample()
        sample.gender = request.POST.get('gender', None)

        #性別確認テスト
        print(sample.gender)

        #画像判定モデルの使用---ここから---
        img = request.FILES['img']
        from .pcf_model import finder

        finder(img)
        
        # base_value = personal_color_finder(img)

        #---ここまで---

        #モデルで結果をDBから取り出し変数に格納
        ###モデルの呼び出し###


        #結果をresult.htmlに送ってHTML生成
        context={
            ###データベースからのデータを渡す処理
        }
        return render(request, 'result.html', context)
        # {
        #     'form': self.form_class , 
        #     #'result': result ,
        #     'sample_img': sample_img,
        #     }
        #)


class InquiryView(generic.FormView):
    template_name = "form.html"
    form_class = InquiryForm
    success_url = reverse_lazy('personal_color:form')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class IntroductionView(generic.TemplateView):
    template_name = "introduction.html"


class LoginView(generic.TemplateView):
    template_name = "login.html"
    

class LogoutView(generic.TemplateView):
    template_name = "signup.html"


class MembersView(generic.TemplateView):
    template_name = "members.html"