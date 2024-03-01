import pyautogui
import os
import tkinter as tk
import time
pyautogui.FAILSAFE = False

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def encontrar_IP():
    time.sleep(5)

    try:

        img_ip = pyautogui.locateCenterOnScreen('/home/breno/ScriptGravacaoColibri/NovoScriptColibri/Novos_Scripts/Scripts/IP.png')

        # Funções para cada objeto encontrado
        def IP_encontrando():
            print("IP encontrado!")
            pyautogui.doubleClick(img_ip.x, img_ip.y)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'shift', 'c')
            print("IP copiado!")
            import sudo_vinagre_ip
            sudo_vinagre_ip.funcao_executar_sudo_vinagre_instalar_SO()
            
        def IP_nao_encontrado():
            print("Nenhum IP encontrado.")
            funcao_janela_popup_micro_USB()

        # Verifica se o objeto 1 está na tela
        if img_ip is not None:
            IP_encontrando()

        # Se nenhum objeto for encontrado
        else:
            IP_nao_encontrado()
            
    except pyautogui.ImageNotFoundException:
        print("Nenhum IP encontrado.")
        os._exit(0)
        #funcao_janela_popup_micro_USB()

def funcao_janela_popup_micro_USB():
    def fechar_janela():
        janela.destroy()
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        os._exit(0)

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Endereço de IP não encontrado")
    
    label = tk.Label(janela, text="\nO endereço de IP da Colibri não foi encontrado,\no script foi forçado a ser encerrado.\n\nFeche todas as abas abertas do notebook e inicie o script novamente.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 500
    altura_janela = 160

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

