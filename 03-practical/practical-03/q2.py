# This is like the previous question, only with lists. Again, try
# to predict what will happen before running the code. Then run the code
# to test your prediction. Can you explain what is happening? How does this
# compare to the results in the previous question?

l1 = [1, 2, 3]
l2 = l1

print('l1 == l2: ', l1 == l2) #Predict True
print('l1 is l2: ', l1 is l2) #Predict True

l3 = [1, 2, 3]
l4 = [1, 2, 3]

print('l3 == l4: ', l3 == l4) #Predict True
print('l3 is l4: ', l3 is l4) #Predict false

#Prediction correct, list are mutable, l3,l4 differ as they point to different lists, but they share the same value at this moment.