print("Examen 0458")
class Hospital0458:
        Medicamento0458 = {
"Medicamentos:": "Aspirina",
"ID_Medicamento:": 1,
"Descripción": "Antianalgésico",
"Dosis:": "1 pastilla",
"Frecuencia:": "8 horas",
"Efectos_Secundarios": "Nauseas, adormecimiento",
"Precio:": 40
}
        for x, y in Medicamento0458.items():
                print(x, y)
                Médico0458 = {
"\nNombre del médico:": "José Alfredo \n",
"ID_Médico:": 1,
"\nApellido": "Jimenez Alvarado\n",
"Especialidad:": "Neurología\n",
"Número de teléfono:": "656 147 8742\n",
"Correo": "Josealfredo@gmail.com\n",
"Fecha de contratación:": "7 de octubre 2019"
}
        for x, y in Médico0458.items():
                print(x, y)
                Paciente0458 = {
"\nNombre del paciente:": "Pepito \n",
"ID_Paciente:": 1,
"\nApellido": "Juanes\n",
"Fecha de nacimiento:": "10 de noviembre 2015\n",
"Número de teléfono:": "656 851 8411\n",
"Dirección": "Calle del perro #8124\n",
"Fecha de registro:": "10 de noviembre 2016"
}
        for x, y in Paciente0458.items():
                print(x, y)
                Receta0458 = {
"\nID_Receta:": 1,
"ID_Paciente:": 1,
"ID_Médico": "1",
"Fecha de Receta:": "10 de noviembre 2016\n",
"Instrucciones:": "Inyectar en glúteos cada 2 meses\n",
"Validez": "Contactar a Josealvarado@gmail.com\n",
"ID_Medicamento:": 5
}
        for x, y in Receta0458.items():
                print(x, y)

Objeto = Hospital0458()
print("\nMedicamento")
print(Hospital0458.Medicamento0458)
print("\nMédico")
print(Hospital0458.Médico0458)
print("\nPaciente")
print(Hospital0458.Paciente0458)
print("\nMedicamento")
print(Hospital0458.Receta0458)