mascota = {
    "nombre": 'firulais',
    "edad": 7,
    "raza": 'golden retriever',
    "color": 'chocolate'
}

print(mascota)
# Nombre nuevo -> Ayudante de santa
mascota.update({"nombre": "Ayudante de santa"})

# nueva clave,valor -> "ciudad" : "CABA"
mascota["ciudad"] = 'CABA'


print(mascota)