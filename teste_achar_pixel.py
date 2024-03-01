import pyautogui
import os
import tkinter as tk
import time
pyautogui.FAILSAFE = False

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def janela_imagem_encontrada():
    def fechar_janela():
        janela.destroy()
        os._exit(0)

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Script finalizado")
    
    label = tk.Label(janela, text="IMAGEM ENCONTRADA!")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 500
    altura_janela = 110

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def janela_imagem_nao_encontrada():
    def fechar_janela():
        janela.destroy()
        os._exit(0)

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Script finalizado")
    
    label = tk.Label(janela, text="IMAGEM NÃO ENCONTRADA!")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 500
    altura_janela = 110

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def encontrar_imagem():

    time.sleep(5)

    try:
        img_nosuchfileordirectory = pyautogui.locateCenterOnScreen('/home/breno/ScriptColibri/zImage.png')
    except pyautogui.ImageNotFoundException:
        img_nosuchfileordirectory = None

    if img_nosuchfileordirectory is not None:
        print("IMAGEM ENCONTRADA!")
        time.sleep(0.5)
        janela_imagem_encontrada()
    else:
        print("IMAGEM NÃO ENCONTRADA!")
        time.sleep(0.5)
        janela_imagem_nao_encontrada()

encontrar_imagem()