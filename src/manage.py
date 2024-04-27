
#!/usr/bin/env python
# Djangos command-line utility for administrative tasks.
import os
import sys
import dotenv


def main():
    # Run administrative tasks.
    dotenv.load_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
"""

import os
import sys

from dotenv import load_dotenv  # Import load_dotenv instead of read_dotenv

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        load_dotenv()  # Use load_dotenv here
    except ImportError:
        pass

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
"""