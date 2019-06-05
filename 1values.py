def how_many(list_of_things):
      count = len(list_of_things)
      return count
how_many(robots)

def how_many(list_of_things):
      count = len(list_of_things)
      return count, 1
(x, y) = how_many(robots)
print(x)
print(y)
