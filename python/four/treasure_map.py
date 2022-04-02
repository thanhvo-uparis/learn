row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure?")
# cot
column = int(position[0])
# hang
row = int(position[1])
# map[hang][cot]

map[row-1][column-1] = "X"
print(f"\n{row1}\n{row2}\n{row3}")
