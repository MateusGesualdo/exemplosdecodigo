# Python
- [Comando de saída e tipos primitivos de dados](#comando-de-saída-e-tipos-primitivos-de-dados)
- [Variáveis e manipulação de strings](#variáveis-e-manipulação-de-strings)
- [Comando de entrada](#comando-de-entrada)
- Condicionais
  - [`if`/`elif`/`else`](#ifelifelse)
  - [`match`/`case`](#matchcase)
- Loops
  - [`while`](#while)
  - [`for`](#for)
- [`try`/`except`](#tryexcept)
- [Funções e asserções](#funções-e-asserções)
- [Listas](#listas)

## Comando de saída e tipos primitivos de dados
```python
print("Hello, world!")

print(4 + 8) 
# 12

print(4 / 8) 
# 0.5

print(4 > 8)
# False
```
[Voltar ao início](#python)

## Variáveis e manipulação de strings
```python
message = "Hello, world!"

print(message)
# Hello, world!

print(type(message))
# <class 'str'>

print(len(message))
# 13

print(bool(message))
# True

print(int(message))
# ValueError: invalid literal for int() with base 10: 'Hello, world!' 

print(float(message))
# ValueError: could not convert string to float: 'hello, world!'

print(message.replace('world', 'friend'))
# Hello, friend!

print(message.upper())
# HELLO, WORLD!

print(message * 2)
# Hello, world!Hello, world!

print(message + ' =)')
# Hello, world! =)

print(message + 2)
# TypeError: can only concatenate str (not "int") to str

print(f"O valor atual da variável message é {message}")
# O valor atual da variável message é Hello, world!

print(message[0])
# H
```
[Voltar ao início](#python)

## Comando de entrada
```python
response = input("Quem está aí?")

print(f"Olá, {response}!")
```
[Voltar ao início](#python)

## Condicionais
### `if`/`elif`/`else`

```python
username = input("Digite seu nome de usuário (3 a 20 letras): ")

if not username.isalpha():
  print('ERRO: nome deve conter apenas letras')
elif len(username) < 3:
  print('ERRO: nome deve conter no mínimo 3 letras')
elif len(username) > 20:
  print('ERRO: nome deve conter no máximo 20 letras')
else:
  print(f'Olá, {username}!')

```
[Voltar ao início](#python)

### `match`/`case`
```python
day = "domingo"

match day:
  case "segunda" | "terça" | "quarta"| "quinta" | "sexta":
    print("Dia de trabalhar")
  case "sábado" | "domingo":
    print("Dia de descansar")
  case _:
    print("Dia da semana inválido")
```
[Voltar ao início](#python)
## Loops

### `while`
```python
dividend = 10
divisor = 3
quotient = 0
remainder = dividend

while remainder >= divisor:
  quotient = quotient + 1
  remainder = remainder - divisor
```
[Voltar ao início](#python)

### `for`
```python
message = "Hello, world!"

for character in message:
  print(character)
```
```python
for i in range(1,25,3):
  print(i)
```
[Voltar ao início](#python)

## `try`/`except`
```python
import random

try:
  random_number = random.randint(1, 10)
  user_guess = int(input("Digite um número inteiro de 1 a 10: "))

  print("Obrigado")
except ValueError as error:
  print(error)
```
[Voltar ao início](#python)

## Funções e asserções
```python
def get_remainder(dividend, divisor):

  remainder = dividend

  while remainder >= divisor:
    remainder -= divisor

  return remainder
```
```python
assert get_remainder(10, 3) == 1
# gera um AssertionError se a condição for falsa

assert get_remainder(42, 7) == 0
assert get_remainder(28, 10) == 8
```
[Voltar ao início](#python)

## Listas
```python
players = ['ada', 'bob', 'chris', 'dan']

print(players)
```
[Voltar ao início](#python)