from datetime import date
from tkinter import *

dia = date.today().day
mes = date.today().month
ano = date.today(). year

conta = 0

#valor = entrada2.get()


janela = Tk()
janela.title('Sale Controler')
janela.iconbitmap("icon.ico")

img = PhotoImage(file="sale1.png")
imagem = Label(janela, image=img, width=280, height=170)
imagem.place(x=590, y=40)


#------------Produtos------------------------
texto = Label(janela, text='Produto:', font='Arial 15',  bg="white")
texto.place(x=200, y=250)

entrada = Entry(janela, width=35, bg='#F1EFEF')
entrada.place(x=280, y=250, height=27)


#------------Quantidade-----------------------
texto1 = Label(janela, text='Quantidade:', font='Arial 15',  bg="white")
texto1.place(x=550, y=250)

entrada1 = Entry(janela, width=35, bg='#F1EFEF')
entrada1.place(x=670, y=250, height=27)


#--------------Preço---------------------------
texto2 = Label(janela, text='Preço:', font='Arial 15',  bg="white")
texto2.place(x=990, y=250)

entrada2 = Entry(janela, width=35, bg='#F1EFEF')
entrada2.place(x=1060, y=250, height=27)


#------------Peso------------------------
texto3 = Label(janela, text='Peso:', font='Arial 15',  bg="white")
texto3.place(x=200, y=400)

entrada3 = Entry(janela, width=35, bg='#F1EFEF')
entrada3.place(x=280, y=400, height=27)


#------------Forma de pagamento-----------------------
texto4 = Label(janela, text='Pagamento:', font='Arial 15',  bg="white")
texto4.place(x=550, y=400)

entrada4 = Entry(janela, width=35, bg='#F1EFEF')
entrada4.place(x=670, y=400, height=27)


#--------------Observação---------------------------
texto5 = Label(janela, text='Observação:', font='Arial 15',  bg="white")
texto5.place(x=935, y=400)

entrada5 = Entry(janela, width=35, bg='#F1EFEF')
entrada5.place(x=1060, y=400, height=27)


def vendas():
    janela1 = Tk()
    janela1.title('Vendas')
    janela1.iconbitmap("icon.ico")
    
    texto7 = Label(janela1, text='VENDAS:', bg='white', font='Arial 40 bold')
    texto7.place(x=600, y=40)
    
    texto6 = Label(janela1, text='Produto:            Quantidade:            Preço:            Peso:            Pagamento:            Observação:    ', bg='white', font='Arial 20 bold')
    texto6.place(x=100, y=200)
    
    botao4 = Button(janela1, text='Voltar', command=janela1.destroy, bg='white', bd=0, font='Arial 15 italic bold')
    botao4.place(x=20, y=0)
    
    texto12 = Label(janela1, text=entrada.get(), bg='white', font='Arial 15')
    texto12.place(x=100, y=300)
    
    texto13 = Label(janela1, text=entrada1.get(), bg='white', font='Arial 15')
    texto13.place(x=350, y=300)
    
    texto14 = Label(janela1, text=entrada2.get(), bg='white', font='Arial 15')
    texto14.place(x=570, y=300)
    
    texto15 = Label(janela1, text=entrada3.get(), bg='white', font='Arial 15')
    texto15.place(x=770, y=300)
    
    texto16 = Label(janela1, text=entrada4.get(), bg='white', font='Arial 15')
    texto16.place(x=950, y=300)
    
    texto17 = Label(janela1, text=entrada5.get(), bg='white', font='Arial 15')
    texto17.place(x=1200, y=300)
    

    janela1.config(bg='white')
    janela1.state('zoomed')
    janela1.mainloop()

botao = Button(janela, text="Última venda", command=vendas, bg='white', bd=0, font='Arial 15 italic bold')
botao.place(x=120, y=0)

botao2 = Button(janela, text='Sair', command=janela.destroy, bg='white', bd=0, font='Arial 15 italic bold')
botao2.place(x=20, y=0)

def perfil():
    texto8 = Label(janela, text='--', bg='#F1EFEF', fg='#F1EFEF', font='Arial 800 bold')
    texto8.place(x=1000, y=0)

    def perf():
        texto8.destroy()
        botao6.destroy()
        texto9.destroy()
        texto10.destroy()
        texto11.destroy()
        texto12.destroy()
    
    botao6 = Button(janela, text='Voltar', command=perf, bg='#F1EFEF', bd=0, font='Arial 15 italic bold')
    botao6.place(x=1000, y=10)
    
    
    texto9 = Label(janela, text='Caio Lamas', font='Arial 25', bg='#F1EFEF')
    texto9.place(x=1150, y=100)
    
    texto10 = Label(janela, text='Vendas: '+str(conta), bg='#F1EFEF', font='Arial 15')
    texto10.place(x=1050, y=240)
    
    texto11 = Label(janela, text='Data: 19/12/2023', bg='#F1EFEF', font='Arial 15')
    texto11.place(x=1050, y=320)
    
    texto12 = Label(janela, text='Total: '+str(entrada2.get()), bg='#F1EFEF', font='Arial 15')
    texto12.place(x=1050, y=400)

    
    

botao5 = Button(janela, text="Perfil", command=perfil, bg='white', bd=0, font='Arial 15 italic bold')
botao5.place(x=350, y=0)



def conc():
    print('Produto: ', entrada.get(), '  Quantidade: ' ,entrada1.get(), '  Preço: ',entrada2.get(), '  Peso: ', entrada3.get(), '  Pagamento: ', entrada4.get(), '  Observação: ', entrada5.get())
    #entrada.delete(0, 'end')
    #entrada1.delete(0, 'end')
    #entrada2.delete(0, 'end')
    #entrada3.delete(0, 'end')
    #entrada4.delete(0, 'end')
    #entrada5.delete(0, 'end')
    
    global conta
    conta=conta+1

    
botao1 = Button(janela, text='Concluir Venda', command=conc, width=50, height=3, bd=1, bg='#F1EFEF', font='Arial 10')
botao1.place(x=520, y=500)



janela.config(bg='white')
janela.state('zoomed')
janela.mainloop()