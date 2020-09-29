import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def input_control(num, message):
    while num is None:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            pass
        return num
    while num is False:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            if text.lower() == 'x':
              return text
        return num
    while num is True:
        text = input(message)
        if text in '1234':
            return str(text)
        else: 
            return num  

def get_data(operation):

    a = input_control(None,"Podaj pierwszą liczbę: ")
    b = input_control(None,"Podaj drugą liczbę: ")
    others = []
    if operation in "12":
        while True:
            c = input_control(False, "Podaj kolejną liczbę: ")
            if c == 'x':
                break
            else:
                others.append(c)

    return a, b, others


def add(a, b, *others):
    logging.info("Dodaję %s i %s do sumy %s" %(a,b,others))
    return a + b + sum(others)

def mul(a, b, *others):
    res = a * b
    for i in others:
        res = res * i
    logging.info("Mnożę %s przez %s i otrzymany iloczyn %s" %(a,b,others))
    return res

def sub(a,b):
    logging.info("Odejmuję %s i %s" %(a,b))
    return a-b

def div(a,b):
    if b != 0:
        logging.info("Dzielę %s przez %s" %(a, b))
        return a/b
    else:
        logging.info("Nie dziel przez zero")
        exit(1)

operations = {
	"1": add,
	"2": mul,
    "3": sub,
    "4": div
}

if __name__ == "__main__":
    operation = input_control(True,"Podaj działanie, posługując się odpowiednią liczbą: \n 1 Dodawanie,\n 2 Mnożenie,\n 3 Odejmowanie,\n 4 Dzielenie: \n ")
    a, b, others = get_data(operation)
    result = operations[operation](a, b, *others)
    print(result)