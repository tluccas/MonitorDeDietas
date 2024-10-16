import time
import os
# Dicionário de alimentos com calorias por 100g
alimentos = {
    "Arroz": 130,
    "Feijão": 77,
    "Frango": 165,
    "Maçã": 52,
    "Banana": 89,
    "Pão": 265,
    "Leite": 42,
    "Ovo": 155,
    "Abacate": 96,
    "Carne bovina grelhada": 278
}
consumidos = [] #Lista para armazenar os alimentos consumidos
IMC = [] #Lista para armazenar o tipo de dieta recomendado baseado no IMC
def Limpar(): #Funçao para limpar o terminal
    os.system('cls')
    
while True: # Entrada do nome do usuário, verificando se o nome contém apenas letras
    nome = str(input('Digite seu nome: '))
    if nome.isalpha():
        Limpar()
        print(f"\n== Olá {nome}! ==\n Seja Bem vindo ao nosso programa de \033[92mMonitoria de dieta e limitador de calorias!\033[0m\n ")
        break
    
    else:
        print("\n\033[91mERRO:\033[0m INSIRA APENAS LETRAS!\n")

def MostrarAlimentos(): # Função que exibe todos os alimentos disponíveis e suas calorias por 100g
    print("\nAlimentos na Dieta: ")
    for caloria in alimentos:
        print(f"== {caloria} ({alimentos[caloria]})Kcal/100g ==")
    print('\n')
    
def Nova_Refeição():  # Função para adicionar uma nova refeição e calcular as calorias consumidas
    print('==================== < \033[32mNOVA REFEIÇÃO\033[0m > ====================\n\n')
    calorias = 0
     
    while True: # Mostra os alimentos disponíveis
        MostrarAlimentos()
        while True:
            entrada = input("\033[92m[1]\033[0m ADD REF.\n\033[91m[2]\033[0m VOLTAR: ")
            controle = str(entrada)
    
            if controle == '1': 
                registro = input("\nNome do Alimento: ").capitalize()
                while True: # Mantém o loop até que o usuário insira um número válido
                    try:
                        quant = float(input("Quantidade (em gramas): ").strip())# Solicita um número diretamente e remove espaços
                        break  
                    except ValueError:
                            print("\033[91mERRO:\033[0m ENTRADA INVÁLIDA! INSIRA O VALOR RECOMENDADO\n")
                # Verifica se o alimento está no dicionário
                if registro in alimentos:
                    soma = (alimentos[registro] * quant) / 100 # Calcula as calorias baseadas na quantidade inserida
                    calorias += soma # Adiciona as calorias calculadas ao total
                    print("\n\033[32mALIMENTO INSERIDO\033[0m")
                    if not registro in consumidos:
                        consumidos.append(registro)
                else:
                    print(f"\n\033[91mO alimento {registro} não está na sua dieta!\033[0m\n")
                
            
            elif controle == '2':
                print("\n\033[91mDIRECIONANDO P/ MENU...\033[0m")
                time.sleep(1.5)
                Limpar()
                break
            else:
                print("\n\033[91mERRO:\033[0m ENTRADA INVÁLIDA!\n")
                continue

        return calorias
      

def Adicionar_alimentos_na_dieta():
    print('==================== < \33[32mNOVO ALIMENTO NA DIETA\033[0m > ====================\n\n')

    while True:

     entrada = input("\033[92m[1]\033[0m NOVO ALIMENTO\n\033[91m[2]\033[0m VOLTAR: ")
     controle = str(entrada)
     if controle == '1':
         novo = str(input("\nNome do Alimento: ")).capitalize()

         while True:  
            try:
                cal = float(input("\nKcal/100g: "))
                break                
            except ValueError:
                print("\033[91mERRO:\033[0m ENTRADA INVÁLIDA!\n")
         
         if novo in alimentos:  # Verifica se o alimento já existe no dicionário
             print("\n\033[91mERRO:\033[0m O ALIMENTO JÁ EXISTE\n")
         else:
             alimentos[novo] = cal
     elif controle == '2':
         print("\n\033[91mDIRECIONANDO P/ MENU...\033[0m")
         time.sleep(1.5)
         Limpar()
         break
     else:
         print("\n\033[91mERRO:\033[0m ENTRADA INVÁLIDA\n")


