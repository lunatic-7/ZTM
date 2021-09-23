# Testing is an important term in python, asa we start working in a company, they usually have,
# older codes running created by someone else. We modify them, and that leads us to bugs,
# So, to check them and remove them before deployment we use testing.
# We usually create a testing file with a every main file, to test it. It is just for us
# not to show the users.
# Luckily, we have a in-build module for this purpose (unittest).

import unittest
import being_tested  # The file which needs to be tested.


class TestMain(unittest.TestCase):
    def setUp(self):  # We can use this build-in setUp method to print anything before our each tests.
        print('about to test a function!')

    def test_do_stuff(self):
        test_param = 10
        result = being_tested.do_stuff(test_param)
        self.assertEqual(result, 15)  # This checks if a == b, means result == 15 here.

    def test_do_stuff2(self):
        test_param = 'whbjhdb'
        result = being_tested.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)  # Better ay to write upper line.

    def test_do_stuff3(self):
        test_param = None
        result = being_tested.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        test_param = ''
        result = being_tested.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff5(self):
        test_param = 0
        result = being_tested.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):  # We can use this build-in tearDown method to print anything after each tests.
        print('cleaning Up!')


if __name__ == '__main__':  # This is just to make sure that test runs only when main file is correct.
    unittest.main()

# Some useful assert methods...

# Method                                 Use
# assertEqual(a, b)              Verify that a == b
# assertNotEqual(a, b)           Verify that a != b
# assertTrue(x)                  Verify that x is True
# assertFalse(x)                 Verify that x is False
# assertIn(item, list)           Verify that item is in list
# assertNotIn(item, list)        Verify that item is not in list
# assertIsInstance(a, b)         Verify that isinstance(a, b)
# assertNotIsInstance(a, b)      Verify that not isinstance(a, b)

# python -m unittest -v  # We call test methods like this for more details.
