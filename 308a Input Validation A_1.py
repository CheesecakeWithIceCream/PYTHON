test_score = []
test_scores = int(input("What is your test score: "))
while test_scores < 0 or test_scores > 100:
    print("Error, please put a number between 0 and 100")
    test_scorse = int(input("What is your test score: "))

test_score.append(test_scores)
print(test_score)

    