class Calculator:
    def history(self):
        self._history = []
        
    def add(self, a, b):
        result = a + b
        self._history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self._history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self._history.append(f"{a} * {b} = {result}")
        return result
    
    def devide(self, a, b):
        if b == 0:
            self._history.append(f"{a} / {b} = Error")
            return "Error: Division by zero"
        result = a / b
        self._history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        return self._history
    
    def clear_history(self):
        self._history = []
    
    def save_history(self, filename):
        with open(filename, 'w') as file:
            for record in self._history:
                file.write(record + '\n')
                
    def load_history(self, filename):
        with open(filename, 'r') as file:   
            self._history = [line.strip() for line in file.readlines()]
            
    def __init__(self):
        self.history()
        

calc = Calculator()
calc.add(5, 3)
calc.subtract(10, 4)
calc.multiply(2, 6)
calc.devide(8, 2)
calc.devide(5, 0)
print(calc.get_history())
calc.save_history('calc_history.txt')
calc.clear_history()
calc.load_history('calc_history.txt')
print(calc.get_history())