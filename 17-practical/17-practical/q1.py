# Below there is a collection of values. Pickle each of them with 
# pickle.dumps(). This will give you byte string representations of 
# those values. Then, "unpickle" the values and verify that they are
# restored.

import pickle

# Here are our values to pickle
a_num = 42
a_str = 'spam'
a_dict = {'a': 1, 'b': 7}

class MyClass:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return str(self.data)

an_obj = MyClass('hello')

# Pickle these values below with pickle.dumps()
pkl_a_num = pickle.dumps(a_num)
pkl_a_str  = pickle.dumps(a_str)
pkl_a_dict = pickle.dumps(a_dict)
pkl_an_obj = pickle.dumps(an_obj)

#pickle.dump(a_num, open('save.s', 'wb'))
#pickle.dump(a_str, open('save.s', 'wb'))
#pickle.dump(a_dict, open('save.d', 'wb'))
#pickle.dump(an_obj, open('save.o', 'wb'))

# The line below clears out the values of our variables.
a_num, a_str, a_dict, an_obj = None, None, None, None

# Now unpickle the pickled data
a_num = pickle.loads(pkl_a_num)
a_str = pickle.loads(pkl_a_str)
a_dict = pickle.loads(pkl_a_dict)
an_obj = pickle.loads(pkl_an_obj)

#a_num = pickle.load(open('save.n', 'rb'))
#a_str = pickle.load(open('save.s', 'rb'))
#a_dict = pickle.load(open('save.d', 'rb'))
#an_obj = pickle.load(open('save.o', 'rb'))

# If you pickled/unpickled successfully, these print()s should work.
print(a_num)
print(a_str)
print(a_dict)
print(an_obj)

# Expected output:
# 42
# spam
# {'a': 1, 'b': 7}
# hello
