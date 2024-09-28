import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para validar o CPF
def verificador_cpf(cpf_entry):
    cpf = cpf_entry.get()

    # Remover pontos e hífens do CPF digitado
    cpf_formatado = cpf.replace('.', '').replace('-', '')

    # Verificar se o CPF tem 11 dígitos
    if len(cpf_formatado) != 11:
        messagebox.showerror("Erro", "CPF incorreto. Digite novamente.")
        return
    
    # Calculando o DV1
    soma_dv1 = sum(int(cpf_formatado[i]) * (10 - i) for i in range(9))
    resto_dv1 = 11 - (soma_dv1 % 11)
    dv1 = 0 if resto_dv1 > 9 else resto_dv1

    # Calculando o DV2
    soma_dv2 = sum(int(cpf_formatado[i]) * (11 - i) for i in range(10))
    resto_dv2 = 11 - (soma_dv2 % 11)
    dv2 = 0 if resto_dv2 > 9 else resto_dv2
    
    # Verificando os dígitos verificadores
    if dv1 == int(cpf_formatado[9]) and dv2 == int(cpf_formatado[10]):
        messagebox.showinfo("Resultado", f'CPF {cpf} é válido.')
    else:
        messagebox.showinfo("Resultado", f'CPF {cpf} é inválido.')

# Função para formatar o CPF enquanto é digitado
def formatar_cpf(entry):
    value = entry.get()
    if len(value) == 3 or len(value) == 7:
        entry.insert(tk.END, '.')
    elif len(value) == 11:
        entry.insert(tk.END, '-')
    elif len(value) > 14:
        entry.delete(len(value)-1, tk.END)

# Função principal para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Verificador de CPF")
    
    # Criando rótulo e campo de entrada para o CPF
    cpf_label = tk.Label(root, text="CPF: ")
    cpf_label.grid(row=0, column=0, padx=10, pady=10)

    cpf_entry = ttk.Entry(root)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    cpf_entry.bind('<KeyRelease>', lambda event: formatar_cpf(cpf_entry))

    # Botão para acionar a verificação do CPF
    verificar_button = ttk.Button(root, text="Verificar CPF", command=lambda: verificador_cpf(cpf_entry))
    verificar_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Chamando a função principal para criar a interface gráfica
if __name__ == '__main__':
    criar_interface()
