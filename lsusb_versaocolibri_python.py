import tkinter as tk
import pyautogui
import time
from threading import Thread
pyautogui.FAILSAFE = False
import esc_button
import os

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela

def janela_popup_thread_check_microsub():
    thread = Thread(target=funcao_janela_popup_check_microsub)
    thread.start()
    thread.join()

def janela_popup_thread_reconectar_microsub():
    thread = Thread(target=funcao_janela_popup_reconectar_microusb)
    thread.start()
    thread.join()

def funcao_sim():
    time.sleep(2)
    import selecionar_versao_colibri
    selecionar_versao_colibri.funcao_selecionar_versao_colibri()

def funcao_nao():
    janela_popup_thread_reconectar_microsub()
    funcao_lsusb_versaocolibri_python()

def encerrar_script():
    print("Fim do script")
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    os._exit(0)

def funcao_janela_popup_check_microsub():
    janela = tk.Tk()
    janela.title("Confirmar Conexão Micro USB")

    mensagem = 'Confirme se o Micro USB conectou corretamente.\n\nA mensagem abaixo está aparecendo no terminal?\n\n"Micro USB conectado em: Bus 001 Device 0XX: ID 15a2:0061 Freescale Semiconductor, Inc. i.MX 6Solo/6DualLite SystemOnChip in RecoveryMode."'

    lbl_mensagem = tk.Label(janela, text=mensagem, padx=20, pady=20)
    lbl_mensagem.pack()

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack()

    btn_sim = tk.Button(frame_botoes, text="Sim", command=lambda: [janela.destroy(), funcao_sim()])
    btn_sim.pack(side=tk.LEFT, padx=10)

    btn_nao = tk.Button(frame_botoes, text="Não", command=lambda: [janela.destroy(), funcao_nao()])
    btn_nao.pack(side=tk.LEFT, padx=10)

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    largura_janela = 1100
    altura_janela = 170

    x_pos = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
    y_pos = (janela.winfo_screenheight() // 2) + 50

    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.protocol("WM_DELETE_WINDOW", lambda: None)

    janela.mainloop()

def funcao_janela_popup_reconectar_microusb():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Remover e Conectar Micro USB novamente")
    
    label = tk.Label(janela, text="\nOcorreu um problema:\n\nA conexão do cabo micro USB não foi reconhecida.\n\nRemova e conecte novamente o Micro USB na mesma entrada.\n\nApós ter conectado novamente o cabo, clique em 'Prosseguir'.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="Prosseguir", command=fechar_janela)
    botao_ok.pack()

    # Botão "Encerrar script"
    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    largura_janela = 750
    altura_janela = 210

    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def funcao_lsusb_versaocolibri_python():
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("usb_info=$(lsusb | grep '15a2:0061')")
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(3)
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite('echo "Micro USB conectado em: $usb_info"')
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    import check_microusb
    check_microusb.encontrar_recoverymode()
    esc_button.checar_botao_emergencia()

def funcao_primeiro_lsusb():
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    import abrir_nova_aba_terminal
    abrir_nova_aba_terminal.funcao_abrir_nova_aba_terminal()
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    # ! Janela trocar entrada para entra B.
    #import janela_popup
    #janela_popup.funcao_janela_popup_micro_USB()
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    funcao_lsusb_versaocolibri_python()

