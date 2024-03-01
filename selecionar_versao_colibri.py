import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import pickle
pyautogui.FAILSAFE = False
import esc_button
import os

def encerrar_script():
    print("Fim do script")
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    os._exit(0)

# Função que faz o usuário selecionar a versão desejada e em seguida executa uma ação:
def funcao_selecionar_versao_colibri():
    def exibir_mensagem():
        versao_selecionada = versao_var.get()

        # Mapeamento entre versões e funções
        funcoes_por_versao = {
            "V1.0.0": funcao_v1_0_0,
            "V1.1.0": funcao_v1_1_0,
            "V1.2.0": funcao_v1_2_0,
            "V2.0.0": funcao_v2_0_0,
            "V2.1.0": funcao_v2_1_0,
            "V2.2.0": funcao_v2_2_0,
        }

        if versao_selecionada in funcoes_por_versao:
            mensagem = f"Você selecionou a versão: {versao_selecionada}. Deseja confirmar?"
            
            # Mostra uma caixa de diálogo para confirmação
            resposta = messagebox.askquestion("Confirmação", mensagem)
            
            if resposta == "yes":
            # Se o usuário confirmar, execute a função correspondente à versão
                versao_escolhida = versao_selecionada
                with open("versao_escolhida.pkl", "wb") as f:
                    pickle.dump(versao_escolhida, f)
                janela.withdraw()  # Esconde a janela
                funcoes_por_versao[versao_selecionada]()
                label_mensagem_final.config(text="Versão confirmada e função executada.")
            else:
                label_mensagem_final.config(text="Seleção cancelada.")

    def atualizar_mensagem(*args):
        versao_selecionada = versao_var.get()
        mensagem = f"Você selecionou a versão: {versao_selecionada}. Deseja confirmar?"
        label_mensagem_final.config(text=mensagem)

    def fechar_janela():
        # Adicione aqui qualquer código adicional que você queira executar antes de fechar a janela
        janela.destroy()

    def mostrar_janela(event=None):
        janela.deiconify()  # Exibe a janela novamente

    # Funções correspondentes às versões
    def funcao_v1_0_0():
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
        pyautogui.typewrite("cd Documents/V1.0.0/Colibri-iMX6_ToradexEasyInstaller_1.8-20181019")
        pyautogui.hotkey('enter')
        esc_button.checar_botao_emergencia()
        time.sleep(1)
        esc_button.checar_botao_emergencia()
        import ativando_python
        ativando_python.funcao_ativando_python()

    def funcao_v1_1_0():
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
        pyautogui.typewrite("cd Documents/V1.1.0/Colibri-iMX6_ToradexEasyInstaller_1.8-20181019")
        pyautogui.hotkey('enter')
        esc_button.checar_botao_emergencia()
        import ativando_python
        ativando_python.funcao_ativando_python()

    def funcao_v1_2_0():
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
        pyautogui.typewrite("cd Documents/V1.2.0/Colibri-iMX6_ToradexEasyInstaller_1.8-20181019")
        pyautogui.hotkey('enter')
        esc_button.checar_botao_emergencia()
        import ativando_python
        ativando_python.funcao_ativando_python()

    def funcao_v2_0_0():
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
        pyautogui.typewrite("cd Documents/V2.0.0/Colibri-iMX6_ToradexEasyInstaller_1.8-20181019")
        pyautogui.hotkey('enter')
        esc_button.checar_botao_emergencia()
        import ativando_python
        ativando_python.funcao_ativando_python()

    def funcao_v2_1_0():
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
        pyautogui.typewrite("cd Documents/V2.1.0/Colibri-iMX6_ToradexEasyInstaller_1.8-20181019")
        pyautogui.hotkey('enter')
        esc_button.checar_botao_emergencia()
        import ativando_python
        ativando_python.funcao_ativando_python()

# teste
    def funcao_v2_2_0():
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
        pyautogui.typewrite("cd Documents/V2.2.0/Colibri-iMX6_ToradexEasyInstaller_1.8-20181019")
        pyautogui.hotkey('enter')
        esc_button.checar_botao_emergencia()
        import ativando_python
        ativando_python.funcao_ativando_python()
        # TODO: adicionar caminho alternativo para a versão 2.2.0.

    # Criar a janela
    janela = tk.Tk()
    janela.title("Seleção de Versão")

    # Obter a largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir o tamanho da janela
    largura_janela = 800
    altura_janela = 300

    # Calcular a posição central da tela
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Configurar a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    # Adicionar uma mensagem inicial acima dos botões
    label_mensagem_inicial = tk.Label(janela, text="Selecione a versão desejada a ser gravada e clique em Confirmar.")
    label_mensagem_inicial.pack(pady=10)

    # Adicionar radiobuttons
    versoes = ["V1.0.0", "V1.1.0", "V1.2.0", "V2.0.0", "V2.1.0", "V2.2.0"]
    versao_var = tk.StringVar()

    # Configurar a função de atualização quando a seleção muda
    versao_var.trace_add("write", atualizar_mensagem)

    for versao in versoes:
        radiobutton = tk.Radiobutton(janela, text=versao, variable=versao_var, value=versao)
        radiobutton.pack(pady=5)

    # Adicionar botão de confirmar
    botao_confirmar = tk.Button(janela, text="Confirmar", command=exibir_mensagem)
    botao_confirmar.pack(pady=10)

    # Adicionar uma mensagem final
    label_mensagem_final = tk.Label(janela, text="")
    label_mensagem_final.pack(pady=10)

    botao_encerrar = tk.Button(janela, text="Encerrar script", command=encerrar_script)
    botao_encerrar.place(relx=1, rely=1, anchor='se')

    # Configurar a função para impedir o fechamento padrão da janela
    janela.protocol("WM_DELETE_WINDOW", lambda: None)  # Impede o fechamento da janela

    # Iniciar o loop principal
    janela.mainloop()

