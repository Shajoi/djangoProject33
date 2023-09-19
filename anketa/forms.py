from django import forms

class Nashaforma(forms.Form):
    name = forms.CharField(label='Ваше имя')
    num = forms.IntegerField(label='Номер', required=False, max_value=100,initial=12, help_text='помогите',)

class Forma2(forms.Form):
    pass

class Forma3(forms.Form):
    k1 = forms.DecimalField(label='десятичные числа', decimal_places=True)
    k2 = forms.EmailField(label='email')
    k3 = forms.BooleanField(label='поставьте галочку')
    k4 = forms.NullBooleanField(label='вы человек')
    k5 = forms.URLField(label='adres', help_text='https://qwerqwerqw.com')
    k6 = forms.GenericIPAddressField(label='ip')
    k7 = forms.FilePathField(label='выберите файл', path='C:\\Users\\serge\\Desktop', allow_folders=True, match='.*\.txt')
    k8 = forms.ImageField(label='picture')
    k9 = forms.FileField(label='файл')
    vibor = (1,('En'),(2,'Ru'),(3,'Fr'))
    k10 = forms.TypedChoiceField(coerce=vibor)

class Uploadforma(forms.Form):
    name = forms.CharField()
    img = forms.ImageField()

class Socialform(forms.Form):
    name = forms.CharField(label='имя')
    surname = forms.CharField(label='фамилия')
    otchestvo = forms.CharField(label='отчество')
    vibor_age = ((1,'Молодой'),(2,'Зрелый'),(3,'Старый'))
    vibor_iazik = ((1,'En'),(2,'Ru'),(3,'Fr'))
    age = forms.TypedChoiceField(label='возраст',coerce=vibor_age)
    language = forms.TypedChoiceField(label='язык',coerce=vibor_iazik)
    email = forms.EmailField(label='email')
    can_cook = forms.BooleanField(label='может готовить')
    with_cat = forms.BooleanField(label='живёт с котом')
    img = forms.ImageField(label='картинка')