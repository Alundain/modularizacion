local_val = "unicornios mágicos"
def square(x):
    return x * x

class Usuario:
    def __init__(self, name):
        self.name = name
    
    def di_hola(self):
        return "hola"
print(square(5))
user = Usuario("Anna")
print(user.name)
print(Usuario.di_hola())


