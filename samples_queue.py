from collections import deque

# declarando um deque
queue = deque()
print('Deque vazio =', queue)

# inserindo dados no deque
queue.append(1)
print('Deque com 1 item =', queue)
queue.append(2)
print('Deque com 2 itens =', queue)
queue.append(3)
print('Deque com 3 itens =', queue)

# removendo/pegando dados do deque
data = queue.popleft()
print('Removendo item 1 =', data, queue)
data = queue.popleft()
print('Removendo item 2 =', data, queue)
data = queue.popleft()
print('Removendo item 3 =', data, queue)

import time

num_max = 1000000
print(f"Numero de elementos = {num_max}")
stack = deque()

s_time = time.time()
for i in range(num_max):
    stack.append(i)
e_time = time.time()
print(f"Tempo médio pra empilhar um elemento =", (e_time - s_time)/num_max)

s_time = time.time()
for i in range(num_max):
    stack.popleft()
e_time = time.time()
print(f"Tempo médio pra desempilhar um elemento =", (e_time - s_time)/num_max)


####################################################
from queue import Queue
# declarando uma fila
queue = Queue()

# inserindo dados na fila
queue.put(1)
queue.put(2)
queue.put(3)
print(queue)

# removendo/pegando dados da fila
data = queue.get()
print('Retornando 1 =', data)
data = queue.get()
print('Retornando 2 =', data)
data = queue.get()
print('Retornando 3 =', data)



##################################################
# declarando uma lista
queue = []
print('Lista vazia = ', queue)

# inserindo dados na lista
queue.append(1)
print('Lista com 1 item =', queue)
queue.append(2)
print('Lista com 2 itens =', queue)
queue.append(3)
print('Lista com 3 itens =', queue)

# removendo/pegando dados da lista
data = queue.pop(0) # o argumento `0` no método `.pop` representa o índice que será retirado da lista. Como estamos representando uma fila, há a necessidade de se retirar sempre o elemento mais antigo.
print('Removendo item 1 =', data, queue)
data = queue.pop(0)
print('Removendo item 2 =', data, queue)
data = queue.pop(0)
print('Removendo item 3 =', data, queue)


import time

num_max = 1000000
print(f"Numero de elementos = {num_max}")
queue = []

s_time = time.time()
for i in range(num_max):
    queue.append(i)
e_time = time.time()
print(f"Tempo médio pra empilhar um elemento =", (e_time - s_time)/num_max)

s_time = time.time()
for i in range(num_max):
    queue.pop(0)
e_time = time.time()
print(f"Tempo médio pra desempilhar um elemento =", (e_time - s_time)/num_max)