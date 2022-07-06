from django.shortcuts import render, redirect
from django.views import generic
from .forms import InquiryForm, ImgForm
from .models import Sample
from config.settings import *
import shutil
import os

class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = ImgForm

    # postメソッドをオーバーライドする
    def post(self, request, *args, **kwargs):
        form = ImgForm(request.POST)

        # 前の画像データを消す
        shutil.rmtree(MEDIA_ROOT)
        os.mkdir(MEDIA_ROOT)

        # フォームから受け取った画像データを保存する
        sample = Sample()
        sample.img = request.FILES['img']
        sample.save()

        #sample_imgをresult.htmlで表示できるか
        #削除予定↓
        sample_img = sample.img

        #画像判定モデルの使用
        from personal_color_finder import personal_color_finder
        img = request.FILES['img']
        base_value = personal_color_finder(img)

        #モデルで結果をDBから取り出し
        #ここに処理を書く


        #結果をresult.htmlに送ってHTML生成
        return render(request, 'result.html', {
            #'form': self.form_class , 'result': result ,
            'sample_img': sample_img
            }
        )



class InquiryView(generic.FormView):
    template_name = "form.html"
    form_class = InquiryForm


class IntroductionView(generic.TemplateView):
    template_name = "introduction.html"


class ResultView(generic.TemplateView):
    template_name = "result.html"

class LoginView(generic.TemplateView):
    template_name = "login.html"