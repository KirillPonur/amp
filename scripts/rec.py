from pylab import *
from matplotlib import rc
from functions import parsing
import os.path as path
import sys
from scipy import interpolate
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
        
    Aout,Ain=parsing(C_off,1,0)
    Aout,Ain=Aout/2,Ain/2/1000
    figOff3=figure('3.C_off')
    # title(r'$C_e$ отключен')
    
    ylabel(r'$U^m_{\text{вых}}, \text{В}$',fontsize=16)
    xlabel(r'$U^m_{\text{вх}}, \text{мВ}$',fontsize=16)
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    
    z=polyfit(Ain[6:-1]*1000,Aout[6:-1],1)
    print(z[0])
    z=poly1d(z)
    x=linspace(Ain[6]*1000,Ain[-1]*1000,1000)
    y=z(x)
    plot(Ain*1000, Aout, 'r.',label='эксперимент')
    plot(x,y,label='аппроксимация',color='darkblue')

    legend()
    savefig(path.abspath('..'+'\\fig\\3_C_off.pdf'))



    fig3On=figure('3.C_on')
    # title(r'$C_e$ включен')
    Aout,Ain=parsing(C_on,1,0)
    Aout,Ain=Aout/2,Ain/2/1000
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$U^m_{\text{вых}}, \text{В}$',fontsize=16)
    xlabel(r'$U^m_{\text{вх}}, \text{мВ}$',fontsize=16)


    z=polyfit(Ain[1:-1]*1000,Aout[1:-1],1)
    print(z[0])
    z=poly1d(z)
    x=linspace(Ain[1]*1000,Ain[-1]*1000, 1000)
    y=z(x)
   
    plot(x,y,label='аппроксимация',color='darkblue')
    plot( Ain*1000,Aout,'r.',label='эксперимент')
    legend()
    savefig(path.abspath('..'+'\\fig\\3_C_on.pdf'))


    try:
        C_off = path.abspath('..'+'\\rec\\5.C_off.tsv')
        C_on = path.abspath('..'+'\\rec\\5.C_on.tsv')
        open(C_off)
        open(C_on)
    except:
        C_off = path.abspath('..'+'\\rec\\5.C_off_old.tsv')
        C_on = path.abspath('..'+'\\rec\\5.C_on_old.tsv')

    f,Aout=parsing(C_off,0,1)
    Ain=0.1/2
    Aout=Aout/2
    figOff=figure('5.C_off')
    # title(r'$C_e$ отключен')
    
    g = interpolate.interp1d(f,Aout/Ain, 'cubic')
    x=linspace(20,200*10**3,10000)
    plot(x,g(x),label='интерполяция',color='darkblue')
    semilogx(f, Aout/Ain,'r.', label='эксперимент')

    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    # ylabel(r'$K,\text{отн.ед.}$',fontsize=16)
    # xlabel(r'$\nu, \text{Гц}$',fontsize=16)
    legend()
    # savefig(path.abspath('..'+'\\fig\\5_C_off.pdf'))


    figOn=figure('5.C_on')
    f,Aout=parsing(C_on,0,1)
    Ain=0.2/2
    Aout=Aout/2
    figure('5.C_on')
    # title(r'$C_e$ включен')
    

    g = interpolate.interp1d(f,Aout/Ain, 'quadratic')
    x=linspace(20,200*10**3,100000)

    plot(x,g(x),label='интерполяция',color='darkblue')
    semilogx(f, Aout/Ain,'r.',label='эксперимент')

    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    # ylabel(r'$K,\text{отн.ед.}$',fontsize=16)
    # xlabel(r'$\nu, \text{Гц}$',fontsize=16)
    legend()
    # savefig(path.abspath('..'+'\\fig\\5_C_on.pdf'))
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
    savefig(path.abspath('..'+'\\fig\\111_5.pdf'))


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
    savefig(path.abspath('..'+'\\fig\\111_3.pdf'))
    # show()
############################################################
#Не забудь переписать Ain
CE()

