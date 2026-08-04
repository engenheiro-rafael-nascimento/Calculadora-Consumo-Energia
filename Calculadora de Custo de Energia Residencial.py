import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
lista_equipamentos = []
titulo_fonte = ("Calibri Title", 15, "bold")

janela = tk.Tk()
janela.geometry("800x600")
janela.title("Calculadora de Energia")

tk.Label(janela, text=("Nome do Equipamento"), font=(titulo_fonte)).pack(pady=10)
equipamento_nome = tk.Entry(janela)
equipamento_nome.pack(pady=10)

tk.Label(janela, text=("Potência do Equipamento"), font=(titulo_fonte)).pack(pady=10)
equipamento_potencia = tk.Entry(janela)
equipamento_potencia.pack(pady=10)

tk.Label(janela, text=("Tempo de Utilização do Equipamento"), font=(titulo_fonte)).pack(pady=10)
equipamento_uso = tk.Entry(janela)
equipamento_uso.pack(pady=10)

tk.Label(janela, text=("Preço kW"), font=(titulo_fonte)).pack(pady=10)
tarifa_kw = tk.Entry(janela)
tarifa_kw.pack(pady=10)

def cadastro():
    try:
        equipamento = {}
        if not equipamento_nome.get().strip():
            messagebox.showerror("Erro", "Preencha o Campo do Nome do Equipamento!")
            return
        equipamento['nome'] = equipamento_nome.get().strip()
        if not equipamento_potencia.get().strip():
            messagebox.showerror("Erro", "Preencha o Campo da Potência do Equipamento")
            return
        equipamento['potencia'] = float(equipamento_potencia.get().replace(',', '.'))
        if not equipamento_uso.get().strip():
            messagebox.showerror("Erro", "Preencha o Campo do Tempo de Utilização do Equipamento")
            return
        equipamento['tempo_uso'] = float(equipamento_uso.get().replace(',', '.'))
        if not tarifa_kw.get().strip():
            messagebox.showerror("Erro", "Preencha o Preço do kW")
            return
        tarifa_calculo = float(tarifa_kw.get().replace(',', '.'))
        equipamento['consumo_equipamento'] = equipamento['potencia'] * equipamento['tempo_uso'] * tarifa_calculo * 30 / 1000
        lista_equipamentos.append(equipamento)
        messagebox.showinfo("Sucesso", "Equipamento Cadastrado")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos nos campos de potência, tempo e tarifa!")

botao_cadastro = tk.Button(janela, text=("Cadastrar Equipamento"), font=(titulo_fonte), command=cadastro)
botao_cadastro.pack(pady=15)

def exportar_salvar():
    if not lista_equipamentos:
        messagebox.showerror("Erro", "Cadastre ao Menos Um Equipamento")
        return
    df = pd.DataFrame(lista_equipamentos)
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=(".xlsx"), filetypes=[("Arquivos de Planilha", "*.xlsx"), ("Todos os Arquivos", "*.")], title=("Salvar Relatório"))
    if not caminho_arquivo:
        return
    df.to_excel(caminho_arquivo, index=False)

botao_exportar_salvar = tk.Button(janela, text=("Exportar e Salvar Relatório"), command=exportar_salvar, font=(titulo_fonte))
botao_exportar_salvar.pack(pady=15)

def abrir_relatório():
    caminho_arquivo = filedialog.askopenfilename(defaultextension=(".xlsx"), filetypes=[("Arquivos de Planilha", "*.xlsx"), ("Todos os Arquivos", "*.")], title=("Abrir Relatório"))
    if not caminho_arquivo:
        return
    df = pd.read_excel(caminho_arquivo)
    print(df)

botao_abrir = tk.Button(janela, text=("Abrir Relatório"), font=(titulo_fonte), command=abrir_relatório)
botao_abrir.pack(pady=15)

janela.mainloop()

