from text_based_game_classes import Enemy, Bat, Tiger, Dragon, Hero, Mouse, Wizard
import random
import time

answer = None
hero = Hero('Superman', 400, 80, 200, 350)
enemies = [Mouse('Squeaky', 2),
           Bat('Frank', 5), 
           Tiger('Attilah', 30, True), 
           Dragon('Scaly', 75, 150, False),
           Wizard('Frodo', 90, True, 100)
           ]

while len(enemies) != 0:
    enemy = random.choice(enemies)
    answer = input('The Hero emerges from the dark forest...do you want to Attack (A), Run(R), or Look Around(L)? ').lower().strip()
    if answer == 'x':
        break

    elif answer == 'a':
        if hero.attack(enemy):
            print(f'{hero.name} has defeated {enemy.name} with a score of {hero.hero_attack} to {enemy.other_attack}!!!\n')
            enemies.remove(enemy)
        else:
            print(f'{hero.name}\'s score: {hero.hero_attack}   {enemy.name}\'s score:   {enemy.other_attack}')
            print(f'{hero.name} fought valiantly against {enemy.name} but lost, and will retreat to fight another day...\n')
            time.sleep(5)
    
    elif answer == 'r':
        print(f'{hero.name} has retreated to fight another day!!!\n')
    
    elif answer == 'l':
        print(f'{hero.name} is looking around and sees:\n')
        for e in enemies:
            print(f'A(n) {e.__class__.__name__} named {e.name}, with a level of {e.level}.')
        print()
    
    else:
        print('Sorry, please enter "a", "r", "l", or "x" to exit.')
    
            
if not enemies:
    print('Congratulations! You won the game!!!')
else:
    print('Thanks for playing!!! Bye!!!')
