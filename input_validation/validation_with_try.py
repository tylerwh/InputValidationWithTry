"""
Author: Tyler Hochstetler
For: Python CIS189
Purpose: This program is to demonstrate gathering user input, formatting the data, and the ouput of that data.
"""


def average(value1, value2, value3):

  score1 = float(value1)
  score2 = float(value2)
  score3 = float(value3)

  
  number_of_tests = 3

  
  return (score1 + score2 + score3) / number_of_tests


if __name__ == "__main__":
    
    
    # Commented out for the purpose of testing
    # first_name = input("Hello, what is your first name? ").capitalize()
    # last_name = input("Your last name? ").capitalize()
    # age = input("And your age: ")
    # print(f'{first_name}' + ", you are now going to enter the score for each of your last three tests.\n")
    # average_scores = average()
    # print("\n" + f'{last_name}' + ", " + f'{first_name}' + " age : " + f'{age}' + " average score: {0:.2f}".format(average_scores))


# The below table are a series of tests run for average()

#      Input      // Expected Output // Actual Output
#  85, 90, 95     //      90.00      //      90.00
# 93.3, 92.2, 91.1//      92.20      //      92.20
#  90, 79.9, 83   //      84.30      //      84.30
# 90, 90, ninety  //   ValueError    // "ValueError: could not convert string to float: 'ninety'"