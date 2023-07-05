print('Chord method\nEquation f(x)=x³+3x²-24x-3\nAccuracy: 10⁻⁶\n')

equation = lambda x: x ** 3 + 3 * x ** 2 - 24 * x - 3

def chord_method(lower: float, upper: float, accuracy: float = 1e-6) -> float | None:
    # Results
    lower_result = equation(lower)
    upper_result = equation(upper)

    while abs(upper - lower) > accuracy:
        # Calculate the next approximation
        x = (lower * upper_result - upper * lower_result) / (upper_result - lower_result)
        # Value
        result = equation(x)

        # found root?
        if abs(result) < accuracy:
            return x

        # Narrow the interval
        if result * lower_result < 0:
            upper, upper_result = x, result
        else:
            lower, lower_result = x, result

    # Nothing found?

try:
    lower = float(input('Lower bound: '))
    upper = float(input('Upper bound: '))

    if not lower < upper:
        raise ValueError('Lower bound must be less than upper bound')

    solution = chord_method(lower, upper)

    if solution is None:
        print('No solution found')
    else:
        print(f'Approximate solution: {solution}')

except Exception as e:
    print(f'Invalid input. {e.args[0][0].upper() + e.args[0][1:]}.')
