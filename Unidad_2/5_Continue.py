for contador in range(1,11):
#1.Contador=1  1% 2== 0 ---->Si lo imprime
#2.Contador=2  2% 2== 0  ----> No lo imprime
#3.Contador=3  3% 2== 0   ---->Si lo imprime
#4.Contador=4  4% 2== 0   ---->No lo imprime
    if contador %2 ==0:
        continue
    print(contador)