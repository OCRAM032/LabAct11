str1 = "James"

first = str1[0]

middle_index = len(str1) // 2
middle = str1[middle_index]

last = str1[-1]

result = first + middle + last

print(result) 

str1 = "JhonDipPeta"


middle_index = len(str1) // 2


result = str1[middle_index - 1 : middle_index + 2]

print(result)  
s1 = "America"
s2 = "Japan"


s1_first = s1[0]
s1_middle = s1[len(s1) // 2]
s1_last = s1[-1]


part1 = s1_first + s1_middle + s1_last


s2_first = s2[0]
s2_middle = s2[len(s2) // 2]
s2_last = s2[-1]


part2 = s2_first + s2_middle + s2_last


result = part1 + part2

print(result)  