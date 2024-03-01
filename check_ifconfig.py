import pyautogui
import os
import tkinter as tk
import time
pyautogui.FAILSAFE = False

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def janela_colibri_reiniciada():
    def fechar_janela():
        janela.destroy()
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        os._exit(0)

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("AVISO: PROBLEMA, COLIBRI REINICIADA!")
    
    label = tk.Label(janela, text="\nOcorreu um problema:\n\nAo retornar o cabo micro USB para a entrada B houve contato com o cabo de alimentação e a Colibri reiniciou.\n\nO processo de gravação foi interrompido e o script foi encerrado.\n\nInicie o script de gravação novamente.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 800
    altura_janela = 200

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def check_ifconfig():

    time.sleep(3)

    try:
        img_nosuchfileordirectory = pyautogui.locateCenterOnScreen('/home/breno/ScriptGravacaoColibri/NovoScriptColibri/Novos_Scripts/Scripts/ifconfig3.png')
    except pyautogui.ImageNotFoundException:
        img_nosuchfileordirectory = None

    if img_nosuchfileordirectory is not None:
        import encontrar_ip
        encontrar_ip.encontrar_IP()
    else:
        print("Ifconfig pode ser realizado.")
        janela_colibri_reiniciada()

