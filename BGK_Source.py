#start of game
def start(first = False):
  if first == True:
    print "There are doors to your left and right and a long hallway in front of you."
    print "The hallway is brightly lit by rows of torches on the wall that don't seem like"
    print "they'll go out any time soon. Where would you like to go?"
  while True:
    answer = raw_input().lower()
    if answer == "l" or answer == 'door1':
	  staircase()
    elif answer == 'r' or answer == 'door2':
      brickdoor()
    elif answer == 'myah':
      print 'MYAH!!!!'
    elif answer == 'crazy':
      print 'YEAH!'
    elif answer == 'pick up a torch':
      print 'You walk up to one of the torches on the wall and try to pull it off, but it seems to be rooted in place. It doesn\'t budge no matter how hard you pull.'
      print ''
    elif answer == 'to see the seer':
      print "There's no seer here"
    elif answer == '':
	  print ""
    elif answer == 'any door stupid':
      print 'Pick a door stupid'
    elif answer == 'leave':
      print 'You turn around to leave, but to your surprise, there\'s no door behind you!'
      print 'How did you get in here?'
      print ''
    elif answer == 'die' or answer == 'kill myself' or answer == 'commit suicide' or answer == 'seppuku':
      print 'You scream "SEPPUKU!!!" at the top of your lungs and pull your katana out of its sheathe.'
      print 'Flipping your katana around so it faces you, you plung it into your stomach in a swift motion.'
      print 'Like a true warrior, you manage to cut all the way across your body, spilling your innards all over the nice red carpet.'
      print 'The hallway fades from your view.'
      game_over()
    elif answer == 'here' or answer == 'stay still':
      print 'You stand right where you are.'
    elif answer == 'yes' or answer == 'ye':
      print 'ok'
    elif answer == 'go back':
      print 'Go back to where?'
    elif answer == 'ok':
      print 'Ok what?'
    elif answer == 'yes i am':
      print 'Sure you are'
    elif answer == 'backflip'or answer == 'do a backflip':
      print 'You do an awesome, perfectly executed backflip.'
      print 'Nice!'
    elif answer == 'dance like a maniac' or answer == 'dance' or answer == 'bust a move':
      print 'You dance around for a bit like someone who\'s lost their mind.'
      print 'Your vision fades and then you black out.'
      print ''
      print 'You wake up and wipe the drool off of your face'
    elif answer == 'turn around':
      print 'You turn around and look at the wall behind you... huh, I wonder how you got in here.'
      print 'You turn back around and look at your surroundings.'
    elif answer == 'climb the walls' or answer == 'climb the wall' or answer == 'up':
      print "You desperately try to climb up the wall but you can't manage to do much more than jump up and grasp at the stones feebly."
      print ''
      print 'Eventually you give up and return deciding where you should go.'
    elif answer == 'king' or answer == 'painting of king':
      print 'You walk down the hall to look at the paintings, many of them are of past kings and nobles.'
      hall()
    elif answer == 'qq' or answer == 'tt' or answer == 'cry':
      print 'You cry for a little bit, you big baby'
    elif answer == 'climb up the stairs':
      print 'There are no stairs here.'
    elif answer == 'fireball' or answer == 'throw a fireball' or answer == 'i throw a fireball':
      print "A raging fireball bursts out of your hand and you throw it down the hallway. The walls, ceiling, and floors are illuminated as it flies by, and as it passes the paintings"
      print "on the walls, some of them are ignited. It begins to fade from your view, and then finally it reaches the end of the hall and explodes in a brilliant burst of light and heat."
      print "You can feel it even from where you're standing. The flames rapidly expand and consume any objects they come into contact with, spreading the fire further and causing it"
      print "to become even more violent. In a matter of minutes the flames have made it almost all the way back to you. The heat emanating from them causes your eyes to dry and the"
      print "smoke begins to choke you.  You crouch down to escape it, but it has already filled the entire hallway from top to bottom. This may not have been that good of an idea"
      print "after all. You continue choking on the smoke as the flames race to you and quickly engulf your body. Your skin begins to boil and as you try to let out a scream,"
      print "the overwhelming heat cooks your throat."
      raw_input()
      print "Roughly half an hour later, all that remains of the great castle is a huge pile of molten stone."
      print "Near where the front gate used to be lie a few scattered and badly charred bone fragments."
      game_over()
#keyword identifiers
    elif answer.find('right') != -1:
      brickdoor()
    elif answer.find('left') != -1:
      staircase()
    elif answer.find('hall') != -1 or answer.find('painting') != -1:
      print 'You walk down the hall and pass many beautiful paintings. As you near the end, you can make out the shape of a door'
      hall()
    else:
      if defaults(answer):
        continue
      print "I don't know that response. Try again."
      answer = answer + ' : '
      output_filename = 'starterror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#if player goes left from start
def staircase():
  num_tries = 0
  print 'A long, narrow staircase lies behind the door, you walk up a few steps and it seems like the door at the top hasn\'t moved'
  print 'Do you want to keep going?'
  while True:
    answer = raw_input()
    if answer.find('yes') != -1 or answer.find('yeah') != -1 or answer == 'y':
      if num_tries == 0:
        print "You walk up the stairs for what seems like hours, and the top doesn't get any closer."
        print 'You look behind yourself and to your surprise,the door you just went through is only five steps down.'
        num_tries += 1
        print 'Do you want to keep going?'
      elif num_tries == 1 or num_tries == 2:
        print "You walk up the stairs for what seems like hours, and the top doesn't get any closer."
        print 'You look behind yourself and to your surprise,the door you just went through is still only five steps down.'
        num_tries += 1
        print 'Do you still want to keep going?'
      elif num_tries == 3:
        print "You continue walking up the stairs, it still seems as though the top isn't getting any closer glancing over your shoulder, you can easily see you"
        print "aren't making any progress but for some reason you decide that you just have to keep marching forward. Your legs begin to ache and sweat covers"
        print "your forehead and completely soaks your shirt, but you don't care, you need to get up these dastardly stairs."
        print ''
        print "Hours later, you've been reduced to crawling, ever so slowly upwards. Your vision blurs slightly, and you can't remember if you were up two stairs"
        print "from the bottom or three but you're a good five now. Ecstatic that progress is being made, you continue to push your poor body to make it"
        print "to the top of the stairs. Suddenly, you begin to hear loud groaning sounds coming from nearby. Startled, you look around but you don't see"
        print "anything that could possibly be making that noise, it must just be your imagination."
        print "Your vision gets even more blurry and you fall, face down upon the treacherous stone steps."
        raw_input()
        print ""
        print ""
        print ""
        print '.'
        print '..'
        print '...'
        print '...' + player_name + '...'
        raw_input()
        print player_name + '...'
        print "wake up " + player_name + '...'
        answer = raw_input().lower()
        if answer == 'no' or answer == 'nah' or answer == "i don't want to" or answer == "i don't wanna" or answer == "i don't feel like it":
          print 'You have to wake up ' + player_name
          raw_input()
          print 'You wake up in the hallway that you were originally in. You blink groggily and feel very refreshed after your marathon of stairs. It feels good to just'
          print 'lay on the ground for a little bit, but you realize you need to get up and continue your exploration of this mysterious place.'
          start()
        else:
          print 'You wake up in the hallway that you were originally in. You blink groggily and feel very refreshed after your marathon of stairs. It feels good to just'
          print 'lay on the ground for a little bit, but you realize you need to get up and continue your exploration of this mysterious place.'
          start()
    elif answer == 'I want to go home':
      print "You can't go home now, you're in a castle!"
    elif answer.find('no') != -1 or answer == 'n':
      print 'You walk down the steps and close the door behind you.'
      print 'Where would you like to go now?'
      start()
    elif answer == 'myah':
      print 'MYAH!!'
      print 'Your "MYAH" echoes up and down the stairs.'
      print ''
    else:
      if defualts(answer) == True:
        continue
      print 'You stand in the stairway for a while, unsure of what to do.'
      answer = answer + ' : '
      output_filename = 'staircaseerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#if player goes right from start, add a program after this to print out the death sequence to cut down on repetetive code
def brickdoor():
  print 'You open the door and behind it lies a brick wall, about 3 feet in'
  while True:
    answer = raw_input().lower()
    if answer == 'close the door' or answer == 'close it':
      print "You close the door, and hear a loud grinding noise that sounds like it's getting closer and closer to the door."
      answer = raw_input()
      if answer == 'reopen the door' or answer == 'try the door' or answer == 'open it again':
        print "You reopen the door and the brick wall is now touching the frame, good thing you weren't in there."
        start()
      else:
        start()
    elif answer == 'turn around':
      print 'You turn back to the hall.'
      start()
    elif answer == 'go in and die':
      print 'You gleefully step into the brick room, ready to accept your death.'
      print 'The wall begins to slide forward and you start giggling like a crazed little schoolgirl maniac.'
      print 'You try to pull the brick wall to the door frame, to speed your own death.'
      print 'As you are slowly crushed to death, the biggest smile crosses your face.'
      print ''
      raw_input()
      print 'Your head explodes under the sheer pressure of the wall, just like you wanted.'
      game_over()
    elif answer.find('in') != -1 or answer == 'touch the wall' or answer == 'push on the wall' or answer == 'kick the wall' or answer == 'punch the wall':
      print 'As you walk inside, the door shuts behind you, and the brick wall begins advancing towards you, making a horrible grinding sound as it scrapes along the floor.'
      answer = raw_input()
      if answer == 'push the wall back' or answer == 'push it back':
        print 'You push as hard as you can against the wall but it continues to slide forward.'
        print 'You desperately brace your back up against the wall and put your feet against the door, pushing with all of your might.'
        print "The wall halts for a second. It appears you've stopped its progress. You begin to relax, but then the wall starts closing in on the door again."
        print 'Your legs buckle under the insane amount of pressure the sliding wall is producing. You put your arms out to help your now bent legs and once again you'
        print "manage to stop the wall's death-march. However, the stop doesn't last long."
        print 'The wall ends its advance at the doorframe, blood leaks out into the hall and your quest comes to an unfortunately early end.'
        game_over()
      elif answer.find('quit') != -1 or answer == 'die':
        print "You give up on life, accepting your impending doom."
        print 'The wall ends its advance at the doorframe, blood leaks out into the hall and your quest comes to an unfortunately early end.'
        game_over()
      elif answer == 'run into the wall':
        print 'You lower your shoulder and run into the advancing wall as hard as you can.  You hear a loud pop and then an incredible pain.'
        print 'As your body slumps to the floor you can see blood trickling out of your arm.'
        print 'Everything begins fading away as you feel yourself sliding across the ground closer to the door.'
        print 'The wall ends its advance at the doorframe, blood leaks out into the hall and your quest comes to an unfortunately early end.'
        game_over()
      elif answer == 'holy brick wall i have a request of you on this day, please end my life as i cannot find a way out of this place...':
        print 'The brick wall grinds forward and grants your final wish.'
        print 'The Old Gods are pleased'
        game_over()
        raise SystemExit
      elif answer == 'scream':
        print 'You scream at the top of your lungs as the wall inches closer to you.'
        print 'The wall ends its advance at the doorframe, blood leaks out into the hall and your quest comes to an unfortunately early end.'
        game_over()
      elif answer == 'leav' or answer == 'leave' or answer == 'open the door' or answer == 'turn around':
        print 'You turn around to try and open the door, but there\'s no handle on this side!'
        print 'Frantically, you grasp at the sides of the door and try to pry it open, as you\'re working, you can hear'
        print 'the wall grinding closer. The wall touches your back, and slowly pushes you against the door.'
        print 'You continue flailing around, trying to escape, but you don\'t get to struggle long.'
        print 'The wall ends its advance at the doorframe, blood leaks out into the hall and your quest comes to an unfortunately early end.'
        game_over()
      else:
        print "I'm sorry I don't know that command."
        answer = answer + ' : '
        output_filename = 'inbrickwallerror.txt'
        output_file_obj = open(output_filename, 'a')
        output_file_obj.write(answer)
        output_file_obj.close()
        print 'You stand there dumbstruck, as the wall closes in.'
        print 'The wall ends its advance at the doorframe, blood leaks out into the hall and your quest comes to an unfortunately early end.'
        game_over()
    elif answer == 'find the hidden latch and enter' or answer == 'look for a hidden latch':
      print "You feel around the door but there doesn't seem to be a hidden latch anywhere."
      print "As you're searching for the hidden latch, the door closes on its own."
      start()
    elif answer == 'left door' or answer == 'go back to the door on the left':
      print 'You turn around and open the door behind you.'
      staircase()
    elif answer == 'walk':
      print 'Where would you like to walk? (the hall or the left door?)'
      start()
    elif answer == 'quit':
      quit()
    elif answer.find('ok') != -1:
      print 'As you watch the door closes itself.'
      start()
    elif answer.find('sit') != -1:
      sit()
      print "As you stand up, the door shuts on its own"
      hall()
    else:
      print "I don't know that response, sorry"
      answer = answer + ' : '
      output_filename = 'brickwallerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
      print "You stand there for a while, looking inside, and then the door closes itself."
      start()
