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
  except:
    raise ValueError

  
  number_of_tests = 3

  
  return (score1 + score2 + score3) / number_of_tests


if __name__ == "__main__":
  pass   