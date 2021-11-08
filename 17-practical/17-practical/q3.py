# Create an instance of MyClass and use pickle.dump() to save
# it to a file. Verify that the file is created. Then use
# pickle.load() to load the saved data from the file.

import pickle
import os.path

class MyClass:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return str(self.data)

an_obj = MyClass('Anything')

with open('save.myClass', 'wb') as outfile:
    pickle.dump(an_obj, outfile)

if os.path.isfile('save.myClass'):
    print ("File exist")
else:
    print ("File does not exist")

an_obj = None

an_obj = pickle.load(open('save.myClass', 'rb'))

print(an_obj)