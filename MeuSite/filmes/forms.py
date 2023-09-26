from django import forms

from filmes.models import Filme

class InsereFilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'nacionalidade', 'ano', 'sinopse', 'diretor', 
                  'nota', 'review', 'visto']
        
class AtualizaFilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'review', 'nota']
        
        def salva(self, commit = True):
            filmeInsert = self.instance
            filmeInsert.titulo = self.cleaned_data['titulo']
            filmeInsert.nacionalidade = self.cleaned_data['nacionalidade']
            filmeInsert.ano = self.cleaned_data['ano']
            filmeInsert.sinopse = self.cleaned_data['sinopse']
            filmeInsert.diretor = self.cleaned_data['diretor']
            filmeInsert.nota = self.cleaned_data['nota']
            filmeInsert.review = self.cleaned_data['review']
            filmeInsert.visto = self.cleaned_data['visto']
            
            if commit:
                filmeInsert.save()
            
            return filmeInsert
