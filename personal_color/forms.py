import email
from django import forms
# #from .models import UploadImage

# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = UploadImage
#         fields = ['image']

class InquiryForm(forms.Form):
    CHOICE = {
    ('0','商品について'),
    ('1','アプリについて'),
    ('2','その他について'),
}

    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.ChoiceField(label='タイトル', widget=forms.RadioSelect, choices= CHOICE, required=True)
    message = forms.CharField(laber='メッセージ', widget=forms.Textarea)