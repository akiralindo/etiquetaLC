# entradas
etiqueta = ""
nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
cpf = input("Digite seu CPF:")

# processamento
etiqueta = "\n\n\n"
etiqueta += "#########-DADOS-#########\n"
etiqueta += "# Nome: " + nome + " \t\t#\n"
etiqueta += "# Idade: " + str(idade) + " \t\t#\n"
etiqueta += "# CPF: " + str(cpf) + " \t#\n"
etiqueta += "#########################"
etiqueta += "\n\n\n"

# saídas
print(etiqueta)
