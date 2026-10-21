def remove_failing(scores):
    for score in scores:
        if score < 60:
            scores.remove(score)
            scores = remove_failing(scores)
    return scores

def average(numbers):
    return sum(numbers) / len(numbers)

scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
passing_scores = remove_failing(scores)

print(f"Passing scores: {passing_scores}")
print(f"Number of passing scores: {len(passing_scores)}")
print(f"Average of passing scores: {average(passing_scores)}")