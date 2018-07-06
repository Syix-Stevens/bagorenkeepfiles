class Player:
  #player entered traits
  name = "" #raw_input("What is your name?\t")
  race = "" #raw_input("What is your race? (dwarf, human, elf, etc)\t")
  gender = "" #raw_input("What is your gender? (M/F)\t")
  age = 0
  height = 0
  weight = 0
  
  #given stats&inventory
  health = 100
  energy = 100
  inventory = {'chest' : 'common shirt', 'back' : 'empty', 'hand' : 'empty', 'legs' : 'common pants', 'pocket' : 'empty', 'feet' : 'common boots'}
  
  #game variables
  last_location = "" #string value here
  
  #function for the game to be able to get input from the player
  def getIn(self):
    input = raw_input().lower()
    #add in general inputs that will work regardless of location here? or possibly just in the game
    #would be easy with a simple if check here
    return input
    
  def printInventory(self):
    print 'Current Inventory:'
    for thing in self.inventory:
      print thing + ' : ' + self.inventory[thing]
    

  def save(self):
    #will print all player info into a file for saving purposes
    output_filename = 'character_save.txt'
    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(self.name)
    output_file_obj.write(self.race)
    output_file_obj.write(self.gender)
    output_file_obj.write(self.age)
    output_file_obj.write(self.height
    output_file_obj.write(self.weight)
    output_file_obj.write(self.health)
    output_file_obj.write(self.energy)
    #output_file_obj.write(self.inventory)       Will have to iterate through inventory and record each item since slots won't change
    #output_file_obj.write(self.last_location)
    output_file_obj.close()
    
  def __init__(self, name="Player name", race="Player race", gender="Player gender", age="Player age", height="Player height", weight="Player weight"):
    self.name = name
    self.race = race
    self.gender = gender
    self.age = age
    self.height = height
    self.weight = weight
#randint%10+20 (cave counter)