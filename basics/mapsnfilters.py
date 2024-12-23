x = [1, 2, 3, 4, 5, 45, 35, 45, 23]

mp = map(lambda i: i * 2, x) #so what we're doing here is passing a list, and then a mini function to map all the elements in he list by a rule
#the rule here is defined in the anonymous lambda function (adding 2 to every element in the list)

print(list(mp)) #typecasted because map returns a map object.

nmp = filter(lambda j: j%2 == 0, x) #instead of returning values to put in a map, it returns true or false
#so in this case if the number is even, it's put in the list nmp.
print(list(nmp))