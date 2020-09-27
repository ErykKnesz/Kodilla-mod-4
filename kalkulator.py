
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def kalkulator():
    dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    
    dodawanie = 0
    mnozenie = 1

    if dzialanie <= 4:
        num = float(input("Podaj pierwszą liczbę: "))
        num_2 = float(input("Podaj drugą liczbę: "))
    else:
        dzialanie = int(input("Koniecznie podaj liczbę z zakresu 1-4 dla: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
        num = float(input("Podaj pierwszą liczbę: "))
        num_2 = float(input("Podaj drugą liczbę: "))

    while dzialanie == 1:
        prompt_1 = input("Podaj kolejną liczbę, albo wciśnij x, by zakończyć: ")
        if prompt_1 == 'x':
            break
        else:
            logging.info("Najpierw obliczam sumę dodatkowych liczb")
            dodawanie = dodawanie + float(prompt_1)
    if dzialanie == 1:         
        logging.info("Dodaję %s i %s do sumy %s" %(num, num_2, dodawanie))        
        print(num + num_2 + dodawanie)
    
    if dzialanie == 2:
        logging.info("Odejmuję %s i %s" %(num, num_2))
        print(num - num_2)

    while dzialanie == 3:
        prompt_1 = input("Podaj kolejną liczbę, albo wciśnij x, by zakończyć: ")
        if prompt_1 == 'x':
            break
        else:
            logging.info("Najpierw mnożę dodatkowe liczby")
            mnozenie = mnozenie * float(prompt_1)
    if dzialanie == 3:        
        logging.info("Mnożę %s przez %s i otrzymany iloczyn %s" %(num, num_2, mnozenie))        
        print(num * num_2 * mnozenie)

    if dzialanie == 4:
        if num_2 != 0:
            logging.info("Dzielę %s przez %s" %(num, num_2))
            print(num / num_2)
        else:
            logging.info("Nie dziel przez zero")
            exit(1)


kalkulator()