from dataclasses import replace

from CreateRoomsAulas import output_file_9, output_file_10, output_file_11, replacements_10, replacements_12, \
    replacements_14, replacements_15, replacements_17, replacements_18, replacements_19


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
output_file_9 = r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room9.lua'
output_file_10= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room10.lua'
output_file_11= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room11.lua'
output_file_12= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room12.lua'
output_file_13= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room13.lua'
output_file_14= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room14.lua'
output_file_15= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room15.lua'
output_file_16= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room16.lua'
output_file_17= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room17.lua'
output_file_18= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room18.lua'
output_file_19= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room19.lua'
output_file_20= r'c:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\room20.lua'

# Diccionarios de palabras a reemplazar para cada archivo
replacements_2 = {
    '1"': '2"',
    'Aul1': 'Aul2',
    'Tick1':'Tick2',
    'room1':'room2',
    '"accion1':'"accion2',
    'TimerID1':'TimerID2',
    'scanCycle1':'scanCycle2',
    'TimerAccion1':'TimerAccion2',
    'TimerDuration1':'TimerDuration2',
    'tiempoRestante1':'tiempoRestante2',
    'TiempoAnterior_1':'TiempoAnterior_2',
    'TiempoPosterior_1':'TiempoPosterior_2'
}

replacements_3 = {
    '2"': '3"',
    'Aul2':'Aul3',
    'Tick2':'Tick3',
    'room2':'room3',
    '"accion2':'"accion3',
    'TimerID2':'TimerID3',
    'scanCycle2':'scanCycle3',
    'TimerAccion2':'TimerAccion3',
    'TimerDuration2':'TimerDuration3',
    'tiempoRestante2':'tiempoRestante3',
    'TiempoAnterior_2':'TiempoAnterior_3',
    'TiempoPosterior_2':'TiempoPosterior_3'
}

replacements_4 = {
    '3"':'4"',
    'Aul3':'Aul4',
    'Tick3':'Tick4',
    'room3':'room4',
    '"accion3':'"accion4',
    'TimerID3':'TimerID4',
    'scanCycle3': 'scanCycle4',
    'TimerAccion3':'TimerAccion4',
    'TimerDuration3':'TimerDuration4',
    'tiempoRestante3':'tiempoRestante4',
    'TiempoAnterior_3':'TiempoAnterior_4',
    'TiempoPosterior_3':'TiempoPosterior_4'
}

replacements_5 = {
    '4"':'5"',
    'Aul4':'Aul5',
    'Tick4':'Tick5',
    'room4':'room5',
    '"accion4':'"accion5',
    'TimerID4':'TimerID5',
    'scanCycle4':'scanCycle5',
    'TimerAccion4':'TimerAccion5',
    'TimerDuration4':'TimerDuration5',
    'tiempoRestante4':'tiempoRestante5',
    'TiempoAnterior_4':'TiempoAnterior_5',
    'TiempoPosterior_4':'TiempoPosterior_5'
}

replacements_6 = {
    '5"':'6"',
    'Aul5':'Aul6',
    'Tick5':'Tick6',
    'room5':'room6',
    '"accion5':'"accion6',
    'TimerID5':'TimerID6',
    'scanCycle5':'scanCycle6',
    'TimerAccion5':'TimerAccion6',
    'TimerDuration5':'TimerDuration6',
    'tiempoRestante5':'tiempoRestante6',
    'TiempoAnterior_5':'TiempoAnterior_6',
    'TiempoPosterior_5':'TiempoPosterior_6'
}

replacements_7 = {
    '6"':'7"',
    'Aul6':'Aul7',
    'Tick6':'Tick7',
    'room6':'room7',
    '"accion6':'"accion7',
    'TimerID6':'TimerID7',
    'scanCycle6':'scanCycle7',
    'TimerAccion6':'TimerAccion7',
    'TimerDuration6':'TimerDuration7',
    'tiempoRestante6':'tiempoRestante7',
    'TiempoAnterior_6':'TiempoAnterior_7',
    'TiempoPosterior_6':'TiempoPosterior_7'
}

