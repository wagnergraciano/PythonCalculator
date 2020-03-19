# class Calculator:
#     def __init__(self, a ,b, op):
#         self.a = a
#         self.b = b
#         self.op = op

#     def sum(self,a,b):
#         return a+b
    
#     def sub(self,a,b):
#         return a-b
    
#     def mult(self,a,b):
#         return a*b

#     def div(self,a,b):
#         return a/b

#     def mod(self,a,b):
#         return a%b    
    
#     def exp(self,a,b):
#         return a**b

#     def med(self,a,b):
#         return (a+b)/2

#     def fat(self,a):
#         rst=1
#         count=1

#         while count <= a:
#             rst *= count
#             count += 1

#         return rst

op= input("Escolha a operacao de acordo com o menu -\n" 
        "1. Soma\n 2.Subtracao \n 3.divisao \n 4.Multiplicacao\n"
        "5.Modulo\n 6.Exponenciacao 7.media entre dois valores \n 8.Fatorial \n") 

if op == 8:
    a = input("Digite o numero para calcular fatorial:")
    rst=1
    count=1
    while count <= a:
        rst *= count
        count += 1

    print(rst)
else:
    if op < 8 or op > 1:
        a = input("Digite o primeiro numero para o calculo:")
        b = input("Digite o segundo numero para o calculo:")

        if op == 1:
            print(a+b)
        
        elif op == 2:
            print(a-b)
    
        elif op == 3:
            print(a/b)

        elif op == 4:
            print(a*b)

        elif op == 5:
            print(a%b)
    
        elif op == 6:
            print(a**b)

        else:
            print((a+b)/2)
    else:
        print("Numero de operacao invalida!")