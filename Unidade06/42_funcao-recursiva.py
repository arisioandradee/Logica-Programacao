#O recurso de função recursiva é quando uma função chama a si mesma. Ela não é tão comum!
    #Temos que ter cuidado pois pode ser criado um loop infinito. 

def soma_ate_100(n):
    if n < 100:
        n += 1
        print(n)
        soma_ate_100(n)
    else:
        return n
    
numero = 94

num_100 = soma_ate_100(numero)
    

