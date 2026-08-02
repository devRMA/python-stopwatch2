from colorama import just_fix_windows_console

from .profile import profile
from .statistics import Statistics
from .stopwatch import Stopwatch
from .utils import format_elapsed_time

just_fix_windows_console()

__all__ = ['Statistics', 'Stopwatch', 'format_elapsed_time', 'profile']
