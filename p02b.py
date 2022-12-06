s = """A Y
B X
C Z"""

lines = s.split("\n")

lines = [line.strip() for line in open("p02.txt").readlines()]

# if A: X draw, Y wins, Z loses
# if B: X loses, Y draws, Z wins
# if C: X wins, Y loses, Z draws
result_matrix = ((3, 6, 0), (0, 3, 6), (6, 0, 3))

total_score = 0
for line in lines:
    (opponent, yours) = (line[0], line[2])

    opponent_index = "ABC".index(opponent)
    required_outcome = "XYZ".index(yours) * 3
    your_index = result_matrix[opponent_index].index(required_outcome)
    
    turn_score = (your_index + 1) + required_outcome

    total_score += turn_score

print(total_score)