import unittest
import unittest.mock as mock
from input_validation import validation_with_try as validation_with_try


class MyTestCase(unittest.TestCase):
  
  
  def test_average_negative_input(self):
    with self.assertRaises(ValueError):
      with mock.patch('builtins.input', side_effect=[-1, 1, 1]):
        ValueError
  