def bubble_sort(a: list):
    size = len(a)
    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):
            if a[i] > a[i+1]:
                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp
                swapped = True
            print(a)

        if swapped == False:
            break

bubble_sort([5,4,3,2])

# exercise
# Modify bubble_sort function such that it can sort following list of transactions happening in 
# an electronic store,

# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]

# bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

# bubble_sort(elements, key='transaction_amount')

# This will sort elements by transaction_amount and your sorted list will look like,

# elements = [
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
# But if you call it like this,

# bubble_sort(elements, key='name')
# output will be,

# elements = [
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'}]

def bubble_sort_by_key(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

    print(elements)
                


bubble_sort_by_key([
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ], "name")