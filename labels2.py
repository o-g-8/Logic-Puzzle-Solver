from datetime import datetime
from datetime import time

monitor_labels = ["13'", "15'", "15.6'", "21.5'", "27'"]
processor_labels = ["2.0 MHz", "2.3 MHz", "2.5 MHz", "2.7 MHz", "3.1 MHz"]
harddisk_labels = ["250 Gb", "320 Gb", "500 Gb", "750 Gb", "1024 Gb"]
price_labels = ["$699,00", "$999,00", "$1.149,00", "$1.349,00", "$1.649,00"]

prices = [699,999,1149,1349,1649]
processor = [2.0,2.3,2.5,2.7,3.1]

andrew_price_index = []

clues = []

def add_or(string, grid, x, y, b,i):
    if i == 0:
        string += "("+grid+"["+str(x)+","+str(y)+"] = " + b
    else:
        string += "\/ ("+grid+"["+str(x)+","+str(y)+"] = " + b

    return string

def add_and(string, grid, x, y, b):
    string += "/\ "+grid+"["+str(x)+","+str(y)+"] = " + b
    return string


def clue1(model):
    less_than_threehundred = []
    more_than_threehundred = []
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i!=j and prices[j]-prices[i] == 300:
                less_than_threehundred.append(i)
                more_than_threehundred.append(j)
    
    less_than_pointfour = []
    more_than_pointfour = []
    for i in range(len(processor)):
        for j in range(len(processor)):
            if i!=j and round(processor[j]-processor[i],3) == 0.4:
                less_than_pointfour.append(i)
                more_than_pointfour.append(j)

    twentyone_monitor = monitor_labels.index("21.5'")

    constraints = []
    constraint = "constraint exists(m,m1 in Monitor where m != "+str(twentyone_monitor)+" /\ m1 != m /\ m1 != "+str(twentyone_monitor)+") ("
    
    for i in range(len(less_than_threehundred)):
        constraint = add_or(constraint, "P3","m",str(more_than_threehundred[i]),"true",i)
        constraint += "/\ ("
        for j in range(len(less_than_pointfour)):
            constraint = add_or(constraint, "P1","m",str(more_than_pointfour[j]),"true",j)
            constraint = add_and(constraint,"P1",str(twentyone_monitor),str(less_than_pointfour[j]),"true")
            constraint += "/\ P3[m1, "+str(less_than_threehundred[i])+"])"
        constraint += "))"

    constraint += ");"
    
    global andrew_price_index
    andrew_price_index = less_than_threehundred
    model.add_string(constraint)



def clue2(model):
    twentyseven_monitor_index = monitor_labels.index("27'")
    fifteen_monitor_index = monitor_labels.index("15'")
    twopointseven_processor_index = processor_labels.index("2.7 MHz")
    twopointzero_processor_index = processor_labels.index("2.0 MHz")
    twohundredfifty_hd_index = harddisk_labels.index("250 Gb")
    thousandhundredfortynine_price = price_labels.index("$1.149,00")

    constraint = "constraint exists(m1,m2,m3,m4,m5,m6 in Monitor, p in "+str(andrew_price_index)+", p1 in Processor, h1,h2,h3 in Harddisk where m1 != "+str(twentyseven_monitor_index)+" /\ m5 != "+str(fifteen_monitor_index)+" /\ h1 < h2 /\ h2 < h3 /\ p1 < "+str(twopointseven_processor_index)+" /\ m1 != m2 /\ m1 != m3 /\ m1 != m4 /\ m1 != m5 /\ m2 != m3 /\ m2 != m4 /\ m2 != m5 /\ m3 != m4 /\ m3 != m5 /\ m4 != m5 /\ m6 != m5) (P1[m2,"+str(twopointzero_processor_index)+"] /\ P2[m3,"+str(twohundredfifty_hd_index)+"] /\ P3[m4,"+str(thousandhundredfortynine_price)+"] /\ P3[m1,p] /\ P2[m5,h2] /\ P2[m1,h1] /\ P1[m6,"+str(twopointseven_processor_index)+"] /\ P2[m6,h3]);\n" 
    model.add_string(constraint)

def clue3(model):
    threehundredtwenty_hd_index = harddisk_labels.index("320 Gb")
    possible_processors_index = []
    possible_processors_index.append(processor_labels.index("2.0 MHz"))
    possible_processors_index.append(processor_labels.index("2.3 MHz"))

    constraint = "constraint exists(m in Monitor, p in "+str(possible_processors_index)+")(P2[m,"+str(threehundredtwenty_hd_index)+"] /\ P1[m,p]);"
    model.add_string(constraint + "\n")  

    fifteen_monitor_index = monitor_labels.index("15'")
    triplenine_price_index = price_labels.index("$999,00")
    thousandthreehundredfortynine_price_index = price_labels.index("$1.349,00")

    constraint = "constraint exists(m1,m2 in Monitor, p1,p2,p3 in Processor where p1 < p2 /\ p2 < p3 /\ m1 != m2 /\ m1 != "+str(fifteen_monitor_index)+" /\ m2 != "+str(fifteen_monitor_index)+")(P1["+str(fifteen_monitor_index)+",p2] /\ P3[m1,"+str(triplenine_price_index)+"] /\ P1[m1,p1] /\ P3[m2,"+str(thousandthreehundredfortynine_price_index)+"] /\ P1[m2,p3]);"
    model.add_string(constraint + "\n")

def clue4(model):
    twentyseven_monitor_index = monitor_labels.index("27'")
    threehundredtwenty_hd_index = harddisk_labels.index("320 Gb")

    constraint = "constraint P2["+str(twentyseven_monitor_index)+","+str(threehundredtwenty_hd_index)+"] = false;"

    model.add_string(constraint + "\n")

    sixhundredninetynine_price_index = price_labels.index("$699,00")

    constraint ="constraint exists(m in Monitor)(P2[m,"+str(threehundredtwenty_hd_index)+"] = false /\ P3[m,"+str(sixhundredninetynine_price_index)+"]);"

    model.add_string(constraint + "\n")

    fivehundred_hd_index = harddisk_labels.index("500 Gb")

    constraint = "constraint exists(m1,m2 in Monitor, p1,p2 in Processor where m1 < m2 /\ p1 < p2) (P2[m2,"+str(fivehundred_hd_index)+"] /\ P3[m1,"+str(sixhundredninetynine_price_index)+"] /\ P2[m2,p2] /\ P2[m1,p1]);"

    model.add_string(constraint + "\n")