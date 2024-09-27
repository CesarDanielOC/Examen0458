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
"\nNombre del médico:": "José Alfredo ",
"ID_Médico:": 1,
"Apellido": "Jimenez Alvarado",
"Especialidad:": "Neurología",
"Número de teléfono:": "656 147 8742",
"Correo": "Josealfredo@gmail.com",
"Fecha de contratación:": "7 de octubre 2019"
}
        for x, y in Médico0458.items():
                print(x, y)
                Paciente0458 = {
"\nNombre del paciente:": "Pepito ",
"ID_Paciente:": 1,
"Apellido": "Juanes",
"Fecha de nacimiento:": "10 de noviembre 2015",
"Número de teléfono:": "656 851 8411",
"Dirección": "Calle del perro #8124",
"Fecha de registro:": "10 de noviembre 2016"
}
        for x, y in Paciente0458.items():
                print(x, y)
                Receta0458 = {
"\nID_Receta:": 1,
"ID_Paciente:": 1,
"ID_Médico": "1",
"Fecha de Receta:": "10 de noviembre 2016",
"Instrucciones:": "Inyectar en glúteos cada 2 meses",
"Validez": "Contactar a Josealvarado@gmail.com",
"ID_Medicamento:": 5
}
        for x, y in Receta0458.items():
                print(x, y)