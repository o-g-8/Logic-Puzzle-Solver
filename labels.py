from datetime import datetime
from datetime import time

actor_labels = ["Jessica", "Laurie", "Mark", "Mary", "Sally"]
film_labels = ["88 Minutes", "Donnie Brasco", "Scarecrow", "Scarface", "The Recruit"]
day_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_labels = ["7:35 pm", "7:40 pm", "8:20 pm", "8:30 pm", "8:45 pm"]
film_release_date = {
    "88 Minutes": 2007,
    "Donnie Brasco": 1997,
    "Scarecrow": 1973,
    "Scarface": 1983,
    "The Recruit": 2003
}
clues = ["Of the 20-hundreds releases, neither of which was Jessica's choice, one opened the week and one closed the week.",
         "The latest of the 19-hundreds releases was shown at 30 minutes past the hour.",
         "The releases shown before 8:00pm were on consecutive days, as were the releases shown after 8:00pm.",
         "One of the men and one of the women had a showing before 8:00pm, but neither was mid-week",
         "Mark, whoses choice was Scarecrow, had a showing at a time of one hour and five minutes after that of Scarface.",
         "Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day.",
         "88 Minutes showed at a time both 40 minutes to the hour and 40 minutes after the Thursday showing."]

def clue1(model):
    jessica_index = actor_labels.index("Jessica")

    films_not_choice_index = []
    for i in range(len(film_labels)):
        if film_release_date[film_labels[i]] >= 2000 and film_release_date[film_labels[i]] < 3000:
            films_not_choice_index.append(i)

    constraints = []

    for i in films_not_choice_index:
        constraints.append("constraint P1["+str(jessica_index)+","+str(i)+"] == false;")
        constraints.append("constraint forall(a in Actor) ( P1[a,"+str(i)+"] -> (P2[a,0] \/ P2[a, "+str(len(day_labels)-1)+"]) );")

    for i in constraints:
        model.add_string(i + "\n")

def clue2(model):
    film_index : int = 0
    film_rd : int = 0
    for i in range(len(film_labels)):
        if film_release_date[film_labels[i]] < 2000 and film_release_date[film_labels[i]] > film_rd:
            film_rd = film_release_date[film_labels[i]]
            film_index = i
    
    times_not_choice_index = []
    for i in range(len(time_labels)):
        if datetime.strptime(time_labels[i], "%I:%M %p").minute != 30:
            times_not_choice_index.append(i)
    
    constraints = []

    for i in times_not_choice_index:
        constraints.append("constraint forall(a in Actor) (P1[a,"+str(film_index)+"] -> P3[a,"+str(i)+"] == false);")

    for i in constraints:
        model.add_string(i+"\n")

def clue3(model):
    reference_hour = datetime.strptime("8:00 pm", "%I:%M %p").time()

    before8pm = []
    after8pm = []

    for i in range(len(time_labels)):
        hour = datetime.strptime(time_labels[i], "%I:%M %p").time()
        if hour < reference_hour:
            before8pm.append(i)
        else:
            after8pm.append(i)
    
    before_8pm = "[0,1]"
    after_8pm = "[2,3,4]"
    constraints = []

    constraints.append("constraint forall(t1,t2 in "+before_8pm+" where t1 < t2) (exists(a1,a2 in Actor, d1,d2 in Day where a1 != a2 /\ d1 == d2-1) (((P3[a1,t1]=true /\ P3[a2,t2]=true) \/ (P3[a1,t2]=true /\ P3[a2,t1]=true)) /\ P2[a1,d1] /\ P2[a2,d2]) );")
    constraints.append("constraint forall(t1 in "+after_8pm+") (exists(a1,a2 in Actor, d1,d2 in Day, t2 in "+after_8pm+" where a1 != a2 /\ d1 == d2-1 /\ t2 != t1) (P3[a1,t1] /\ P3[a2,t2] /\ ((P2[a1,d1] /\ P2[a2,d2])\/(P2[a1,d2] /\ P2[a2,d1])) )  );")
    for i in constraints:
        model.add_string(i+"\n")   

def clue4(model):
    women = "[0,3,4]"
    men = "[1,2]"
    
    reference_hour = datetime.strptime("8:00 pm", "%I:%M %p").time()

    before8pm = []
    for i in range(len(time_labels)):
        hour = datetime.strptime(time_labels[i], "%I:%M %p").time()
        if hour < reference_hour:
            before8pm.append(i)
    constraints = []
    constraints.append("constraint exists(a in "+women+", t in Time where t < "+str(len(before8pm))+") (P3[a,t]==true);")
    constraints.append("constraint exists(a in "+men+", t in Time where t < "+str(len(before8pm))+") (P3[a,t]==true);")

    for i in constraints:
        model.add_string(i+"\n")

def clue5(model):
    mark_index = actor_labels.index("Mark")
    scarecrow_index = film_labels.index("Scarecrow")
    scarface_index = film_labels.index("Scarface")
    scarecrow_time_index = time_labels.index("8:45 pm")
    scarface_time_index = time_labels.index("7:40 pm")

    constraints = []
    constraints.append("constraint P1["+str(mark_index)+","+str(scarecrow_index)+"];")
    constraints.append("constraint P3["+str(mark_index)+","+str(scarecrow_time_index)+"];")
    constraints.append("constraint exists(a in Actor) (P1[a,"+str(scarface_index)+"] -> P3 [a,"+str(scarface_time_index)+"]);")

    for i in constraints:
        model.add_string(i+"\n")

def clue6(model):
    mary_index = actor_labels.index("Mary")
    jessica_index = actor_labels.index("Jessica")

    even_nb_day = [1,3]
    constraints = []
    for i in even_nb_day:
        constraints.append("constraint P2["+str(mary_index)+","+str(i)+"]=false;")
        constraints.append("constraint P2["+str(jessica_index)+","+str(i)+"]=false;")
    
    for i in constraints:
        model.add_string(i+"\n")

def clue7(model):
    doubleeight_minutes_index = film_labels.index("88 Minutes")
    thursday_index = day_labels.index("Thursday")

    minutes_list = []
    for time_str in time_labels:
        time_obj = datetime.strptime(time_str, "%I:%M %p").time()
        minutes = time_obj.hour * 60 + time_obj.minute
        minutes_list.append(minutes)
    
    times_not_choice_index = []
    for i in range(len(time_labels)):
        if datetime.strptime(time_labels[i], "%I:%M %p").minute != 20:
            times_not_choice_index.append(i)
    
    constraints = []

    for i in times_not_choice_index:
        constraints.append("constraint forall(a in Actor) (P1[a,"+str(doubleeight_minutes_index)+"] -> P3[a,"+str(i)+"] == false);")

    doubleeighty_time_index : int

    for i in range(len(time_labels)):
        if datetime.strptime(time_labels[i], "%I:%M %p").minute == 20:
            doubleeighty_time_index = i 
            break
    
    times_not_choice_index = []

    for i in range(len(time_labels)):
        if minutes_list[doubleeighty_time_index]-minutes_list[i] != 40:
            times_not_choice_index.append(i)

    for i in times_not_choice_index:
        constraints.append("constraint forall(a in Actor) (P2[a,"+str(thursday_index)+"] -> P3[a,"+str(i)+"] == false);")


    for i in constraints:
        model.add_string(i+"\n")
    



    
    
        