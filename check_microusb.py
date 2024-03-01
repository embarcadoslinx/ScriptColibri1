import pyautogui
import os
import tkinter as tk
import time
pyautogui.FAILSAFE = False
import esc_button

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def janela_encerrar_script():
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
    janela.title("AVISO: PROBLEMA DE CONEXÃO CABO MICRO USB!")

    label = tk.Label(janela, text="\nNão foi possível conectar corretamente o cabo micro USB na entrada B.\n\n O processo de gravação da Colibri foi interrompido e o script encerrado.\n\n Remova o cabo USB do notebook e conecte novamente. \n\nRetorne o cabo micro USB para a entrada A.\n\n Inicie o script novamente.\n")

    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 700
    altura_janela = 230

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def lsusb_usb():
    pyautogui.typewrite("usb_info=$(lsusb | grep '15a2:0061')")
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite('echo "Micro USB conectado em: $usb_info"')
    pyautogui.hotkey('enter')


def encontrar_recoverymode(tentativas_restantes=3):
    if tentativas_restantes == 0:
        print("Limite de tentativas cabo micro USB alcançado. Encerrando o script.")
        janela_encerrar_script()

    time.sleep(1)
    
    try:
        img_nosuchfileordirectory = pyautogui.locateCenterOnScreen('/home/breno/ScriptGravacaoColibri/NovoScriptColibri/Novos_Scripts/Scripts/systemrecoverymode.png')
    except pyautogui.ImageNotFoundException:
        img_nosuchfileordirectory = None

    if img_nosuchfileordirectory is not None:
        print("Micro USB conectado corretamente na entrada B")
        time.sleep(2)
        import selecionar_versao_colibri
        selecionar_versao_colibri.funcao_selecionar_versao_colibri()

    else:
        print("Micro USB NÃO foi conectado corretamente na entrada B!!!")
        time.sleep(0.5)
        import lsusb_versaocolibri_python
        lsusb_versaocolibri_python.janela_popup_thread_reconectar_microsub()
        time.sleep(2)
        lsusb_usb()
        encontrar_recoverymode(tentativas_restantes - 1)
        