#if player goes down the hall from start
def hall():
  print 'You stand in the hallway looking at all of the paintings on the walls.'
  while True:
    answer = raw_input().lower()
    if answer == 'the throne room' or answer == 'throne room' or answer == 'towards the throne room' or answer == 'door' or answer == 'walk to the door' or answer == 'kings room' or answer == 'go to the door' or answer == 'keep walking' or answer == 'i want to go through the door' or answer == 'kings door' or answer == 'door at the end of the hall':
      print "You approach the door and an inscription above it reads 'Only the worthy can enter the throne-room of King Ren!'"
      throne_door()
    elif answer == 'open the door':
      print "You approach the door and an inscription above it reads 'Only the worthy can enter the throne-room of King Ren!'"
      print "You try the handle, but the door doesn't budge."
      throne_door()
    elif answer == 'kick':
      print 'You kick the air in front of you, HI YA!'
      print 'pwned.'
    elif answer.find('two doors') != -1 or answer == 'go to where i started' or answer == 'walk back to the beginning':
      print 'You walk back over by the two doors you were originally by.'
      start()
    elif answer == 'walk down the hall' or answer == 'leave this place' or answer == 'walk down the hallway' or answer == 'go down the hall' or answer == 'walk':
      print 'Which way? Towards the throne room or towards the two doors?'
    elif answer == 'paintings' or answer == 'liik at eh paintings' or answer == 'look at paintings' or answer == 'look at the paintings' or answer == 'the good king' or answer == 'the king' or answer == 'pick a painting' or answer == 'choose a painting' or answer == 'realistic painting' or answer == 'who is in painting' or answer == 'see painting' or answer == 'look at all the paintings' or answer == 'look at painting' or answer == 'look at it':
      print 'You look at all of the paintings, many of them are portraits of kings and knights but a few are of other subjects. One in particular catches your eye titled "The Good King".'
      print "It is of King Ren, sitting at the head of a large table and smiling as his guests are served food. It looks so lifelike, almost as if someone froze that very scene and trapped"
      print "it within a canvas. You look for the artist's mark but oddly you can't find one."
      the_good_king()
    elif answer == 'what kind of paintings':
      print 'Many of them are portraits of kings and knights but a few are of other subjects.'
    elif answer == 'knight' or answer == 'knight painting':
      print 'You look through all the paintings of knights, each one has a small plaque below it indicating the knight\'s name.'
      print 'There\'s "Sir Balthazar", "Sir Edgar", "Sir Quill", "Sir Thain", and "Sir Aldrin"'
    elif answer == 'backflip'or answer == 'do a backflip':
      print 'You do an awesome, perfectly executed backflip.'
      print 'Nice!'
    elif answer == 'jog around':
      print 'You jog around the hall enthusiastically until you\'ve produced a substantial amount of sweat'
    elif answer == 'touch the paintings' or answer == 'reach into the painting':
      print "You walk forward to touch the paintings and one in particular catches your eye. It's titled " + '"The Good King"'
      print "It is of King Ren, sitting at the head of a large table and smiling as his guests are served food. It looks so lifelike, almost as if someone froze that very scene and trapped"
      print "it within a canvas. You look for the artist's mark but oddly you can't find one."
      the_good_king()
    elif answer == 'talk to the paintings' or answer == 'talk to the painting' or answer == 'talk':
      print 'You talk to all of the paintings for a long while. Telling them story after story. Some of them are quite funny and you find yourself laughing at them.'
      print 'Clarence, a painting to your right, seems to be a very good listener so you tell him all about your life and how you got there. He smiles at you.'
      print "After an hour or two you begin to realize that you're driving yourself insane. You're talking to paintings!"
      print ''
      print "You decide it's probably time to stop, you calm yourself down and then back up."
    elif answer == 'stop at the paintings':
      print 'You are stopped at the paintings.'
    elif answer == 'use a spell on the painting of the king' or answer == 'fireball' or answer == 'throw a fireball':
      print 'You charge up all of your magical energy and target it at the picture of the king.'
      print 'You throw your hand forward and yell "FIREBALL!!"'
      print 'A small spark shoots out of your hand and does nothing... oh well, it was worth a shot.'

    elif answer == 'talk to the king':
      print 'You walk up to "The Good King" and talk to the king for a while.'
      print "He doesn't respond."
      the_good_king()
    elif answer == 'scream at the king' or answer == 'yell at the king':
      print 'You yell at "The Good King" at the top of your lungs.'
      print "He is not amused, and doesn't respond."
      the_good_king()
    elif answer == 'talk to yourself':
      print 'You stand there muttering to yourself for a while. Your eyes gleam crazily and you begin to scream and laugh.'
      print "You've gone absolutely bonkers! You run around enjoying your mad self and manage to run into a wall."
      print 'That seems to knock you back into your senses. Jeeze, what were you thinking?'
    elif answer == 'key to door':
      print "What key to what door? You're standing in the middle of a hallway."
    elif answer == 'eat the food from the painting' or answer == 'eat food in painting':
      print 'Only one of the paintings has food in it, you walk up to "The Good King"'
      print 'You wonder if you should really try to eat the food on it.'
      the_good_king()
    elif answer == 'kick the painting' or answer == 'slap the painting':
      print "That's probably not a good idea."
    elif answer == 'remove the painting of the king':
      print 'You remove the picture from the wall and behind it is a large hole that you could easily fit through.'
      the_good_king_hole()
    elif answer == 'grab the good king and smash it against the ground':
      print 'The good king lays in pieces on the ground. The spot on the wall where it used to be has a large hole in it.'
      the_good_king_hole()
    elif answer == 'touch the key on the painting' or answer == 'find key on frame' or answer == 'find key behind frame':
      print 'You look for a key on any of the paintings but none of them have one.'
    elif answer == 'ask the king to make you worthy':
      print 'You walk up to "The Good King" to voice your request'
      the_good_king()
    elif answer == 'enchanted painting':
      print '"The Good King" appears to be a very odd painting, maybe ' + "it's enchanted!"
      print 'You walk up to it.'
      the_good_king()
    elif answer == 'open sesame':
      print 'You utter the magic incantation but nothing appears to happen.'
    elif answer == 'fight painting' or answer == 'fight the paintings':
      print 'You get into a battle stance and challenge the paintings to a fight.'
      print ''
      print 'None of them step up to fight, yellow-bellied cowards.'
    elif answer == 'run fingers over painting':
      print "That's bad for the oil in the paintings, we shouldn't do that."
    elif answer == 'poke king' or answer == 'poke the king' or answer == 'touch the king':
      print 'You walk up to "The Good King" with your finger ready to poke him.'
      the_good_king()
    elif answer == 'break spell on painting' or answer == 'wake up painting' or answer == 'help king':
      print '"The Good King" appears to be under some sort of spell, you try to break the spell with a little'
      print 'magic of your own. However, nothing happens.'
      the_good_king()
    elif answer == 'take king out of painting':
      print 'You go stand in front of "The Good King" and ponder how to get him out.'
      the_good_king()
    elif answer == 'move':
      print 'Move where?'
    elif answer == 'drop':
      print 'You drop to the ground, letting your legs swing out from under you. Ow, that hurt a bit.'
      print "You stand back up rubbing your back and butt, that wasn't the greatest idea ever."
    elif answer == 'serve king':
      print 'You kneel in front of "The Good King" and say, "I\'m" here to serve you my king.'
      print ''
      print 'Nothing happens'
      the_good_king()
    elif answer == 'straighten paintings':
      print 'All of the paintings are perfectly straight'
    elif answer == 'who is in the painting with the king':
      print 'You walk up to "The Good King" to get a better look at it.'
      print "Other than the king, you don't see anyone you recognize."
      the_good_king()
    elif answer == 'enter painting' or answer == 'step into painting':
      print "You can't really enter a painting..."
    elif answer == 'painting is important':
      print 'Is it?'
    elif answer == 'find the important painting':
      print "I don't know which one is important"
    elif answer == 'look at the king' or answer == 'king ren' or answer == 'good king' or answer == 'look for the king' or answer == 'go to the king' or answer == 'king':
      print 'You walk up to "The Good King"'
      the_good_king()
    elif answer == 'yell':
      print 'You yell and scream in the halls'
      print "Your screams echo satisfyingly off the stone walls of the hallway."
      print ''
    elif answer == 'right' or answer == 'go right':
      print 'There are many exquisite paintings to your right.'
    elif answer == 'turn my head':
      print 'You turn your head to the side...'
      print 'Huh, the pictures look kinda funny like this.'
    elif answer == 'poop':
      print 'You squat down to take a poop, you squeeze and squeeze but nothing comes out.'
      print 'Oh well. You stand back up.'
    elif answer == 'gay' or answer == 'fuck you bitch':
      print 'That\'s not very nice.'
    elif answer == 'turn into a midget':
      print 'You squat down and tuck your arms into your shirt.'
	#various nonspecific painting results
    elif answer.find('painting') != -1 or answer == 'touch frame':
      print 'What painting do you mean? There are tons!'
    elif answer == 'hallway':
      print "You're in the hallway."
    elif answer == 'worthy':
      print 'What?'
    elif answer == 'enter':
      print "There's nothing to enter here, you're standing in the hall."
    elif answer == 'read the sign':
      print 'Which sign?'
    elif answer == 'spit on it':
      print 'Spit on what?'
    elif answer == 'go back':
      break
    else:
      if defaults(answer) == True:
        continue
      print "I'm sorry I don't know that command"
      answer = answer + ' : '
      output_filename = 'hallwayerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#interesting picture on the wall
def the_good_king():
  while True:
    answer = raw_input().lower()
    if answer == 'yes' or answer == 'y':
      print "Ok, what do you want to do then?"
    elif answer == 'the good king':
      print "That is the title of this painting."
    elif answer == 'look at it some more' or answer == 'look at it' or answer == 'look at the painting':
      print 'Upon studying the picture further, you see that many of the guests are laughing and talking to one another but no one seems to be paying attention to the King. All the'
      print "servants are giving food to the guests first, and the bard playing his lute jovially is over near the end of the table. The king doesn't seem to mind though."
#insta-secret tunnel
    elif answer == 'go in' or answer == 'dive in' or answer == 'jump in':
      print 'You dive into "The Good King" the canvas rips open and you shoot into the hole in the wall behind the painting... good thing that was there.'
      secret_tunnel()

    elif answer == 'slash the painting' or answer == 'slash the painting to break the curse':
      print 'You slash the painting with your mighty fingers, it rips cleanly, creating four large holes in the canvas.'
      print 'Standing back slightly, you admire how monster-like those cuts in the painting look, and you notice how there\'s no wall'
      print 'that you can see through the holes. As you look closer, the rips begin to repair themselves, until the painting is whole again'
    elif answer == 'hit it' or answer == 'punch the king' or answer == 'punch it' or answer == 'punch it again':
      print "You punch right through the picture. You're thrown off balance by how easily your fist went through the canvas and you fall forward, ripping the rest of the picture."
      print "The top half of your body goes through the picture into a hole in the wall. You stand up, relieved that you didn't end up punching the wall. That would've sucked."
      answer = raw_input('What do you want to do now?').lower()
      if answer == 'climb in' or answer == 'climb through' or answer == 'go in' or answer == 'climb in the hole' or answer == 'go in the hole' or answer == 'in' or answer == 'climb inside':
        print 'You brush the remaining canvas out of the way, widening the gap in the wall.'
        secret_tunnel()
      elif answer == 'take it off the wall' or answer == 'move it' or answer == 'remove the picture':
        print 'You take the picture off the wall, revealing a large hole that you could easily climb through.'
        the_good_king_hole()
      else:
        print "You stand in front of the picture, admiring the destruction you've caused. As you watch, the painting begins to put itself back together, and before long, it's"
        print "back to it's original appearance."
        answer = answer + ' : '
        output_filename = 'punchkingerror.txt'
        output_file_obj = open(output_filename, 'a')
        output_file_obj.write(answer)
        output_file_obj.close()
    elif answer == 'talk to the king' or answer == 'talk to it' or answer == 'talk' or answer == 'talk to king ren':
      raw_input('What do you want to say?')
      print "The painting doesn't reply."
    elif answer == 'reach into picture' or answer == 'reach into the picture' or answer == 'open the picture':
      print 'You attempt to reach into the picture and your hand goes right through.'
      print "You pull your hand back and the hole in the painting begins to repair itself."
      print "You see that there's no wall behind the picture."
      print ''
    elif answer == 'step into the painting' or answer == 'step into it' or answer == 'step into the painting to join the king':
      print "Mesmerized by the life-like painting, you attempt to step in and you rip a rather large hole in the painting. You pull your foot back and you can see that there's"
      print 'a hole in the wall behind "The Good King". As you watch, the painting begins to repair itself and then returns to its original form.'
    elif answer == 'unfreeze the occupants of the painting' or answer == 'unlock the painting' or answer == 'unfreeze the painting' or answer == 'break the spell' or answer == 'untrap the painting':
      print 'You attempt to break the spell on the painting.'
      print 'Unfortunately, nothing happens.'
    elif answer == 'look for the bad king':
      print 'You look all along the wall for "The Bad King", but you don\'t find it.'
    elif answer == 'look for the painting of fruit':
      print 'You look around for a painting of fruit but can\'t find one.'
      print 'You return to looking at all the paintings in the hallway.'
      hall()
    elif answer == 'add an artists mark' or answer == "add an artist's mark":
      print "It would be terribly rude to take credit for someone else's work"
    elif answer == 'look closely' or answer == 'look closely at it' or answer == 'look closely at the painting of king ren':
      print 'You look closely at the picture and nothing seems out of the ordinary, but you can feel a slight draft coming from'
      print 'the edges of the frame and through the picture'
    elif answer == 'straighten the painting':
      print "It's already perfectly straight."
    elif answer == 'no' or answer == 'move to another painting' or answer == 'n' or answer == 'turn around' or answer == 'go back' or answer == 'leave' or answer == 'move':
      print 'You walk away from "The Good King"'
      break
    elif answer == 'who painted this' or answer == 'who is the artist':
      print 'You look over the entire painting for the mark of an artist but you can\'t find one anywhere.'
      print 'Whoever painted it was a master though.'
    elif answer == 'your magesty' or answer == 'bow':
      print 'You bow to the picture.'
      print 'It shimmers in acknowledgement.'
    elif answer == 'smiling' or answer == 'smile' or answer == 'smile at the picture' or answer == 'smile at the king':
      print 'You smile nicely at "The Good King"'
      print ''
    elif answer == 'it seems real':
      print 'Yes it does.'
    elif answer == 'king':
      print 'You look at the king, he looks happy.'
    elif answer == 'take it' or answer.find('move the') != -1 or answer == 'take the picture' or answer == 'take it off the wall' or answer == 'take the painting off the wall' or answer == 'look behind the painting' or answer == 'use the painting to open the door at the end of the hall' or answer == 'move it':
      print 'You remove the picture from the wall and behind it is a large hole that you could easily fit through.'
      the_good_king_hole()
    elif answer.find('touch') != -1 or answer.find('poke') != -1:
      print 'You put your hand up and slowly move it forward to touch the painting. As it reaches the canvas, suddenly the painting breaks and your finger goes right through.'
      print 'You pull your finger back and the hole it created slowly stitches itself back together.'
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "Terribly sorry I don't know what you mean"
      print 'You stare at "The Good King" blankly'
      answer = answer + ' : '
      output_filename = 'goodkingerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#player removes good king from wall
