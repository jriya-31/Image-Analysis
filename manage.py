#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import subprocess

try:
    import django
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)