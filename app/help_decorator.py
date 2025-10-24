
# Help Menu Decorator  #


def dynamic_help(commands):
    """Generate a help menu dynamically from available commands."""
    print("=== Available Commands ===")
    for name, desc in commands.items():
        print(f"{name:<12} - {desc}")
