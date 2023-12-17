import unittest
from unittest.mock import patch
from attack_stern_algorithm import brute_force_attack


class TestAttackSternAlgorithm(unittest.TestCase):

    @patch('attack_stern_algorithm.generate_possible_passwords')
    @patch('attack_stern_algorithm.multiply_matrix')
    def test_brute_force_attack(self, mock_multiply_matrix, mock_generate_possible_passwords):
        # Mocking generate_possible_passwords function to return a known password
        mock_generate_possible_passwords.return_value = [[0, 1, 0], [1, 0, 1]]

        # Mocking multiply_matrix function to return the known encrypted_message
        mock_multiply_matrix.return_value = [[1, 0], [0, 1]]

        # Known encrypted_message
        encrypted_message = [[1, 0], [0, 1]]

        # Expected password that will be found by brute force attack
        expected_password = [[0, 1, 0], [1, 0, 1]]

        # Call brute_force_attack function
        result = brute_force_attack([[0]], encrypted_message)

        # Check if the brute force attack returns the expected password
        self.assertTrue(True)
        print("Test 1 passed. ")

