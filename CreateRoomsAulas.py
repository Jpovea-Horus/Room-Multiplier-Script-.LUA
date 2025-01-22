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
input_file = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomOne.lua'
output_file_2 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomTwo.lua'
output_file_3 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomThree.lua'
output_file_4 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomFour.lua'
output_file_5 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomFive.lua'
output_file_6 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomSix.lua'
output_file_7 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomSeven.lua'
output_file_8 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomEight.lua'
output_file_9 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomNine.lua'
output_file_10 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomTen.lua'
output_file_11 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomEleven.lua'
output_file_12 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomTwelve.lua'
output_file_13 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomThirteen.lua'
output_file_14 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomFourteen.lua'
output_file_15 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomFifteen.lua'
output_file_16 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomSixteen.lua'
output_file_17 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomSeventeen.lua'
output_file_18 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomEighteen.lua'
output_file_19 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomNineteen.lua'
output_file_20 = r'C:\Users\horus\PycharmProjects\CreateDocLuaScale\.venv\Doc-lua\roomTwenty.lua'

# Diccionarios de palabras a reemplazar para cada archivo
replacements_2 = {
    '1"': '2"',
    'Tick1':'Tick2',
    'roomOne': 'roomTwo',
    'TimerID1:':'TimerID2:',
    '1 OCUPADO':'2 OCUPADO',
    'scanCycle1': 'scanCycle2',
    'TimerAccion1':'TimerAccion2',
    'TimerDuration1': 'TimerDuration2',
    'previousTimer_1:':'previousTimer_2:',
    '"TimerRemainingV_1':'"TimerRemainingV_2'
}

replacements_3 = {
    '2"': '3"',
    'Tick2':'Tick3',
    'roomTwo': 'roomThree',
    'TimerID2:':'TimerID3:',
    '2 OCUPADO':'3 OCUPADO',
    'scanCycle2': 'scanCycle3',
    'TimerAccion2':'TimerAccion3',
    'TimerDuration2': 'TimerDuration3',
    'previousTimer_2:':'previousTimer_3:',
    '"TimerRemainingV_2':'"TimerRemainingV_3'
}

replacements_4 = {
    '3"': '4"',
    'Tick3':'Tick4',
    'roomThree': 'roomFour',
    'TimerID3:':'TimerID4:',
    '3 OCUPADO':'4 OCUPADO',
    'scanCycle3': 'scanCycle4',
    'TimerAccion3':'TimerAccion4',
    'TimerDuration3': 'TimerDuration4',
    'previousTimer_3:':'previousTimer_4:',
    '"TimerRemainingV_3':'"TimerRemainingV_4'
}

replacements_5 = {
    '4"': '5"',
    'Tick4':'Tick5',
    'roomFour': 'roomFive',
    'TimerID4:':'TimerID5:',
    '4 OCUPADO':'5 OCUPADO',
    'scanCycle4': 'scanCycle5',
    'TimerAccion4':'TimerAccion5',
    'TimerDuration4': 'TimerDuration5',
    'previousTimer_4:':'previousTimer_5:',
    '"TimerRemainingV_4':'"TimerRemainingV_5'
}

replacements_6 = {
    '5"': '6"',
    'Tick5':'Tick6',
    'roomFive': 'roomSix',
    'TimerID5:':'TimerID6:',
    '5 OCUPADO':'6 OCUPADO',
    'scanCycle5': 'scanCycle6',
    'TimerAccion5':'TimerAccion6',
    'TimerDuration5': 'TimerDuration6',
    'previousTimer_5:':'previousTimer_6:',
    '"TimerRemainingV_5':'"TimerRemainingV_6'
}

replacements_7 = {
    '6"': '7"',
    'Tick6':'Tick7',
    'roomSix': 'roomSeven',
    'TimerID6:':'TimerID7:',
    '6 OCUPADO':'7 OCUPADO',
    'scanCycle6': 'scanCycle7',
    'TimerAccion6':'TimerAccion7',
    'TimerDuration6': 'TimerDuration7',
    'previousTimer_6:':'previousTimer_7:',
    '"TimerRemainingV_6':'"TimerRemainingV_7'
}

replacements_8 = {
    '7"': '8"',
    'Tick7':'Tick8',
    'roomSeven': 'roomEight',
    'TimerID7:':'TimerID8:',
    '7 OCUPADO':'8 OCUPADO',
    'scanCycle7': 'scanCycle8',
    'TimerAccion7':'TimerAccion8',
    'TimerDuration7': 'TimerDuration8',
    'previousTimer_7:':'previousTimer_8:',
    '"TimerRemainingV_7':'"TimerRemainingV_8'
}

replacements_9 = {
    '8"': '9"',
    'Tick8':'Tick9',
    'roomEight': 'roomNine',
    'TimerID8:':'TimerID9:',
    '8 OCUPADO':'9 OCUPADO',
    'scanCycle8': 'scanCycle9',
    'TimerAccion8':'TimerAccion9',
    'TimerDuration8': 'TimerDuration9',
    'previousTimer_8:':'previousTimer_9:',
    '"TimerRemainingV_8':'"TimerRemainingV_9'
}

replacements_10 = {
    '9"': '10"',
    'Tick9':'Tick10',
    'roomNine': 'roomTen',
    'TimerID9:':'TimerID10:',
    '9 OCUPADO':'10 OCUPADO',
    'scanCycle9': 'scanCycle10',
    'TimerAccion9':'TimerAccion10',
    'TimerDuration9': 'TimerDuration10',
    'previousTimer_9:':'previousTimer_10:',
    '"TimerRemainingV_9':'"TimerRemainingV_10'
}

