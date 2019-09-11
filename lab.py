from control.matlab import*
import matplotlib.pyplot as plt
'''Коэффициенты звеньев'''
''' Безинерционное звено'''
k1=5;
'''Апериодическое звено'''
k2=1;
T2=2;
'''Интегрирующее звено'''
k3=2;
T3=0;
'''Идеально дифференсирующее звено'''
k4=1;
T4=0;
'''Реально дифференсирующее звено'''
k5=2;
T5=3;

W11=tf(k1,[10**(-100), 1]);          W12=tf(k1/2,[10**(-100), 1]);
W21=tf(k2,[T2, 1]);                  W22=tf(k2/2,[T2/2, 1]);
W31=tf(k3,[1, 0]);                   W32=tf(k3/2,[1, 0]);
W41=tf([k4, 0],[10**(-100),1]);      W42=tf([k4/2, 0],[10**(-100),1]);
W51=tf([k5, 0],[T5, 1]);             W52=tf([k5/2, 0],[T5/2, 1]);
print('Первичные передаточные функции');
print('W1 = ',W11); print('W2 = ',W21); print('W3 = ',W31); print('W4 = ',W41); print('W5 = ',W51);
print('Измененные передаточные функции');
print('W1 = ',W12); print('W2 = ',W22); print('W3 = ',W32); print('W4 = ',W42); print('W5 = ',W52);
def one(w):
    '''Переходная функция'''
    y, x = step(w);
    plt.plot(x,y);
    plt.title('Переходная характеристика');
    plt.ylabel('Амплитуда');
    plt.xlabel('Время');
    plt.grid(True);
    plt.show();

    '''Импульсная функция'''
    y,x=impulse(w);
    plt.plot(x,y);
    plt.title('Импульсная характеристика');
    plt.ylabel('Амплитуда');
    plt.xlabel('Время');
    plt.grid(True);
    plt.show();

    '''ЛАЧХ и ЛФЧХ'''
    mag, phase, omega = bode(w, dB=False);
    plt.plot();
    plt.show();


one(W12);
