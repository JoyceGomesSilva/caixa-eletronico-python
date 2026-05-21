# CLASSE DA CONTA 
class conta:
    def __init__(self, saldo_inicial):
        self.dinheiro = saldo_inicial
        self.historico = []

    def formatar(self, valor):
        return f"R${valor:.2f}".replace('.',',')
     
    def ver_saldo(self):
        print("Seu saldo atual é ", self.formatar(self.dinheiro))

    def depositar(self):
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            self.dinheiro += valor
            self.historico.append(f"Depósito: +R$ {self.formatar(valor)}")
            print(f"Valor depositado. Agora seu saldo é de {self.formatar(self.dinheiro)}")
        else:
            print("Valor inválido.")
            
    def saque(self):
        saque = float(input("Quanto deseja sacar? "))
        if 0 < saque <= self.dinheiro:
            self.dinheiro -= saque
            self.historico.append(f"Saque: -{self.formatar(saque)}")
            print("Saque realizado com sucesso!")
            print(f"Seu saldo atual é de {self.formatar(self.dinheiro)}")
        else:
                print("Saldo insuficiente ou valor inválido.")

    def mostrar_historico(self):
         print("\n----- HISTÓRICO -----")
         if len(self.historico) == 0:
              print("Nenhuma operação realizada.")
         else:
              for item in self.historico:
                   print("-", item)

#CLASSE DO USUARIO
class usuario:
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.senha = ""
        self.logado = False

    def cadastrar(self):
        self.nome = input("Digite seu nome: ")
        self.email = input("Digite seu e-mail: ")
        self.senha = input("Digite sua senha: ")
        print("Cadastro realizado com sucesso!!\n")

    def login(self):
        if self.email == "":
            print("Você precisa se cadastrar primeiro!\n")
            return False

        print("\n------ LOGIN ------")
        email = input("Digite seu e-mail: ")
        self.digitada = input("Digite sua senha: ")

        if email == self.email and self.digitada == self.senha:
            print("Login realizado com sucesso!\n")
            self.logado = True
            return True
        else:
            print("Usuário ou senha incorretos.\n")
            return False

#CAIXA PRINCIPAL
usuario2 = usuario()

print("===============================")
print("Bem-Vindo ao Caixa Eletônico")
print("===============================")

opcao = 0
tentativas = 0

# MENU LOGIN / CADASTRO
while opcao != 3:
    print("O que você deseja fazer?\n")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair\n")

    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
        if usuario2.login():
            break
        else:
              tentativas +=1
              if tentativas >= 3:
                print("Muitas tentativas. Tente novamente mais tarde.")
                exit()

    elif opcao == 2:
        usuario2.cadastrar()

    elif opcao == 3:
        print("Caixa encerrado...")
        exit();
    
    else:
        print("Opção Inválida. Tente novamente.\n")


#VERIFICACAO DE LOGIN
if not usuario2.logado:
    print("Você precisa fazer login primeiro")
    exit();


# DENTRO DA CONTA
dinheiro = float(input("Digite seu saldo inicial: "))
Conta = conta(dinheiro)

# MENU DA CONTA
while True:
    print("\n-----------------------------")
    print("O que você deseja fazer hoje?")
    print("-----------------------------")
    print("\n1 - Ver saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("4 - Histórico")
    print("5 - Sair")

    escolha = int(input("\nEscolha uma opção: \n"))

    if escolha == 1:
        Conta.ver_saldo()

    elif escolha == 2:
         Conta.depositar()

    elif escolha == 3:
        Conta.saque()
    
    elif escolha == 4:
         Conta.mostrar_historico()

    elif escolha == 5:
            print("Caixa encerrado.")
            print("-----------------------------")
            break

    else:
            print("Opção Inválida. Tente novamente.")
