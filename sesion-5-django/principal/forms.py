from django import forms


class FormularioPrincipal(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30)
    apellido = forms.CharField(label="Apellido", max_length=30)
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.SelectDateWidget(years=range(1900, 2026)),
    )

    GENERO_OPCIONES = [("M", "Masculino"), ("F", "Femenino")]
    genero = forms.ChoiceField(
        choices=GENERO_OPCIONES, widget=forms.RadioSelect, label="Genero"
    )

    clave = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
