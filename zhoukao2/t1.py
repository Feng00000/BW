#1.生成50个范围在0-80的整数，并且能够打印输出？
import  random
s=[]
for i in range(50):
    f=random.choice(range(0,81))
    s.append(f)
print('50个范围在0-80的整数',s)



