import sys

## Part 1
x = 0
with open('input.txt', 'r') as file:
    for line in file:
        string = line.strip()
        frst = 0
        scnd = 0
        for letter in string:
          if letter.isdigit():
            if frst == 0:
              frst = int(letter)
            scnd = int(letter)
        if frst != 0 and scnd != 0:
          concatenated = str(frst) + str(scnd)
          x += int(concatenated)
print(x)

def check_digit(string):
  if string[0].isdigit():
    return int(string[0])

  d = next(filter(string.startswith, mydic), None)
  return mydic.get(d, 0)


## Part 2
mydic = {"one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "zero" : 0}

a = 0
total2 = 0
with open('input.txt', 'r') as file:
    for line in file:
        string = line.strip()
        total2 += 10 * next(filter(None, map(check_digit, (line[i:] for i in range(len(line))))))
        total2 += next(filter(None, map(check_digit, (line[i:] for i in range(len(line) -1, -1, -1)))))
print(total2)

