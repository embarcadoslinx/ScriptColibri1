import pyautogui
import os
import tkinter as tk
import time
pyautogui.FAILSAFE = False
import esc_button

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def janela_imxd6l_encontrado():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
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
    janela.title("AVISO: NÃO FOI POSSÍVEL ENVIAR O ARQUIVO IMX6DL PRA COLIBRI!")

    label = tk.Label(janela, text="\nNão foi possível enviar o arquivo imxd6l para a Colibri.\n\n O processo de gravação da Colibri foi interrompido e o script encerrado.\n\n Inicie o script novamente.\n\nSe o problema persistir, consulte um desenvolvedor da equipe de Embarcados \nno setor Engenharia de Software.\n\n")

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


def encontrar_imx6dl(tentativas_restantes=3):
    if tentativas_restantes == 0:
        print("Limite de tentativas ao tentar encontrar imx6dl. Encerrando o script.")
        janela_encerrar_script()
        os._exit(0)

    time.sleep(3)
    
    try:
        img_nosuchfileordirectory = pyautogui.locateCenterOnScreen('/home/breno/ScriptColibri/imx6dl.png')
    except pyautogui.ImageNotFoundException:
        img_nosuchfileordirectory = None

    if img_nosuchfileordirectory is not None:
        print("imx6dl encontrado e enviado!!!")
        time.sleep(2)


    else:
        print("imx6dl não foi encontrado.")
        time.sleep(2)
        encontrar_imx6dl(tentativas_restantes - 1)
        