class Calculator:
    def __init__(self, a,b= None):
        self.a = a
        if (b is not None):
            self.b = b


    def sum(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def mult(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

    def mod(self):
        return self.a%self.b    
    
    def exp(self):
        return self.a**self.b

    def med(self):
        return (self.a+self.b)/2

    def fat(self):
        rst=1
        count=1

        while count <= self.a:
            rst *= count
            count += 1

        return rst

op= input("Escolha a operacao de acordo com o menu -\n" 
        "1. Soma\n 2.Subtracao \n 3.divisao \n 4.Multiplicacao\n"
        "5.Modulo\n 6.Exponenciacao 7.media entre dois valores \n 8.Fatorial \n") 

if op == 8:
    a = input("Digite o numero para calcular fatorial:")
    c = Calculator(a)
    print(c.fat())
    
else:
    if op < 8 or op > 1:
        a = input("Digite o primeiro numero para o calculo:")
        b = input("Digite o segundo numero para o calculo:")
        c = Calculator(a,b)

        if op == 1:
            print(c.sum())
        
        elif op == 2:
            print(c.sub())
    
        elif op == 3:
            print(c.div())

        elif op == 4:
            print(c.mult())

        elif op == 5:
            print(c.mod())
    
        elif op == 6:
            print(c.exp())

        else:
            print(c.med())
    else:
        print("Numero de operacao invalida!")