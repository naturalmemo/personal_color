from dataclasses import field
import email
from django import forms
from .models import Sample


class InquiryForm(forms.Form):
    CHOICE = {
    ('1','商品について'),
    ('2','アプリについて'),
    ('3','その他について'),
}

    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.ChoiceField(label='お問い合わせの種類', widget=forms.Select, choices= CHOICE, initial=0)
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].widget.attrs['placeholder']='山田 太郎'

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='xxx@email'

        self.fields['title'].widget.attrs['class']='form-control'

        self.fields['message'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['rows']='3'


class ImgForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('img',)