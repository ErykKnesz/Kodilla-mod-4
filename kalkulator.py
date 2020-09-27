import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def input_value_control(num, message):
    while num is None:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            pass
    return num

def prompt_control(num, message):
    while num is None:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            if text.lower() == 'x':
              return text
    return num

def kalkulator():

    dodawanie = 0
    mnozenie = 1

    num = None
    num_2 = None
    num_3 = None

    dzialanie = input_value_control(num,"Podaj działanie, posługując się odpowiednią liczbą: \n 1 Dodawanie,\n 2 Odejmowanie,\n 3 Mnożenie,\n 4 Dzielenie: \n ")

    if dzialanie <= 4:
        num = input_value_control(num, "Podaj pierwszą liczbę: ")
        num_2 = input_value_control(num_2, "Podaj drugą liczbę: ")
    else:
        dzialanie = input_value_control(num,"Koniecznie podaj liczbę z zakresu 1-4 dla: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        num = input_value_control(num, "Podaj pierwszą liczbę: ")
        num_2 = input_value_control(num_2, "Podaj drugą liczbę: ")

    while dzialanie == 1:
        prompt_1 = prompt_control(num_3,"Podaj kolejną liczbę, albo wciśnij x, by zakończyć: ")
        if prompt_1 == 'x':
            break
        else:
            logging.info("Najpierw obliczam sumę dodatkowych liczb")
            dodawanie = dodawanie + float(prompt_1)
            print(dodawanie)
    if dzialanie == 1:         
        logging.info("Dodaję %s i %s do sumy %s" %(num, num_2, dodawanie))        
        return num + num_2 + dodawanie
    
    if dzialanie == 2:
        logging.info("Odejmuję %s i %s" %(num, num_2))
        return num - num_2

    while dzialanie == 3:
        prompt_1 = prompt_control(num_3,"Podaj kolejną liczbę, albo wciśnij x, by zakończyć: ")
        if prompt_1 == 'x':
            break
        else:
            logging.info("Najpierw mnożę dodatkowe liczby")
            mnozenie = mnozenie * float(prompt_1)
    if dzialanie == 3:        
        logging.info("Mnożę %s przez %s i otrzymany iloczyn %s" %(num, num_2, mnozenie))        
        return num * num_2 * mnozenie 

    if dzialanie == 4:
        if num_2 != 0:
            logging.info("Dzielę %s przez %s" %(num, num_2))
            return num / num_2
        else:
            logging.info("Nie dziel przez zero")
            exit(1)


wynik = kalkulator()
print(wynik)

