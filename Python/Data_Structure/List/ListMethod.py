# print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# help(list)
#some methods are:

#  |  append(self, object, /)
#  |      Append object to the end of the list.
#  |
#  |  clear(self, /)
#  |      Remove all items from list.
#  |
#  |  copy(self, /)
#  |      Return a shallow copy of the list.
#  |
#  |  count(self, value, /)
#  |      Return number of occurrences of value.
#  |
#  |  extend(self, iterable, /)
#  |      Extend list by appending elements from the iterable.
#  |
#  |  index(self, value, start=0, stop=9223372036854775807, /)
#  |      Return first index of value.
#  |
#  |      Raises ValueError if the value is not present.
#  |
#  |  insert(self, index, object, /)
#  |      Insert object before index.
#  |
#  |  pop(self, index=-1, /)
#  |      Remove and return item at index (default last).
#  |
#  |      Raises IndexError if list is empty or index is out of range.
#  |
#  |  remove(self, value, /)
#  |      Remove first occurrence of value.
#  |
#  |      Raises ValueError if the value is not present.
#  |
#  |  reverse(self, /)
#  |      Reverse *IN PLACE*.
#  |
#  |  sort(self, /, *, key=None, reverse=False)
#  |      Sort the list in ascending order and return None.
#  |
#  |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
#  |      order of two equal elements is maintained).
#  |
#  |      If a key function is given, apply it once to each list item and sort them,
#  |      ascending or descending, according to their function values.
#  |
#  |      The reverse flag can be set to sort in descending order.

l=[1,2,2,3,4,5]
print("List: ",l)
l.append(6)
print("List after Append: ",l)
l.insert(1,10)
print("List after inserting at 10 at 1th index: ",l)
l.sort()
print("Sorted List: ",l)
l.remove(2)
print("Remove first occurance of 2: ",l)
l1=[11,12,13]
l.extend(l1)
print("L+ L1(extend): ",l)