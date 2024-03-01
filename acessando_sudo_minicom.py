import pyautogui
import time
pyautogui.FAILSAFE = False
import esc_button
import os

# Desativando CAPSLOCK se estiver ativo.
# import desativar_capslock
# desativar_capslock.funcao_desativar_capslock()

def funcao_acessar_sudo_minicom():
    time.sleep(1)
    pyautogui.typewrite("setxkbmap -option caps:none", interval=0.1)
    pyautogui.hotkey("enter")
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    pyautogui.typewrite("sudo minicom", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey("enter")
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("agtech2024", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey("enter")
    esc_button.checar_botao_emergencia()