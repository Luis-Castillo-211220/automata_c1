import tkinter as tk

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                         'U', 'V', 'W', 'X', 'Y', 'Z', '-'}
        
        self.transitions = {
            'q0': {'H': 'q1'},
            'q1': {'H': 'q2', 'I': 'q2', 'J': 'q2', 'K': 'q2', 'L' : 'q2', 'M': 'q2', 'N': 'q2', 'O': 'q2', 'P': 'q2', 'Q' : 'q2', 
                   'R': 'q2', 'S': 'q2', 'T': 'q2'},
            'q2': {'-': 'q3'},
            'q3': {'0': 'q4' ,'1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9' : 'q10'},
            'q4': {'0': 'q5' ,'1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9' : 'q11'},
            'q5': {'0': 'q6' ,'1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9' : 'q12'},
            'q6': {'1': 'q7', '2': 'q7', '3': 'q7', '4': 'q7', '5': 'q7', '6': 'q7', '7': 'q7', '8': 'q7', '9' : 'q7'},
            'q7': {'-': 'q8'},
            'q8': {'A': 'q9', 'B': 'q9', 'C': 'q9', 'D': 'q9', 'E' : 'q9', 'F': 'q9', 'G': 'q9', 'H': 'q9', 'I': 'q9', 'J': 'q9', 
                   'K': 'q9', 'L': 'q9', 'M': 'q9', 'N': 'q9', 'O': 'q9', 'P': 'q9', 'Q' : 'q9', 'R': 'q9', 'S': 'q9', 'T': 'q9', 
                   'U': 'q9', 'V': 'q9', 'W': 'q9', 'X': 'q9', 'Y' : 'q9', 'Z': 'q9'},
            'q9': {},
            'q10': {'0': 'q11' ,'1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9' : 'q11'},
            'q11': {'0': 'q12','1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9' : 'q12'},
            'q12': {'0': 'q7', '1': 'q7', '2': 'q7', '3': 'q7', '4': 'q7', '5': 'q7', '6': 'q7', '7': 'q7', '8': 'q7', '9' : 'q7'},
        }
        self.start_state = 'q0'
        self.accept_states = {'q9'}
        
    def validar(self, input_string):
        current_state = self.start_state
        visited_states = [current_state]  # Lista para almacenar los estados visitados
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # Caracter no valido
            if current_state not in self.states:
                return False  # Estado no valido
            current_state = self.transitions[current_state].get(symbol, None)
            visited_states.append(current_state)  # Agregar el estado actual a la lista de estados visitados
            if current_state is None:
                return False  # No hay transicion para el símbolo

        if current_state in self.accept_states:
            return visited_states  # Devolver la lista de estados visitados si la cadena es válida

        return False

automata = AFD()

def verificarCadena():
    input_string = entrada.get()
    result = automata.validar(input_string)
    if result:
        resultado.config(text=f"Cadena válida: {input_string}")
        mostrarRecorrido(result)
    else:
        resultado.config(text=f"Cadena no válida: {input_string}")
        mostrarRecorrido([])  # Limpiar el recorrido en caso de cadena no válida

def mostrarRecorrido(visited_states):
    recorrido_text = " - ".join(visited_states)
    recorrido_label.config(text=f"Recorrido:\n{recorrido_text}")

ventana = tk.Tk()
ventana.title("Autómata Rangos")
ventana.geometry("420x280")

etiqueta = tk.Label(ventana, text="Ingrese una cadena:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Verificar", command=verificarCadena)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

recorrido_label = tk.Label(ventana, text="Recorrido:")
recorrido_label.pack()

# Ejecutar la ventana
ventana.mainloop()