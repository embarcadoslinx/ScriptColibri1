import pyautogui
import time
from threading import Thread
import tkinter as tk
pyautogui.FAILSAFE = False
import esc_button
import esc_button_vinagre
import os

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela
    
def encerrar_script():
    print("Fim do script")
    os._exit(0)

def funcao_janela_popup_desconectar_conectar_cabo_alimentacao():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Desconectar e Conectar o Cabo de Alimentação")
    
    label = tk.Label(janela, text="\nLeia as instruções abaixo e realize os devidos passos:\n\n\n1. Desconecte e conecte novamente o cabo de alimentação na placa.\n\n2. Após ter feito isso, clique em 'Prosseguir'.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="Prosseguir", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 1000
    altura_janela = 180

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def janela_popup_thread():
    thread = Thread(target=funcao_janela_popup_desconectar_conectar_cabo_alimentacao)
    thread.start()
    thread.join()

def funcao_executar_sudo_vinagre_instalar_SO():

    # Abrir nova aba do terminal
    import abrir_nova_aba_terminal
    abrir_nova_aba_terminal.funcao_abrir_nova_aba_terminal()
    
    # Executar "sudo vinagre" e colar o IP.
    esc_button.checar_botao_emergencia()
    time.sleep(3)
    pyautogui.typewrite("sudo vinagre ", interval=0.02)
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('shift', 'insert')
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.typewrite("agtech2024", interval=0.02)
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()

    # Dentro do Vinagre.
    pyautogui.hotkey('tab')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('tab')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('tab')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('tab')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('f')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('down')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    esc_button_vinagre.checar_botao_emergencia()
    pyautogui.typewrite("http://192.168.3.149:8000/image_list.json", interval=0.02)
    time.sleep(2)
    esc_button_vinagre.checar_botao_emergencia()
    pyautogui.hotkey('tab')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    esc_button_vinagre.checar_botao_emergencia()
    pyautogui.hotkey('down')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('enter')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(20)
    pyautogui.hotkey('up')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('up')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('i')
    time.sleep(2)
    esc_button_vinagre.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button_vinagre.checar_botao_emergencia()

    #! 80 segundos esperando + esc button vinagre
    import time_sleep80
    time_sleep80.time_sleep_80_segundos_esc_button()
    #time.sleep(80)

    pyautogui.hotkey('tab')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('enter')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(1)
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(1)
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(1)
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(1)
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(1)
    esc_button_vinagre.checar_botao_emergencia()
    pyautogui.hotkey('ctrl', 'w')
    esc_button_vinagre.checar_botao_emergencia()
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    esc_button_vinagre.checar_botao_emergencia()

    time.sleep(3)
    esc_button.checar_botao_emergencia()
    janela_popup_thread()
    esc_button.checar_botao_emergencia()
    import alterando_ip_colibri
    alterando_ip_colibri.funcao_alterar_ip_colibri()


