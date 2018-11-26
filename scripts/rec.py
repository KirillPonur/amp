from pylab import *
from matplotlib import rc
from functions import parsing
import os.path as path
import sys
from scipy import interpolate
from scipy.signal import medfilt
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

def CE():
    C_off = path.abspath('..'+'\\rec\\3.C_off.tsv')
    C_on = path.abspath('..'+'\\rec\\3.C_on.tsv')
    Aout,Ain=parsing(C_off,1,0)
    Aout,Ain=Aout/2,Ain/2/1000
    figOff3=figure('3.C_off')   
    ylabel(r'$U^m_{\text{вых}}, \text{В}$',fontsize=16)
    xlabel(r'$U^m_{\text{вх}}, \text{мВ}$',fontsize=16)
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    
    z=polyfit(Ain[1:-1]*1000,Aout[1:-1],1)
    print(z[0])
    z=poly1d(z)
    x=linspace(Ain[0]*1000,Ain[-1]*1000,1000)
    y=z(x)
    
    plot(x,y,label=r'$C_{\text{Э}}$ выключен')
    plot(Ain*1000, Aout,'.')
    Aout,Ain=parsing(C_on,1,0)
    Aout,Ain=Aout/2,Ain/2/1000
    z=polyfit(Ain[6:-1]*1000,Aout[6:-1],1)
    print(z[0])
    z=poly1d(z)
    x=linspace(Ain[0]*1000,Ain[-1]*1000, 1000)
    y=z(x)
   
    plot(x,y,label=r'$C_{\text{Э}}$ включен',color='darkblue')
    plot( Ain*1000,Aout,'r.')
    legend()
    savefig(path.abspath('..'+'\\fig\\3.pdf'))
    show()


    C_off = path.abspath('..'+'\\rec\\5.C_off_new.tsv')
    C_on = path.abspath('..'+'\\rec\\5.C_on.tsv')

    f,Aout=parsing(C_off,0,1)
    Ain=0.1/2
    Aout=Aout/2

    figOff=figure('5')    
    g = interpolate.interp1d(f,Aout/Ain, 'cubic')
    x=linspace(20,200*10**3,10000)
    
    plot(x,g(x),label=r'$C_\text{э}$ выключен',color='olivedrab')
    semilogx(f, Aout/Ain,'.')

    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$K,\text{отн.ед.}$',fontsize=16)
    xlabel(r'$\nu, \text{Гц}$',fontsize=16)

    f,Aout=parsing(C_on,0,1)
    Ain=0.1/2
    Aout=Aout/2
    g = interpolate.interp1d(f,Aout/Ain, 'quadratic')
    x=linspace(20,200*10**3,100000)
    plot(x,g(x),'-.',label=r'$C_\text{э}$ включен',color='darkblue')
    semilogx(f, Aout/Ain,'r.')
    legend()
    savefig(path.abspath('..'+'\\fig\\5.pdf'))

def CK():
    name = path.abspath('..'+'\\rec\\111.5.tsv')
    f,Aout=parsing(name,0,1)
    Ain=3/2
    Aout=Aout/2
    fig1=figure()
    # title(r'Эммитерный повторитель')
    semilogx(f, Aout/Ain,'r.',label='эксперимент')

    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$K,\text{отн.ед.}$',fontsize=16)
    xlabel(r'$\nu, \text{Гц}$',fontsize=16)
    ylim((0,1.1))

    legend(loc='lower right')
    savefig(path.abspath('..'+'\\fig\\111_5.pdf'))



    name = path.abspath('..'+'\\rec\\111.3.tsv')

    Aout,Ain=parsing(name,1,0)
    Aout,Ain=Aout/2,Ain/2
    fig2=figure()
    z=polyfit(Ain,Aout,1)
    print(z[0])
    z=poly1d(z)
    x=linspace(Ain[0],Ain[-1], 100)
    y=z(x)
    plot(x,y,label='аппроксимация',color='darkblue')
    plot(Ain,Aout,'r.',label='эксперимент')
    
    ylabel(r'$U^m_{\text{вых}}, \text{мВ}$',fontsize=16)
    xlabel(r'$U^m_{\text{вх}}, \text{мВ}$',fontsize=16)
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    legend()
    savefig(path.abspath('..'+'\\fig\\111_3.pdf'))
    show()
    
############################################################
#Не забудь переписать Ain
CK()
CE()

