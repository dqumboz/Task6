# Q1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
lst.sort()
print(lst[-1])
lst.remove(lst[0])
lst.sort(reverse=True)
print(lst[-1:2:-1])

# Q2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
i = 0
count = 0
for i in range(len(main_lst)):
    if "python" in main_lst[i]:
        count += 1
print(count)

# Q3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(' '.join(my_lst).title())

# Q4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
new_lst = my_lst[:]
print(new_lst)

# Q5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
a = my_lst[2]
b = my_lst[4]
my_lst[2] = b
my_lst[4] = a
print(my_lst)

# Q6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
result = 0
for i in nums:
    result += i
print(result)

# Q7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
print(tuple1 + (9,))

# Q8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
print(tuple1 + (9,) + tuple2)
