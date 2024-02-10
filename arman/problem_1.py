n = int(input("Enter the number of participants: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))
max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

runner_up_score = max(scores)
print("The runner-up score is:", runner_up_score)
