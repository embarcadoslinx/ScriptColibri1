import esc_button
import os
import keyboard
import pyautogui
import time

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

import keyboard
import tkinter as tk

def checar_botao_emergencia():
    if keyboard.is_pressed('esc'):
        print("Botão de emergência pressionado. Encerrando o script.")
        def fechar_janela():
                janela.destroy()
                janela.quit()  # Encerra o loop de eventos do Tkinter
                time.sleep(0.5)
                pyautogui.hotkey('alt', 'f4')
                time.sleep(0.5)
                pyautogui.hotkey('enter')
                pyautogui.hotkey('enter')
                pyautogui.hotkey('enter')
                pyautogui.hotkey('enter')
                os._exit(0)

        janela = tk.Tk()
        janela.title("Script Encerrado")
        janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
        
        label = tk.Label(janela, text="O script foi forçado a se encerrar e foi encerrado.")
        label.pack()

        botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
        botao_ok.pack()

        # Obter as dimensões da tela
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        # Definir o tamanho da janela
        largura_janela = 500
        altura_janela = 60

        # Calcular a posição central da tela
        x_pos = largura_tela // 2 - largura_janela // 2
        y_pos = altura_tela // 2 - altura_janela // 2

        # Configurar a geometria da janela para centralizá-la
        janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

        janela.mainloop()
        print("Script encerrado")
