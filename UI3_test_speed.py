# use psutil test internet speed
from tkinter import *
import psutil
import time


# make ui
def make_app():
    app = Tk()
    app.config(bg='#303030')
    app.geometry('300x150')
    Label(text='speed test:', font=('Arial', 14, 'bold'),
          fg='white', bg='#303030').pack()
    Label(app, name='lb', text='_kb/s', font=('Arial', 10, 'bold'),
          fg='white', bg='#303030').pack()
    return app


# ui update
def ui_update():
    lb = app.children['lb']
    lb.config(text=test_speed() + ' kb/s')
    # # 1秒后调用ui_update
    app.after(1000, ui_update)


def test_speed():
    s1 = psutil.net_io_counters()
    time.sleep(1)
    # 得到一秒前后收到的字节数
    s2 = psutil.net_io_counters()
    # 返回1秒字节数
    result = '%.2f'%((s2.bytes_recv - s1.bytes_recv)/1024)
    return result


app = make_app()
# 1秒后自动运行ui_update
app.after(1000, ui_update)
app.mainloop()
