from datetime import datetime
from datetime import time

person_labels = ["Person1", "Person2", "Person3"]
object_labels = ["Object1", "Object2", "Object3"]
place_labels = ["Place1", "Place2", "Place3"]

clues = []

def rename():
    global person_labels
    person_labels = []
    for i in range(3):
        name = input("Enter the name of Person "+str(i)+" : ")
        person_labels.append(name)