def the_good_king_hole():
  while True:
    answer = raw_input().lower()
    if answer == 'reach into the hole' or answer == 'take something out of the hole':
      print 'You reach out into the hole, other than the walls, you don\'t feel anything.'
    elif answer == 'put it back' or answer == 'put the good king back' or answer == 'put it back on the wall':
      print 'You put "The Good King" back on the wall.'
      the_good_king()
    elif answer == 'leave' or answer == 'left':
      print 'You walk away from "The Good King", leaving it on the floor.'
      hall()
    elif answer.find('in') != -1 or answer.find('enter') != -1 or answer.find('climb') != -1 or answer == 'fit through the hole' or answer == 'go through the hole' or answer == 'go to the hole':
      secret_tunnel()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "I'm sorry I don't quite understand what you want to do."
      answer = answer + ' : '
      output_filename = 'goodkingholeerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#player enters after removing the good king
def secret_tunnel():
  print 'You climb through the hole in the wall and crawl for about 20ft until you reach a split in the tunnel.'
  while True:
    answer = raw_input('right or left?').lower()
    if answer.find('right') != -1 or answer == 'r' or answer == 'rihgt':
      print "You follow the path to the right and the tunnel begins to widen out. Eventually you're able to stand up again."
      print 'Continuing to follow the tunnel, you come to a very plain looking wooden door. To the right of the door hangs a'
      print 'small sign that reads: "Feyndrin the Seer"'
      seer_door()
    elif answer.find('left') != -1 or answer == 'l':
      print 'You follow the path to the left and the tunnel begins to slope gradually down. You continue crawling and the slope gets steeper and steeper'
      print 'it becomes so steep that you start sliding down headfirst into whatever may be below.'
      print 'You try to slow yourself down by pushing against the walls with your hands and feet, but that does little to help decelerate your descent.'
      print 'The slope continues getting steeper...'
      print 'Suddenly, the floor drops out from under you and you begin falling into the darkness below!'
      print ''
      print ''
      print "You don't have much time to react as you're suddenly plunged, head first into ice-cold water."
      print 'The shock from the water prevents you from moving at first, and you sink further into the icy depths.'
      print 'Finally, you regain control of yourself.'
      cave_underwaterwater()
    elif answer.find('no') != -1:
      print 'You sit in the tunnel doing nothing.'
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'Please try again'
      answer = answer + ' : '
      output_filename = 'secrettunnelerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#player sits
def sit():
  print 'You sit down and contemplate the meaning of the universe... Why are you here, why are any of us here? Is it all for nothing? Or is there some meaning to it all?'
  answer = raw_input()
  if answer == 'nothing' or answer == 'there is no meaning':
    print 'Oh well, I guess there is no meaning to it all.'
    print 'You stand back up and prepare yourself to figure this place out. Even if it is meaningless, might as well have fun with the time you get.'
  elif answer == 'because' or answer == 'just because' or answer == 'because i feel like it' or answer == "i don't know":
    print "There doesn't have to be a reason for everything. Let's just drop it and carry on with the quest."
    print 'You stand back up, feeling refreshed after your short meditation.'
  elif answer == 'stand' or answer == 'stand up':
    print 'You stand up, feeling a little unfulfilled by your lack of universal knowledge...oh well.'
  elif answer == 'quit':
    quit()
    sit()
  else:
    print "I don't know how to respond to that."
    print 'You stand up, feeling a little unfulfilled by your lack of universal knowledge...oh well.'
    answer = answer + ' : '
    output_filename = 'siterror.txt'
    output_file_obj = open(output_filename, 'a')
    output_file_obj.write(answer)
    output_file_obj.close()
#all the way down the hall from the start
def throne_door():
  while True:
    answer = raw_input().lower()
    if answer == 'pound' or answer == 'pound on it' or answer == 'pound on the door':
      print 'You pound on the door ferociously...'
      print 'As you wait for a response, your hand throbs a little bit.'
      print ''
      print "Sadly, there's no response."
    elif answer == 'feel on the door for a secret latch' or answer == 'feel on the wall for a secret latch':
      print 'You feel all over for a secret latch, but you can\'t seem to find one.'
    elif answer == 'kick it' or answer == 'kick the door' or answer == 'kick the door again':
      print 'You bring your leg back and then swing it forward, hitting the door with a solid kick. It makes a resounding thud off of the thick wooden surface,'
      print 'and a sharp pain shoots up your leg.  You hobble around for a little bit. The pain subsides and you return to the door.'
    elif answer == 'punch it' or answer == 'punch' or answer == 'punch the door':
      print "You wind up for a punch and the thought crosses your mind that this might not be a good idea, but oh well. You throw a punch with perfect form and"
      print "land a solid hit right on the center of the door.  You're amazed by how perfect that punch was and then you realize that your fist is throbbing."
      print "As you pull it away from the door you see that your knuckles are bruised and they hurt pretty bad. You shake your hand to help ease the pain"
      print "You return to the door."
    elif answer == 'push on it' or answer == 'push on the door' or answer == 'push the door':
      print "You push on the door but it doesn't budge"
    elif answer == 'find a hidden key' or answer == 'locate a hidden key':
      print 'You search all around the door for a hidden key but there are none to be found.'
    elif answer == 'poop' or answer == 'pooop' or answer == 'poooop':
      print "You poop in your pants...wow, that's not a good feeling." 
    elif answer == 'how do i become worthy?' or answer == 'tell the door to open' or answer == 'how do i become worthy' or answer == 'how do i get in?' or answer == 'how do i get in' or answer == 'what do i do to enter?' or answer == 'make me worthy' or answer == 'what makes me worthy':
      print 'The door has no response for you, it is a door after all.'
    elif answer == 'am i willing it to open' or answer == 'am i willing it to open?':
      print "It appears so, and the door isn't budging... unfortunately."
    elif answer == 'use my cell phone to call someone inside and tell them to open the door':
      print "What's a cell phone?"
    elif answer == 'check for a peep hole':
      print "You search all over the door for a peep hole, but don't find one."
    elif answer == 'use an axe on the door' or answer == 'use an ax on the door' or answer == 'hit the door with an axe' or answer == 'hit the door with an ax':
      print 'You whip out your greataxe from its sheathe on your back and start going to work on the door, chopping everything in sight.'
      print ''
      print "Ten minutes later you regain your composure and realise that you don't have an axe, you were just waving your shirt around and hitting the door"
      print "with it as if you'd gone mad.  Good thing no one was around to see that."
    elif answer == 'call your friend inside to open the door':
      print 'You call out to your friend Dave to open the door!'
      print ''
      print ''
      print "I guess Dave didn't hear you"
    elif answer == 'i want the door to open':
      print "Don't we all?"
    elif answer == 'breathe on the door':
      print 'You stand about an inch away from the door, breathing right on it.'
      print "Once you're satisfied that it's learned its lesson, you back away."
      print "That'll teach a door to mess with you."
    elif answer == 'spit on the door' or answer == 'spit on it':
      print 'You spit on the nice shiny door.'
      print "That'll show 'im"
      print 'You watch as the spit drips to the ground.'
    elif answer == 'is there a secret knock for the door?' or answer == 'is there a secret knock':
      print "Possibly, but you don't know it if there is one."
    elif answer == 'ajar':
      print "No, it's a door"
    elif answer == 'unlock the door' or answer == 'use the key on my belt' or answer == 'unlock it' or answer == 'unlock':
      print "You don't have a key."
    elif answer == 'i am worthy':
      print "If you were, the door would open for you."
    elif answer == 'try again':
      print 'Try what again?'
    elif answer == "well that's stupid":
      print "What did you expect? It's a door."
    elif answer == 'maybe its not a door' or answer == "maybe it's not a door":
      print 'Maybe not'
    elif answer == 'yell' or answer == 'yell at it' or answer == 'yell at the door' or answer == 'yell open':
      print 'You yell and scream at the door.'
      print 'The door has no response for you.'
      print ''
    elif answer == 'touch the door' or answer == 'touch door':
      print 'You touch the door, it\'s made of excellently polished wood, gilded with iron.'
    elif answer == 'good king':
      print 'The good king isn\'t here.'
    elif answer.find('open sesame') != -1:
      print 'As you utter the ancient incantation of opening, the hall begins to shake! You hear rumbling in all of the walls and the door starts to glow.'
      print 'You begin to congratulate yourself on your utter genius and suddenly everything stops.'
      print 'The door returns to its original state and nothing else happens.'
    elif answer.find('open') != -1 or answer == 'try the handle' or answer == 'go into the room' or answer == 'go in the room' or answer == 'go in':
      print "You try the handle but the door doesn't budge."
    elif answer.find('knock') != -1 or answer == 'wrap on the door' or answer == 'wrap on it':
      print "You knock on the door. It's made of very solid, thick wood.  You stand there for a while but your knock goes unanswered."
    elif answer == 'turn around and go right':
      print 'You turn around, walk down the hall and go to the door on the right'
      staircase()
    elif answer.find('go back') != -1 or answer == 'goback' or answer.find('paintings') != -1 or answer == 'turn around' or answer.find('leave') != -1 or answer.find('hall') != -1:
      print 'You walk back down the hall, passing the paintings again.'
      break
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "I'm sorry I don't know that command."
      answer = answer + ' : '
      output_filename = 'thronedoor_error.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
      print ''
      print 'You stand in front of the door for a while, staring at it.'
#if the player opens the seer_door add a library of books to the seers room that the player can read
def seer():
  while True:
    answer = raw_input().lower()
#questions to/about feyndrin
    if answer.find('how did you know i was coming') != -1 or answer.find('what do you know') != -1 or answer == 'how did you know':
      print 'I know a great many things. I knew you were going to arrive here long ago, before this castle had fallen to this treacherous curse.'
    elif answer == 'why are you here':
      print 'I forsaw you coming to this place long ago, and have been waiting for you ever since.'
    elif answer.find('why am i here') != -1:
      print 'You have been brought here to rid this castle of its curse!'
    elif answer == 'why are you waiting for me' or answer == 'waiting' or answer == 'why have you been waiting for me':
      print 'Only you can break the curse ' + player_name
      print 'I just had to wait for you to arrive'
    elif answer == 'wait for what' or answer.find('why') != -1 and answer.find('waiting') != -1:
      print 'For you! Of course!'
      print 'Only you can break the curse ' + player_name
    elif answer == 'what are you doing here':
      print "I'm here to help you on your quest"
    elif answer == 'how can you help me' or answer == 'how can you help me?':
      print 'I can try and answer any questions you may have.'
    elif answer == 'what are you going to do now?':
      print "I'll be here to answer any questions you may have, but I'm afraid this poor old body won't permit me to adventure around the castle with you."
    elif answer == 'how did you get here?' or answer == 'how did you get here':
      print 'I came back here to hide from the warlock who cursed this place'
    elif answer == 'who are you':
      print 'I am just an old Seer.'
      print 'My name is Feyndrin.'
      print "I'd say by now, I'm about 167 years old, give or take about 5 years."
      print "I'm here to aid you on your quest...but I can only sit here and answer questions."
    elif answer == 'what is a seer' or answer == "what's a seer":
      print 'A seer is a person who can see into the future, usually they also'
      print 'have magical capabilities.'
    elif answer == 'why cant you understand me' or answer == "why can't you understand me":
      print 'I can understand you perfectly fine.'
    elif answer == 'how did you forsee it?' or answer == 'how did you forsee it':
      print 'I am a seer, I was born with the gift of being able to see events that will occur in the future.'
    elif answer == 'what is your name':
      print 'My name is Feyndrin'
    elif answer == 'youve been waiting for me?' or answer == "you've been waiting for me?" or answer == 'youve been waiting for me' or answer == "you've been waiting for me" or answer == 'you have?':
      print "Yes, I knew you'd be here at some point, I just had to wait for you."
    elif answer == 'who can help me':
      print 'I can try to answer any question you may have.'
      print "Other than that, I don't think you'll have much help elsewhere in the castle."
    elif answer == 'how long' or answer == 'how long have you been waiting' or answer == 'how long?' or answer == 'how long have you been waiting for me?' or answer == 'for how long':
      print 'It has been many years now.'
      print 'Many, many years...'
      print ''
      print 'The Seer closes his eyes and bows his head in silence, and then looks back up at you.'
      print "Now you're here! And I shall wait no longer!"
    elif answer == 'im tired of waiting':
      print 'Are you?'
    elif answer == 'excuse my language' or answer == 'excuse my language feyndrin':
      print 'Excused.'
    elif answer == 'thank you' or answer == 'thanks':
      print 'Feyndrin smiles at you and nods his head'
      print "You're welcome."
    elif answer == 'hello':
      print 'Hello'
    elif answer == 'is your mom hot':
      print 'Is yours?'
