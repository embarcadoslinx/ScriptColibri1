import pyautogui
import os
import tkinter as tk
import time
pyautogui.FAILSAFE = False

def disable_close_button():
    pass  # Esta função não faz nada, impedindo o fechamento da janela
    
def funcao_janela_popup_sshroot_nao_identificado():
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
    janela.title("AVISO: PROBLEMA AO CONECTAR NA COLIBRI VIA ROOT!")
    
    label = tk.Label(janela, text="\nOcorreu um problema:\n\nUma situação incomum ocorreu durante o processo de gravação.\n\nO script foi encerrado, feche todas as abas abertas no notebook e inicie o script novamente.\n\n Tente mais algumas vezes. Se o problema persistir entre em contato com alguém da equipe de Embarcados\ndo setor Engenharia de Software.\n")
    label.pack()

    botao_ok = tk.Button(janela, text="OK", command=fechar_janela)
    botao_ok.pack()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    largura_janela = 750
    altura_janela = 220

    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    janela.mainloop()

def encontrar_sshroot():

    time.sleep(12)

    # Procura por todas as três imagens
    try:
        img_default = pyautogui.locateCenterOnScreen('/home/breno/ScriptGravacaoColibri/NovoScriptColibri/Novos_Scripts/Scripts/sshroot1_default.png')
    except pyautogui.ImageNotFoundException:
        img_default = None

    try:
        img_nosuchfileordirectory = pyautogui.locateCenterOnScreen('/home/breno/ScriptGravacaoColibri/NovoScriptColibri/Novos_Scripts/Scripts/sshroot2_nosuchfileordirectory.png')
    except pyautogui.ImageNotFoundException:
        img_nosuchfileordirectory = None

    try:
        img_password = pyautogui.locateCenterOnScreen('/home/breno/ScriptGravacaoColibri/NovoScriptColibri/Novos_Scripts/Scripts/sshroot3_password.png')
    except pyautogui.ImageNotFoundException:
        img_password = None

    def caso1sshroot_default():
        print("SSH ROOT: Caso 1, sem necessidade de intervenção.")
        time.sleep(0.5)
        pyautogui.typewrite('ssh root@192.168.2.15', interval=0.2)
        pyautogui.hotkey('enter')
        time.sleep(2)
        import mover_app_agtech
        mover_app_agtech.funcao_move_files()
        
    def caso2sshroot_nosuchfileordirectory():
        print("SSH ROOT: Caso 2, No such file or directory.")
        time.sleep(0.5)
        pyautogui.typewrite('exit', interval=0.2)
        pyautogui.hotkey('enter')
        pyautogui.typewrite('ssh-keygen -f "/home/breno/.ssh/known_hosts" -R "192.168.2.15"')
        pyautogui.hotkey('enter')
        pyautogui.typewrite('ssh root@192.168.2.15', interval=0.2)
        pyautogui.hotkey('enter')
        time.sleep(0.5)
        print("Caso 2 finalizado.")
        time.sleep(2)
        import mover_app_agtech
        mover_app_agtech.funcao_move_files()

    def caso3sshroot_password():
        print("SSH ROOT: Caso 3, problema de password.")
        pyautogui.doubleClick(img_password.x, img_password.y)
        os._exit(0)

    # Verifica se o objeto 1 está na tela
    if img_default is not None:
        caso1sshroot_default()

    elif img_nosuchfileordirectory is not None:
        caso2sshroot_nosuchfileordirectory()

    elif img_password is not None:
            caso3sshroot_password()
    else:
        print("Nenhum caso encontrado. Situação atípica.")
        time.sleep(1)


    # Verifica qual imagem foi encontrada
    if img_default:
        caso1sshroot_default()

    elif img_nosuchfileordirectory:
        caso2sshroot_nosuchfileordirectory()

    elif img_password:
        caso3sshroot_password()

    else:
        print("Nenhum caso encontrado. Situação atípica.")
        funcao_janela_popup_sshroot_nao_identificado()
