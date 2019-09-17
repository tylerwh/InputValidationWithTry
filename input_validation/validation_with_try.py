"""
Author: Tyler Hochstetler
For: Python CIS189
Purpose: This program is to demonstrate gathering user input, formatting the data, and the ouput of that data.
"""


def average(value1, value2, value3):

  score1 = float(value1)
  score2 = float(value2)
  score3 = float(value3)


  try:
    assert(score1 >= 0)
    assert(score2 >= 0)
    assert(score3 >= 0)
  except:
    raise ValueError


  number_of_tests = 3

  
  return (score1 + score2 + score3) / number_of_tests


if __name__ == "__main__":
  first_name = input("Enter your first name: ")
  last_name = input("Last name: ")
  age = input("Age: ")
  print("\n" + f'{first_name}' + ", you are now going to enter your test scores.\n\n")
  score1 = float(input("Score 1: "))
  score2 = float(input("Score 2: "))
  score3 = float(input("Score 3: "))


  # Inserted below try/exception to valid input from the console
  try:
    assert(score1 >= 0)
    assert(score2 >= 0)
    assert(score3 >= 0)
  except:
    raise ValueError
  

  average_scores = average(score1, score2, score3)


  print("\n" + f'{last_name}' + ", " + f'{first_name}' + "\nAge : " + f'{age}' + " \nAverage score : {0:.2f}".format(average_scores))