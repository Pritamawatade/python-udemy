sales = [11,22,32,23,54,78,4,9,3,23]


# generator comprehensions are used to save memory since it doesn't create data/list in memory it gives the object of generator which gives the data one by one
generator_comprehension = (sale for sale in sales if sale > 10)
