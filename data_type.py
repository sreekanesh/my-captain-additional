#list

#append
list1=['a,b,c,d']
list1.append('e')
print(list1)

#clear
list1=['a,b,c,d,e']
list1.clear()
print(list1)

#copy
list1=['a,b,c,d,e']
xyz=list1.copy()
print(xyz)

#count
list1=['a,b,c,d,e']
xyz=list1.count('a')
print(xyz)

#extend
fruits=['apple,orange,melon']
cars=['ford,BMW,volvo']
fruits.extend(cars)
print(fruits)

#index
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)


#insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#remove
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#reverse
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#exercise 1
fruits=['apple','banana','cherry']
print(fruits[1])

#exercise 2
fruits=['apple','banana,cherry']
fruits[0]='kiwi'
print(fruits)

#exercise 3
fruits=['apple,banana,cherry']
fruits.append('orange')
print(fruits)

#exercise 4
fruits=['apple','banana','cherry']
fruits.insert(1,'lemon')

#exercise 5
fruits=['apple','banana','cherry']
fruits.remove('banana')
print(fruits)

#exercise 6
fruits=['apple','banana','cherry']
print(fruits[-1])

#exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#tuples
#methods


#count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

#exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])




 


