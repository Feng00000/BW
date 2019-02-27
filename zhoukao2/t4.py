#编写一个函数，判断一个字符串是否为回文，
# 如果是回文返回整数1，否则返回返 回整数0

def fn():
    f=input("请输入一个字符串：")
    if len(f)/2==0:
        if f[0]==f[-1] and f[1]==f[-2] and f[2]==f[-3]:
            print("是回文")
            return 1
        else:
            return 0
    elif len(f)/2==1:
        if f[0]==f[-1] and f[1]==f[-2] and f[2]==f[-3]:
            print("是回文")
            return 1
        else:
            return 0

fn()


