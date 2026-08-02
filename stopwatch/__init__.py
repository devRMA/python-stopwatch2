from colorama import just_fix_windows_console

from .profile import profile
from .statistics import Statistics
from .stopwatch import Stopwatch
from .utils import format_elapsed_time

# The reports are colored with ANSI escapes, which a Windows console only
# understands once virtual terminal processing is enabled. colorama was
# always a dependency for this, but nothing ever called it, so on Windows
# the escapes were printed raw. Unlike colorama.init(), this does not wrap
# sys.stdout, which a library has no business doing, and it is a no-op
# everywhere else.
just_fix_windows_console()

__all__ = ['Statistics', 'Stopwatch', 'format_elapsed_time', 'profile']
