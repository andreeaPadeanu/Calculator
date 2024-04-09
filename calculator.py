class CalculatorException(Exception):
    pass

class Calculator(object):
    def read(self):
        return input('>')
    
    def __init__(self):
        self.operators={'+': 1, '-': 1, '*': 2, '/': 2}
    
    def checkOperator(self, char):
        return char in self.operators
    
    def checkOrder(self, el1, el2):
        return self.operators[el2]>=self.operators[el1]
    
    def performOperation(self, val, operators):
        operator=operators.pop()
        right=val.pop()
        left=val.pop()
        if operator=='+':
            val.append(left + right)
        elif operator=='-':
            val.append(left - right)
        elif operator=='*':
            val.append(left * right)
        elif operator=='/':
            if right==0:
                raise CalculatorException("You can not divide by 0")
            val.append(left / right)
    
    def eval(self, string):
        val=[]
        operators=[]
        i=0
        while i<len(string):
            if string[i]==' ':
                i=i+1
                continue
            if string[i]=='(':
                operators.append(string[i])
            elif string[i].isdigit():
                j=i
                while j<len(string) and (string[j].isdigit() or string[j]=='.'):
                    j=j+1
                val.append(int(string[i:j]))
                i=j - 1
            elif string[i]==')':
                while operators[-1]!='(':
                    self.performOperation(val, operators)
                operators.pop()
            elif self.checkOperator(string[i]):
                while (operators and operators[-1] in self.operators and
                       self.checkOrder(string[i], operators[-1])):
                    self.performOperation(val, operators)
                operators.append(string[i])
            else:
                raise CalculatorException("The character "+string[i]+" is invalid")
            i=i+1
        while operators:
            if operators[-1]=='(':
                raise CalculatorException("The bracket is not closed")
            self.performOperation(val, operators)
        return val[0]
    
    def loop(self):
        while True:
            line=self.read()
            if line=='quit':
                break
            try:
                result =self.eval(line)
                print(result)
            except CalculatorException as e:
                print("Error: ")
                print(e)

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
