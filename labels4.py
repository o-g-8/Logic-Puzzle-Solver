from datetime import datetime
from datetime import time

women_labels = ["Woman 1", "Woman 2", "Woman 3", "Woman 4", "Woman 5"]
shirt_labels = ["blue", "green", "red", "white", "yellow"]
name_labels = ["Andrea","Holly","Julie","Leslie","Victoria"]
surname_labels = ["Brown","Davis","Lopes","Miller","Wilson"]
pasta_labels = ["farfalle","lasagne","penne","spaghetti","ravioli"]
wine_labels = ["Australian","Argentine","Chilean","French","Italian"]
age_labels = ["30 years", "35 years", "40 years", "45 years", "50 years"]
age = [30,35,40,45,50]


def clue1(model):
    white_shirt_index = shirt_labels.index("white")
    italia_wine_index = wine_labels.index("Italian")
    constraint = "constraint exists(w1, w2 in Women, s in Shirt where abs(w1-w2)==1 /\ s!="+str(white_shirt_index)+") (P1[w1,"+str(white_shirt_index)+"] /\ P1[w2,s] /\ P5[w2,"+str(italia_wine_index)+"]);\n"
    model.add_string(constraint)

def clue2(model):
    miller_surname_index = surname_labels.index("Miller")
    davis_surname_index = surname_labels.index("Davis")
    brown_surname_index = surname_labels.index("Brown")

    constraint = "constraint exists(w1,w2,w3 in Women where w1 < w2 /\ w2 < w3) (P3[w1,"+str(davis_surname_index)+"] /\ P3[w2,"+str(miller_surname_index)+"] /\ P3[w3,"+str(brown_surname_index)+"]);\n"
    model.add_string(constraint)

def clue3(model):
    lowest_age_index = age.index(min(age))

    constraint = "constraint P6[2,"+str(lowest_age_index)+"];\n"

    model.add_string(constraint)

def clue4(model):
    fortyfive_age_index = age_labels.index("45 years")
    red_shirt_index = shirt_labels.index("red")

    constraint = "constraint exists(w1,w2 in Women where w1 < w2)(P1[w1,"+str(red_shirt_index)+"] /\ P6[w2,"+str(fortyfive_age_index)+"]);\n"

    model.add_string(constraint)

def clue5(model):
    chilean_wine_index = wine_labels.index("Chilean")
    farfalle_pasta_index = pasta_labels.index("farfalle")

    constraint = "constraint exists(w in Women)(P4[w,"+str(farfalle_pasta_index)+"] /\ P5[w,"+str(chilean_wine_index)+"]);\n"

    model.add_string(constraint)

def clue6(model):
    argentine_wine_index = wine_labels.index("Argentine")

    constraint = "constraint P5[0,"+str(argentine_wine_index)+"];\n"

    model.add_string(constraint)

def clue7(model):
    andrea_name_index = name_labels.index("Andrea")
    thirtyfive_age_index = age_labels.index("35 years")

    constraint = "constraint exists(w1,w2 in Women where w1 == w2-1)(P2[w2,"+str(andrea_name_index)+"] /\ P6[w1,"+str(thirtyfive_age_index)+"]);\n"

    model.add_string(constraint)

def clue8(model):
    blue_shirt_index = shirt_labels.index("blue")
    davis_surname_index = surname_labels.index("Davis")
    holly_name_index = name_labels.index("Holly")

    constraint = "constraint exists(w1,w2,w3 in Women where w1 < w2 /\ w2 < w3) (P3[w1,"+str(davis_surname_index)+"] /\ P1[w2,"+str(blue_shirt_index)+"] /\ P2[w3,"+str(holly_name_index)+"]);\n"
    model.add_string(constraint)

def clue9(model):
    victoria_name_index = name_labels.index("Victoria")
    leslie_name_index = name_labels.index("Leslie")
    constraint = "constraint exists(w1, w2 in Women where abs(w1-w2)==1) (P2[w1,"+str(victoria_name_index)+"] /\ P2[w2,"+str(leslie_name_index)+"]);\n"
    model.add_string(constraint)

def clue10(model):
    australia_wine_index = wine_labels.index("Australian")
    red_shirt_index = shirt_labels.index("red")

    constraint = "constraint exists(w1,w2 in Women where w1 < w2)(P1[w1,"+str(red_shirt_index)+"] /\ P5[w2,"+str(australia_wine_index)+"]);\n"

    model.add_string(constraint)