#odd dude answers
    elif answer == 'hey dude' or answer == 'hey dude ':
      print 'WASSUP!?!?!'
    elif answer == 'good move dude':
      print 'Thanks bro'
    elif answer == 'hey, dude why am i here' or answer == 'dude why am i here':
      print 'Bro, you have to like lift the curse on the castle man!'
    elif answer == 'dude' or answer == 'dude bro' or answer == 'bro':
      print 'Duuude...'
    elif answer.find('are you tripping') != -1 or answer.find('are you drunk') != -1:
      print 'Unfortunately I am not'
#seer's room
    elif answer == 'explore' or answer == 'explore the room' or answer == 'look around' or answer == 'look around the room':
      print 'You get up from the table and explore the seer\'s room, there is a small bed in the corner but the majority of the room is taken over by heaps upon heaps of books.'
      print 'Behind the large stacks you can see some bookshelves sticking out.'
      print 'You can see the seer\'s name written on many of them.'
      print 'You conclude your exploration of the room, back at the table across from where the seer is seated and reclaim your own seat.'
      print 'Feyndrin smiles at you as you sit down and says, "It\'s not much but it\'s home."'
    elif answer == 'flip the table' or answer == 'i flip the table' or answer == 'flip the table over':
      print 'You grab the edges of the table with a mischievious gleam in your eye.'
      print "You attempt to flip the table over with all of your might, but sadly, it's attached firmly to the ground."
      print 'Feyndrin looks at you oddly, not understanding what you\'re trying to do.'
      print ''
#bookshelves
    elif answer == 'check out the bookshelves':
      print 'They look pretty good.'
    elif answer == 'what is in the bookshelves':
      print 'Books are in the bookshelves.'
    elif answer == 'read a book' or answer == 'pick up a book':
      print "You pick up a book and attempt to read it, but all of the letters seem to blend into each other. Then you realize, you can't read."
      print 'It was a miracle that you were able to somehow make out what the signs have said so far. Dang, maybe you should\'ve paid more attention in school.'
#crystal ball
    elif answer == 'touch the crystal ball' or answer == 'touch the ball' or answer == 'look into the crystal ball' or answer == 'look at the crystal ball':
      print 'You reach forward and touch the crystal ball, smoke swirls around inside. You begin to see shapes and figures moving within the smoke.'
      print 'Every time you try to focus on one, it fades back into the smoke, almost as if it\'s unwilling to show you exactly what scene you are looking at.'
      print 'You take your hand off the ball and look up to see Feyndrin watching you.'
      print '"Quite mystifying isn\'t it? Unfortunately, only a seer like myself can make any sense of what\'s happening within the depths of the ball."'
      print ''
    elif answer == 'i eat the crystal ball' or answer == 'eat the crystal ball':
      print "You grab the crystal ball off the table hungrily. You attempt to bite it, but it won't fit in your mouth."
      print "The seer eyes you curiously, and you realize how much of a fool you just made of yourself."
      print 'You set the ball back down and mutter "sorry..."'
      print 'Feyndrin chuckles to himself and replies, "It\'s quite alright young one."'
      print ''
    elif answer == 'poke the ball' or answer == 'poke the crystal ball':
      print 'You poke the floating crystal ball and watch as the gasses inside swirl around'
#fortune/quest related
    elif answer == 'tell my fortune' or answer == 'why me' or answer == 'who will lift the curse':
      print 'I forsaw you coming to this place long ago, in a dream'
      print 'Our great kingdom had fallen into a slumber.'
      print 'All of it\'s inhabitants sit in the great hall of the castle, frozen in time'
      print 'Years would pass, and the kingdom would continue it\'s unnatural sleep.'
      print ''
      print 'Until an adventurer who had lost their way wakes up within the slumbering palace.'
      print 'That adventurer is destined to break the curse that befell the kingdom.'
      print 'You are the adventurer of which I speak, and now it is time for my kingdom to wake from it\'s nap'
      print ''
    elif answer == 'what should i do' or answer == 'what am i supposed to be doing' or answer == 'what do i do' or answer == 'send me on my first mission' or answer == 'what should i do next' or answer == 'where should i go':
      print "You need to find a way to get into the throne-room. Be it through the king's door, or by some alternative method."
      print 'That is your goal.'
      print 'Simply exploring the castle may allow you to find your way.'
      print ''
    elif answer == 'what quest' or answer == 'my quest' or answer == 'quest' or answer == 'what is my quest':
      print "Your quest is to break the curse on this castle."
#hall of paintings questions
    elif answer == 'paintings' or answer == 'paintngs':
      print 'What about the paintings?'
#king_door(throne room) questions
    elif answer == 'what tests must i do to become worthy' or answer == 'how do i aquire these traits' or answer == 'what do i do to become worthy' or answer == 'how do i prove my worthiness' or answer == 'what do i need to accomplish to become worthy' or answer == 'how do i prove myself':
      print 'The seer stares at you for a moment, thinking about how to respond.'
      print ''
      print "I'm not sure what needs to be done to make yourself worthy of the kings door, however I expect whatever trials you come across"
      print "as you explore this castle will test your attributes."
      print 'I believe the best thing you can do is to simply explore, and you may find the challenges you seek along the way.'
    elif answer == 'who is worthy' or answer == 'whois worthy' or answer == 'how do i become worthy' or answer == 'what makes worthy' or answer == 'what does worthy mean':
      print "I assume you're talking about the inscription over the throne-room door."
      print 'To be worthy, one must have all of the traits that a king must have:'
      print 'Courage, Honor, Perserverance, and a Strong Sense of Righteousness'
    elif answer == 'what is a strong sense of righteousness':
      print 'The ability to be able to tell what is right and what is wrong, even in the most difficult decisions.'
    elif answer == "how do i get in the throne room" or answer == 'how do i get into the throne room' or answer == 'how do i get to the throne':
      print ''
      print "I'm not entirely certain..."
      print "If you can't get through the King's Door, then you either have to obtain the traits of a king, or find some alternative means of entry."
    elif answer == 'thrown room' or answer == 'throne room' or answer == 'throne':
      print "You can get into the King's Throne Room through the King's Door"
      print "I bet there are some other ways in as well."
    elif answer == 'i am worthy' or answer == 'i am worthy!!!' or answer == 'am i worthy':
      print 'Are you?'
      answer == raw_input().lower()
      if answer == 'yes' or answer == 'y' or answer == 'of course':
        print 'Well go get the kings crown from the throne room then, what are you waiting for?'
      elif answer == 'maybe':
        print 'Go check to see if the King\'s door will open for you, if not, you\'re not worthy yet.'
      elif answer == 'are you':
        print "I don't believe so, I'm not courageous enough."
      else:
        print 'ok'
        answer = answer + ' : '
        output_filename = 'seerworthyerror.txt'
        output_file_obj = open(output_filename, 'a')
        output_file_obj.write(answer)
        output_file_obj.close()
    elif answer.find('traits of a king') != -1 or answer == 'the worthy traits':
      print 'Ah yes,'
      print 'The traits of a king are Courage, Honor, Perserverance, and a Strong Sense of Righteousness'
      print ''
#crown stuff
    elif answer == 'how do i get the royal crown' or answer == 'how to get crown' or answer == 'crown room' or answer == 'where is the crown' or answer == 'where do i get the crown' or answer == 'how do i get the crown':
      print "The King's Royal Crown sits on the seat of his throne."
      print 'You just have to find a way into the throne room to get it.'
    elif answer == 'is the crown lost':
      print 'No, the crown rests in the throne room of the king.'
    elif answer == 'crown' or answer == 'the crown' or answer == 'royal crown':
      print "The King's Royal Crown sits on the seat of his throne."
    elif answer == 'why is the crown not with its owner':
      print "The warlock took the kings crown and put it in the throne room when he"
      print 'put the castle under its curse'
#hole related questions
    elif answer == 'how do i get thrown into the hole':
      print 'You don\'t want to get thrown in the hole'
    elif answer == 'what is the hole in the dungeon ledger' or answer == 'punishment of the hole' or answer == 'wht is the hole' or answer == 'what punishment is the hole' or answer == 'tell me about the punishment called the hole' or answer == 'what is the punishment called te hole' or answer == 'what is the punishment called the hole' or answer == 'what is the hole in the dungeon' or answer == 'what is the dungeon hole' or answer == 'what is the hole punishment' or answer == 'what is the hole in the dungeon punishment' or answer == 'what is the hole' or answer == 'hole in the dungeon ledger' or answer == 'the hole' or answer == 'what does the hole mean in the dungeon ledger':
      print '"The Hole" was a punishment the dungeon keepers used for the most notorious, or the most troublesome occupants of the dungeon. If an inmate fell into either of those'
      print 'catagories, one of the dungeon officers would come in the middle of the night and take the inmate out of their cell. They would walk them into the main room and then'
      print 'guide them over to the hole in the dungeon wall. The officer would drop a torch down onto one of the ledges and then allow the inmate to collect it to aid them in the'
      print 'rest of their descent. They were instructed that they had to walk until their torch ran out, and collect some water from an ice cold lake with a bucket that was thrown'
      print "down to them. I've never heard of anyone making it back. No one knows what dwells in that cave, but I suspect the torchlight draws them or it in."
      print ''
      print 'Most inmates knew not to try and fight the officers when they were about to go to "The Hole". If they did that, instead of climbing down they would find themselves hurled'
      print 'into the darkness below.  Although since none of them ever make it back anyway, I wonder if that might be the better fate to choose, over being killed by whatever dwells'
      print 'within the heart of that cavern.'
    elif answer == 'what dwells in the hole' or answer == 'what is in the cavern' or answer == 'what dwells int he heart of the cavern' or answer == 'what dwells in the heart of the cavern' or answer == 'what lurks in the cavern' or answer == 'what is in the hole' or answer == 'what dwells in the cavern' or answer == 'cavern dweller':
      print "I'm not entirely sure, but I do know that it, or they are dark and twisted beings."
    elif answer == 'how do i escape the hole':
      print 'If you ever had the misfortune of going into the hole, you\'d have to find your way to the crack in the dungeon wall somehow, and then climb out.'
    elif answer == 'do i go through the hole':
      print 'I wouldn\'t reccomend it.'
#dungeon questions
    elif answer == 'how do i escape the dungeon':
      print 'I don\'t know of anyone escaping the dungeon, and you shouldn\'t have to worry about that considering the guards are all frozen in the great hall.'
    elif answer == 'will i be thrown into the dungeon':
      print 'Doubtful, the guards are all frozen in the great hall, and once the curse is broken, you will be a hero!'
    elif answer == 'where is the dungeon':
      print 'The dungeon is almost directly opposite to where we are in the castle.'
    elif answer == 'what is in the dungeon':
      print 'Usually there are criminals in the dungeon, but I suspect none of them have survived since the castle was cursed.'
    elif answer == 'dungeon' or answer == 'what is the dungeon' or answer == 'the dungeon' or answer == 'tell me about the dungeon':
      print "There is only one dungeon in this castle, it's had many occupants over the course of its life."
      print 'We pride ourselves on being the most fair castle in the entire world when it comes to our dungeon.'
      print 'Where other kingdoms would throw someone in the dungeon almost indefinitely for any crime, we incorporate other'
      print 'punishments and keep our dungeon sentences as short as they should be.'
#grand hall questions
    elif answer == 'how do i enter the hal' or answer == 'how do i enter the hall':
      print 'The Grand Hall should be just up the staircase on the door to the left of where you entered this place.'
      print "Although, the warlock may have placed some spell on it to prevent you from entering, there must be an alternative"
      print 'entrance somewhere. There are all sorts of tunnels for the servants in this castle, maybe one of those leads to the hall.'
#curse stuff
    elif answer == 'how do i rid the castle of its curse' or answer == 'how is the curse broken' or answer == 'how do i rid the castle of the curse' or answer == 'how will the curse be broken' or answer == 'break the curse' or answer == 'rid the castle of the curse' or answer == 'how do i break the curse' or answer == 'how do i undo the curse' or answer == 'how do i wake up the castle':
      print "You must return the royal crown to the king."
    elif answer.find('curse') != -1:
      print ''
      print 'Many years ago, a young, but very powerful warlock arrived. He entered the castle and demanded to see the king.'
      print 'King Ren cancelled all of his duties for the day to see the young warlock as soon as he could and provide enough time to see what the warlock wanted.'
      print 'I could not see what happened during that meeting, but I do know that afterward, the warlock left and the king seemed more happy than'
      print 'anyone had ever seen him before.'
      print ''
      raw_input()
      print 'Days later, the warlock reappeared, armed with a blank canvas and a cart full of oil paints.'
      print 'He went into the throne room with the king and minutes later a feast was announced. Everyone in the kingdom was invited to attend.'
      print 'The great hall of the castle was quickly remodeled to host the residents of the kingdom and all the chefs in the land were gathered up and sent to the kitchen.'
      print 'Townsfolk and nobles began filing into the hall, excited for the feast.'
      print ''
      raw_input()
      print 'A few chosen gaurds helped everyone get to the hall and made sure that no one in the kingdom missed this tremendous event. It was the King\'s will after all.'
      print 'Once everyone had arrived and packed themselves into the hall, the king made a grand toast to the health of the kingdom and everyone in it.'
      print 'The servants began to bring food out to the tables, and then suddenly a huge wave of magical energy washed over the crowd, freezing them in their places.'
      print "The warlock stood in the corner of the room and made his masterful painting of the scene, he took his time with it too."
      print ''
      raw_input()
      print 'Once he had finished, he walked down the steps to the hall of paintings and placed his picture in the center.'
      print 'Little did he know that the hole he covered with his painting led to my hiding place.'
      print 'As he laid the picture down and placed his final enchantments on this castle, he said:'
      print "The hall will remain frozen until someone worthy enters the king's throne room, and brings the royal crown to its owner." #make this a better riddle at some point
      print ''
      print 'That is all'
