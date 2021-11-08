# You can't pickle everything. What happens when you try to
# pickle the values below? Why can't they be pickled?
import pickle

fobj = open('file', 'w')
fn = lambda x: x + 2

pickle.dumps(fn)
#_pickle.PicklingError: Can't pickle <function <lambda> at 0x00000292267CF040>: attribute lookup <lambda> on __main__ failed
pickle.dumps(fobj)
#TypeError: cannot pickle '_io.TextIOWrapper' object