student_heights = input("Input a list of student heights: ").split()
somme = 0
length = 0
for height in student_heights:
    somme += int(height)
    length += 1

average_height = round(somme / length)
print(average_height)
