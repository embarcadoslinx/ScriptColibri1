# Script para abrir uma nova aba do terminal do Linux (via atalho).

import time
import pyautogui
pyautogui.FAILSAFE = False
import os


# Abrir nova aba do terminal
def funcao_abrir_nova_aba_terminal():
    pyautogui.hotkey('ctrl', 'shift', 't')