#this program grades multiple-choice tests for you.  First input a solution .txt file
# then input how many papers need graded, then watch as the scores are printed after each test paper file path is inputted!

print("This program will grade your multiple-choice tests for you!")
print("Tests must be formatted EXACTLY as your answer key in order to ensure accurate grading! \n") #fair warning

input_complete = False #program requires further input from the user
total_tests = str() #test to ensure the user enters an integer for number of tests that need to be graded

try: #this is in case an invalid file path is entered for the answer key or any test
    solution_filepath = input("Please input your answer key's file path:  ") #easier than the with open(input) statement

    test_solutions = open(solution_filepath, "r") #read-only

    while input_complete is False: #continues to ask the user how many tests need graded until an integer is entered
        try:
            total_tests = int(input("Please enter how many tests need graded: "))
        except ValueError:
            print("Only integers can be entered here.")
        if total_tests == str(): #checks to make sure total_tests is now an integer of the user's choosing
            input_complete = False
        else:
            input_complete = True #breaks while loop

    answer_key = [] #converts answer key to list
    for solution in test_solutions:
        answer_key.append(solution)

    for k in range(1, total_tests + 1): #asks for files and grades papers one at a time until the user's specified total is reached
        with open(input("Please input a test paper's filepath:  ")) as test_paper: #opens text file of test paper
            score = 0 #sets test score to zero
            incorrect = 0
            student_response = [] #converts test paper to list
            for answer in test_paper:
                student_response.append(answer)

            for i in range(len(answer_key)): #grades test
                if student_response[i] == answer_key[i]:
                    score += 1
                else:
                    incorrect += 1
            print("Test " + str(k) + " scored " + str(score) + "/" + str(len(answer_key))) #prints test's score/total
            test_paper.close() #closes test
    print("Grading complete.  Please check at least a few tests to"
          " confirm they were graded properly as improper formatting can lead to an inaccurate score.") #fair warning
    test_solutions.close() #closes answer key

except FileNotFoundError: #in case answer key or test paper file path is not found, program must be re-run for security purposes
    print("Your file could not be located.  Please check the file path and try again.")