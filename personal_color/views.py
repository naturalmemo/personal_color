
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
#from .forms import DocumentForm
#from .models import Document
#import cv2
from django.conf import settings

from .forms import InquiryForm

# def index(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = DocumentForm()
#         max_id = Document.objects.latest('id').id
#         obj = Document.objects.get(id = max_id)
#         input_path = settings.BASE_DIR + obj.photo.url
#         output_path = settings.BASE_DIR + "/media/output/output.jpg"
#         gray(input_path,output_path)

#     return render(request, 'app1/index.html', {
#         'form': form,
#         'obj':obj,
#     })


# ###########ここをカスタマイズ############

# def gray(input_path,output_path):
#     img = cv2.imread(input_path)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite(output_path, img_gray)

# ######################################

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "form.html"
    form_class = InquiryForm


class IntroductionView(generic.TemplateView):
    template_name = "introduction.html"


class ResultView(generic.TemplateView):
    template_name = "result.html"

class LoginView(generic.TemplateView):
    template_name = "login.html"