def Calcular_IMC():  # Aqui temos a funcão para calcular o IMC

    print("\n\n============== < \33[32mCALCULE SEU IMC E TIPO DE DIETA\33[0m > ==============\n\n")
    while True:
     entrada = input("\n\033[92m[1]\033[0mCALCULAR\n\033[91m[2]\033[0mVOLTAR: ")
     controle = str(entrada)
     if controle == '1':
        IMC.clear() #Exclui as recomendações anteriores
        try:
            altura = float(input('\nDigite sua altura: '))
            peso = float(input('\nDigite seu peso: '))

            if altura > 3: # Converte altura para metros, caso seja digitada em centímetros
                altura/= 100

        except ValueError:
            print("\n\033[91mERRO:\033[0m ENTRADA INVÁLIDA\n")
            continue
        imc = peso / (altura*altura) # Aqui ocorre o processamento dos dados do usuário e calcula o Imc
        
        if imc < 18.5: # Condições para definir o tipo de dieta baseado no IMC
            print(f'ATENÇÃO {nome}: Você está abaixo do peso! | IMC: {imc:.2f}\n')
            print("SUA DIETA: \033[32mSUPERÁVIT CALORICO\033[0m")
            IMC.append("SUPERÁVIT CALORICO")
        elif imc == 18.5 or imc <= 24.99:
            print(f'Seu IMC está ideal {nome} | IMC: {imc:.2f}\n')
            print("SUA DIETA: \033[32mMANUTENÇÃO\033[0m")
            IMC.append("MANUTEÇÃO")
        elif imc == 25.0 or imc <= 29.99:
            print(f'ATENÇÃO: Você está acima do peso {nome}! | IMC: {imc:.2f}\n')
            print("SUA DIETA: \033[32mDÉFICIT CALORICO\033[0m")
            IMC.append("DÉFICIT CALORICO")
        elif imc >= 30:
            print(f'ATENÇÃO: Você está obeso {nome}! | IMC: {imc:.2f}\n')
            print("SUA DIETA: \033[32mDÉFICIT CALORICO\033[0m")
            IMC.append("DÉFICIT CALORICO")  
            
     elif controle == '2':
         print("\n\033[91mDIRECIONANDO P/ MENU...\033[0m")
         time.sleep(1.5)
         Limpar()
         break
     else:
         print("\n\033[91mERRO:\033[0m OPÇÃO INVÁLIDA")
    
      
def Definir_Limite():
    limite = 0
    
    print('==================== < \033[32mLIMITE SUAS CALORIAS\033[0m > ====================\n\n')
    if len(IMC) > 0:
        print('DIETA RECOMENDADA: ')
        print(''.join(IMC))
        print('\n')
    else:
        print("FAÇA UMA AVALIAÇÃO EM == \033[32mDIETA IDEAL\033[0m ==\n")
    while True:
        entrada = input("\033[92m[1]\033[0mLIMITAR\n\033[91m[2]\033[0mAPAGAR LIMITE\n\033[92m[3]\033[0mVOLTAR: ")
        controle = str(entrada)
        if controle == '1':
            while True:  # Mantém o loop até que uma entrada válida seja fornecida
                try:
                    limite = float(input("INSIRA O LIMITE DE CALORIAS: "))
                    break                
                except ValueError:
                    print("\033[91mERRO:\033[0m Entrada inválida! Por favor, insira um valor em Kcal válido.\n")
            print("\033[32mADICIONANDO...\033[0m\n")
            time.sleep(1)
            
        elif controle == '2':
         limite -= limite
         print("\n\033[91mAPAGANDO...\033[0m")
         time.sleep(1)
        elif controle == '3':
         print("\n\033[91mDIRECIONANDO P/ MENU...\033[0m")
         time.sleep(1.5)
         Limpar()
         break
        else:
            print("\n\033[91mERRO:\033[0m OPÇÃO INVÁLIDA!")
    print("\n\033[32mLIMITE DEFINIDO: \033[0m",limite,"kcal\n")
    return limite

            
def Mostrar_Menu():
    limite2 = 0 # Armazena o limite de calorias diário
    calorias_total = 0 # Total de calorias consumidas
    while True:
     print('==================== < \033[32mMENU\33[0m > ====================\n\n')
     entrada = input("\033[91m[1]\033[0m< Inserir refeição >\n\033[92m[2]\033[0m< Add Novo Alimento na Dieta >\n\033[91m[3]\033[0m< Tipo Dieta Ideal >\n\033[92m[4]\033[0m< Limitar Calorias >\n\033[91m[5]\033[0m< Ver Macros >: ")
     inicio = str(entrada)
     if inicio == '1':
         Limpar()
         calorias = Nova_Refeição()
         calorias_total += calorias
         
        
     elif inicio == '2':
         Limpar()
         Adicionar_alimentos_na_dieta()
         
     elif inicio == '3':
        Limpar()
        Calcular_IMC() 
         
     elif inicio == '4':
        Limpar()
        limite = Definir_Limite()
        limite2 = limite
        
         
     elif inicio == '5':
         Limpar()
         print('==================== < \033[32mMACROS\33[0m > ====================\n\n')
         time.sleep(1)
         if len(IMC) > 0:
          print('TIPO DE DIETA RECOMENDADO :','\033[92m',IMC[0],'\033[0m')
         else:
             print("NENHUMA RECOMENDAÇÃO DE DIETA!")

         if len(consumidos) > 0:
          print("\nAlimentos consumidos:\n")
          for x in consumidos:
            print(f"{x}")
          print(f"\nCalorias consumidas {calorias_total:.2f}kcal\n")
         else:
             print("NENHUMA REFEIÇÃO COMPLETA\n")
         if limite2 != 0: # Compara as calorias consumidas com o limite definido
            if limite2 > calorias_total:
                falta = limite - calorias_total
                print(f"Ainda faltam {falta:.2f}kcal")
            elif limite2 == calorias_total:
                print("Parabéns você alcançou sua meta!")
            elif limite2 < calorias_total:
                passou = calorias_total - limite
                print(f"Você ultrapassou seu limite, consumiu {passou:.2f}kcal a mais!")
              
     else:
         print("\n\033[91mERRO:\033[0m OPÇÃO INVÁLIDA!")

Mostrar_Menu()
