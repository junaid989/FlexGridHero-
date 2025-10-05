#!/usr/bin/env python3
"""Simple inline editor challenge: user types a CSS line and we check basic correctness."""
def css_challenge(ui):
    ui.print_info('Mini Editor Challenge: Write a CSS rule that sets display to grid for .layout')
    ui.print_info('Example correct answer: .layout { display: grid; }')
    attempt = input('Enter CSS: ').strip().lower()
    normalized = ''.join(attempt.split())
    ok_variants = ['.layout{display:grid;}', '.layout{display:grid}']
    if normalized in ok_variants:
        ui.print_good('Nice! Challenge passed.')
        return True
    else:
        ui.print_bad('Not quite. Make sure to set display: grid for .layout')
        return False
