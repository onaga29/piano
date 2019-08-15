
from playsound import playsound
save = {}
while True:
        nt = str(input('Enter number or if you wanna see the things you saved before type "load": '))
        if nt == 'load':
            print(save)
            ask_p = str(input('Wanna play any of these?(y/n): '))
            if ask_p == 'n':
                pass
            if ask_p == 'y':
                name_l = str(input('Enter the name you want to play: '))
                if name_l in save:
                    for i in save[name_l]:
                        if i == '0':
                            playsound('11.wav')
                        elif i == '1':
                            playsound('12.wav')
                        elif i == '2':
                            playsound('13.wav')
                        elif i == '3':
                            playsound('14.wav')
                        elif i == '4':
                            playsound('15.wav')
                        elif i == '5':
                            playsound('16.wav')
                        elif i == '6':
                            playsound('21.wav')
                        elif i == '7':
                            playsound('22.wav')
                        elif i == '8':
                            playsound('23.wav')
                        elif i == '9':
                            playsound('24.wav')
                if name_l not in save:
                    print('There is no such thing!!!')

        else:
            for i in nt:
                if i == '0':
                    playsound('11.wav')
                elif i == '1':
                    playsound('12.wav')
                elif i == '2':
                    playsound('13.wav')
                elif i == '3':
                    playsound('14.wav')
                elif i == '4':
                    playsound('15.wav')
                elif i == '5':
                    playsound('16.wav')
                elif i == '6':
                    playsound('21.wav')
                elif i == '7':
                    playsound('22.wav')
                elif i == '8':
                    playsound('23.wav')
                elif i == '9':
                    playsound('24.wav')

            ask = str(input('Wanna save it?(y/n): '))
            if ask == 'n':
                pass
            if ask == 'y':
                name = str(input('Choose a name: '))
                if name in save:
                    ask_o = str(input('This name is already taken, wanna override it?(y/n): '))
                    if ask_o == 'y':
                        save[name] = nt
                    if ask_o == 'n':
                        name_n = str(input('Choose another name: '))
                        save[name_n] = nt
                else:
                    save[name] = nt
           
        


