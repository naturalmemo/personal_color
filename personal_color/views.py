from asyncio.log import logger
import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import InquiryForm, PersonalForm
from .models import Sample
from config.settings import *
from config.settings_dev import *
from .models import Base_type, Colors, Items

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
        sample.img = request.FILES['img']
        sample.save()
        img_path = sample.img.url
        

        #性別確認テスト
        print(sample.gender)
        print(img_path)

        #画像判定モデルの使用
        from .pcf_model.main import finder
        try:
            S, contrast = finder("." + img_path)
            print(S, contrast)
        except IndexError:
            return render(request, 'index.html', context={
                'form': self.form_class, 
                'error_message': '※顔を認識できませんでした。\n別の写真でお試しください。',
            })
        except Exception:
            return render(request, 'index.html', context={
                'form': self.form_class, 
                'error_message': '※画像ファイルを読み込めませんでした。\n別の写真でお試しください。',
            })

        
        #モデルで結果をDBから取り出し変数に格納
        ###モデルの呼び出し###
        # from .models import Colors
        # model = Colors
        # colors = get_queryset(self)
        # def get_queryset(self):
        #     colors = Colors.objects.filter(base_type_id=4)
        #     return colors
        
        # def get_queryset(self):
        #     return super().get_queryset()
        
        

        #結果をresult.htmlに送ってHTML生成
        # context={
        #     'colors': colors
        # }
        return render(request, 'result.html')
        # {
        #     #'result': result ,
        #     }
        # )
        # def get_success_url(self):
        #     return reverse_lazy("personal_color:result", kwargs={"pk": 2222})

class ResultView(generic.ListView):
    template_name = "result.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context["base"] = Base_type.objects.filter(id=1).first()
        context["colors"] = Colors.objects.filter(base_type=1)
        return render(request, 'result.html', context)

    # def get(self, request, *args, **kwargs):
    #     base_type = Base_type.objects.filter(id=1).first()
    #     colors = base_type.colors_set.all()
    #     context = {}
    #     context["base"] = base_type
    #     context["colors"] = colors
    #     context["items"] = Items.objects.filter()
    #     return render(request, 'result.html', context)

    # def get_queryset(self):
    #     #colors = Colors.objects.filter(base_type_id__exact=1).all()
    #     # items = Items.objects.filter(colors__base_type__id=1).all()
    #     #items = Items.objects.filter(color=1).all()
    #     base_type = Base_type.objects.select_related().get(id=1)
    #     return base_type
    #colors = Colors.objects.filter(base_type_id__exact=1).all()
    # items = Items.objects.filter(colors__base_type__id=1, gender=1).all()
    
    # def get_queryset(self):
    #     return Base_type.objects


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


class TestView(generic.TemplateView):
    template_name = "403.html"