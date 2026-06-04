alumnos = [
    {
        "id": 10,
        "nombre": 'JuanPa',
        "provincia": 'Buenos Aires',
        "estado": 'graduado'
    },
    {
        "id": 25,
        "nombre": 'Facu',
        "provincia": 'Cordoba',
        "estado": 'graduado'
    },
    {
        "id": 100,
        "nombre": 'Pepe',
        "provincia": 'Buenos Aires',
        "estado": 'en curso'
    }
]

materias = [
    {
        "id": 101,
        "nombre": "Progra I",
        "horas": 8
    },
    {
        "id": 102,
        "nombre": "Progra II",
        "horas": 8
    },
    {
        "id": 103,
        "nombre": "Progra III",
        "horas": 8
    },
    {
        "id": 104,
        "nombre": "Progra IV",
        "horas": 8
    }
]

notas_alumno_materia = [
    {
        "id": 1,
        "id_alumno": 10,
        "id_materia": 101,
        "nombre_examen": 'Primer Parcial',
        "nota": 4
    },
    {
        "id": 100,
        "id_alumno": 10,
        "id_materia": 101,
        "nombre_examen": 'Recuperatorio Primer Parcial',
        "nota": 8
    }
]

# registros
estado_cursado = [
    {"id": 1, "id_alumno": 10, "id_materia": 101},
    {"id": 2, "id_alumno": 10, "id_materia": 102},
    {"id": 3, "id_alumno": 10, "id_materia": 103},
    {"id": 4, "id_alumno": 10, "id_materia": 104},

    {"id": 5, "id_alumno": 25, "id_materia": 101},
    {"id": 6, "id_alumno": 25, "id_materia": 102},
    {"id": 7, "id_alumno": 25, "id_materia": 103},
    {"id": 8, "id_alumno": 25, "id_materia": 104},

    {"id": 9, "id_alumno": 100, "id_materia": 101},
    {"id": 10, "id_alumno": 100, "id_materia": 102}
]

ids_alumnos_unicos = set()
info_saneada = []

for registro in estado_cursado:
    ids_alumnos_unicos.add(registro.get('id_alumno'))

for id_alumno in ids_alumnos_unicos:
    info_alumno = {
        id_alumno: []
    }
    info_saneada.append(info_alumno)

"""
[
    {25: []},
    {10: []},
    {100: []}
]
"""
from diccionario_10 import filtrar_elementos
from diccionario_11 import buscar_datos_por_id

for alumno in info_saneada:
    id_alumno = list(alumno.keys())[0]
    materias_ap = filtrar_elementos(estado_cursado, filtrar_por='id_alumno', valor_buscado=id_alumno)
    
    for materia in materias_ap:
        materias_alumno = alumno.get(id_alumno)
        materias_alumno.append(materia.get('id_materia'))
    
# print(info_saneada)

# mostrar informacion de alumnos y materias aprobadas

for alumno in info_saneada:

    for id_alumno, l_materias_aprobadas in alumno.items():

        info_alumno = buscar_datos_por_id(alumnos, clave_busqueda='id', id_abuscar=id_alumno)

        info_alumno_str =\
        f"""_________________________________________________\n
ID: {info_alumno.get('id')}   Nombre: {info_alumno.get('nombre')}  Provincia: {info_alumno.get('provincia')}    ESTADO: {info_alumno.get('estado').upper()}
Materias Aprobadas:\n
""" 
        # total_horas_cursadas = 0
        for id_materia in l_materias_aprobadas:
            info_materia_ap = buscar_datos_por_id(materias, clave_busqueda='id', id_abuscar=id_materia)
            # total_horas_cursadas += info_materia_ap.get('horas')

            info_materia_str = f'   ID: {info_materia_ap.get("id")}'\
                 f' Nombre: {info_materia_ap.get("nombre")}\n'
                #  f' Carga_Horaria: {info_materia_ap.get("horas")}\n'
            
            info_alumno_str = f'{info_alumno_str}{info_materia_str}'
        
        # info_alumno_str = f'{info_alumno_str}Total_Carga_horaria: {total_horas_cursadas}\n'
        
        
    print(info_alumno_str)


"""
_________________________________________________
ID: X   Nombre: Pepito  Provincia: X    ESTADO: GRADUADO
Materias Aprobadas:
    ID: 101 Nombre: P1  Carga_Horaria: 8
        ID Examen: X    Tipo_Examen: PP Nota: 8
        ID Examen: X    Tipo_Examen: PP Nota: 8
        ID Examen: X    Tipo_Examen: PP Nota: 8
        ID Examen: X    Tipo_Examen: PP Nota: 8
    ID: 102 Nombre: P2  Carga_Horaria: 8
    ID: 103 Nombre: P3  Carga_Horaria: 8
    ID: 104 Nombre: P4  Carga_Horaria: 8
    
    Total_Carga_horaria: 32
_________________________________________________

"""