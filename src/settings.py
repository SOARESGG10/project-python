import PySimpleGUI as sg
import re


def validate(regex, text):
    result = re.search(regex, text)
    return False if result is None or result.group() != text else True


icon = "../public/img/compass.svg"

sg.theme("Reddit")
layout_title = sg.Text("Validador de CPF's", size=22, font=(0, 18), text_color="#1F6FEB",
                       justification="center", pad=(0, 10))
layout_title_input = sg.Text("Informe um CPF:", font=10)
layout_input = sg.Input(size=17, font=10, key="IN1", enable_events=True)
layout_button_submit = sg.Button("Verificar", size=43, pad=(0, 10))
paht_icon = "../public/img/approved.png"
