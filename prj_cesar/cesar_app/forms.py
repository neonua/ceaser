from django import forms


class SampleForm(forms.Form):
    """Form text and shift

    """
    text = forms.CharField(
        label='Text',
        max_length=512,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your text',
            'class': 'form-control',
            'cols': 10,
            'rows': 10,
            'style': 'resize:none;'
        })
    )

    shift = forms.CharField(
        label='Shift',
        max_length=8,
        widget=forms.NumberInput(attrs={
            'value': '3',
            'class': 'form-control',
            'style': 'width:80px;'
        })
    )
