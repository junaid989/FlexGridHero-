#!/usr/bin/env python3
import os, sys, time

CYAN='\033[96m'; BLUE='\033[94m'; GREEN='\033[92m'; YELLOW='\033[93m'; MAG='\033[95m'; RED='\033[91m'; RESET='\033[0m'; BOLD='\033[1m'

class UI:
    def __init__(self):
        self.width = self._get_width()
    def _get_width(self):
        try:
            return os.get_terminal_size().columns
        except Exception:
            return 80
    def clear(self): os.system('cls' if os.name=='nt' else 'clear')
    def header(self, text):
        line = '=' * min(self.width,80)
        print(CYAN + BOLD + line + RESET)
        print(BLUE + BOLD + text.center(min(self.width,80)) + RESET)
        print(CYAN + BOLD + line + RESET + '\n')
    def section_title(self,text):
        print(GREEN + BOLD + f"-- {text} --" + RESET + '\n')
    def type_writer(self, text, speed=0.004):
        for ch in text:
            sys.stdout.write(MAG + ch + RESET); sys.stdout.flush(); time.sleep(speed)
        print('\n')
    def prompt(self,label):
        try:
            return input(YELLOW + f"{label}: " + RESET)
        except EOFError:
            return ''
    def print_good(self,msg): print(GREEN + BOLD + '✔ ' + msg + RESET)
    def print_bad(self,msg): print(RED + BOLD + '✖ ' + msg + RESET)
    def print_info(self,msg): print(BLUE + msg + RESET)
    def print_warn(self,msg): print(YELLOW + msg + RESET)
    def print_badge(self,badge): print(CYAN + BOLD + '\n[🏅 ' + badge + ' ]\n' + RESET)
    def pause(self, sec=0.5): time.sleep(sec)
