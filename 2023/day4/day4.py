from helpers import getDailyInputByFolderName
import re
from collections import defaultdict

def def_value():
    return 0

inputData = getDailyInputByFolderName()

part1_ans = 0
part2_ans = 0

dictOfWonPerCard = defaultdict(def_value)
num_of_all_cards = len(inputData)

for card_index, card in enumerate(inputData):
    trueGameNum = card_index + 1
    dictOfWonPerCard[card_index] += 1

    # Some regex magic to remove trailing Card with dynamic numbers and random amount of whitespaces
    splitCard = re.sub(r'Card\s+\d+\s*: ', '', card)

    # MORE regex magic to normalize amount of whitespaces to 1
    normalizedSpaces = re.sub(r'\s+', ' ', splitCard)

    cardNumsArray = normalizedSpaces.split(" | ")

    current_winning = cardNumsArray[0].split(" ")
    current_my = cardNumsArray[1].split(" ")
    # Calculate the number of common elements between winning and player's numbers
    num_of_bonus = len(set(current_winning) & set(current_my))

    # Update the wins count in the dictionary for subsequent cards
    for index_bonus in range(num_of_bonus):
        dictOfWonPerCard[card_index + 1 + index_bonus] += dictOfWonPerCard[card_index]

    currentPointsPerCard = 0
    for winning in current_winning:
        if winning in current_my:
            if currentPointsPerCard:
                currentPointsPerCard *= 2
            else:
                currentPointsPerCard = 1

    part1_ans += currentPointsPerCard

print("Part 1: " + str(part1_ans))
print("Part 2: " + str(sum(dictOfWonPerCard.values())))
