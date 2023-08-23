def func_submitted(weekday, vacation):
    return weekday

test_case = [(True, True), (False, False), (False, True), (True, False)]

def func_resolved(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False
count = 0
index = 1
number_of_params = len(test_case[0])

message = ""
for case in test_case:
    response_from_user = func_submitted(*case)
    response_correct = func_resolved(*case)

    passed = response_from_user == response_correct

    message = message + "Test #{}: input = {}, output = {}, Passed: {}\n".format(index,case,response_from_user,passed)

    if passed:
        count = count + 1

    index = index + 1
print()
message = message + "Total numbers of test passed: {}/{}".format(count,len(test_case))

print(message)

def get_test_case_factor_from_output(message):

    factor = message[len(message)-3:]
    return int(factor[0])/int(factor[2])

print(get_test_case_factor_from_output(message))


print(1.0 == 1)
