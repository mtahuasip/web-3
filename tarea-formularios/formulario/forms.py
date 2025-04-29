from django import forms


class FormularioUsuario(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=50)
    email = forms.EmailField(label="Dirección e-mail:")

    CIUDADES_OPCIONES = [
        ("LP", "La Paz"),
        ("SC", "Santa Cruz de la Sierra"),
        ("CB", "Cochabamba"),
        ("PT", "Potosí"),
        ("OR", "Oruro"),
        ("CH", "Chuquisaca (Sucre)"),
        ("TJ", "Tarija"),
        ("BN", "Beni"),
        ("PD", "Pando"),
        ("EA", "El Alto"),
    ]
    AFICIONES_OPCIONES = [
        ("DE", "Deportes"),
        ("CO", "Coches"),
        ("MU", "Música"),
    ]
    SEXO_OPCIONES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    ciudad = forms.ChoiceField(
        choices=CIUDADES_OPCIONES, widget=forms.Select, label="Ciudad:"
    )
    aficiones = forms.MultipleChoiceField(
        choices=AFICIONES_OPCIONES,
        widget=forms.CheckboxSelectMultiple,
        label="Aficiones:",
    )
    sexo = forms.ChoiceField(
        choices=SEXO_OPCIONES, widget=forms.RadioSelect, label="Sexo:"
    )
