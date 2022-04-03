list_scores = input("Input a list of student scores: ").split()

for n in range(0, len(list_scores)):
    list_scores[n] = int(list_scores[n])

max = list_scores[0]

for score in list_scores:
    if score > max:
        max = score

# for n in range(0, len(list_scores)):
#     if list_scores[n] > max:
#         max = list_scores[n]

print(max)
