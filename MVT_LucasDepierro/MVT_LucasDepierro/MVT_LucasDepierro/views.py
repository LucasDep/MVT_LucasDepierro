from json import load
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from appFamilia.models import Familiar
import datetime
import sqlite3

def saludo(request):
    fechaNac=datetime.date(1997,8,25)
    documentoDeTexto=f"Hola Django - Coder- {fechaNac}"

    return HttpResponse(documentoDeTexto)

#def familiar(self): 

    #con = sqlite3.connect('db.sqlite3')#Conecto a la DB
    #cur = con.cursor()#Puntero de la DB
    
    #diccionario={}
    #indice=0

    #for row in cur.execute('SELECT * FROM appFamilia_familiar ORDER BY id'):
    #    diccionario[indice]=row
    #    indice+=1

    #for (x) in diccionario:
    #    print(x)

    #plantilla = loader.get_template('template_0.html')

    #documento = plantilla.render(diccionario)
    
    #con.close()#Cierro conección con la DB
    
    #return HttpResponse(documento)

def familiar(self):
    
    #Cargo y guardo cada uno de los valores en la base de datos
    lucas = Familiar(nombre="Lucas",apellido="Depierro",edad=24,fechaNac=datetime.datetime.strptime('1997-8-25', "%Y-%m-%d"))
    lucas.save()

    tomas = Familiar(nombre="Tomas",apellido="Depierro",edad=21,fechaNac=datetime.datetime.strptime('2001-5-3', "%Y-%m-%d"))
    tomas.save()

    laura = Familiar(nombre="Laura",apellido="Comezaña",edad=47,fechaNac=datetime.datetime.strptime('1974-6-30', "%Y-%m-%d"))
    laura.save()

    miguel = Familiar(nombre="Miguel",apellido="Depierro",edad=58,fechaNac=datetime.datetime.strptime('1963-11-18', "%Y-%m-%d"))
    miguel.save()

    #Genero un diccionario para poder pasarlo a la plantilla
    diccionario={"nombre":lucas.nombre,"apellido":lucas.apellido,"edad":lucas.edad,"fechaNac":lucas.fechaNac,
                "nombreH":tomas.nombre,"apellidoH":tomas.apellido,"edadH":tomas.edad,"fechaNacH":tomas.fechaNac,
                "nombreM":laura.nombre,"apellidoM":laura.apellido,"edadM":laura.edad,"fechaNacM":laura.fechaNac,
                "nombreP":miguel.nombre,"apellidoP":miguel.apellido,"edadP":miguel.edad,"fechaNacP":miguel.fechaNac}

    plantilla = loader.get_template('template_0.html')
    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
