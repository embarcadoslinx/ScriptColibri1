import pyautogui
import time
pyautogui.FAILSAFE = False
import esc_button
import os

def funcao_acessando_bmode_usb():
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("bmode usb", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey("enter")
    esc_button.checar_botao_emergencia()
    import lsusb_versaocolibri_python
    esc_button.checar_botao_emergencia()
    lsusb_versaocolibri_python.funcao_primeiro_lsusb()
    esc_button.checar_botao_emergencia()

