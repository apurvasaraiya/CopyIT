from pynput import keyboard as kb

COMBINATIONS = [
    {kb.Key.alt, kb.KeyCode(char='q')},
    {kb.Key.alt, kb.KeyCode(char='w')}
    ]
