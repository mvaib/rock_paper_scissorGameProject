from random import randint

user = input("\n To play game, enter your name : ")
t = ['rock', 'paper', 'scissor']
dict = {t[2]: '✌️', t[1]: '🖐️', t[0]: '✊', "winner": '🎉🎉'}
print(t[0] + ":" + dict[t[0]])
print(t[1] + ":" + dict[t[1]])
print(t[2] + ":" + dict[t[2]])

computer_move = t[randint(0, 2)]
player_count = 0
computer_count = 0
player_move = 1
draw = 0
player = ""
while player != "exit" and player_move <= 5:
  player = input("\n rock , paper, scissor ? : ")
  player = player.lower()
  computer_move = t[randint(0, 2)]
  player_score = 0
  computer_score = 0
  if player != 'rock' and player != 'paper' and player != 'scissor' and player != 'exit':
    print("[That's not a valid play, please check your spelling!]")

  if player == exit:
    break

  if player_move > 5:
    break

  elif player == computer_move:
    print("\n Computer chose " + " " + player + ":" + dict[player])
    print("\nDraw!")
    player_move += 1
    draw += 1
    print("\n" + user + " " + "score is :" + " " + str(player_score))
    print("Computer score is :" + " " + str(computer_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)?")

    print("..................................................................")

  elif player == t[0] and computer_move == t[1]:
    print("\n Computer chose (paper)" + " " + dict[t[1]])
    print("\n" + t[1] + ":" + dict[t[1]] + " " +
          "is a winner! \n [paper covers rock]")
    computer_count += 1
    player_move += 1
    computer_score += 1

    print("\nComputer score is :" + " " + str(computer_score))
    print(user + " " + "score is :" + " " + str(player_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)?")

    print("..................................................................")

  elif player == t[1] and computer_move == t[2]:
    print("\n Computer chose (scissor)" + " " + dict[t[2]])
    print("\n" + t[2] + ":" + dict[t[2]] + " " +
          "is a winner!  \n [scissor cut paper]")
    computer_count += 1
    player_move += 1
    computer_score += 1

    print("\nComputer score is :" + " " + str(computer_score))
    print(user + " " + "score is :" + " " + str(player_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)?")

    print("..................................................................")

  elif player == t[2] and computer_move == t[0]:
    print("\n Computer chose (rock)" + " " + dict[t[0]])
    print("\n" + t[0] + ":" + dict[t[0]] + " " +
          "is a winner! \n [scissor cannot cut rock]")
    computer_count += 1
    player_move += 1
    computer_score += 1
    print("\nComputer score is :" + " " + str(computer_score))
    print(user + " " + "score is :" + " " + str(player_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)?")

    print("..................................................................")

  elif player == t[0] and computer_move == t[2]:
    print("\n Computer chose (scissor)" + " " + dict[t[2]])
    print("\n" + t[0] + ":" + dict[t[0]] + " " +
          "is a winner! \n [scissor cannot cut rock]")
    player_count += 1
    player_move += 1
    player_score += 1

    print("\n" + user + " " + "score is :" + " " + str(player_score))
    print("Computer score is :" + " " + str(computer_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)")

    print("..................................................................")

  elif player == t[1] and computer_move == t[0]:
    print("\n Computer chose (rock)" + " " + dict[t[0]])
    print("\n" + t[1] + ":" + dict[t[1]] + " " +
          "is a winner! \n [paper covers rock]")
    player_count += 1
    player_move += 1
    player_score += 1
    print("\n" + user + " " + "score is :" + " " + str(player_score))
    print("Computer score is :" + " " + str(computer_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)")

    print("..................................................................")

  elif player == t[2] and computer_move == t[1]:
    print("\n Computer chose (paper)" + " " + dict[t[1]])
    print("\n" + t[2] + ":" + dict[t[2]] + " " +
          "is a winner! \n [scissor cut paper]")
    player_count += 1
    player_move += 1
    player_score += 1
    print("\n" + user + " " + "score is :" + " " + str(player_score))
    print("Computer score is :" + " " + str(computer_score))
    if player_move < 5:
      print("\n Do you want to continue or (exit)")

    print("..................................................................")

if player == "exit" or player_move > 5:
  if computer_count > player_count:
    print("\n Computer total score is " + " " + str(computer_count))
    print("\n" + user + " " + "total score is" + " " + str(player_count))
    print('\n Computer' + " " + "is a winner" + dict['winner'])
  elif player_count == computer_count:
    print("\n" + user + " " + "total score is" + " " + str(player_count))
    print("\n Computer total score is " + " " + str(computer_count))
    print("\nDraw")
  else:
    print("\n" + user + " " + "total score is" + " " + str(player_count))
    print("\n Computer total score is " + " " + str(computer_count))
    print("\n" + user + " " + " is a winner" + dict['winner'])

print("\n Total number of draw is :" + " " + str(draw))
