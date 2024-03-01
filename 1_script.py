# Início do Script para Gravação das Colibris

# Importação das bibliotecas Python necessárias.
import pyautogui
import time
pyautogui.FAILSAFE = False
import os
import esc_button

print("Iniciando o script")

# Abrindo o terminal do Linux. (função importada)
esc_button.checar_botao_emergencia()
time.sleep(2)
import abrir_terminal
abrir_terminal.funcao_abrir_terminal()
esc_button.checar_botao_emergencia()

# Acessando sudo minicom.
esc_button.checar_botao_emergencia()
time.sleep(2)
esc_button.checar_botao_emergencia()
import acessando_sudo_minicom
acessando_sudo_minicom.funcao_acessar_sudo_minicom()
esc_button.checar_botao_emergencia()

# Janela pop-up informando usuário para conectar cabo de alimentação na Colibri.
esc_button.checar_botao_emergencia()
time.sleep(1)
esc_button.checar_botao_emergencia()
import janela_popup
janela_popup.funcao_janela_popup_cabo_alimentacao()
esc_button.checar_botao_emergencia()

# Pressionando ENTER várias vezes para impedir inicialização da Colibri.
esc_button.checar_botao_emergencia()
import pressionar_enter_sudo_minicom
pressionar_enter_sudo_minicom.funcao_pressionar_enter()
esc_button.checar_botao_emergencia()

# Inserindo o comando "bmode usb".
esc_button.checar_botao_emergencia()
time.sleep(2)
esc_button.checar_botao_emergencia()
import acessando_bmode_usb
acessando_bmode_usb.funcao_acessando_bmode_usb()
esc_button.checar_botao_emergencia()



