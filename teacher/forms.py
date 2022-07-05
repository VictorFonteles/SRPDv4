from django.forms import ModelForm
from teacher.models import Lista_presenca, Estudante_ad

#class ListForm(ModelForm):
#    class Meta:
#        model = attendance_list
#       fields = "__all__"


class ListForm(ModelForm):

    class Meta:
        model = Lista_presenca
        fields = ['materia', 'data_criacao', 'turma']

class FormEstudante(ModelForm):

    class Meta: 
        model = Estudante_ad
        fields = "__all__"


    
