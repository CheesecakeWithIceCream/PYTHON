test_scores = []
test_score = int(input("What is your test score: "))
while test_score < 0 or test_score > 100:
    print("Error, please put a number between 0 and 100")
    test_scorse = int(input("What is your test score: "))

test_scores.append(test_score)
print(test_scores)

    