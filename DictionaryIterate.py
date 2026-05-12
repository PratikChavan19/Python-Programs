Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}

print("Data of Dictionary : ", Batches)

print("Data traversal using loop")
for x in Batches :
    print(x)

print("Data traversal using loop")
for x in Batches :
    print(x, Batches[x])


print("Data traversal using loop")
for x in Batches :
    print(x, Batches.get(x))

keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)

for i in range(0, len(Batches)) :
    print("Value is : ", keyBatches[i], end = " ")
    print("Fees are : ", valueBatches[i])