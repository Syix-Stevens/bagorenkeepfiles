import Player

def main():
  name = "name" #raw_input("name?")
  race = "race" #raw_input("race?")
  gender = "m" #raw_input("gender")
  age = 20 #raw_input("age")
  height = 180 #raw_input("height")
  weight = 200 #raw_input("weight")
  player = Player.Player(name,race,gender,age,height,weight)
  print "Player made!"
  raw_input()
  player.save()
  print "yay"
  raw_input()

main()