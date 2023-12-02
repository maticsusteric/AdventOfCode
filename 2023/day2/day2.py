from helpers import getDailyInputByFolderName

inputData = getDailyInputByFolderName()


maxColorValues = {"red": 12, "green": 13, "blue": 14}
colorIndexes = {"red": 0, "green": 1, "blue": 2}

part1_ans = 0
part2_ans = 0

for gameIndex, game in enumerate(inputData):
    # Get true game number
    currentGameNum = gameIndex + 1
    # If game was playable
    isOk = True

    # GameMinimumPerColor representing min value: index 0 -> red, index 1 -> green, index2 -> blze
    gameMinimumPerColor = [float('-inf'), float('-inf'), float('-inf')]

    # Strip unnecessary game number at the beginning, we have stored gamenum in currentGameNum
    game = game.replace(f'Game {currentGameNum}: ', "")

    # Do some split magic to get color and number seperate in arrays
    currentGameBySet = game.split("; ")
    for cGame in currentGameBySet:
        curGameValues = cGame.split(", ")
        for oneGame in curGameValues:
            num = int(oneGame.split(" ")[0])
            color = oneGame.split(" ")[1]
            # If current number is bigger than allowed, then the game is invalid
            if num > maxColorValues[color]:
                isOk = False
            # For part 2 -> if the corresponding color array index is smaller than currently written, overwrite it with current num for current game
            if gameMinimumPerColor[colorIndexes[color]] < num:
                gameMinimumPerColor[colorIndexes[color]] = num
    # If the game is valid, add true game index to the sum for the final part 1 answer
    if isOk:
        part1_ans += currentGameNum
    # Multiply the biggest color values of the game and add to the total sum for part 2 answer
    part2_ans += (gameMinimumPerColor[0] * gameMinimumPerColor[1] * gameMinimumPerColor[2])

print("Answer P1: " + str(part1_ans))
print("Answer P2: " + str(part2_ans))
