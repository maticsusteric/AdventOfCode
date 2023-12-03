from collections import defaultdict
from helpers import getDailyInputByFolderName

def process_grid(grid, row_len, column_len):
    part1_ans = 0
    nums = defaultdict(list)

    for r in range(row_len):
        gears = set() # Init a tuple for gears
        partitial = False
        n = 0
        for c in range(column_len + 1):
            if c < column_len and grid[r][c].isdigit():
                n = n * 10 + int(grid[r][c])
                for rr in range(max(0, r - 1), min(row_len, r + 2)):
                    for cc in range(max(0, c - 1), min(column_len, c + 2)):
                        char = grid[rr][cc]
                        # If its not a number, or not a default '.', then it's partitial
                        if not char.isdigit() and char != '.':
                            partitial = True
                        # If the cur character is a star, then add a tuple of current loc to gears
                        if char == '*':
                            gears.add((rr, cc))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n)
                if partitial:
                    part1_ans += n
                n = 0
                partitial = False
                gears = set()

    return part1_ans, nums

def calculate_p2(nums):
    p2 = 0
    # Iterate over tuples, to get gear ratios
    for k, v in nums.items():
        if len(v) == 2:
            p2 += v[0] * v[1]
    return p2

if __name__ == "__main__":
    inputData = getDailyInputByFolderName()
    grid = [[char for char in line] for line in inputData]
    row_len = len(grid)
    column_len = len(grid[0])

    part1_ans, nums = process_grid(grid, row_len, column_len)

    print("Part 1:", part1_ans)
    print("Part 2:", calculate_p2(nums))