from django import forms

from mail_service.models import Messages


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class MessagesForm(StyleFormMixin, forms.ModelForm, ):

    class Meta:
        model = Messages
        exclude = ('user',)

    def clean_title(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['title']

        for item in words:
            if item in cleaned_data.lower():
                raise forms.ValidationError(f'"{item}" запрещено, выберите другое')

        return cleaned_data

    def clean_body(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['body']

        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'"{word}" запрещено, выберите другое')

        return cleaned_data