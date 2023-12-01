# Day 1 :)
D = open("d1Input.txt", "r").read()
part1Sum = 0
part2Sum = 0

for line in D.split('\n'):
  part1Nums = []
  part2Nums = []

  for index, character in enumerate(line):
    # If its a number, append to arrays
    if character.isdigit():
      part1Nums.append(character)
      part2Nums.append(character)
    # Scan for remaining part of line
    for digitInd, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      # If the remaining part of the line starts with the spelled out digit, its appended to p2_digits.
      if line[index:].startswith(val):
        part2Nums.append(str(digitInd+1))
  part1Sum += int(part1Nums[0] + part1Nums[-1])
  part2Sum += int(part2Nums[0] + part2Nums[-1])


print("Answer P1: " + str(part1Sum))
print("Answer P2: " + str(part2Sum))