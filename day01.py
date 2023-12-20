
def p1(f):
    lines = f.splitlines()
    res = 0
    for line in lines:
        digits = [char for char in line if char.isnumeric()]
        if digits:
            res += int(digits[0] + digits[-1])
    return res

digit_name = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def p2(f):
    lines = f.splitlines()
    res = 0
    for line in lines:
        digits = [char for char in translate(line) if char.isnumeric()]
        res += int(digits[0] + digits[-1])
    return res
def translate(line):
    for num, name in enumerate(digit_name):
        line = line.replace(name, f"{name}{num}{name}")
    return line