def clue11(model):
    wilson_surname_index = surname_labels.index("Wilson")
    thirty_age_index = age_labels.index("30 years")
    constraint = "constraint exists(w1, w2 in Women where abs(w1-w2)==1) (P3[w1,"+str(wilson_surname_index)+"] /\ P6[w2,"+str(thirty_age_index)+"]);\n"
    model.add_string(constraint)

def clue12(model):
    leslie_name_index = name_labels.index("Leslie")
    thirty_age_index = age_labels.index("30 years")

    constraint = "constraint exists(w1,w2 in Women where w1 == w2-1)(P2[w1,"+str(leslie_name_index)+"] /\ P6[w2,"+str(thirty_age_index)+"]);\n"

    model.add_string(constraint)

def clue13(model):
    holly_name_index = name_labels.index("Holly")
    red_shirt_index = shirt_labels.index("red")

    constraint = "constraint exists(w1,w2 in Women where w1 < w2)(P1[w1,"+str(red_shirt_index)+"] /\ P2[w2,"+str(holly_name_index)+"]);\n"

    model.add_string(constraint)

def clue14(model):
    julie_name_index = name_labels.index("Julie")
    brown_surname_index = surname_labels.index("Brown")

    constraint = "constraint exists(w1,w2 in Women where w1 == w2-1)(P3[w1,"+str(brown_surname_index)+"] /\ P2[w2,"+str(julie_name_index)+"]);\n"

    model.add_string(constraint)

def clue15(model):
    lowest_age_index = age.index(min(age))
    penne_pasta_index = pasta_labels.index("penne")

    constraint = "constraint exists(w in Women)(P6[w,"+str(lowest_age_index)+"] /\ P4[w,"+str(penne_pasta_index)+"]);\n"

    model.add_string(constraint)

def clue16(model):
    wilson_surname_index = surname_labels.index("Wilson")
    white_shirt_index = shirt_labels.index("white")

    constraint = "constraint exists(w in Women)(P1[w,"+str(white_shirt_index)+"] /\ P3[w,"+str(wilson_surname_index)+"]);"
    model.add_string(constraint)

def clue17(model):
    lasagne_pasta_index = pasta_labels.index("lasagne")
    italia_wine_index = wine_labels.index("Italian")
    spaghetti_wine_index = pasta_labels.index("spaghetti")

    constraint = "constraint exists(w1,w2,w3 in Women where w1 < w2 /\ w2 < w3) (P5[w1,"+str(italia_wine_index)+"] /\ P4[w2,"+str(lasagne_pasta_index)+"] /\ P4[w3,"+str(spaghetti_wine_index)+"]);\n"
    model.add_string(constraint)

def clue18(model):  
    blue_shirt_index = shirt_labels.index("blue")

    constraint = "constraint P1[1,"+str(blue_shirt_index)+"];\n"

    model.add_string(constraint)

def clue19(model):
    forty_age_index = age_labels.index("40 years")
    lasagne_pasta_index = pasta_labels.index("lasagne")

    constraint = "constraint exists(w in Women)(P6[w,"+str(forty_age_index)+"] /\ P4[w,"+str(lasagne_pasta_index)+"]);\n"

    model.add_string(constraint)

def clue20(model):
    lopes_surname_index = surname_labels.index("Lopes")

    constraint = "constraint P3[4,"+str(lopes_surname_index)+"];\n"

    model.add_string(constraint)

def clue21(model):
    australia_wine_index = wine_labels.index("Australian")
    victoria_name_index = name_labels.index("Victoria")
    france_wine_index = wine_labels.index("French")

    constraint = "constraint exists(w1,w2,w3 in Women where w1 < w2 /\ w2 < w3) (P1[w1,"+str(victoria_name_index)+"] /\ P5[w2,"+str(australia_wine_index)+"] /\ P5[w3,"+str(france_wine_index)+"]);\n"
    model.add_string(constraint)

def clue22(model):
    yellow_shirt_index = shirt_labels.index("yellow")
    thirtyfive_age_index = age_labels.index("35 years")

    constraint = "constraint exists(w1,w2 in Women where w1 == w2-1)(P1[w1,"+str(yellow_shirt_index)+"] /\ P6[w2,"+str(thirtyfive_age_index)+"]);\n"

    model.add_string(constraint)

