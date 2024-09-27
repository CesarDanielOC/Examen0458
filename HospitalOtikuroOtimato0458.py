print("Examen 0458\n")
class Hospital0458:
    def Medicamento0458(self):
        Medicamento0458 = {
"Medicamentos:": "Aspirina",
"ID_Medicamento:": 1,
"Descripción": "Antianalgésico",
"Dosis:": "1 pastilla",
"Frecuencia:": "8 horas",
"Efectos Secundarios": "Nauseas, adormecimiento",
"Precio:": 40
        }
        for x,y in Medicamento0458.items():
            print(x,y)

    def Medico0458(self):
        Médico0458 = {
"Nombre del médico:": "José Alfredo ",
"ID_Médico:": 1,
"Apellido": "Jimenez Alvarado",
"Especialidad:": "Neurología",
"Número de teléfono:": "656 147 8742",
"Correo": "Josealfredo@gmail.com",
"Fecha de contratación:": "7 de octubre 2019"
        }
        for x,y in Médico0458.items():
            print(x,y)

    def Paciente0458(self):
        Paciente0458 = {
"Nombre del paciente:":"Pepito",
"Apellido": "Juanes",
"ID_Paciente:": 1,
"Fecha de nacimiento:": "10 de noviembre 2015",
"Número de teléfono:": "656 851 8411",
"Dirección": "Calle del perro #8124",
"Fecha de registro:": "10 de noviembre 2016"
        }
        for x, y in Paciente0458.items():
                print(x, y)

    def Receta0458(self):
        Receta0458 = {
"ID_Receta:": 1,
"ID_Paciente:": 1,
"ID_Médico": 1,
"Fecha de Receta:": "10 de noviembre 2016",
"Instrucciones:": "Inyectar en glúteos cada 2 meses",
"Validez": "Contactar a Josealvarado@gmail.com",
"ID_Medicamento:": 5
        }
        for x, y in Receta0458.items():
                print(x, y)

objeto = Hospital0458()

print("\nDatos del Medicamento")
objeto.Medicamento0458()
print("\nDatos del médico")
objeto.Medico0458()
print("\nDatos del paciente")
objeto.Paciente0458()
print("\nDatos de la Receta")
objeto.Receta0458()
