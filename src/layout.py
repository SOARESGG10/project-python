import PySimpleGUI as sg
from settings import layout_title, layout_input, layout_button_submit, layout_title_input, paht_icon, validate

regex = "^[+]?([0-9](\d{0,11}))?$"
old = {"IN1": ""}

layout = [
    [layout_title],
    [layout_title_input, layout_input],
    [layout_button_submit]
]

window = sg.Window("Validador de CPF", layout, icon=paht_icon, finalize=True)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "IN1":
        element, text = window[event], values[event]
        if validate(regex, text):
            try:
                if len(text) > 11:
                    element.update(old[event])
                    continue
            except ValueError as e:
                pass
            old[event] = text
        else:
            element.update(old[event])
