import tkinter as tk
import time
import pyautogui
import pickle
import os
pyautogui.FAILSAFE = False
from threading import Thread

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def funcao_janela_popup_gravacao_concluida():
    def fechar_janela():
        janela.destroy()
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        os._exit(0)
        

    try:
        with open("versao_escolhida.pkl", "rb") as f:
            versao_escolhida = pickle.load(f)
    except FileNotFoundError:
        print("Arquivo de versão não encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo de versão: {e}")
        return

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Gravação concluída com sucesso")
    
    label = tk.Label(janela, text=f"A gravação da versão {versao_escolhida} foi concluída com sucesso.\nRemova o cabo de alimentação da placa e em seguida remova a Colibri.\nFim do script.")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 500
    altura_janela = 90

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def janela_popup_thread():
    thread = Thread(target=funcao_janela_popup_gravacao_concluida)
    thread.start()
    thread.join()

def funcao_gravacao_concluida():
    time.sleep(2)
    #pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    #pyautogui.hotkey('enter')
    janela_popup_thread()

