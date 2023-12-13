from django import forms
from first_app.models import StudentModel


class ContactForm(forms.Form):
    name = forms.CharField(label= 'User Name' )
    email = forms.EmailField(label='Eamail')
    address = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),required = False,disabled=True )
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    cheack=  forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'type':'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs= {'type':'datetime-local'}))
    Choices = [('S','Small'),('M','Medium',),('L','Large')]
    Size = forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
    Foods = [('P','Pizza'),('B','Burger',),('N','Nan-Ruti')]
    food = forms.MultipleChoiceField(choices=Foods, widget=forms.CheckboxSelectMultiple)
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)




class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields ='__all__'

    date_field = forms.DateField(widget=forms.DateInput(attrs= {'type':'date'}))

    date_time_field = forms.DateTimeField(widget=forms.DateInput(attrs= {'type':'datetime-local'}))