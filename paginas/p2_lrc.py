from tkinter import *
from tkinter.font import BOLD

from algoritmos.lrc import *
from algoritmos.noise_1_bits import *
######################################################################################################
# Pagina 2
def tab2(root, common_img, bits_n, bits_p):
    pagina1 = Toplevel(root)
    pagina1.geometry("1200x800")
    pagina1.title('LRC')
    label1=Label(pagina1,text='LRC', font=('Times_New_Roman',20), width=800 , height=50, image=common_img, compound='c')
    label1.place(x=200, y=10)

    lbl2_bits_normales = Label(pagina1, text='Bits: ',font=('Times_New_Roman',10, BOLD), image=common_img, compound='c', height=50)
    lbl2_bits_normales.place(x=100, y=100)
    lbl2_bits_codificados = Label(pagina1, text='LRC: ',font=('Times_New_Roman',10, BOLD), image=common_img, compound='c', height=50)
    lbl2_bits_codificados.place(x=100, y=175)

    # Label bits originales
    txt1 = 'Bits: '
    for i in bits_n:
        txt1 = txt1 + i + ' : '
    lbl2_bits_normales['text']=txt1

    # Codificacion LRC
    lrc_codificado = lrc(bits_p)

    # Label bits condificados
    txt2 = 'LRC: '
    y = "".join(lrc_codificado) 
    lrc_1 = []
    lrc_1 = bits_n.copy()
    lrc_1.append(y)
    for i in lrc_1:
        txt2 = txt2 + i + ' : '
    lbl2_bits_codificados['text']=txt2

    
    print(bits_p)
    print(lrc_codificado)
    print(lrc_1)

    print('Ruido')
    bits_ruido = noise(bits_p, 'lrc')
    print(bits_ruido)
    print(bits_p)
    

    # BOTON DE TRANSMITIR
    btn2_transmitir = Button(pagina1, text='Transmitir', font=('Times_New_Roman',15, BOLD), image=common_img, compound='c', height=50, width=200)
    btn2_transmitir.place(x=500, y=250)
    # Label del Ruido
    lbl2_errados = Label(pagina1, text='Posible trama errada',font=('Times_New_Roman',10, BOLD), image=common_img, compound='c', height=50)
    lbl2_errados.place(x=100, y=325)
     # Label Comprobacion LRC
    lbl2_comprobado = Label(pagina1, text='Comprobacion',font=('Times_New_Roman',10, BOLD), image=common_img, compound='c', height=50)
    lbl2_comprobado.place(x=100, y=400)
