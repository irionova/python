font1 = ('Comic Sans MS', 32, 'bold')
font2 = ('Comic Sans MS', 10)
font3 = ('Comic Sans MS', 20)
font4 = ('Comic Sans MS', 14)
WARN = '''ВНИМАНИЕ! Калькулятор считает только 
        значения простых логических функций nor,
        nand, nxor. Ввод иных логических функций
        и конструкций даст ошибку обработки функции.
        Примечание: nAnd и nand -  не одно и то же'''
ERR = 'error'
forma = '564x512'

from tkinter import *

root = Tk()
root.config(background='black')
root.geometry(forma)
root.title('Очень странный калькулятор')
root.resizable(width = False, height = False)


hello = Label( text='Добро пожаловать ', font=font1, fg='white', bg='black')
hello.pack(side = TOP)






def ti_open():
    tabs['text'] = 'Таблицы истинности'

    nan['text'] = '''nand
    0  0  1
    0  1  1
    1  0  1
    1  1  0'''
    no['text'] = '''nor
    0  0  1
    0  1  0
    1  0  0
    1  1  0'''
    nxo['text'] = '''nxor
    0  0  1
    0  1  0
    1  0  0
    1  1  1'''

    but_ti['text']='Cпрятать таблицы \n истинности'
    but_ti['command']=ti_close

def ti_close():
    nan['text']=''
    no['text'] = ''
    nxo['text'] = ''
    tabs['text']=''

    but_ti['text'] = 'Показать таблицы \n истинности'
    but_ti['command'] = ti_open

tabs = Label(text ='', font = font3, fg='white', bg = 'black')

nan = Label(font=font3, fg='white', bg='black')
no = Label(font=font3, fg='white', bg='black')
nxo = Label(font=font3, fg='white', bg='black')
but_ti = Button(text='Показать таблицы \n истинности', padx ='5', pady = '5')
but_ti.config(command=ti_open)
but_ti.place(x = 380, y = 100,  width = 120, height = 50)

tabs.place(x = -30, y = 90,  width = 420, height = 50)
nan.pack(side=LEFT)
no.pack(side=LEFT)
nxo.pack(side=LEFT)


def nand(a,b):
    if (not (a * b)):
        return 1
    else:
        return 0

def nor(a, b):
    if (not (a or b)):
        return 1
    else:
        return 0

def nxor(a, b):
    if (a == b):
        return 1
    else:
        return 0
tb_title = Label(text ='Калькулятор', font = font3, fg='white', bg = 'black')
tb_title.place(x = 380, y = 200)
textbox_input = Entry()
textbox_input.place(x = 380, y = 250)
rez_title = Label(text ='Результаты:', font = font3, fg='white', bg = 'black')
rez = Label (text='', font=font4, fg='white', bg='black')
warnin = Label (text='в формате: 1 nor 1', font=font2, fg='white', bg='black')
rez_title.place(x = 380, y = 300)
rez.place(x = 380, y = 350)


p = []
c = []
def enter():
    c = (textbox_input.get()).split(' ')
    kalk (c)

but = Button(text = 'ввод', command =enter)
but.place(x = 380, y = 270)
warnin.place(x = 420, y = 270)

warn_in = Label (text=WARN, font=font2, fg='white', bg='black')
warn_in.place(x = -10, y = 400)

def kalk(c):
    def err():
        p.append (c)
        p[-1] += ':'+ERR
        p[-1] = ' '.join(p[-1])
        s = '\n'.join(p)
        rez['text'] = s
        return
    if (len (c) == 3):
        if ('0' <= c[0] <= '1') and ('0' <= c[2] <= '1') and (c[1] == 'nand' or c[1] == 'nor' or c[1] == 'nxor'):
            a, b = int(c[0]), int(c[2])
            p.append(c)

            if c[1] == 'nand':
                p[-1] +=  '='+str(nand(a, b))
            elif c[1] == 'nor':
                p[-1] += '='+ str(nor(a, b))
            elif c[1] == 'nxor':
                p[-1] += '='+str(nxor(a, b))
            p[-1] = ' '.join(p[-1])
        else:
            err()
    else:
        err()
    if len(p)>6:
        del p[0]

    s = '\n'.join(p)
    rez['text'] = s


root.mainloop()
