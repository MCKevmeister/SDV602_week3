import PySimpleGUI as sg
import menu


def send_message(message):
    # TODO
    return 0


def get_messages():
    # TODO
    return 0


def chat_window():
    layout = [[sg.Menu(menu.menu_def, tearoff=False)],
              [sg.T('Welcome to the Covid19 data explorer chat.')],
              [sg.Output(size=(100, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=False, key='-CHAT-', do_not_clear=False),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True)]]

    window = sg.Window(menu.TITLE + ' - Chat window', layout)

    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):
            break
        if event == 'SEND':
            message = value['-CHAT-'].rstrip()
            send_message(message)
            print(f'{message}', flush=True)
        if event in menu.menu_options:
            menu.run_menu(event, window)