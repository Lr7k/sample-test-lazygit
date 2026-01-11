#!/usr/bin/env python3

def greet(name: str) -> str:
    return f"Hello, {name}!"

def farewell(name: str) -> str:
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
