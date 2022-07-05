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
    title = forms.ChoiceField(label='お問い合わせの種類', widget=forms.RadioSelect, choices= CHOICE, initial=0)
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].widget.attrs['placeholder']='山田 太郎'

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='xxx@email'

        self.fields['title'].widget.attrs['class']='form-control'

        self.fields['message'].widget.attrs['class']='form-control'