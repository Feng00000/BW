#使用while循环，
# 实现持续的用户录入信息，
# 将录入的信息以追加的方式保存至文件中，
# 当用户输入exit时，退出程序。

while True:
    s=input("请输入信息：")
    f=open('qqq.txt','w')
    f.write(s)
    if exit:
        break
f.close()



