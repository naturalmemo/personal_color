from asyncio.log import logger
import logging
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from .forms import InquiryForm, PersonalForm
from .models import Sample
from config.settings import *
from config.settings_dev import *
from .models import Base_type, Colors, Items
from django.urls import reverse
from urllib.parse import urlencode



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
        

        # #性別確認テスト
        # print(sample.gender)
        # print(img_path)

        #画像判定モデルの使用
        from .pcf_model.main import finder
        try:
            S, contrast = finder("." + img_path)
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

        #彩度Sは50を、コントラストcontrastは70を基準にベースタイプを振り分け
        if int(S) >= 50:
            if int(contrast) < 70:
                id = 1    #春
            else:
                id = 3    #秋
        else:
            if int(contrast) < 70:
                id = 2    #夏
            else:
                id = 4    #冬


        redirect_url = reverse('result')
        parameters = urlencode(dict(param_a=id))
        url = f'{redirect_url}?{parameters}'
        return redirect(url)
        # success_url = reverse_lazy("result", id)
        # return success_url

        # def get_success_url(self):
        #     return redirect('personalcolor:result', id)

        #return render(request, 'result.html')
        # def get_success_url(self):
        #     return reverse_lazy("personal_color:result", kwargs={"pk": 2222})

class ResultView(generic.ListView):
    template_name = "result.html"
    def get(self, request, pk):
        #URLからbase取得
        context = {}
        context["base"] = Base_type.objects.filter(id=pk).first()
        context["colors"] = Colors.objects.filter(base_type=pk)
        context["items"] = Items.objects.filter(color__base_type__id=1, gender=1).all()
        return render(request, 'result.html', context)


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

