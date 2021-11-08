""" Answer the questions in the code below. Keep in mind the LEGB rule."""

st0 = 'cats'
st1 = 'dogs'
counter = 23

def animals():
    animals = ['ducks', 'sheep', 'goats', 'dogs']
    counter = 0
    for a in animals:  # Q1: What namespace is animals in right now?
        if a == st1:   # Q2: What namespace is st1 in right now?
            a = a.upper()
        counter += 1   # Q3: What namespace is counter in here?
        print(a)
 
animals()  # Q4: What namespace is animals in here?
print(counter)  # Q5: What namespace is counter in here?
print(a) # Q6: Why does this raise an exception? 

# Put your answers to the questions below.
#Q1: Enclosing
#Q2: Global
#Q3: Enclosing
#Q4: Global
#Q5: Global
#Q6: a is undefined globally, only within the local namespace