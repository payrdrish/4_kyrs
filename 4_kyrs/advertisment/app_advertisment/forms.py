from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label='Заголовок')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}), label='Описание')
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                               min_value=0, label='Цена')

    auction = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input'}), required=False,
        label='Возможность торга'
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}), label='Изображение', required=False)