# Info do user
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
cor_favorita = input("Qual é a sua cor favorita? ")
comida_favorita = input("Qual é a sua comida favorita? ")
animal_favorito = input("Qual é o seu animal favorito? ")

# Bobagens e vozes da minha cabeça
print("\nResumo das suas preferências:")
print(f"Olá, {nome}! Aqui está o que descobrimos sobre você:")
print(f"- Você tem {idade} anos, mas ainda ama {animal_favorito}s como uma criança!")
print(f"- Se você pudesse escolher uma cor para o mundo inteiro, ele seria {cor_favorita}.")
print(f"- Quando o assunto é comida, nada supera um bom prato de {comida_favorita}.")
print(f"- E se você fosse um super-herói, seu uniforme certamente teria toques de {cor_favorita}.")

# Frases com números aleatórios
import random

anos_futuros = random.randint(1, 10)
print(f"\nPrevisão: Em {anos_futuros} anos, você estará viajando pelo mundo com seu {animal_favorito} de estimação,")
print(f"vestindo uma capa de super-herói da cor {cor_favorita} e comendo {comida_favorita} em todas as refeições!")
