#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
from unittest.mock import patch
from io import StringIO

HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class TestHBNBCommand(unittest.TestCase):
    """Class to test the functionality of the HBNBCommand class"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test the help command output"""
        cmd = HBNBCommand()
        cmd.onecmd("help")
        self.assertIn("Documented commands (type help <topic>):",
                      mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test the create command"""
        cmd = HBNBCommand()
        cmd.onecmd("create Place")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        self.assertTrue(output.isalnum())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test the show command"""
        cmd = HBNBCommand()
        cmd.onecmd("create Place")
        place_id = mock_stdout.getvalue().strip()
        cmd.onecmd(f"show Place {place_id}")
        output = mock_stdout.getvalue()
        self.assertIn(place_id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test the destroy command"""
        cmd = HBNBCommand()
        cmd.onecmd("create Place")
        place_id = mock_stdout.getvalue().strip()
        cmd.onecmd(f"destroy Place {place_id}")
        cmd.onecmd(f"show Place {place_id}")
        output = mock_stdout.getvalue()
        self.assertIn("no instance found", output)
