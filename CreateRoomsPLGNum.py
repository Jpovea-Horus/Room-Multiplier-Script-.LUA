
# Función reemplazar palabras en un archivo .lua
def replace_in_lua(input_file, output_file, replacements):
    try:
        # Abrir arch .lua orig
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Reemplazar
        for old_word, new_word in replacements.items():
            content = content.replace(old_word, new_word)

        # Escribir nuevo archivo
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f'Archivo procesado exitosamente: {output_file}')

    except FileNotFoundError:
        print(f'El archivo {input_file} no se encuentra.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')


# Definir el archivo de entrada y salida para los archivos hasta el octavo
input_file = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room1.lua'
output_file_2 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room2.lua'
output_file_3 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room3.lua'
output_file_4 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room4.lua'
output_file_5 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room5.lua'
output_file_6 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room6.lua'
output_file_7 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room7.lua'
output_file_8 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room8.lua'

# Diccionarios de palabras a reemplazar para cada archivo
replacements_2 = {
    '1"': '2"',
    'aul1': 'aul2',
    'Tick1':'Tick2',
    'room1':'room2',
    'accion 1':'accion 2',
    'TimerID1':'TimerID2',
    '1 OCUPADO':'2 OCUPADO',
    'scanCycle1':'scanCycle2',
    'TimerAccion1':'TimerAccion2',
    'TimerDuration1':'TimerDuration2',
    'previousTimer_1':'previousTimer_2',
    'tiempoRestante1':'tiempoRestante2',
    'TiempoAnterior_1':'TiempoAnterior_2',
    'TiempoPosterior_1':'TiempoPosterior_2',
    '"TimerRemainingV_1':'"TimerRemainingV_2'
}

replacements_3 = {
    '2"': '3"',
    'aul2':'aul3',
    'Tick2':'Tick3',
    'room2':'room3',
    'accion 2':'accion 3',
    'TimerID2':'TimerID3',
    '2 OCUPADO':'3 OCUPADO',
    'scanCycle2':'scanCycle3',
    'TimerAccion2':'TimerAccion3',
    'TimerDuration2':'TimerDuration3',
    'tiempoRestante2':'tiempoRestante3',
    'previousTimer_2':'previousTimer_3',
    'TiempoAnterior_2':'TiempoAnterior_3',
    'TiempoPosterior_2':'TiempoPosterior_3',
    '"TimerRemainingV_2':'"TimerRemainingV_3'
}

replacements_4 = {
    '3"':'4"',
    'aul3':'aul4',
    'Tick3':'Tick4',
    'room3':'room4',
    'accion 3':'accion 4',
    'TimerID3':'TimerID4',
    '3 OCUPADO':'4 OCUPADO',
    'scanCycle3': 'scanCycle4',
    'TimerAccion3':'TimerAccion4',
    'TimerDuration3':'TimerDuration4',
    'tiempoRestante3':'tiempoRestante4',
    'previousTimer_3':'previousTimer_4',
    'TiempoAnterior_3':'TiempoAnterior_4',
    'TiempoPosterior_3':'TiempoPosterior_4',
    '"TimerRemainingV_3':'"TimerRemainingV_4'
}

replacements_5 = {
    '4"':'5"',
    'aul4':'aul5',
    'Tick4':'Tick5',
    'room4':'room5',
    'accion 4':'accion 5',
    'TimerID4':'TimerID5',
    '4 OCUPADO':'5 OCUPADO',
    'scanCycle4':'scanCycle5',
    'TimerAccion4':'TimerAccion5',
    'TimerDuration4':'TimerDuration5',
    'tiempoRestante4':'tiempoRestante5',
    'previousTimer_4':'previousTimer_5',
    'TiempoAnterior_4':'TiempoAnterior_5',
    'TiempoPosterior_4':'TiempoPosterior_5',
    '"TimerRemainingV_4':'"TimerRemainingV_5'
}

replacements_6 = {
    '5"':'6"',
    'aul5':'aul6',
    'Tick5':'Tick6',
    'room5':'room6',
    'accion 5':'accion 6',
    'TimerID5':'TimerID6',
    '5 OCUPADO':'6 OCUPADO',
    'scanCycle5':'scanCycle6',
    'TimerAccion5':'TimerAccion6',
    'TimerDuration5':'TimerDuration6',
    'tiempoRestante5':'tiempoRestante6',
    'previousTimer_5':'previousTimer_6',
    'TiempoAnterior_5':'TiempoAnterior_6',
    'TiempoPosterior_5':'TiempoPosterior_6',
    '"TimerRemainingV_5':'"TimerRemainingV_6'
}

replacements_7 = {
    '6"':'7"',
    'aul6':'aul7',
    'Tick6':'Tick7',
    'room6':'room7',
    'accion 6':'accion 7',
    'TimerID6':'TimerID7',
    '6 OCUPADO':'7 OCUPADO',
    'scanCycle6':'scanCycle7',
    'TimerAccion6':'TimerAccion7',
    'TimerDuration6':'TimerDuration7',
    'tiempoRestante6':'tiempoRestante7',
    'previousTimer_6':'previousTimer_7',
    'TiempoAnterior_6':'TiempoAnterior_7',
    'TiempoPosterior_6':'TiempoPosterior_7',
    '"TimerRemainingV_6':'"TimerRemainingV_7'
}

replacements_8 = {
    '7"':'8"',
    'aul7':'aul8',
    'Tick7':'Tick8',
    'room7':'room8',
    'accion 7':'accion 8',
    'TimerID7':'TimerID8',
    '7 OCUPADO':'8 OCUPADO',
    'scanCycle7':'scanCycle8',
    'TimerAccion7':'TimerAccion8',
    'TimerDuration7':'TimerDuration8',
    'tiempoRestante7':'tiempoRestante8',
    'previousTimer_7':'previousTimer_8',
    'TiempoAnterior_7':'TiempoAnterior_8',
    'TiempoPosterior_7':'TiempoPosterior_8',
    '"TimerRemainingV_7':'"TimerRemainingV_8'
}

replacements_9 = {
    '8"':'9"',
    'aul8':'aul9',
    'Tick8':'Tick9',
    'room8':'room9',
    'accion 8':'accion 9',
    'TimerID8':'TimerID9',
    '8 OCUPADO':'9 OCUPADO',
    'scanCycle8':'scanCycle9',
    'TimerAccion8':'TimerAccion9',
    'TimerDuration8':'TimerDuration9',
    'tiempoRestante8':'tiempoRestante9',
    'previousTimer_8':'previousTimer_9',
    'TiempoAnterior_8':'TiempoAnterior_9',
    'TiempoPosterior_8':'TiempoPosterior_9',
    '"TimerRemainingV_8':'"TimerRemainingV_9'
}

# Llamar a la función para crear los archivos hasta el octavo
replace_in_lua(input_file, output_file_2, replacements_2)
replace_in_lua(output_file_2, output_file_3, replacements_3)
replace_in_lua(output_file_3, output_file_4, replacements_4)
replace_in_lua(output_file_4, output_file_5, replacements_5)
replace_in_lua(output_file_5, output_file_6, replacements_6)
replace_in_lua(output_file_6, output_file_7, replacements_7)
replace_in_lua(output_file_7, output_file_8, replacements_8)