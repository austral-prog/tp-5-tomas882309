# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    root = (b**2 - 4*a*c)
    root_pos = (-b + (b**2 - 4*a*c)**(1/2) ) / 2*a
    root_neg = (-b - (b**2 - 4*a*c)**(1/2) ) / 2*a

    if root >= 0:
        if root == 0:
            return (f"({root_pos})")
        else:
            return (f"({root_pos}, {root_neg})")
    else:
        return "( )"


def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return y


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return (f"f(x) = {a} * X^2 + {b} * X + {c}")
    elif a == 0 and b == 0 and c == 0:
        return "f(x) = 0"
    elif a == 0 and b == 0:
        return (f"f(x) = {c}")
    elif a == 0 and c == 0:
        return (f"f(x) = {b} * X")
    elif a == 0:
        return (f"f(x) = {b} * X + {c}")
    elif b == 0 and c == 0:
        return (f"f(x) = {a} * X^2")
    elif b == 0:
        return (f"f(x) = {a} * X^2 + {c}")

def derivation(a, b):
        if a != 0 and b != 0:
        return (f"f'(x) = {a*2} * X + {b}")
    elif a == 0 and b == 0:
        return ("f'(x) = 0")
    elif a == 0:
        return (f"f'(x) = {b}")
    elif b == 0:
        return (f"f'(x) = {a*2} * X")