#warlock questions
    elif answer == 'meet warlock':
      print "He left after he placed the curse,"
      print "unfortunately I never learned his name or"
      print "where he went."
      print ''
#anti seer responses (some violent)
    elif answer == 'punch him in the face' or answer == 'punch him' or answer == 'punch feyndrin':
      print 'You stand up, lean over the table, grab Feyndrin by his robes'
      print 'and pull your fist back. His eyes open wide as it begins its'
      print 'advance. Almost in slow motion, your knuckles meet the corner of'
      print 'his cheekbone. You hear a loud snapping sound'
      print 'Suddenly, your hand halts its progress.'
      print 'His eyes, now glowing, two brilliant purple lights in the darkness'
      print 'stare straight at you.'
      print '"Apparently I was mistaken. You are not the chosen one."'
      print ''
      game_over()
    elif answer == 'i hate you':
      print "Well that's unfortunate, I'm your only help."
#vague questions/things that would be used in normal conversation, but poor old Feyndrin has horrible short term memory
    elif answer == 'what happened?' or answer == 'what happened' or answer == 'explore the punishments' or answer == 'tell me about the punishment':
      print 'What do you mean?'
    elif answer == 'do they eat humans' or answer == "i don't even know what he is" or answer == 'are they dangerous' or answer == 'that is me':
      print 'Who?'
    elif answer == 'nope' or answer == 'k':
      print 'Ok.'
    elif answer == 'hallway':
      print 'There are many hallways in the castle.'
    elif answer == 'help me':
      print 'What do you need help with?'
    elif answer == 'how does that happen':
      print 'How does what happen?'
    elif answer == 'how do i accomplish that task':
      print 'What task?'
    elif answer == 'what now' or answer == 'where do i start' or answer == 'is there anything else i need to know' or answer == 'what next' or answer == 'what else' or answer == 'what then':
      print "I'm not sure, that's up to you to decide."
    elif answer == 'you stupid old seer just tell me how to get into the room':
      print "*the Seer ignores your childish remark"
      print 'What room?'
    elif answer == 'then' or answer == 'pass' or answer == 'next' or answer == 'ah' or answer == 'have you' or answer == 'show me' or answer == 'into the hole' or answer == 'tell me' or answer == 'how':
      print '...'
      print 'What?'
    elif answer == '':
      print 'Do you have anything else to ask me?'
    elif answer == 'i have the traits':
      print 'What traits?'
    elif answer == 'yes':
      print 'Indeed.'
    elif answer == 'how do i do that' or answer == 'how do i do that?' or answer == 'how do i edo that':
      print 'Do what?'
    elif answer == 'what can i use':
      print "What can you use for what?"
    elif answer == 'who can i help':
      print "By breaking the curse you'll be helping everyone in the kingdom!"
    elif answer == 'who can i fight':
      print "I don't think you'll run into anything you need to fight in these halls."
    elif answer == 'can you make me a steak':
      print 'Sadly, I don\'t have any steak. Sorry.'
    elif answer == 'really' or answer == 'really???':
      print 'Really really.'
    elif answer == 'what is drawn to the light':
      print 'Moths are drawn to light, and so are many other bugs.'
    elif answer == 'sit' or answer == 'sit down':
      print "You're already sitting across from the seer."
    elif answer == 'okey dokey':
      print 'Artichokey'
    elif answer == 'it does?':
      print ''
      print 'What does?'
    elif answer == 'why' or answer == 'but why' or answer == 'whhy':
      print 'Why what?'
    elif answer == 'let me in':
      print 'To where?'
    elif answer == 'no?' or answer == 'no':
      print 'no what?'
    elif answer == 'fine' or answer == 'just fine':
      print 'and dandy'
    elif answer == 'who holds the key':
      print 'The key to what?'
    elif answer.find('grr') != -1:
      print 'GRRR!'
    elif answer == 'how do i explore' or answer == 'how do i explore the castle':
      print 'You just have to explore. I don\'t know how to explain it any better than that.'
    elif answer.find('thanks') != -1:
      print "You're very welcome"
#leaving the seer's room
    elif answer.find('leave') != -1 or answer == 'explore castle' or answer == 'go back' or answer.find('bye') != -1 or answer == 'stand':
      print 'You say goodbye to the wise old Seer. He gives you a nod, and then puts his chin to his chest as if he fell asleep.'
      print 'You walk out of his room, open the door, and walk back out into the hallway you were in before you climbed in the hole.'
      start()
    elif answer == 'i am ready':
      print 'Ok, good luck'
      print 'You say goodbye to the wise old Seer. He gives you a nod, and then puts his chin to his chest as if he fell asleep.'
      print 'You walk out of his room, open the door, and walk back out into the hallway you were in before you climbed in the hole.'
      start()
#error
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "The Seer stares at you blankly. It seems as if he didn't understand what you said."
      answer = answer + ' : '
      output_filename = 'seererror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#if the player goes right in the secret tunnel
def seer_door():
  while True:
    answer = raw_input().lower()
    if answer.find('enter') != -1 or answer.find('in') != -1 or answer.find('open') != -1:
      print 'You walk up to the door and push it open.'
      print 'Inside, the room is dimly lit, and you can see a figure sitting at a table with a crystal ball floating over it.'
      print 'You feel compelled to walk up to the table and take a seat.'
      print "As you sit down, the figure's details become more clear to you and you can see a wrinkled face and gleaming purple eyes."
      print "The old man stares at you for a while and then says:"
      print ''
      print '"Welcome ' + player_name + ' I\'ve been waiting for you for quite some time."'
      seer()
    elif answer.find('knock') != -1:
      print 'You walk up to the door and knock on it.'
      print 'The door slowly opens by itself.'
      print 'Inside, the room is dimly lit, and you can see a figure sitting at a table with a crystal ball floating over it.'
      print 'You feel compelled to walk up to the table and take a seat.'
      print "As you sit down, the figure's details become more clear to you and you can see a wrinkled face and gleaming purple eyes."
      print ''
      print "The old man stares at you for a while and then says:"
      print ''
      print '"Welcome ' + player_name + ' I\'ve been waiting for you for quite some time."'
      seer()
    elif answer == 'no':
      print 'Ok?'
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'Apologies ' + player_name + " I'm not familiar with that word."
      answer = answer + ' : '
      output_filename = 'seerdoorerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
      print 'You remain standing outside the seer\'s door.'
#if the player goes left in the secret tunnel
def cave_underwaterwater():
  answer = raw_input().lower()
  if answer == 'float':
    print 'You calmly try float and begin rising towards the surface.'
    print 'It seems like an eternity passes and you just continue floating up.'
    print 'Right as your breath is about to run out, you breach the surface.'
    print 'You open your eyes and see nothing... have you gone blind, or is it just dark in here?'
    cave_water()
  elif answer == 'explore':
    print 'You attempt to explore the icy waters.'
    print 'As you swim along, the termperature seems to drop even further.'
    print 'The cold sets in, and all of your muscles begin to lock up.'
    print 'You begin to see spots and finally you fall victim to hypothermia.'
    print ''
    game_over()
  elif answer.find('down') != -1:
    print 'You attempt to swim downward.'
    print 'As you get deeper and deeper into the icy water, the termperature seems to drop even further.'
    print 'The cold sets in, and all of your muscles begin to lock up.'
    print 'You begin to see spots and finally you fall victim to hypothermia.'
    print ''
    game_over()
  elif answer.find('surface') != -1 or answer.find('up') != -1:
    print ''
    print 'You quickly swim towards the surface, you went down a lot farther than you thought you did.'
    print 'You begin to see spots as your body begins to be deprived of oxygen.'
    print "Finally you break the surface of the water."
    print 'You open your eyes and see nothing... have you gone blind from the shock?!?'
    cave_water()
  elif answer.find('quit') != -1:
    print 'You decide to give up on life.'
    print 'You let all the oxygen out of your lungs and take a nice, deep breath of'
    print 'ice cold water.'
    game_over()
  else:
    print "Whatever you wanted to try doesn't work. You die in the pitch black, icy water."
    answer = answer + ' : '
    output_filename = 'caveunderwatererror.txt'
    output_file_obj = open(output_filename, 'a')
    output_file_obj.write(answer)
    output_file_obj.close()
    raise SystemExit
#if the player manages to make it to the surface add a counter to see how long they stay in the water and if its above a certain point, they don't make it out
def cave_water():
  print 'You float on the surface of the icy water'
  while True:
    answer = raw_input().lower()
    if answer == 'swim to wall' or answer == 'find the wall':
      print 'You try to swim in the direction of where the wall might be.'
      print 'As your muscles begin to tire and lock up from the cold, you begin to sink.'
      print 'Your leg cramps and you stick it straight out, luckily you feel solid ground.'
      print 'You manage to get yourself to the shore.'
      print 'Soaking wet and freezing, you enjoy laying on the luke-warm rocks for a short amount of time'
      print ''
      print 'You just lay there for a while, happy that you survived.'
      print "After you've recovered sufficiently, you get up"
      print "You still can't see anything, it must be pitch black in here."
      print "At least the room is somewhat warm, but the cold water that's still in your clothes keeps you from enjoying it."
      cave()
    elif answer == 'can i touch the bottom':
      print "Considering you just had to swim a long ways to the surface, and you're freezing, it might not be a good idea to try and touch the bottom."
    elif answer == 'float' or answer == 'float to the right':
      print "You continue floating on the icy water, it's freezing"
    elif answer == 'freezing':
      print 'Yes, you are.'
    elif answer == 'swim forward' or answer == 'swim left' or answer == 'swim right' or answer == 'swim back':
      print 'You swim for a while.'
      print 'As your muscles begin to tire and lock up from the cold, you begin to sink.'
      print 'Your leg cramps and you stick it straight out, luckily you feel solid ground.'
      print 'You manage to get yourself to the shore.'
      print 'Soaking wet and freezing, you enjoy laying on the luke-warm rocks for a short amount of time'
      print ''
      print 'You just lay there for a while, happy that you survived.'
      print "After you've recovered sufficiently, you get up"
      print "You still can't see anything, it must be pitch black in here."
      print "At least the room is somewhat warm, but the cold water that's still in your clothes keeps you from enjoying it."
      cave()
    elif answer.find('swim') != -1 or answer == 'sim' or answer == 'find the shore' or answer == 'find land':
      print 'You pick a random direction and attempt to find land.'
      print 'As your muscles begin to tire and lock up from the cold, you begin to sink.'
      print 'Your leg cramps and you stick it straight out, luckily you feel solid ground.'
      print 'You manage to get yourself to the shore.'
      print 'Soaking wet and freezing, you enjoy laying on the luke-warm rocks for a short amount of time'
      print ''
      print 'You just lay there for a while, happy that you survived.'
      print "After you've recovered sufficiently, you get up"
      print "You still can't see anything, it must be pitch black in here."
      print "At least the room is somewhat warm, but the cold water that's still in your clothes keeps you from enjoying it."
      cave()
    elif answer.find('sit') != -1:
      print "You're swimming, you can't sit."
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'no compredo amigo'
      answer = answer + ' : '
      output_filename = 'cavewatererror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#if the player gets to the shore, add fedolio's body somewhere... player may need to come back with a torch, make this area more scary in general
def cave():
  while True:
    answer = raw_input().lower()
    if answer == '':
      print 'You stand still'
    elif answer == 'look around':
      print 'You look around you but can\'t manage to see anything. It\'s pitch black in here.'
    elif answer == 'rock':
      print 'There are rocks littered on the ground, it\'s very bumpy.'
    elif answer == 'pick up a rock':
      if player_inventory['pocket'] == 'empty':
        print 'You pick up a rock and put it in your pocket'
        player_inventory['pocket'] = 'rock'
      else:
        print 'You pick up a rock, but your pocket is already full!.'
        print 'You return the rock to its place on the cavern floor.'
    elif answer.find('walk') != -1 or answer.find('explore') != -1 or answer.find('wander') != -1 or answer == 'wander around':
      print 'You cautiously walk around, trying to figure out where you are.'
      print 'By feeling the ground and the musty feeling in the air, you determine you must be in some sort of cave.'
      print 'As you are wandering, you see a tiny point of light in the distance.'
      distant_light()
    elif answer.find('sit') != -1:
      sit()
      print 'You hear some odd noises coming from nearby and then there\'s a splash in the water, it sounds like somethings swimming out to where you fell.'
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "Error 1309: DOES NOT COMPUTE"
      answer = answer + ' : '
      output_filename = 'caveerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#make this harder to get to
