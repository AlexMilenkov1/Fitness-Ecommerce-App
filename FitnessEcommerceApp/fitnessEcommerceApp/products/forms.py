from django import forms

from fitnessEcommerceApp.products.models import Product


class BaseProductForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Product


class CreateProductForm(BaseProductForm):
    class Meta:
        fields = '__all__'
        model = Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Enter the name of the product'

            if field_name == 'description':
                field.widget.attrs['placeholder'] = 'Add a description'

            if field_name == 'price':
                field.widget.attrs['placeholder'] = 'Enter the price of the product'

            if field_name == 'in_stock':
                field.widget.attrs['placeholder'] = 'Amount of the product'


class EditProductForm(BaseProductForm):
    pass
