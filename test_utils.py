# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils # fichier à tester

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(utils.fact(6) , 720)
        self.assertEqual(utils.fact(0) , 1)

        with self.assertRaises(ValueError):
            utils.fact(-5)


    
    def test_roots(self):
        # À compléter...
        self.assertEqual(type(utils.root(1,1,1)) , tuple)
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