def distant_light():
  while True:
    answer = raw_input().lower()
    if answer == 'pick up a rock':
      if player_inventory['pocket'] == 'empty':
        print 'You pick up a rock and put it in your pocket'
        player_inventory['pocket'] = 'rock'
      else:
        print 'You pick up a rock, but your pocket is already full!.'
        print 'You return the rock to its place on the cavern floor.'
    elif answer == 'explore':
      print 'You decide to continue exploring and walk away from the light to furthur investigate the cavern.'
      cave()
    elif answer.find('go to') != -1 or answer == 'to toward the light' or answer == 'walk to the light' or answer == 'walk toward the light' or answer == 'walk toward the light' or answer == 'follow the light' or answer == 'walk towards the light' or answer == 'find the light':
      print 'You head in the direction of the light, and are gradually able to see more and more of your surroundings.'
      print 'You are most definitely in some sort of underground cavern.'
      print "You continue approaching the light and see that it's coming from a small hole in the cavern wall, about fifty feet above the ground."
      cavern()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'I don\'t know that one capn'
      answer = answer + ' : '
      output_filename = 'distantlighterror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def cavern():
  if player_inventory['hand'] == 'torch':
    print 'Your torch throws flickering light onto the stone ground littered with small rocks.'
    while True:
      answer = raw_input().lower()
      if answer == 'blarg':
        print 'You blarg out into the darkness, it echoes around the cavern, spooky.'
      else:
        print 'Sorry, this part isn\'t finished yet.'
        print 'Your torch suddenly dematerializes in your hand'
        player_inventory['hand'] = 'empty'
        print ''
        print 'You stand in the darkness with the light from the hole in the wall shining through'
        print 'above you.'
        answer = answer + ' : '
        output_filename = 'cavern_torch_error.txt'
        output_file_obj = open(output_filename, 'a')
        output_file_obj.write(answer)
        output_file_obj.close()
        break
  while True:
    answer = raw_input().lower()
    if answer == 'walk toward the light' or answer == 'go to it' or answer == 'move to the light' or answer == 'go to the light' or answer == 'go toward the light' or answer == 'light':
      print 'You continue walking toward the light until you reach the wall that it\'s coming from.'
      print 'The wall has plenty of outcroppings that you could use to climb up to the light.'
    elif answer == 'where is the light' or answer == 'whre is the light' or answer == 'find the light':
      print "You look up and you can see the light coming from a small hole in the cavern wall, about fifty feet above the ground."
#nsa
    elif answer == 'walk':
      print 'Where?'
    elif answer == 'swim':
      print 'You proceed to swim on the ground, flopping around like a fish out of water you cause quite a ruckus.'
      print ''
      print "As you're enjoying your bout of mental deficiency you fail to notice the odd gurgling noises approaching you."
      print "The last thing you ever hear is an unearthly growl."
      game_over()
	
    elif answer == 'go in' or answer == 'go in the hole':
      print "You can't just go in, it's 50ft off the ground!"
    elif answer == 'leave':
      print 'You walk away from the light.'
      print 'You return to where you originally got out of the water.'
      print 'Or at least you think you do, you can\'t really see anymore.'
      cave()
    elif answer.find('explore') != -1:
      print "You barely have enough light to see the ground, which is littered with many rocks of varying sizes."
      print 'However, you decide to go explore anyway and you wander off into the darkness, away from the light.'
      cave()
    elif answer == 'rock':
      print "There are rocks everywhere."
    elif answer == 'pick up a rock':
      if player_inventory['pocket'] == 'empty':
        print 'You pick up a rock and put it in your pocket'
        player_inventory['pocket'] = 'rock'
      else:
        print 'You pick up a rock, but your pocket is already full!.'
        print 'You return the rock to its place on the cavern floor.'
    elif answer == 'pick up torch':
      print 'There are no torches here.'
    elif answer.find('climb') != -1:
      print 'You climb up the wall, making sure to stop the larger outcroppings when you get to them to conserve your strength.'
      print 'As you near the hole in the cavern wall you still can\'t see what the light is coming from.'
      print 'Just below the hole, you prepare yourself for the last few feet, and then proceed to pull yourself up.'
      print 'The light blinds you at first as your head crosses the threshold of the hole.'
      print "Your eyes adjust, and you can see that the bright light was sunlight, coming in from a window in the room you're looking into."
      print 'You climb up into the room'
      print ''
      print 'Across from you is a wooden door, to your left and right are two large steel doors with iron bars across them to keep them shut.'
      print 'All of the walls appear to be quite sturdy. They\'d probably be able to withstand the attacks of a small giant or even a decently powerful'
      print 'Magical blast. From here you can see that there\'s an upper level, where the window is, and just below the window is another wooden door.'  
      print "It seems like no one's been in here for a while, a thick layer of dust covers the floor."
      the_dungeon()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'GAH YU DON GUFD'
      print 'trah agaein'
      answer = answer + ' : '
      output_filename = 'cavernerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def the_dungeon():
  while True:
    answer = raw_input().lower()
    if answer == 'look around' or answer == 'look around the dungeon' or answer == 'keep going':
      print 'Across from you is a wooden door, to your left and right are two large steel doors with iron bars across them to keep them shut.'
      print 'All of the walls appear to be quite sturdy. They\'d probably be able to withstand the attacks of a small giant or even a decently powerful'
      print 'Magical blast. High up on the walls are torches, perfectly positioned to light up the area, but still be out of reach for even the tallest'
      print 'of men. They must be lit from above at night.'
      print ''
      print 'From here you can also see that there\'s an upper level, where the window is, and just below the window is a wooden door.'
      print 'On the opposite side of the upper level is another.'	
      print "It seems like no one's been in here for a while, a thick layer of dust covers the floor."
    elif answer == 'up' or answer == 'upstairs' or answer == 'up stairs' or answer == 'upper level' or answer == 'uper level':
      print 'You look up to see a railing that sits on the edge of the wall on all sides. There appears to be a door under the window, and a door directly'
      print 'across from it.'
    elif answer == 'climb the wall' or answer == 'climb up the wall':
      print 'You walk up to the wall and attempt to climb it,'
      print 'unfortunately it\'s too smooth to make any progress.'
    elif answer == 'explore' or answer == 'walk around the room' or answer == 'walk' or answer == 'explore the room' or answer == 'walk around':
      print 'You explore around the room, it seems to be very structurally sound, other than the hole in the wall you just entered through.'
      print 'The bars on the two large doors are heavy, but you can lift them with a little effort. You check the wooden door across from the'
      print 'wall you came in through and inside is a small corridor that leads to a staircase on the right.'
#nonspecific responses
    elif answer == 'open the door' or answer == 'dorr' or answer == 'go to door' or answer == 'steel doors' or answer == 'steel door' or answer == 'open steel door' or answer == 'door' or answer == 'lift the baar on the door' or answer == 'open door' or answer == 'open a door':
      print 'Which door?'
    elif answer == 'go to the upper level' or answer == 'go to upper level':
      print 'How do you get to the upper level?'
    elif answer == 'climb':
      print 'What do you want to climb?'
    elif answer == 'open':
      print 'Open what?'
    elif answer == 'go in':
      print 'Go in what?'
    elif answer == 'lift':
      print 'Lift what?'
    elif answer == 'lift the heavy bars':
      print 'On which door?'
    elif answer == 'enter room':
      print 'Which room?'

    elif answer == 'leave' or answer == 'exit' or answer == 'into the hole' or answer == 'go into the hole' or answer == 'climb down' or answer == 'climb out':
      print 'You go back through the hole in the wall and climb all the way down.'
      cavern()
    elif answer == 'why dont you comprehend':
      print 'Because you\'re using big scary words that I don\'t understand.'
    elif answer == 'break the window' or answer == 'smash the window' or answer == 'throw rock at window':
      if player_inventory['pocket'] == 'rock':
        print 'You take the rock out of your pocket and whip it at the window. The glass shatters as your perfectly aimed missle shoots right through.'
        print 'You congratulate yourself on that awesome throw.'
        print ''
        print 'As you stand there in awe of how beautifully the glass shattered, you notice that small fragments begin floating back up and replacing'
        print 'themselves, back into the window. Larger shards begin to follow, and before you know it, the window is whole again.'
        print ''
        player_inventory['pocket'] = 'empty'
      else:
        print 'You look around for something to break the window with, however there\'s nothing in the room. You might be able to break it with one of the rocks'
        print 'that are littered all over the floor of the cavern below.'
    elif answer == 'window' or answer == 'look at the window':
      print "You look at the window, it's not very large, but it's the perfect size to let light into the cavern." 
    elif answer == 'is the window cursed' or answer == 'cursed window':
      print 'It might be, maybe you could ask Feyndrin.'
    elif answer == 'find the window':
      print 'The window is above a door on the upper floor, across the room from where you came out of the hole.'
    elif answer == 'door under the window' or answer == 'the door under the window':
      print 'You look up at the door under the window, it\'s wooden and looks pretty normal.'
    elif answer == 'look out the window':
      print 'The window is too high up for you to look out of it'
    elif answer == 'touch window':
      print 'The window is on the upper level, you can\'t touch it from here.'
    elif answer == 'rock':
      if player_inventory['pocket'] == 'rock':
        print "Yes, you have a rock."
      else:
        print 'There are no rocks in here.'
    elif answer == 'die':
      print 'You realize you have nothing to live for and that this quest is pointless. The only way to escape this horrible place must be death.'
      print 'You shamble over to the pit and just sit on the edge for a bit, dangling your feet over. Then you decide you\'re ready.'
      print 'Standing up, you take a deep breath, and then allow yourself to fall backwards.'
      print 'Wind rushes past your face as you fall downward, and then you feel nothing.'
      game_over()

    elif answer.find('right') != -1:
      print 'You walk over to the steel door on the right and lift the heavy bar that was locking it in place. As you push it opens slowly,'
      print 'and once the gap in the door is large enough, you enter the room.'
      print ''
      print 'Inside, there are four cells, each seperated by thick stone walls. The fronts and tops of the cells are made of thick metal bars.'
      print 'To your right is a small table with a few stools by it.'
      dungeon_cellblock('r')
    elif answer == 'go left' or answer == 'left steel door' or answer == 'door to the left' or answer == 'left door' or answer == 'left' or answer == 'door on the left':
      print 'You walk over to the steel door on the left and lift the heavy bar that was locking it in place. As you push it opens slowly,'
      print 'and once the gap in the door is large enough, you enter the room.'
      print ''
      print 'Inside, there are four cells, each seperated by thick stone walls. The fronts and tops of the cells are made of thick metal bars.'
      print 'To your left is a small table with a few stools by it.'
      dungeon_cellblock('l')
    elif answer.find('wood') != -1 and answer.find('door') != -1 or answer == 'staircase' or answer == 'climb the stairs' or answer == 'climb stairs' or answer == 'find stairs' or answer == 'go upstairs' or answer == 'go up' or answer == 'stairs' or answer == 'go up stairs' or answer == 'small ccorridor' or answer == 'enter corridor':
      print 'You walk up to the wooden door and open it. Inside, there\'s a wall to your left and stairs to your right.'
      print 'You climb the stairs and come out onto the upper level of the dungeon. Looking over the railing, you can see the lower level.'
      print 'It contains the main room you were just in, and then two side rooms with cells in them that are cut off'
      print 'from the main room by the large iron doors.  Each cell\'s top and front were made of bars so the guards could look'
      print 'in on the prisoners, no matter where they were.'
      print ''
      print 'The upper level is a pathway that surrounds the perimeter of the lower level, with a railing on the side to prevent the'
      print 'guards from accidentally falling down. On the side opposite to where you are currently standing, there is a door with a'
      print 'small sign next to it, and if you walked all the way around the path, you could get to the door under the window.'
      dungeon_upper()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'do not comprehend.'
      answer = answer + ' : '
      output_filename = 'dungeonerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#both of the dungeon cellblocks, takes in str to indicate which side
def dungeon_cellblock(str):
  while True:
    answer = raw_input().lower()
    if answer == 'look around' or answer == 'explore' or answer == 'explre':
      if str == 'r':
        print 'There are four cells, each seperated by thick stone walls. The fronts and tops of the cells are made of thick metal bars.'
        print 'Upon further inspection, you can see that two of the bars in the far left cell are very slightly bent,'
        print 'considering the size of the bars, it would require incredible strength to accomplish such a feat.'
        print 'All of the cells are empty, but the interiors are furnished with a plain bed and blanket and a small bucket.'
        print 'The small table to the right of the door has a pair of dice on it.'
        print ''
      elif str == 'l':
        print 'There are four cells, each seperated by thick stone walls. The fronts and tops of the cells are made of thick metal bars.'
        print 'Upon further inspection, you can see that the floors of the two right cells and the floor in front of the cells,'
        print 'has dark stains on it.  A fight must\'ve broken out here and then the prisoners were forced back into their cells.'
        print 'All of the cells are empty, but the interiors are furnished with a plain bed and blanket and a small bucket.'
        print 'The small table to the left of the door has a pair of dice on it.'
        print ''
    elif answer.find('table') != -1 or answer == 'sit on a stool' or answer == 'sit at stool':
      print 'You walk up to the table and take a seat. Sitting here makes you realize what it would be like to be down here, day after day,'
      print 'the only entertainment you could look forward to was playing dice, and the occasional fight.'
      dungeon_table()
    elif answer == 'open the door':
      print 'What door?'
    elif answer == 'open the cell door' or answer == 'open the cell dorr':
      print 'Which cell?'
    elif answer == 'open the bars':
      print 'What?'
    elif answer == '':
      print 'You stand in the cell block looking around at nothing in particular.'
    elif answer == 'leave' or answer == 'exit':
      print 'You exit the cell block and close the steel door behind you. You make sure to resecure the bar across it as well.'
      the_dungeon()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'Es tut mir leid meine freund. Ich verstehe nichts.'
      answer = answer + ' : '
      output_filename = 'dungeon_cellblock_error.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#minigame goes here \/
