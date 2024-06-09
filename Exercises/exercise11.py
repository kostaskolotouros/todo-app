import FreeSimpleGUI as sg
import bonus.converters14 as cv

sg.theme("Black")

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")

exit_button = sg.Button("Exit")

result_text = sg.Text(key="result")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, exit_button, result_text]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            result = cv.convert(feet, inches)
            window["result"].update(value=result)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()