arr = ['fly', 'me', 'to','the', 'moon']
for val in reversed(arr):
    print("reversed",val)

for i in range(len(arr) - 1, -1, -1):
    print("range",i,arr[i])

for i, val in enumerate(reversed(arr)):
    print("enumerate",i,arr[i],val)

# reversed(arr) → values
# range(...) → indexes
# enumerate →  indexes,values