def dungeon_table():
  while True:
    answer = raw_input().lower()
    if answer == 'leave' or answer == 'stand up' or answer == 'stand':
      print 'You get up from the table, and return to looking around the cell block.'
      break
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'You sit at the table, staring off into space.'
      answer = answer + ' : '
      output_filename = 'dungeon_table_error.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#going to have to make programs for both the guard's door and the exit door
def dungeon_upper():
  while True:
    answer = raw_input().lower()
    if answer == 'go back downstairs' or answer == 'lower level' or answer == 'down stairs' or answer == 'stairway' or answer == 'climb the stairs' or answer == 'exit' or answer == 'go back' or answer == 'go downstairs' or answer == 'go to the lower dungeon' or answer == 'leave':
      print 'You return to the lower level.'
      the_dungeon()
    elif answer == 'what does the sign say?' or answer == 'go to sign' or answer == 'read sign' or answer == 'sign' or answer == 'what does the sign say' or answer == 'read the sign':
      print "You walk up to the sign and it reads Guard's Quarters"
      guard_room_door()
    elif answer == 'door across from the staircase' or answer == 'across from the staircase':
      print "You walk up to the door across from the staircase, the small sign near it reads Guard's Quarters"
      guard_room_door()
    elif answer == 'walk all the way around the path' or answer == 'follow the path' or answer == 'walk around the path':
      print 'You walk all the way around the path to the door under the window.'
      print 'The cracks in the door ooze with odd black gaseous material...'
      door_under_window()
    elif answer == 'door under the window':
      print 'You walk up to the door under the window.'
      print 'The cracks in the door ooze with odd black gaseous material...'
      door_under_window()
    elif answer == 'call' or answer == 'call out':
      print 'You call out for anyone to hear you.'
      print 'Your words bounce around the walls off the dungeon, echoing slightly, but no one responds.'
    elif answer == 'yell' or answer == 'scream':
      print 'Pretending to be an angry guard, you yell down to the lower level'
      raw_input('Yell something: ')
      print 'If anyone was down there, they\'d be scared.'
      print 'You walk away from the ledge, satisfied with yourself.'
    elif answer == 'knock on the door':
      print 'You walk up to the door and knock on it. No one answers.'
    elif answer == 'explore':
      print 'You walk around the upper floor, there\'s not much to see here other than the window and the guard\'s door.'
      print 'You have a clear view of the lower level, much like the guards would have when they were here.'
    elif answer == 'climb higher':
      print 'You walk around and try to find somewhere you could climb up the wall.'
      print 'Unfortunately there are no good spots.'
    elif answer == 'crawl around':
      print 'You crawl around on the ground creepily, if anyone was here to see you they\'d be scared.'
      print 'You decide you\'ve had enough of crawling and stand back up. That was fun.'
    elif answer == 'go to the window' or answer == 'window' or answer == 'look out the windpw' or answer == 'look out the window':
      print 'You walk up to the window and take a look at it, it\'s a little too high up to look out of but it looks like a pretty normal window.'
    elif answer == 'break the window' or answer == 'smash the window' or answer == 'throw rock at window':
      if player_inventory['pocket'] == 'rock':
        print 'You take the rock out of your pocket and whip it at the window. The glass shatters as your perfectly aimed missle shoots right through.'
        print 'You congratulate yourself on that awesome throw.'
        print ''
        print 'As you stand there in awe of how beautifully the glass shattered, you notice that small fragments begin floating back up and replacing'
        print 'themselves, back into the window. Larger shards begin to follow, and before you know it, the window is whole again.'
        print ''
        player_inventory['pocket'] = 'empty'
      else:
        print 'You look around for something to break the window with, however there\'s nothing in the room. You might be able to break it with one of the rocks'
        print 'that are littered all over the floor of the cavern below.'
    elif answer == '':
      print ''
    elif answer == 'go up the stairs' or answer == 'up stairs' or answer == 'upper level':
      print 'You are already on the upper level.'
    elif answer == 'table' or answer == 'book' or answer == 'ledger':
      print 'There\'s no ' + answer + ' here.'
#nonspecific answers
    elif answer == 'door' or answer == 'enter' or answer == 'go to the door' or answer == 'walk to the door':
      print 'Which door? The door across from the staircase or the door under the window?'
    elif answer == 'jump off the path and die':
      print 'You majestically dive over the railing and land headfirst on the stone floor below.'
      game_over()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'try again'
      answer = answer + ' : '
      output_filename = 'dungeonuppererror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#if player reads the sign
def guard_room_door():
  while True:
    answer = raw_input().lower()
    if answer == 'go in' or answer == 'guards quarters' or answer == 'enter the guards quarters' or answer == 'go in the guard room' or answer == 'go in the guards room' or answer == 'guards room' or answer == 'go in the room' or answer == 'go in the door' or answer == 'open the door' or answer == 'enter room' or answer == 'open door' or answer == 'go in room' or answer == 'go into room':
      print 'You open the door'
      print "Surprisingly, it's not locked"
      print "You look around the guard's room, a few oil lanterns hang on the walls."
      print "There's a desk with a large book sitting on top of it just in front of you."
      print 'To the left of the desk is a small gate.'
      print 'Behind the desk is another door.'
      guard_room()
    elif answer == 'leave':
      print 'You walk away from the door to the guard\'s quarters.'
      dungeon_upper()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "I don't understand, sorry"
      answer = answer + ' : '
      output_filename = 'dungeonuppererror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def guard_room():
  while True:
    answer = raw_input().lower()
    if answer == 'look at the book' or answer == 'ledger' or answer == 'read it' or answer == 'open book' or answer == 'open the book' or answer == 'open the ledger' or answer == 'read the ledger' or answer == 'read the book' or answer == 'book':
      print 'You walk around the desk and take a seat in the chair that was pulled up to it, as you sit down you notice'
      print 'the desk has three drawers and two cabinets built into it. The faded leather cover of the book reads "Ba\'Goren Dungeon Ledger"'
      print 'Upon opening the book, you discover that the ledger contains records of everyone'
      print 'who has ever been thrown in the dungeon, what their crime was, and what their punishment was.'
      print ''
      dungeon_ledger()
    elif answer == 'open the back door' or answer == 'back door' or answer == 'door behind desk' or answer == 'open the door with a key' or answer == 'open the door behind the desk':
      if player_inventory['hand'] == 'guard_room_key':
        print 'You take the key you found in the desk out of your pocket and unlock the door.'
        print 'As you open the door, you can make out the shapes of bunks in the dark room.'
        print 'You close the door behind you and stand in the room for a second, allowing your eyes to adjust.'
        print 'A chest in between the two stacks of beds comes into view, as does a wardrobe to your left.'
        guards_chambers()
      else:
        print 'You walk up to the door behind the desk and try the handle, it\'s locked.'
    elif answer == 'sit at the desk' or answer == 'sit at desk':
      print 'You walk around the desk and take a seat in the chair that was pulled up to it, as you sit down you notice'
      print 'the desk has three drawers and two cabinets built into it. The faded leather cover of the book reads "Ba\'Goren Dungeon Ledger"'
      guard_desk()
    elif answer == 'open the gate' or answer == 'open th gate':
      print 'You walk up to the gate next to the desk and push it open.'
    elif answer == 'eat the old food':
      print "You don't see any food nearby."
    elif answer == 'dust the room':
      print 'With what?'
#nonspecifics
    elif answer == 'go in the door' or answer == 'go to the door' or answer == 'open the door' or answer == 'enter the door' or answer == 'walk to the door':
      print 'Which door, the one to exit the Guard\'s Quarters, or the one in the back of the room?'
    elif answer == 'go out' or answer == 'leave':
      print 'You leave the guard\'s room'
      dungeon_upper()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'whaaaaa???'
      answer = answer + ' : '
      output_filename = 'guardroomerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
#need to add sub-programs for each drawer
def guard_desk():
  while True:
    answer = raw_input().lower()
    if answer == 'look in the drawers' or answer == 'drawers' or answer == 'open the drawers':
      print 'You open up each of the drawers.'
      print 'The one on the left has quills and fresh pieces of paper to be added to the ledger.'
      print 'The one in the center has many jars of ink'
      print 'The drawer on the right has a set of cuffs in it'
    elif answer == 'left drawer':
      print 'The drawer has quills and fresh pieces of paper to be added to the ledger.'
    elif answer == 'middle drawer' or answer == 'center drawer':
      print 'You open up the drawer to find many jars of ink.'
    elif answer == 'right drawer':
      print 'This one has a set of cuffs in it.'
    elif answer == 'cabinets' or answer == 'cabinet' or answer == 'what is in the cabinet':
      print 'You open up the cabinets on the desk.'
      print 'The one on the left has a small sword in it and some rope. "ONLY FOR EMERGENCIES" is etched into the wood on the inside of the cabinet door.'
      print 'The cabinet on the right has a small bottle sitting in the corner.'
    elif answer == 'grab the bottle' or answer == 'bottle' or answer == 'look at the bottle' or answer == 'look in the bottle':
      print 'You pick up the bottle, and you can see inside is a rolled up piece of paper.'
      print 'You flip the bottle upside down and pour its contents out onto the desk.'
      print 'The paper unrolls a bit and a small key falls out.'
      print 'You grab the small piece of paper and inside, someone wrote,'
      print '"James, here is the key to the back room, sorry you had to have the night shift after the feast but at least Galvan will be with you."'
      print ''
      print 'You grab the key and put the message back into the bottle'
      player_inventory['hand'] = 'guard_room_key'
    elif answer == 'look at the book' or answer == 'ledger':
      print 'You open the dungeon ledger.'
      dungeon_ledger()
    elif answer == 'stand up' or answer == 'stand' or answer == 'leave':
      print 'You stand up from the desk.'
      guard_room()
    elif answer.find('sit') != -1:
      print "You're already sitting."
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print "You sit at the desk... doing nothing"
      answer = answer + ' : '
      output_filename = 'guarddeskerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()  
	