replacements_8 = {
    '7"':'8"',
    'Aul7':'Aul8',
    'Tick7':'Tick8',
    'room7':'room8',
    '"accion7':'"accion8',
    'TimerID7':'TimerID8',
    'scanCycle7':'scanCycle8',
    'TimerAccion7':'TimerAccion8',
    'TimerDuration7':'TimerDuration8',
    'tiempoRestante7':'tiempoRestante8',
    'TiempoAnterior_7':'TiempoAnterior_8',
    'TiempoPosterior_7':'TiempoPosterior_8'
}

replacements_9 = {
    '8"':'9"',
    'Aul8':'Aul9',
    'Tick8':'Tick9',
    'room8':'room9',
    '"accion8':'"accion9',
    'TimerID8':'TimerID9',
    'scanCycle8':'scanCycle9',
    'TimerAccion8':'TimerAccion9',
    'TimerDuration8':'TimerDuration9',
    'tiempoRestante8':'tiempoRestante9',
    'TiempoAnterior_8':'TiempoAnterior_9',
    'TiempoPosterior_8':'TiempoPosterior_9'
}

replacements_10 = {
    '9"':'10"',
    'Aul9':'Aul10',
    'Tick9':'Tick10',
    'room9':'room10',
    '"accion9':'"accion10',
    'TimerID9':'TimerID10',
    'scanCycle9':'scanCycle10',
    'TimerAccion9':'TimerAccion10',
    'TimerDuration9':'TimerDuration10',
    'tiempoRestante9':'tiempoRestante10',
    'TiempoAnterior_9':'TiempoAnterior_10',
    'TiempoPosterior_9':'TiempoPosterior_10'
}

replacements_11 = {
    '10"':'11"',
    'Aul10':'Aul11',
    'Tick10':'Tick11',
    'room10':'room11',
    '"accion10':'"accion11',
    'TimerID10':'TimerID11',
    'scanCycle10':'scanCycle11',
    'TimerAccion10':'TimerAccion11',
    'TimerDuration10':'TimerDuration11',
    'tiempoRestante10':'tiempoRestante11',
    'TiempoAnterior_10':'TiempoAnterior_11',
    'TiempoPosterior_10':'TiempoPosterior_11'
}

replacements_12 = {
    '11"':'12"',
    'Aul11':'Aul12',
    'Tick11':'Tick12',
    'room11':'room12',
    '"accion11':'"accion12',
    'TimerID11':'TimerID12',
    'scanCycle11':'scanCycle12',
    'TimerAccion11':'TimerAccion12',
    'TimerDuration11':'TimerDuration12',
    'tiempoRestante11':'tiempoRestante12',
    'TiempoAnterior_11':'TiempoAnterior_12',
    'TiempoPosterior_11':'TiempoPosterior_12'
}

replacements_13 = {
    '12"':'13"',
    'Aul12':'Aul13',
    'Tick12':'Tick13',
    'room12':'room13',
    '"accion12':'"accion13',
    'TimerID12':'TimerID13',
    'scanCycle12':'scanCycle13',
    'TimerAccion12':'TimerAccion13',
    'TimerDuration12':'TimerDuration13',
    'tiempoRestante12':'tiempoRestante13',
    'TiempoAnterior_12':'TiempoAnterior_13',
    'TiempoPosterior_12':'TiempoPosterior_13'
}

replacements_14 = {
    '13"':'14"',
    'Aul13':'Aul14',
    'Tick13':'Tick14',
    'room13':'room14',
    '"accion13':'"accion14',
    'TimerID13':'TimerID14',
    'scanCycle13':'scanCycle14',
    'TimerAccion13':'TimerAccion14',
    'TimerDuration13':'TimerDuration14',
    'tiempoRestante13':'tiempoRestante14',
    'TiempoAnterior_13':'TiempoAnterior_14',
    'TiempoPosterior_13':'TiempoPosterior_14'
}

replacements_15 = {
    '14"':'15"',
    'Aul14':'Aul15',
    'Tick14':'Tick15',
    'room14':'room15',
    '"accion14':'"accion15',
    'TimerID14':'TimerID15',
    'scanCycle14':'scanCycle15',
    'TimerAccion14':'TimerAccion15',
    'TimerDuration14':'TimerDuration15',
    'tiempoRestante14':'tiempoRestante15',
    'TiempoAnterior_14':'TiempoAnterior_15',
    'TiempoPosterior_14':'TiempoPosterior_15'
}

