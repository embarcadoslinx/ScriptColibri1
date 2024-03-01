import tkinter as tk
import time
import pyautogui
pyautogui.FAILSAFE = False
import os

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela
    
def encerrar_script():
    print("Fim do script")
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    os._exit(0)

def funcao_janela_popup_cabo_alimentacao():
    def fechar_janela():
        print("Cabo de alimentação conectado.")
        janela.destroy()

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Conexão do Cabo de Alimentação")
    
    label = tk.Label(janela, text="\nSiga as instruções abaixo:\n")
    label.pack()

    botao_ok = tk.Button(janela, text="Clique nesse botão e em seguida insira o cabo de alimentação na placa da Colibri", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 610
    altura_janela = 150

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def funcao_janela_popup_micro_USB():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Trocar cabo micro USB para a entrada B")
    
    label = tk.Label(janela, text="\nLeia as instruções abaixo e realize os devidos passos:\n\n\n1. Primeiro troque o cabo micro USB (que está na entrada A) para a entrada B.\n\n2. Após ter trocado o cabo, clique em 'Prosseguir'.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="Prosseguir", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 700
    altura_janela = 180

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    janela.mainloop()

def funcao_janela_popup_checker_micro_usb():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Confirmar Conexão Micro USB.")
    
    label = tk.Label(janela, text="Confirme se o Micro USB conectou corretamente. A mensagem está abaixo aparecendo no terminal?\n\nMicro USB conectado em: Bus 001 Device 0XX: ID 15a2:0061 Freescale Semiconductor, Inc. i.MX 6Solo/6DualLite SystemOnChip in RecoveryMode\n")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 1200
    altura_janela = 120

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()
