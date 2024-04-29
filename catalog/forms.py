from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category', 'owner')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and description:
            forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                               "радар"]
            for word in forbidden_words:
                if word.lower() in name.lower() or word.lower() in description.lower():
                    self.add_error(None, forms.ValidationError(
                        f'Слово "{word}" не допускается в названии или описании продукта.'))

        return cleaned_data

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(forms.ModelForm):
    is_published = forms.BooleanField(label='Опубликовать', required=False, widget=forms.RadioSelect(choices=(
        (True, 'Да'),
        (False, 'Нет'),
    )))

    class Meta:
        model = Product
        fields = ('name', 'description', 'is_published',)