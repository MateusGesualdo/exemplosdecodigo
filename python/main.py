players = ['ada', 'bob', 'chris', 'dan']

print(players)
# ['ada', 'bob', 'chris', 'dan']

print(type(players))
# <class 'list'>

print(len(players))
# 4

print(players[0])
# ada

players[1] = 'bill'
print(players)
# ['ada', 'bill', 'chris', 'dan']

# índices negativos acessam a lista de trás pra frente
print(players[-1])
# 'dan'  

print(players[1:4])
# ['bill', 'chris', 'dan']

print('fin' in players)
# False

players.append('eve')
print(players)
# ['ada', 'bill', 'chris', 'dan', 'eve']

players.insert(2, 'bob')
print(players)
# ['ada', 'bill', 'bob', 'chris', 'dan', 'eve']

players.remove('dan')
print(players)
# ['ada', 'bill', 'bob', 'chris', 'eve']

players.pop(0)
print(players)
# ['bill', 'bob', 'chris', 'eve']

players.sort(reverse = True)
print(players)
# ['eve', 'chris', 'bob', 'bill']

print(players.index('bob'))
# 2

print(players.index('fin'))
# ValueError: 'fin' is not in list

players.clear()
print(players)
# []