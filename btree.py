from BTrees.OOBTree import OOBTree

t = OOBTree()
t.update({1: "red", 2: "green", 3: "blue", 4: "spades"})

print(list(t.keys()))
