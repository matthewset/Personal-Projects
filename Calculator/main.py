def calculate(x):
    a = ""
    b = ""
    pos = 0
    for i in range(len(x)):
        if x[i] == "+" or x[i] == "-" or x[i] == "x" or x[i] == "/":
            pos = i
            break
    a = x[0:pos]
    b = x[pos + 1:len(x)]
    c = x[pos]
    if c == "+":
        return(int(a) + int(b))
    elif c == "x":
        return(int(a) * int(b))
    elif c == "/":
        return(int(a) / int(b))
    else:
        return(int(a) - int(b))

import PySimpleGUI as sg

sg.theme('Dark')

layout = [[sg.Text(size=(15,1),key='-INPUT-'),sg.Text('|'),sg.Text(size=(5,1),key='-OUTPUT-')],
          [sg.Button('+'), sg.Button('-'),sg.Button('x'),sg.Button('/')],[sg.Button('0'),sg.Button('1'),sg.Button('2'),sg.Button('3')],
          [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('7')],[sg.Button('8'),sg.Button('9'),sg.Button('='),sg.Button('C')]]

window = sg.Window('Calculator', layout)
x=""
e=False
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Turn Off':
        break
    if event == '0':
        x=x+'0'
    elif event == '1':
        x=x+'1'
    elif event == '2':
        x=x+'2'
    elif event == '3':
        x=x+'3'
    elif event == '4':
        x=x+'4'
    elif event == '5':
        x=x+'5'
    elif event == '6':
        x=x+'6'
    elif event == '7':
        x=x+'7'
    elif event == '8':
        x=x+'8'
    elif event == '9':
        x=x+'9'
    elif event == '+' and e==False:
        x=x+'+'
        e=True
    elif event == '-' and e==False:
        x=x+'-'
        e=True
    elif event == '/' and e==False:
        x=x+'/'
        e=True
    elif event == 'x' and e==False:
        x=x+'x'
        e=True
    elif event == '=':
        window["-OUTPUT-"].update(calculate(x))
    elif event =='C':
        x=""
        e=False
        window["-OUTPUT-"].update("")
    window["-INPUT-"].update(x)


window.close()