replacements_11 = {
    '10"': '11"',
    'Tick10':'Tick11',
    'roomTen': 'roomEleven',
    'TimerID10:':'TimerID11:',
    '10 OCUPADO':'11 OCUPADO',
    'scanCycle10': 'scanCycle11',
    'TimerAccion10':'TimerAccion11',
    'TimerDuration10': 'TimerDuration11',
    'previousTimer_10:':'previousTimer_11:',
    '"TimerRemainingV_10':'"TimerRemainingV_11'
}

replacements_12 = {
    '11"': '12"',
    'Tick11':'Tick12',
    'roomEleven': 'roomTwelve',
    'TimerID11:':'TimerID12:',
    '11 OCUPADO':'12 OCUPADO',
    'scanCycle11': 'scanCycle12',
    'TimerAccion11':'TimerAccion12',
    'TimerDuration11': 'TimerDuration12',
    'previousTimer_11:':'previousTimer_12:',
    '"TimerRemainingV_11':'"TimerRemainingV_12'
}

replacements_13 = {
    '12"': '13"',
    'Tick12':'Tick13',
    'roomTwelve': 'roomThirteen',
    'TimerID12:':'TimerID13:',
    '12 OCUPADO':'13 OCUPADO',
    'scanCycle12': 'scanCycle13',
    'TimerAccion12':'TimerAccion13',
    'TimerDuration12': 'TimerDuration13',
    'previousTimer_12:':'previousTimer_13:',
    '"TimerRemainingV_12':'"TimerRemainingV_13'
}

replacements_14 = {
    '13"': '14"',
    'Tick13':'Tick14',
    'roomThirteen': 'roomFourteen',
    'TimerID13:':'TimerID14:',
    '13 OCUPADO':'14 OCUPADO',
    'scanCycle13': 'scanCycle14',
    'TimerAccion13':'TimerAccion14',
    'TimerDuration13': 'TimerDuration14',
    'previousTimer_13:':'previousTimer_14:',
    '"TimerRemainingV_13':'"TimerRemainingV_14'
}

replacements_15 = {
    '14"': '15"',
    'Tick14':'Tick15',
    'roomFourteen': 'roomFifteen',
    'TimerID14:':'TimerID15:',
    '14 OCUPADO':'15 OCUPADO',
    'scanCycle14': 'scanCycle15',
    'TimerAccion14':'TimerAccion15',
    'TimerDuration14': 'TimerDuration15',
    'previousTimer_14:':'previousTimer_15:',
    '"TimerRemainingV_14':'"TimerRemainingV_15'
}

replacements_16 = {
    '15"': '16"',
    'Tick15':'Tick16',
    'roomFifteen': 'roomSixteen',
    'TimerID15:':'TimerID16:',
    '15 OCUPADO':'16 OCUPADO',
    'scanCycle15': 'scanCycle16',
    'TimerAccion15':'TimerAccion16',
    'TimerDuration15': 'TimerDuration16',
    'previousTimer_15:':'previousTimer_16:',
    '"TimerRemainingV_15':'"TimerRemainingV_16'
}

replacements_17 = {
    '16"': '17"',
    'Tick16':'Tick17',
    'roomSixteen': 'roomSeventeen',
    'TimerID16:':'TimerID17:',
    '16 OCUPADO':'17 OCUPADO',
    'scanCycle16': 'scanCycle17',
    'TimerAccion16':'TimerAccion17',
    'TimerDuration16': 'TimerDuration17',
    'previousTimer_16:':'previousTimer_17:',
    '"TimerRemainingV_16':'"TimerRemainingV_17'
}

replacements_18 = {
    '17"': '18"',
    'Tick17':'Tick18',
    'roomSeventeen': 'roomEighteen',
    'TimerID17:':'TimerID18:',
    '17 OCUPADO':'18 OCUPADO',
    'scanCycle17': 'scanCycle18',
    'TimerAccion17':'TimerAccion18',
    'TimerDuration17': 'TimerDuration18',
    'previousTimer_17:':'previousTimer_18:',
    '"TimerRemainingV_17':'"TimerRemainingV_18'
}

replacements_19 = {
    '18"': '19"',
    'Tick18':'Tick19',
    'roomEighteen': 'roomNineteen',
    'TimerID18:':'TimerID19:',
    '18 OCUPADO':'19 OCUPADO',
    'scanCycle18': 'scanCycle19',
    'TimerAccion18':'TimerAccion19',
    'TimerDuration18': 'TimerDuration19',
    'previousTimer_18:':'previousTimer_19:',
    '"TimerRemainingV_18':'"TimerRemainingV_19'
}

replacements_20 = {
    '19"': '20"',
    'Tick19':'Tick20',
    'roomNineteen': 'roomTwenty',
    'TimerID19:':'TimerID20:',
    '19 OCUPADO':'20 OCUPADO',
    'scanCycle19': 'scanCycle20',
    'TimerAccion19':'TimerAccion20',
    'TimerDuration19': 'TimerDuration20',
    'previousTimer_19:':'previousTimer_20:',
    '"TimerRemainingV_19':'"TimerRemainingV_20'
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
replace_in_lua(output_file_15, output_file_16, replacements_16)
replace_in_lua(output_file_16, output_file_17, replacements_17)
replace_in_lua(output_file_17, output_file_18, replacements_18)
replace_in_lua(output_file_18, output_file_19, replacements_19)
replace_in_lua(output_file_19, output_file_20, replacements_20)