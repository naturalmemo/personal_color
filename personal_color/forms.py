import os
from django import forms
from .models import Sample
from django.core.mail import EmailMessage


class InquiryForm(forms.Form):
    CHOICE = [
        ( 'アプリについて', 'アプリについて'),
        ( '商品について', '商品について'),
        ( 'その他について', 'その他について'),
    ]

    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.ChoiceField(label='お問い合わせの種類', widget=forms.Select, choices= CHOICE, initial=0)
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].widget.attrs['placeholder']='山田 太郎'

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='xxx@email.com'

        self.fields['title'].widget.attrs['class']='form-control'

        self.fields['message'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['rows']='3'


    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせの種類{}'.format('title')
        message = '送信者名: {0}\nメールアドレス: {1}\nお問い合わせの種類: {2}\nお問い合わせ内容:\n{3}'.format(name, email, title, message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message,
        from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Sample

        fields = ('gender', 'img')

        widgets = {
            'gender':forms.RadioSelect
        }
