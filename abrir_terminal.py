#  Script para abrir o terminal do Linux (via atalhos).

import pyautogui
import time
import esc_button
pyautogui.FAILSAFE = False
import os

def funcao_abrir_terminal():
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('ctrl', 'alt', 't')
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('alt', 'f10') # terminal em tela cheia.
    esc_button.checar_botao_emergencia()

