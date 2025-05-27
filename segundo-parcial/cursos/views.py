from django.shortcuts import render

cursos=[{'codigo':1,'nombre':'inf-133'},
        {'codigo':2,'nombre':'inf-131'},
        {'codigo':3,'nombre':'inf-124'},
        {'codigo':4,'nombre':'inf-124'},
        {'codigo':5,'nombre':'inf-124'},
        ]

def listado_cursos(request):

    return render(request, 'cursos/listado_cursos.html', {'cursos':cursos})

def detalle_curso (request,codigo):
    curso=cursos[codigo-1]

    return render(request,'cursos/detalle_curso.html', {'curso':curso})