def dungeon_ledger():
  while True:
    answer = raw_input().lower()
    if answer == 'punishments' or answer == 'what are the punishments' or answer == 'what punishments' or answer == 'what are some of the punishments' or answer == 'read punishments' or answer == 'punishment':
      print 'The punishments include everything from one hour in the dungeon to being burned at the stake.'
      print 'A couple of the prisoners have "The Hole" next to their name, but there\'s no indication as to what that means'
    elif answer == 'creature in hole':
      print "There's no mention of what lives in the hole."
    elif answer == 'duration' or answer == 'duration of stay' or answer == 'duration of stay in the dungeon':
      print 'The amount of time people were sentenced to in the dungeon seems to vary with their crime.'
    elif answer == 'the hole' or answer == 'go to the hole' or answer == 'what is the hole':
      print 'You see the hole multiple times next to prisoner\'s names but there\'s no indication as to what it might be.'
    elif answer == 'crime':
      print 'The crimes range anywhere from petty theft to murder'
    elif answer == 'warlock' or answer == 'warlock in ledger':
      print 'You flip through the pages, looking for any mention of a warlock. A few prisoners crime descriptions include warlock in them.'
    elif answer == 'read the names' or answer == 'names' or answer == 'what are the names' or answer == 'read names':
      print "There must be hundreds of names, maybe thousands in the ledger. You look at the ones on the first page:"
      print 'Alduin Weater, Rengar Stoneskull, Garrosh Nal\'gor, Felne Vernais, Fedolio Gregorio, Arthur Quillwyvern, Tyrion Sterg, Sylvanis Thorn, and Falionas Brettamu'
    elif answer == 'alduin' or answer == 'alduin weater':
      print "Alduin Weater, theft of a dragon's skull, one month plus indentured servitude to shopkeeper for three months"
    elif answer == 'rengar' or answer == 'rengar stoneskull':
      print "Rengar Stoneskull, led a brigade of bandits who occupied trading routes and stole from anyone passing by. Killed two guards while attempting to escape arrest, gallows"
    elif answer == 'garrosh' or answer == "garrosh nal'gor" or answer == 'garrosh nalgor':
      print "Garrosh Nal'gor, obtained a magical artefact from a strange man in a cave. Went berserk and started attacking townsfolk, detain until recovery"
    elif answer == 'felne' or answer == 'felne vernais':
      print "Felne Vernais, notorious witch who occupied Ba'Goren Forest was known for changing soldiers into frogs and one townsfolk reported he was turned into a newt but 'got better'"
      print "Thrown into dungeon to await the paladin's who will either train her to properly use her gift or remove it from her."
    elif answer == 'fedolio' or answer == 'fedolio gregorio':
      print "Fedolio Gregorio, travelling magician and con-man known for coercing people out of their money. Claimed he could escape from any prison and volunteered to enter"
      print "Ba'Goren Dungeon and would stay here until he could escape, tried to escape through The Hole and never returned"
    elif answer == 'arthur' or answer == 'arthur quillwyvern':
      print "Arthur Quillwyvern, man of supposedly 'royal blood' who wielded an enchanted sword. Came into the kingdom demanding everyone make him their king., sent to stay in dungeon"
      print 'until recovery from insanity'
    elif answer == 'tyrion sterg' or answer == 'tyrion':
      print 'Tyrion Sterg, once a successful officer in the army. Went on a crusade and didn\'t come back the same. Constantly accused others of "Aiding the Plague"'
      print 'Destroyed a family\'s library due to them being "Demonic Relics", sent to dungeon until he can recieve help and then must repay the family'
    elif answer == 'sylvanis thorn' or answer == 'sylvanis':
      print 'Sylvanis Thorn, notorious theif rumored to be the leader of the "Order of Shadows", many of the towns nearby the kingdom suddenly found themselves'
      print 'bankrupt when she would pass through. Was apprehended by Grand Paladin Ashmorne, sentenced to indentured servitude under the Grand Paladin until'
      print 'she had successfully paid off all that she has stolen.'
    elif answer == 'falionas' or answer == 'falionas brettamu':
      print 'Falionas Brettamu, single-handedly disabled 30 guards as they tried to apprehend him for running from the original guard who was just trying to'
      print 'stop him from stealing an apple, was forced to give the apple back and serve 30 days in the dungeon (One for each guard)'
    elif answer == 'read the last page' or answer == 'last page':
      print 'You turn the book over and open it to the last page, judging by the wear on the page it must be incredibly old.'
      print 'Some of the names and punishments have faded, but you can make out a couple:'
      print 'Charlotte Lizabreadth and Daniel Mittel'
      dungeon_ledger_last()
    elif answer == 'turn the page' or answer == 'go to the next page' or answer == 'page 2':
      print 'You attempt to turn the book to the next page, but it seems as if the next few hundred pages are sealed together and you end up flipping to the'
      print 'last page.'
      print 'Some of the names and punishments have faded, but you can make out a couple:'
      print 'Charlotte Lizabreadth and Daniel Mittel'
      dungeon_ledger_last()
    elif answer == 'close the book' or answer == 'leave' or answer == 'close book' or answer == 'close' or answer == 'finsih' or answer == 'finish' or answer == 'exit' or answer == 'exit book':
      print 'You close the ledger, and sit at the desk, looking at the drawers and cabinets'
      guard_desk()
    elif answer == 'stand up':
      print 'You close the ledger and stand up from the desk.'
      guard_room()
    elif answer == 'open a drawer':
      print 'Which drawer? Left, Right, or the Middle?'
      guard_desk()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'You flip through the pages aimlessly, not sure what you want to look at'
      answer = answer + ' : '
      output_filename = 'dungeonledgererror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def dungeon_ledger_last():
  while True:
    answer = raw_input().lower()
    if answer == 'charlotte' or answer == 'charlotte lizabreadth':
      print 'Charlotte Lizabreadth, a witch who asked people the most interesting of questions. Always challenged authorities by switching her answers nearly every time'
      print 'possible. Large contributor to the "First 1000 Lines", sentenced to the dungeon to forever play a silly text adventure.'
    elif answer == 'daniel' or answer == 'daniel mittel':
      print 'Daniel Mittel, mysterious warlock and great adventurer. Solved puzzles with the greatest of ease, even the ones he shouldn\'t. Tried to sacrifice himself to'
      print 'the trick door in "The Hall of Paintings". Another large contributor to the "First 1000 Lines", sentenced to dungeon until he "wins the game"'
    elif answer == 'the hole':
      print 'You see no mention of the hole on this page.'
    elif answer == 'first page' or answer == 'go back to the first page' or answer == 'go back' or answer == 'back':
      print 'You turn the ledger back to the first page.'
      dungeon_ledger()
    elif answer == 'leave' or answer == 'close the book' or answer == 'stand up' or answer == 'stand':
      print 'You close the ledger and return to exploring the guard\'s quarters.'
      guards_chambers()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'i just don\'t understand what you\'re trying to tell me.'
      answer = answer + ' : '
      output_filename = 'dungeonledger_last_error.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()
      dungeon_ledger()

def guards_chambers():
  while True:
    answer = raw_input().lower()
    if answer == 'look in the wardrobe' or answer == 'wardrobe' or answer == 'open the wardrobe':
      if guards_chambers_wardrobe_contents['shirt'] == "guard's shirt" and guards_chambers_wardrobe_contents['pants'] == "guard's pants":
        print 'You open the wardrobe and inside are multiple guard\'s uniforms and boots.'
        print ''
        guards_chambers_wardrobe()
      else:
        print 'You open the wardrobe and inside are multiple guard\'s uniforms and boots.'
        print 'Along with your old ' + guards_chambers_wardrobe_contents['shirt'] + ' and ' + guards_chambers_wardrobe_contents['pants']
        guards_chambers_wardrobe()
    elif answer == 'look in the chest' or answer == 'go to the chest' or answer == 'chest' or answer == 'open the chest' or answer == 'unlock the chest':
      print 'Inside the chest are piles of cuffs and torches, there are also a few metal buckets stacked in the corner.'
    elif answer == 'sit on the bed':
      print 'You sit down on one of the beds, it\'s surprisingly comfy.'
      print ''
      print 'You decide that you\'ve rested for long enough and get up.'
    elif answer == 'bunks':
      print 'You walk over to the bunks, they don\'t look very nice, but they\'d probably be fine if you were exhausted.'
    elif answer == 'fight the demons':
      print 'Your vision begins to blur and swirl as a crackling portal into the netherworld opens up in front of you. A large clawed hand reaches through and grips'
      print 'the side of the portal. Another one shoots out and grabs the other edge, then in the center, two black dots appear. They grow larger until a grayish'
      print 'circle forms in between them. The circle expands until it meets the black dots and you begin to see a head taking shape as it comes farther out of the'
      print 'portal.'
      print '"NOPE!" You yell and run toward the portal. In one fluid motion, you leap into the air and turn your body into a horizonal arrow of meat and bone, led'
      print 'by your feet. They connect solidly with the head and it flys back into the portal, the hands lose their grip and disappear as well. The force of the'
      print 'impact makes the edges of the portal shudder, and it quickly collapses in on itself as you fall to the ground.'
      print 'Whew, crisis averted'
    elif answer == 'what are the metal buckets for':
      print "Maybe you could ask Feyndrin"
    elif answer == 'turn around':
      print 'You turn around in a circle, weee.'
    elif answer == 'sit at desk' or answer == 'desk':
      print 'There\'s no desk in this room.'
    elif answer == 'leave' or answer == 'go back' or answer == 'exit' or answer == 'exit room' or answer == 'leave room':
      print 'You leave the room.'
      guard_room()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'oi cap, i dun really know wut ya mean.'
      answer = answer + ' : '
      output_filename = 'guards_chamberserror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def guards_chambers_wardrobe():
  while True:
    answer = raw_input().lower()
    if answer == 'put on a uniform':
      print 'You look through all the uniforms in the wardrobe, luckily one of them is your size.'
      print 'You pull it out, and put it on, placing your old clothes where the uniform was.'
      player_inventory['chest'] = "guard's shirt"
      player_inventory['legs'] = "guard's pants"
      guards_chambers_wardrobe_contents['shirt'] = 'common shirt'
      guards_chambers_wardrobe_contents['pants'] = 'common pants'
    elif answer == 'close wardrobe' or answer == 'leave':
      print 'You close the wardrobe and return to looking around the room.'
      guards_chambers()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'You stare into the wardrobe aimlessly, unsure of what to do'
      answer = answer + ' : '
      output_filename = 'guards_chambers_wardrobeerror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def guards_chambers_chest():
  while True:
    answer = raw_input().lower()
    if answer == 'buckets' or answer == 'metal buckets':
      print 'The buckets look pretty sturdy and are sealed tight, they could be used for carrying liquids.'
    elif answer == 'leave' or answer == 'close the chest':
      print 'You close the chest and return to looking around the room.'
      guards_chambers()
    elif answer == 'pick up a torch' or answer == 'grab a torch':
      print 'You grab a torch out of the chest and it flames to life as you hold it up.'
      player_inventory['hand'] = 'torch'
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'You stare into the chest, there are lots of shiny things.'
      answer = answer + ' : '
      output_filename = 'guards_chambers_chesterror.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def door_under_window():
  while True:
    answer = raw_input().lower()
    if answer.find('open') != -1:
      print 'You open the door and a gust of black gas envelopes you.'
      print 'As you breath it in, you start to choke.'
      print 'You try to bat it away, but your limbs don\'t respond.'
      print 'It continues to choke you as you collapse onto the floor'
      print 'struggling for oxygen.'
      print ''
      raw_input()
      print ''
      print '.'
      print ''
      raw_input()
      ghost_of_leo()
    elif answer.find('leave') != -1:
      print 'You walk away from the door.'
      dungeon_upper()
    else:
      flag = defaults(answer)
      if flag == True:
        continue
      print 'der di der I dennur!'
      answer = answer + ' : '
      output_filename = 'door_under_window_error.txt'
      output_file_obj = open(output_filename, 'a')
      output_file_obj.write(answer)
      output_file_obj.close()

def ghost_of_leo():
  print "You wake up and you can't see anything."
  print "It feels like you're floating."
  print "After a few seconds, you begin to see a glow in the distance."
  print "The glow grows larger as it approaches you, and you"
  print "can make out the shape of a man."
  print "As he walks toward you, his shoulders are slumped a little and his face"
  print "is that of a man who has lost all hope."
  print "He forces a smile as he stops and looks at you."
  print '"My name is Leo Dib, can you help me?"'
  while True:
    print "GAH! This part isn't completed yet, sorry."
    print "You can go back to the [hall] you were originally in, the [seer]'s room, or back in the [dungeon]"
    answer = raw_input().lower()
    if answer == 'hall':
      print 'Teleporting you to the hall!'
      print 'BEEP BOOP BEEP BEEP!'
      hall()
    elif answer == 'seer':
      print 'Teleporting you to the seer!'
      print 'BEEP BOOP BEEP BEEP!'
      seer()   
    elif answer == 'dungeon':
      print 'Teleporting you to the dungeon!'
      print 'BEEP BOOP BEEP BEEP!'
      dungeon()
    else:
      print "ERROR ERROR INVALID LOCATION"
      print "TELEPORTING YOU TO START"
      start()
#don't need to set flag = defaults, just if defaults reformat
def defaults(str):
  if str.find('inventory') != -1:
    player.printInventory()
  elif str == '' or str == ' ':
    print 'You do nothing'
  elif str == 'drop':
    if player_inventory['hand'] == 'empty':
      print "You aren't holding anything."
    else:
      print "You drop a " + player_inventory['hand'] + ' onto the ground.'
      player_inventory['hand'] = 'empty'
  elif str.find('try again') != -1:
    print 'You seem to have forgotten what you just did...'
    print ''
    print '...'
    print ''
    print 'Oh well, I guess we just have to try something new'
  elif str == 'poop':
    print "You pull your pants down, squat, and push with all of your might."
    print "Oh well, nothing came out."
  elif str == 'pee':
    print "You try to pee, good thing you didn't have to. You still have your pants on."
  elif str == 'hm':
    print 'hm hm'
  elif str == 'wow' or str == 'cool':
    print 'yep'
  elif str.find('sit') != -1:
    sit()
  elif str.find('quit') != -1:
    quit()
  elif str == 'kill myself' or str == 'commit suicide':
    print "You concentrate your ninja powers and make your own heart explode."
    game_over()
  elif str.find('fuck') != -1 or str.find('bitch') != -1:
    print "That's not very nice."
  elif str.find('ok') != -1 or str.find('kay') != -1:
    print 'Ok, now what are you going to do?'
  else:
    return False
  return True
	
def quit():
  print 'Are you sure you want to quit?'
  answer = raw_input().lower()
  if answer == 'yes' or answer == 'y' or answer == 'ye' or answer == 'yeah' or answer == 'ya':
    raise SystemExit
  else:
    print 'ok'
#game over sequence
def game_over():
  print ''
  print "GAME OVER"
  raw_input()
  raise SystemExit

#GLOBAL VARIABLES DON'T FUCK WITH THEM
player_inventory = {'chest' : 'common shirt', 'back' : 'empty', 'hand' : 'empty', 'legs' : 'common pants', 'pocket' : 'empty', 'feet' : 'common boots'}
guards_chambers_wardrobe_contents =  {'shirt' : "guard's shirt", 'pants' : "guard's pants", 'boots' : "guard's boots"}
#Here's where the quest begins
player_name = raw_input('Hello, what is your name? ')
if player_name == 'Syix' or player_name == 'syix':
  print 'Welcome back Master Syix'
  print 'Hope you have a jolly good time debugging whatever it is you\'re working on.'
  print 'Tally Ho'
  print ''
  godMode = True
elif player_name == 'Shelly':
  print "Welcome back Charlotte Lizabreadth"
  print 'Good to see you\'re working on fulfilling your dungeon sentence.'
  print 'Have fun, and thanks for all of your help.'
  print ''
#make something cool for dane and cody too
elif player_name == 'David':
  print "Welcome back David"
print 'Are you ready to start your adventure ' + player_name + '?'
answer = raw_input().lower()
if answer == '':
  print ''
  print "___'__ ____ ________ __'____ ___!"
elif answer == 'hell yeah':
  print 'ALRIGHTY THEN, HERE WE GO!'
elif answer == 'i suppose':
  print 'ok, i guess we\'ll start then.'
elif answer == 'left':
  print 'Uhh, ok? I\'ll just assume that means yes.'
elif answer.find('no') != -1 or answer == 'n':
  print 'ok'
  raise SystemExit
elif answer.find('y') != -1 or answer == 'si' or answer == 'sure' or answer == 'ja' or answer == 'of course':
  print "You've just entered Ba'Goren Keep!"
else:
  print "I don't know that answer, but we'll just start anyway."
  answer = answer + ' : '
  output_filename = 'introerror.txt'
  output_file_obj = open(output_filename, 'a')
  output_file_obj.write(answer)
  output_file_obj.close()
start(True)
