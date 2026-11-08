def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def main():
    print("CI/CD Demo App")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"'топот' — палиндром: {is_palindrome('топот')}")


if __name__ == "__main__":
    main()