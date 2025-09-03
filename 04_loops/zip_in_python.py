# zip is take two list as arugments and return touple of that list 
# if the two list doesn't have same number of items it doesn't include the extra items

names = ['pritam', 'venky', 'sagar','piyush', 'hitesh']
prices = [10, 11, 12, 1212,1111]

for item in zip(prices, names):
    print(item)