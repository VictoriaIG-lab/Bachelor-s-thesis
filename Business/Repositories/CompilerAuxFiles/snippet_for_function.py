count = 0
index = 1
number_of_params = len(test_case[0])

for case in test_case:
    response_from_user = func_submitted(*case)
    response_correct = func_resolved(*case)

    passed = response_from_user == response_correct

    print("Test #{}: input = {}, output = {}, Passed: {}".format(index,case,response_from_user,passed))

    if passed:
        count = count + 1

    index = index + 1
print()
print("Total numbers of test passed: {}/{}".format(count,len(test_case)))



