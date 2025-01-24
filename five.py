from collections import Counter

my_tuple = (1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 9, 1, 2, 10, 2)  

element_count = Counter(my_tuple)  

print("Elements occurring more than 2 times:")


for element, count in element_count.items():  
    if count > 2:  
        print(f"{element}: {count} times")
