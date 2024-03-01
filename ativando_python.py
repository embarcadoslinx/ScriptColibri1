import pyautogui
import time
import tkinter as tk
import os
from threading import Thread
pyautogui.FAILSAFE = False
import esc_button

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela
    
def encerrar_script():
    print("Fim do script")
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    os._exit(0)

def funcao_janela_popup_voltar_micro_USB():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
    janela.title("Voltar cabo micro USB para a entrada A.")
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela

    label = tk.Label(janela, text="\nLeia as instruções abaixo e realize os devidos passos:\n\n\n1. Volte o cabo micro USB para a entrada A.\n\n2. Após ter voltado o cabo, clique em 'Prosseguir'.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="Prosseguir", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 600
    altura_janela = 190

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def funcao_janela_popup_copiar_ip_colibri():
    def fechar_janela():
        janela.destroy()

    janela = tk.Tk()
    janela.protocol("WM_DELETE_WINDOW", disable_close_button)  # Impede o fechamento da janela
    janela.title("Copiar o endereço de IP, ex: '192.168.2.215'.")
    
    label = tk.Label(janela, text="Copie o endereço de IP que apareceu, (selecione com o mouse, clique com o botão direito e vá em 'copiar').\nEx de endereço IP que você deve copiar: '192.168.2.215'.\nEm seguida clique em 'OK'.")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 900
    altura_janela = 80

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def janela_popup_thread_ip():
    thread = Thread(target=funcao_janela_popup_copiar_ip_colibri)
    thread.start()
    thread.join()

def janela_popup_thread():
    thread = Thread(target=funcao_janela_popup_voltar_micro_USB)
    thread.start()
    thread.join()

def funcao_ativando_python():
    esc_button.checar_botao_emergencia()
    time.sleep(3)
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("chmod +x recovery-linux.sh", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("./recovery-linux.sh", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("agtech2024", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
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
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("cd ..", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("cd eject-hboard-0.3", interval=0.02)
    esc_button.checar_botao_emergencia()
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("python3 -m http.server", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    # ! Pop-up voltar micro USB e puxar IP da Colibri.
    print("Antes de Janela Voltar Micro USB")
    # ! janela voltar micro usb para entrada A.
    #janela_popup_thread()
    # funcao_janela_popup_voltar_micro_USB()
    print("Depois de Janela Voltar Micro USB")
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('alt', '1')
    time.sleep(1)
    esc_button.checar_botao_emergencia()
    time.sleep(0.5)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(0.5)
    esc_button.checar_botao_emergencia()
    # pyautogui.typewrite("ifconfig", interval=0.02)
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    esc_button.checar_botao_emergencia()
    time.sleep(0.5)
    esc_button.checar_botao_emergencia()
    pyautogui.typewrite("ifconfig eth0 | grep 'inet addr' | awk '{print $2}' | cut -d ':' -f 2")
    esc_button.checar_botao_emergencia()
    pyautogui.hotkey('enter')
    time.sleep(2)
    import check_ifconfig
    check_ifconfig.check_ifconfig()
    time.sleep(1)
    print("Depois de rodar a função pra preparar pro ifconfig")
    esc_button.checar_botao_emergencia()
    print("Antes de Janela Copiar IP")
    time.sleep(2)
    import encontrar_ip
    encontrar_ip.encontrar_IP()
    #janela_popup_thread_ip()
    print("Depois de Janela Copiar IP")
    esc_button.checar_botao_emergencia()
    time.sleep(2)
    esc_button.checar_botao_emergencia()
    # TODO: fazer lógica pra pegar o ip (futuramente)
    esc_button.checar_botao_emergencia()
    import sudo_vinagre_ip
    sudo_vinagre_ip.funcao_executar_sudo_vinagre_instalar_SO()
    esc_button.checar_botao_emergencia()