replacemetns_16 = {
    '15"':'16"',
    'Aul15':'Aul16',
    'Tick15':'Tick16',
    'room15':'room16',
    '"accion15':'"accion16',
    'TimerID15':'TimerID16',
    'scanCycle15':'scanCycle16',
    'TimerAccion15':'TimerAccion16',
    'TimerDuration15':'TimerDuration16',
    'tiempoRestante15':'tiempoRestante16',
    'TiempoAnterior_15':'TiempoAnterior_16',
    'TiempoPosterior_15':'TiempoPosterior_16'
}

replacements_17 = {
    '16"':'17"',
    'Aul16':'Aul17',
    'Tick16':'Tick17',
    'room16':'room17',
    '"accion16':'"accion17',
    'TimerID16':'TimerID17',
    'scanCycle16':'scanCycle17',
    'TimerAccion16':'TimerAccion17',
    'TimerDuration16':'TimerDuration17',
    'tiempoRestante16':'tiempoRestante17',
    'TiempoAnterior_16':'TiempoAnterior_17',
    'TiempoPosterior_16':'TiempoPosterior_17'
}

replacements_18 = {
    '17"':'18"',
    'Aul17':'Aul18',
    'Tick17':'Tick18',
    'room17':'room18',
    '"accion17':'"accion18',
    'TimerID17':'TimerID18',
    'scanCycle17':'scanCycle18',
    'TimerAccion17':'TimerAccion18',
    'TimerDuration17':'TimerDuration18',
    'tiempoRestante17':'tiempoRestante18',
    'TiempoAnterior_17':'TiempoAnterior_18',
    'TiempoPosterior_17':'TiempoPosterior_18'
}

replacements_19 = {
    '18"':'19"',
    'Aul18':'Aul19',
    'Tick18':'Tick19',
    'room18':'room19',
    '"accion18':'"accion19',
    'TimerID18':'TimerID19',
    'scanCycle18':'scanCycle19',
    'TimerAccion18':'TimerAccion19',
    'TimerDuration18':'TimerDuration19',
    'tiempoRestante18':'tiempoRestante19',
    'TiempoAnterior_18':'TiempoAnterior_19',
    'TiempoPosterior_18':'TiempoPosterior_19'
}

replacemetns_20 = {
    '19"':'20"',
    'Aul19':'Aul20',
    'Tick19':'Tick20',
    'room19':'room20',
    '"accion19':'"accion20',
    'TimerID19':'TimerID20',
    'scanCycle19':'scanCycle20',
    'TimerAccion19':'TimerAccion20',
    'TimerDuration19':'TimerDuration20',
    'tiempoRestante19':'tiempoRestante20',
    'TiempoAnterior_19':'TiempoAnterior_20',
    'TiempoPosterior_19':'TiempoPosterior_20'
}

# Llamar a la función para crear los archivos hasta el octavo
replace_in_lua(input_file, output_file_2, replacements_2)
replace_in_lua(output_file_2, output_file_3, replacements_3)
replace_in_lua(output_file_3, output_file_4, replacements_4)
replace_in_lua(output_file_4, output_file_5, replacements_5)
replace_in_lua(output_file_5, output_file_6, replacements_6)
replace_in_lua(output_file_6, output_file_7, replacements_7)
replace_in_lua(output_file_7, output_file_8, replacements_8)
replace_in_lua(output_file_8, output_file_9, replacements_9)
replace_in_lua(output_file_9, output_file_10, replacements_10)
replace_in_lua(output_file_10, output_file_11, replacements_11)
replace_in_lua(output_file_11, output_file_12, replacements_12)
replace_in_lua(output_file_12, output_file_13, replacements_13)
replace_in_lua(output_file_13, output_file_14, replacements_14)
replace_in_lua(output_file_14, output_file_15, replacements_15)
replace_in_lua(output_file_15, output_file_16, replacemetns_16)
replace_in_lua(output_file_16, output_file_17, replacements_17)
replace_in_lua(output_file_17, output_file_18, replacements_18)
replace_in_lua(output_file_18, output_file_19, replacements_19)
replace_in_lua(output_file_19, output_file_20, replacemetns_20)