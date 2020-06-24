from LinkedList import LinkedList
from Node import Node

# def containscycle(list):
#     if not list:
#         return False
#     else:
#         seennodes = [{}]
#         nextnode = list[0]
#         node = list[0]
#         while nextnode != "null":
#             node = nextnode
#             if node in seennodes:
#                 return True
#             else:
#                 seennodes.add(node)
#                 nextnode = node.values()
#
#     return False


# testing

a = Node("a", None)
b = Node("b", a)
c = Node("c", b)
d = Node("d", c)

list1 = LinkedList()
list1.append(a)
list1.prepend(b)
list1.prepend(c)
list1.prepend(d)

print(list1)

# print(containscycle(list2))  #false
# print(containscycle(list3))  #false
# print(containscycle(list4))  #false
