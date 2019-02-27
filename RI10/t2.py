#有两个磁盘文件A和B,
# 各存放一行字母,要求把这两个文件中的信息合并
# (按字母顺序排列), 输出到一个新文件C中。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    from Tkinter import *

    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()




