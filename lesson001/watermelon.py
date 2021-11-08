"""Task about watermelon."""


def watermelon(weight):
    """
    Check condition.
    """
    if weight % 2 == 0 and weight > 2:
        return "YES"
    return "NO"


def main():
    """
    Our main function.
    """
    weight = int(input())
    print(watermelon(weight))


if __name__ == "__main__":
    main()
