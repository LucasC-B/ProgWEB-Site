from django import forms
from usuarios.models import Usuario

sexChoices = [
        ('1','Masculino'),
        ('2','Feminino'),
        ('3','Indeterminado'),
    ]

class UsuarioModel2Form(forms.ModelForm):

    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Data de nascimento',
        help_text='Nascimento no formato DD/MM/AAAA',
    )

    sex = forms.ChoiceField(
        choices=sexChoices, 
        label='Sexo',
    )

    class Meta:
        model = Usuario
        fields = '__all__'