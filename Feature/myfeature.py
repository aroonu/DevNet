"""
Basic feature module.
"""


def greet(name: str) -> str:
    """
    Greet a person by name.
    
    Args:
        name: The person's name.
        
    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """
    Add two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(greet("Developer"))
    print(f"2 + 3 = {add(2, 3)}")
print("Welcome to DevNet")