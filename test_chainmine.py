# test_chainmine.py
"""
Tests for ChainMine module.
"""

import unittest
from chainmine import ChainMine

class TestChainMine(unittest.TestCase):
    """Test cases for ChainMine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainMine()
        self.assertIsInstance(instance, ChainMine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainMine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
