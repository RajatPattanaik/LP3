class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

def knapsack(w,arr):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
    '''for item in arr:
        print(item.value, item.weight, item.value/item.weight)'''
    finalvalue = 0.0
    for item in arr:
        if item.weight <= w:
            w -= item.weight
            finalvalue += item.value
        else:
            finalvalue += item.value * w/item.weight
            break
    return finalvalue
 

# Weight of Knapsack
knapsack_weight = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

# Function call
max_val = knapsack(knapsack_weight, arr)
print ('Maximum value we can obtain = {}'.format(max_val))