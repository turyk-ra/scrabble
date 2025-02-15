letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key,value in zip(letters,points)}
letter_to_points.update({" ": 0})
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    x = letter.upper()
    if x in letter_to_points:
      point_total+=letter_to_points.get(x)
    else:
      point_total += 0
  return point_total

brownie_points  = score_word("BROWNIE")
print(brownie_points)

player_to_words = {}
player_to_words["player1"] = ["BLUE","TENNIS","EXIT"]
player_to_words.update({"wordNerd":["EARTH","EYES","MACHINE"]})
player_to_words.update({"Lexi Con":["ERASER","BELLY","HUSKY"]})
player_to_words["Prof Reader"] = ["ZAP","COMA","PERIOD"]

player_to_points = {}
# player_points = 0
# for key,value in player_to_words.items():
#   player = key
#   words = value
#   for word in words:
#     player_points += score_word(word)
#   player_to_points.update({player:player_points})
# print(player_to_points)

def play_word(player, word):
  player_to_words.get(player).append(word)

play_word("player1","DAD")
print(player_to_words)

def update_points_totals():
  player_points = 0
  for key,value in player_to_words.items():
    player = key
    words = value
    for word in words:
      player_points += score_word(word)
    player_to_points.update({player:player_points})

player_to_words["Prof TEST"] = ["API","REST","TEST"]
update_points_totals()
print(player_to_points)

haggard_pts = score_word("haggard")
print(haggard_pts)