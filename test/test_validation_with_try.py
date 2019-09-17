import unittest
import unittest.mock as mock
from input_validation import validation_with_try


class MyTestCase(unittest.TestCase):
  
  
  def test_average_negative_input(self):
    with self.assertRaises(ValueError):
      validation_with_try.average(-1, 1, 1)


  def test_average_negative_input_index_one(self):
    with self.assertRaises(ValueError):
      validation_with_try.average(90, -90, 99)


if __name__ == "__main__":
    unittest.main()
  