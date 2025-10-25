# reduce: reducerecebe uma função e um iterável como argumentos e 
# retorna um único valor que é o resultado da redução do iterável a 
# um único valor usando a função. Por exemplo:

from functools import reduce

def  add( x, y ): 
    return x + y 

numbers = [ 1 , 2 , 3 , 4 , 5 ] 
sum_of_numbers = reduce(add, numbers) 
print(sum_of_numbers) # 15
