
# Color Output Utility #


from colorama import Fore, Style, init

init(autoreset=True)

def success(msg): return f"{Fore.GREEN}✓ {msg}{Style.RESET_ALL}"
def error(msg): return f"{Fore.RED}✗ {msg}{Style.RESET_ALL}"
def warn(msg): return f"{Fore.YELLOW}! {msg}{Style.RESET_ALL}"
