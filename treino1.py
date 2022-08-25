import sys
import math

escolha1 = 0
escolha2 = 0
escolha3 = 0

#valores
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
valor = 0

print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");

escolha1 = int(input(">>> Sua opção "))
print("=-=" * 20)
print("  [Digite os números desejados]")
num1 = float(input("  Primeiro Número = "))
num2 = float(input ("  Segundo Número = "))
print("=-=" * 20)


while escolha1 != 9:
  #soma
    if escolha1 == 1:
        valor = num1 + num2
        print(f"O {num1:.1f} somado com {num2:.1f} é igual {valor:.2f}")

        print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
        escolha2 = int(input(">>> Sua opcao "))
        print("=-=" * 20)

        if escolha2 == 1:
            print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
            escolha1 = int(input(">>> Sua opção "));

        elif escolha2 == 2:
            break; #aa
          
        elif escolha2 >= 3:

            print("Error\n")
            print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
            escolha2 = int(input(">>> Sua opcao "))
            print("=-=" * 20)

            if escolha2 == 1:
                print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
                escolha1 = int(input(">>> Sua opção "));
                print("=-=" * 20)

            elif escolha2 == 2:
                break;
  #divisao
    if escolha1 == 2:
        valor = num1 / num2
        print(f"O {num1:.1f} dividido por {num2:.1f} e igual {valor:.2f}")

        print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
        escolha2 = int(input(">>> Sua opcao "))

        if escolha2 == 1:
            print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
            escolha1 = int(input(">>> Sua opção "));

        elif escolha2 == 2:
            break;

        elif escolha2 >= 3:

            print("Error\n")
            print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
            escolha2 = int(input(">>> Sua opcao "))

            if escolha2 == 1:
              print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
              escolha1 = int(input(">>> Sua opção "));

            elif escolha2 == 2:
                break; #aa
            elif escolha2 >= 3:

              print("Error\n")
              print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
              escolha2 = int(input(">>> Sua opcao "))

              if escolha2 == 1:
                print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
                escolha1 = int(input(">>> Sua opção "));
                print("=-=" * 20)

              elif escolha2 == 2:
                break;  
            
  #multiplicacao
    if escolha1 == 3:
        valor =  num1 * num2
        print(f"O {num1:.1f} vezes {num2:.1f} e igual {valor:.2f}")

        print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
        escolha2 = int(input(">>> Sua opcao "))
        print("=-=" * 20)

        if escolha2 == 1:
            print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
            escolha1 = int(input(">>> Sua opção "));
            print("=-=" * 20)

        elif escolha2 == 2:
            break;

        elif escolha2 >= 3:

            print("Error\n")
            print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
            escolha2 = int(input(">>> Sua opcao "))

            if escolha2 == 1:
                print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
                escolha1 = int(input(">>> Sua opção "));
                print("=-=" * 20)

            elif escolha2 == 2:
                break;
    #raiz          
    if escolha1 == 4:
        num2 = 0
        valor =  math.sqrt(num1)
        print(f"A raiz de {num1:.1f} e igual {valor:.2f}")

        print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
        escolha2 = int(input(">>> Sua opcao "))
        print("=-=" * 20)

        if escolha2 == 1:
            print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
            escolha1 = int(input(">>> Sua opção "));
            print("=-=" * 20)

        elif escolha2 == 2:
            break;

        elif escolha2 >= 3:

            print("Error\n")
            print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
            escolha2 = int(input(">>> Sua opcao "))

            if escolha2 == 1:
                print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
                escolha1 = int(input(">>> Sua opção "));
                print("=-=" * 20)

            elif escolha2 == 2:
                break;
  #Multiplicacao por pi
    if escolha1 == 5:
        
      num2 = 0
      valor =  math.pi * num1
      print(f"O {num1:.1f} vezes PI e {valor:.2f}")

      print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
      escolha2 = int(input(">>> Sua opcao "))
      print("=-=" * 20)

      if escolha2 == 1:
          print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
          escolha1 = int(input(">>> Sua opção "));
          print("=-=" * 20)

      elif escolha2 == 2:
          break;

      elif escolha2 >= 3:

          print("Error\n")
          print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
          escolha2 = int(input(">>> Sua opcao "))

          if escolha2 == 1:
              print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
              escolha1 = int(input(">>> Sua opção "));
              print("=-=" * 20)

          elif escolha2 == 2:
              break;
  #Potencia
    if escolha1 == 6:
        num2 = 0
        valor =  (num1 * num1)
        print(f"A Portencia de {num1:.1f} e igual {valor:.2f}")

        print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
        escolha2 = int(input(">>> Sua opcao "))
        print("=-=" * 20)

        if escolha2 == 1:
            print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
            escolha1 = int(input(">>> Sua opção "));
            print("=-=" * 20)

        elif escolha2 == 2:
            break;

        elif escolha2 >= 3:

            print("Error\n")
            print("  [ 1 ]Voltar ao inicio   \n  [ 2 ]Finalizar programa")
            escolha2 = int(input(">>> Sua opcao "))

            if escolha2 == 1:
                print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");
                escolha1 = int(input(">>> Sua opção "));
                print("=-=" * 20)

            elif escolha2 == 2:
                break;
    #Sair do programa
    if escolha1 == 7:
      print("Finalizando...")
      break;
    #Mudar numeros
    if escolha1 == 8:
      print("  [Digite os números desejados]")
      num1 = float(input("  Primeiro Número = "))
      num2 = float(input ("  Segundo Número = "))
      print("=-=" * 20)
      
      print("Escolha uma das opções abaixo  \n  [ 1 ]Soma  \n  [ 2 ]Divisão  \n  [ 3 ]Multiplicação  \n  [ 4 ]Raiz (Conta apenas com o primeiro numero)  \n  [ 5 ]Multiplicação com PI (Multiplicado apenas o primeiro numero)  \n  [ 6 ]Potência (Multiplicado apenas o primeiro numero)  \n  [ 7 ]Sair do Programa\n  [ 8 ]Mudar numeros");

      escolha1 = int(input(">>> Sua opção "))
      print("=-=" * 20)
      