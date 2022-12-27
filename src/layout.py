import PySimpleGUI as sg
from settings import layout_title, layout_input, layout_button_submit, layout_title_input, paht_icon

layout = [
    [layout_title],
    [layout_title_input, layout_input],
    [layout_button_submit]
]

window = sg.Window("Validador de CPF", layout, icon=paht_icon)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

