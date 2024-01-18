import PySimpleGUI as sg 

layout = [
    [sg.Text('Text')],
    [sg.Button('Button')],
    [sg.Input()]
]

sg.Window('converter',layout).read()
    