import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def kalkulator():
  
    działanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if działanie <= 4:
        num = float(input("Podaj pierwszą liczbę: "))
        num_2 = float(input("Podaj drugą liczbę: "))
    else:
        działanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
        num = float(input("Podaj pierwszą liczbę: "))
        num_2 = float(input("Podaj drugą liczbę: "))
    if działanie == 1:
        logging.info("Dodaję %s i %s" %(num, num_2))
        print(num + num_2)
    if działanie == 2:
        logging.info("Odejmuję %s i %s" %(num, num_2))
        print(num - num_2)
    if działanie == 3:
        logging.info("Mnożę %s przez %s" %(num, num_2))
        print(num * num_2)
    if działanie == 4:
        if num_2 != 0:
            logging.info("Dzielę %s przez %s" %(num, num_2))
            print(num / num_2)
        else:
            exit(1)


    
kalkulator()





