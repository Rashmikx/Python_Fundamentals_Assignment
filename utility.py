#utility functions as assigned

import os

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt):
    """Get user input, stripped of extra spaces"""
    return input(prompt).strip()
