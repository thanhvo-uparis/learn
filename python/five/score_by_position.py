list_scores = input("Input a list of student scores: ").split()
position = int(input("Enter position: "))

for n in range(0, len(list_scores)):
    list_scores[n] = int(list_scores[n])

score_by_position = list_scores[position -1]
print(score_by_position)

