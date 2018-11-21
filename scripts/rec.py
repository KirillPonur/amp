from pylab import *
from matplotlib import rc
from functions import parsing
import os.path as path
import sys
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                           r'\usepackage{amsmath}',
                           r'\usepackage{amssymb}'])


rc('font', family='serif')

def CE():
    try:
        C_off = path.abspath('..'+'\\rec\\3.C_off.tsv')
        C_on = path.abspath('..'+'\\rec\\3.C_on.tsv')
        open(C_off)
        open(C_on)
    except:
        C_off = path.abspath('..'+'\\rec\\3.C_off_old.tsv')
        C_on = path.abspath('..'+'\\rec\\3.C_on_old.tsv')
    

    Aout,Ain=parsing(C_off,2,1)
    Aout,Ain=Aout/2,Ain/2
    figOff3=figure('3.C_off')
    title(r'$C_e$ отключен')
    plot(Aout, Ain,'.',label='эксперимент')
    ylabel(r'$U^m_{out}$')
    xlabel(r'$U^m_{in}$')
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    legend()

    fig3On=figure('3.C_on')
    title(r'$C_e$ включен')
    Aout,Ain=parsing(C_on,2,1)
    Aout,Ain=Aout/2,Ain/2
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$U^m_{out}$')
    xlabel(r'$U^m_{in}$')
    plot(Aout,Ain,'.',label='эксперимент')
    legend()
    try:
        C_off = path.abspath('..'+'\\rec\\5.C_off.tsv')
        C_on = path.abspath('..'+'\\rec\\5.C_on.tsv')
        open(C_off)
        open(C_on)
    except:
        C_off = path.abspath('..'+'\\rec\\5.C_off_old.tsv')
        C_on = path.abspath('..'+'\\rec\\5.C_on_old.tsv')

    f,Aout=parsing(C_off,0,1)
    Ain=108/2/1000
    Aout=Aout/2
    figOff=figure('5.C_off')
    title(r'$C_e$ отключен')
    semilogx(f, Aout/Ain,label='эксперимент')
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$K=\frac{U_{out}}{U_{in}}$')
    xlabel(r'$\omega$')
    legend()

    figOn=figure('5.C_on')
    f,Aout=parsing(C_on,0,1)
    Ain=108/2
    Aout=Aout/2
    figure('5.C_on')
    title(r'$C_e$ включен')
    semilogx(f, Aout/Ain,label='эксперимент')
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$K=\frac{U_{out}}{U_{in}}$')
    xlabel(r'$\omega$')
    legend()
    show()
def CK():

    try:
        name = path.abspath('..'+'\\rec\\111.5.tsv')
        open(name)
    except:
        name = path.abspath('..'+'\\rec\\111.5_old.tsv')

    f,Aout=parsing(name,0,1)
    Ain=7.36
    Aout=Aout/2
    fig1=figure()
    title(r'Эммитерный повторитель')
    semilogx(f, Aout/Ain,label='эксперимент')
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$K=\frac{U_{out}}{U_{in}}$')
    xlabel(r'$\omega$')
    legend()
    try:
        name = path.abspath('..'+'\\rec\\111.3.tsv')
        open(name)
    except:
        name = path.abspath('..'+'\\rec\\111.3_old.tsv')
    Aout,Ain=parsing(name,1,0)
    Aout,Ain=Aout/2,Ain/2
    fig2=figure()
    title(r'Эммитерный повторитель')
    plot(Aout, Ain,'.',label='эксперимент')
    ylabel(r'$U^m_{out}$')
    xlabel(r'$U^m_{in}$')
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    legend()
    show()
############################################################
#Не забудь переписать Ain
CK()
CE()
