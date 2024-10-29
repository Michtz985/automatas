# Primera transición
def transition(state, symbol, stack):
    if state == 'q1' and symbol == 'a' and stack[-1] == 'B':
        stack.pop()
        stack.append('A')
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q1'
simbolo = 'a'
pila = ['B']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Segunda transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'ε' and stack[-1] == '#':
        stack.append('B#')
        return 'q3', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'ε'
pila = ['#']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Tercera transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'ε' and stack[-1] == 'A':
        stack.append('AA')
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'ε'
pila = ['A']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Cuarta transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'ε' and stack[-1] == 'B':
        stack.pop()
        return 'q2', stack
    else:
        return state, stack

# Ejemplo de uso
estado_inicial = 'q2'
simbolo = 'ε'
pila = ['B']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Quinta transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'a' and stack[-1] == 'B':
        stack.append('BB')
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'a'
pila = ['B']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Sexta transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'a' and stack[-1] == 'ε':
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'a'
pila = ['ε']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Séptima transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'a' and stack[-1] == 'A':
        stack.pop()
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'a'
pila = ['A']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Octava transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'a' and stack[-1] == 'B':
        stack.append('BB')
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'a'
pila = ['B']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")


# Novena transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'a' and stack[-1] == 'A':
        stack.pop()
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'a'
pila = ['A']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")

# Décima transición
def transition(state, symbol, stack):
    if state == 'q2' and symbol == 'a' and stack[-1] == 'B':
        stack.append('BB')
        return 'q2', stack
    else:
        return state, stack


estado_inicial = 'q2'
simbolo = 'a'
pila = ['B']
nuevo_estado, nueva_pila = transition(estado_inicial, simbolo, pila)
print(f"Nuevo estado: {nuevo_estado}, Nueva pila: {nueva_pila}")
#se llego a la transicion 10



