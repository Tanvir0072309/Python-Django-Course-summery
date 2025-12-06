# there are some mathodes of list as follow

friends = ["mohit","rohit","lala","virat"]
print(friends)

# .append(<new word>) this method is joint a new word to the end of the list
friends.append("Tanvir")
print(friends)

# .sort() is short the list in to the assanding order
friends.sort()
print(friends)

# .reverse() is sort the list in to reverse
friends.reverse()
print(friends)

# .insert(<Index>,<new Insertation>) is use for inset data in a perticuler index
friends.insert(3,"sima")
print(friends)

# .pop(<index>) this method is delete the element from thi list at the perticuler index
friends.pop(3)
print(friends)

# .remove(<element>) is remove a perticuler element from the list 
friends.remove('lala')
print(friends)