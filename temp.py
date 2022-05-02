import os 
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "mysite.setting")
django.setup()
from m7_python.models import Inmuebles, Region

def get_list_inmuebles(name,descr):
    lista_inmuebles = Inmuebles.objects.filter(nombre_inmueble_contains=name).filter(descripcion_contains=descr)

    archil=open("datos.txt", "w")
    for l in lista_inmuebles.values():
        archil.white(str(1))
        archil.white("\n")
    archil.close()

    return lista_inmuebles

#resultado=get_list_inmuebles("Providencia","Cocina")

def get_list_inmuebles_by_comuna(comuna):
    select = f"""
    SELECT A.id,
    A.nombre_inmueble, 
    A.descripcion
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE C.comuna LIKE '%%{str(comuna)}%%'
    """

    results = Inmuebles.objects.raw(select)

    archi1 = open("datos.txt","w")
    for p in results:
        archi1.write(p.nombre_inmueble+','+p.descripcion)
        archi1.write("\n")
    archi1.close()

def get_list_inmueble_region(id):
    region = str(Region.objects.filter(id=id).values()[0]["Region"])

    lista_inmuebles = Inmuebles.objects.filter(id_region_id =id)
    archi1=open("datos.txt","w")
    for l in lista_inmuebles.values():
        archi1.write(str(l["nombre_inmueble"]))
        archi1.write(',')
        archi1.write(region)
        archi1.write("\n")
    archi1.close()
#get_list_inmueble_region(16)

def get_list_inmuebles_by_region(region):
    select = f"""
    SELECT A.id,    
    A.nombre_inmueble,
    A.descripcion
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE B."Region" LIKE '%%{str(Region)}%%'
    """

    result = Inmuebles.objects.raw(select)


    archi1=open("datos.txt","w")
    for p in result:
        archi1.write(p.nombre_inmueble+','+p.descripcion)
        archi1.write("\n")
    archi1.close()

get_list_inmuebles_by_region("Metrop")




    

