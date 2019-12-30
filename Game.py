import pygame
import time
import pickle
import cuttree
import Chest
import Enemy
from CraftRec import *
pygame.init()
displayw = 400
displayh = 400
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (128,128,128)
brown = (152,138,80)
unit = displayw/8
bgw = 16
sandw = 50
image = {"img": 10,

}
position = { "xs": unit*4,
            "ys": unit*4,
            "tree2":[unit,unit*2,True],
            "tree74":[unit*7,unit*4,True],
            "trees162":[unit*6,unit*2,True],
            "treehouse":[unit*4,unit*7,False],
            "Dungeon1":[unit*6,unit*7,False],
            "axe":0,
            "sec1":[0,unit*4,False],
            "sec2":[0,unit*4,False],
            "sec3":[0,unit*4,False],
            "sec4":[0,unit*4,False],
            "sec5":[0,unit*4,False],
            "sec6":[0,unit*4,False],
            "thchest":[unit*4,unit*4,False,"Sword"],
            "s1chest":[unit*6,0,False,"Gold"],
            "s3chest":[unit*6,unit,False,"AppleSauce"],
            "s2enemy33":[unit*3,unit*3,False,0,10,"Resin"],
            "s5enemy33":[unit*3,unit*3,False,0,10,"Gold"],
            "s5enemy74":[unit*5,unit*2,False,0,10,"Gold"],
            "S6guard61":[unit*6,unit*2,False],
            "s4shop77":[["Apple"],[1]],
            "oldmanhelp":[False,False,False,unit*7,unit*7,False,False]
}
inv = { "Apple": 2,
        "Sword": 1,
        "Axe": 1,
        "Water": 1,
        "Wood": 0,
        "AppleSauce": 0,
        "Stick": 0,
        "Board": 0,
        "Boat":0,
        "Resin":0,
        "Gold":20,
        "Axehead":0,
        "Key":0,
}
health = { "Water": 10,
           "Food": 10,
           "Health": 10,
           "Hunger": 0,
           "Thirst": 0
}
game = pygame.display.set_mode((displayw,displayh))
pygame.display.set_caption("FORGOTTEN")
clock = pygame.time.Clock()
avatar = pygame.image.load('avatar.png')
avatarup = pygame.image.load('avatarup.png')
avatardown = pygame.image.load('avatardown.png')
avatarleft = pygame.image.load('avatarleft.png')
avatarright = pygame.image.load('avatarright.png')
sandbg = pygame.image.load('Sand.png')
treeimg = pygame.image.load('Tree.png')
grass = pygame.image.load('grass.png')
menuimg = pygame.image.load('Menu.png')
selectimg = pygame.image.load('select.png')
blankimg = pygame.image.load('blank.png')
menu2img = pygame.image.load('Menu2.png')
menu3img = pygame.image.load('Menu3.png')
houseimg = pygame.image.load('House.png')
woodbg = pygame.image.load('woodbg.png')
fullmenu = pygame.image.load('Menu4.png')
titleimg = pygame.image.load("title.png")
chestimg = pygame.image.load('chest.png')
waterimg = pygame.image.load('water.png')
floatieimg = pygame.image.load('Floatie.png')
gatehor = pygame.image.load('gate2.png')
gatever = pygame.image.load('gate.png')
gatetr = pygame.image.load('gatetr.png')
gatebr = pygame.image.load('gatebr.png')
gatetl = pygame.image.load('gatetl.png')
gatebl = pygame.image.load('gatebl.png')
rock = pygame.image.load('Rock.png')
stone = pygame.image.load('Stone.png')
gameExit = False
resetGame = True
if resetGame:
    with open("Save.py","wb") as f:
        pickle.dump([inv,position,health],f)
with open('Save.py','rb') as f:
    foo = pickle.load(f)
position = foo[1]
inv = foo[0]
health = foo[2]
def addtree(x,y,touchx,touchy,img,blitimg,torf):
    if torf:
        game.blit(grass,(x,y))
    game.blit(blitimg,(x,y))
    #RIGHT
    if touchy == y and touchx == x-unit and img == avatarright or touchy == y and touchx == x-unit and img == blankimg:
        return 1
    #LEFT
    if touchy == y and touchx == x+unit and img == avatarleft or touchy == y and touchx == x+unit and img == blankimg:
        return 1
    #DOWN
    if touchy == y-unit and touchx == x and img == avatardown or touchy == y-unit and touchx == x and img == blankimg:
        return 2
    #UP
    if touchy == y+unit and touchx == x and img == avatarup or touchy == y+unit and touchx == x and img == blankimg:
        return 2
def sand(x,y):
    game.blit(sandbg,(x,y))
def hero(x,y,img):
    game.blit(img,(x,y))
def joinsand(img):
    hero(0,0,img)
    num = 0
    num2 = 0
    total = 0
    while True:
        num += 1
        hero(unit*num,num2,img)
        if num == 7:
            total += 1
            num = -1
            num2 += unit
        if total == 8:
            break
def disptree(name,x,y,touchx,touchy):
    keys = pygame.key.get_pressed()
    if position[name][2] == True and inv["Axe"] > 0 and position["axe"] < 20:
        tre = cuttree.tree(x,y,touchx,touchy)
        tre.show(game)
        if keys[pygame.K_RETURN] and tre.istouch() == True:
            inv["Wood"] += 2
            message("+2 Wood",black,displayw*0.6,30,15)
            pygame.display.flip()
            time.sleep(0.5)
            position[name][2] = False
            position["axe"] += 1
    elif position["axe"] == 20:
        inv["Axe"] -= 1
        position["axe"] = 0
def addenemy(name,x,y,touchx,touchy,img,enimg):
    a = True
    while a:
        keys = pygame.key.get_pressed()
        if position[name][2] == False and position[name][4] != 0:
            tre = Enemy.enemy(x,y,touchx,touchy,enimg)
            tre.show(game)
            if tre.istouch() == 1:
                if position[name][3] < 30:
                    position[name][3] += 1
                elif position[name][3] == 30:
                    health["Health"] -= 1
                    minmess(1,"Health")
                    position[name][3] = 0
                if keys[pygame.K_RETURN] and inv["Sword"] > 0:
                    if img == avatarright and enimg == avatarleft:
                        position[name][4] -= 1
                        break
                else:
                    return 1
            elif tre.istouch() == 2:
                if position[name][3] < 30:
                    position[name][3] += 1
                elif position[name][3] == 30:
                    health["Health"] -= 1
                    minmess(1,"Health")
                    position[name][3] = 0
                if keys[pygame.K_RETURN] and inv["Sword"] > 0:
                    if img == avatarleft and enimg == avatarright:
                        position[name][4] -= 1
                        break
                else:
                    return 2
            elif tre.istouch() == 3:
                if position[name][3] < 30:
                    position[name][3] += 1
                elif position[name][3] == 30:
                    health["Health"] -= 1
                    minmess(1,"Health")
                    position[name][3] = 0
                if keys[pygame.K_RETURN] and inv["Sword"] > 0:
                    if img == avatarup and enimg == avatardown:
                        position[name][4] -= 1
                        break
                else:
                    return 3
            elif tre.istouch() == 4:
                if position[name][3] < 30:
                    position[name][3] += 1
                elif position[name][3] == 30:
                    health["Health"] -= 1
                    minmess(1,"Health")
                    position[name][3] = 0
                if keys[pygame.K_RETURN] and inv["Sword"] > 0:
                    if img == avatardown and enimg == avatarup:
                        position[name][4] -= 1
                        break
                else:
                    return 4
        elif position[name][4] == 0 and position[name][2]== False:
            inv[position[name][5]] += 1
            plusmess(1,position[name][5])
            position[name][2] = True

        a = False
def plusmess(number,item):
    message("+"+str(number)+" "+item.lower(),black,displayw*0.6,30,15)
    pygame.display.update()
    time.sleep(0.5)
def minmess(number,item):
    message("-"+str(number)+" "+item.lower(),black,displayw*0.6,30,15)
    pygame.display.update()
    time.sleep(0.5)
def message(text,color,x,y,size):
    myfont = pygame.font.Font('PokemonGB.ttf',size)
    label = myfont.render(text, True, color)
    game.blit(label, (x,y))
def chest(name,x,y,touchx,touchy,num,torf):
    keys = pygame.key.get_pressed()
    if position[name][2] == False:
        chst = Chest.chest(x,y,touchx,touchy)
        chst.show(game)
        if torf:
            hero(x,y,floatieimg)
        if keys[pygame.K_RETURN] and chst.istouch() == True:
            game.blit(menuimg,(12.5,25))
            message("+"+str(num)+" "+position[name][3].lower(),black,130,95,15)
            inv[position[name][3]] += num
            pygame.display.update()
            time.sleep(1)
            position[name][2] = True
            return True
def enemy(x,y,touchx,touchy,blitimg):
    game.blit(blitimg,(x,y))
    #RIGHT
    if touchy == y and touchx == x-unit:
        return 1
    #LEFT
    if touchy == y and touchx == x+unit:
        return 1
    #DOWN
    if touchy == y-unit and touchx == x:
        return 2
    #UP
    if touchy == y+unit and touchx == x:
        return 2
def save():
    with open("Save.py","wb") as f:
        pickle.dump([inv,position,health],f)
def shop(lstitems,lstcost,item):
    shopExit = False
    num = 0
    length = 0
    sely = 97
    orderlst = []
    l2 = 97
    lengnum = 0
    credit = 0
    while not shopExit:
        time.sleep(0.15)
        num += 1
        if num == 1:
            sel = blankimg
        elif num == 2:
            sel = selectimg
            num = 0
        game.fill(brown)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_e:
                    sec4()
                elif event.key == pygame.K_DOWN:
                    if sely < length:
                        sely += 50
                elif event.key == pygame.K_UP:
                    if sely > 97:
                        sely -= 50
                elif event.key == pygame.K_RETURN:
                    for i in orderlst:
                        if sely == l2:
                            if orderlst[lengnum] == lstitems[lengnum]:
                                if inv[item] >= lstcost[lengnum]:
                                    inv[item] -= lstcost[lengnum]
                                    inv[lstitems[lengnum]] += 1
                                    plusmess(1,lstitems[lengnum])
                                l2 = 97
                                lengnum = 0
                            break
                        else:
                            l2 += 50
                            lengnum += 1
        hero(0,0,fullmenu)
        message("item",black,70,60,15)
        message("cost",black,300,60,15)
        length = 0
        for o in range(len(lstitems)):
            length += 50
        number = 100
        for i in lstitems:
            if i not in orderlst:
                orderlst.append(i)
            message(str(i)+":",black,70,number,10)
            number += 50
        number = 100
        for i in lstcost:
            if i not in orderlst:
                orderlst.append(i)
            message(str(i)+" "+str(item),black,300,number,10)
            number += 50
        hero(45,sely,sel)
        pygame.display.update()
        clock.tick(30)
def create(name,num):
        if name.Torf:
            if name.item1 in inv and inv[name.item1] > 0 and name.item2 in inv and inv[name.item2] > 0:
                message(name.result,black,70,num,11)
                message(name.item1,black,300,num-10,11)
                message(name.item2,black,300,num+10,11)
                return True
        else:
            if name.item1 in inv and inv[name.item1] > 0:
                message(name.result,black,70,num,11)
                message(name.item1,black,300,num,11)
                return True
def craft(x,y):
    craftExit = False
    num = 0
    length = 0
    sely = 97
    orderlst = []
    l2 = 97
    lengnum = 0
    credit = 0
    while not craftExit:
        time.sleep(0.15)
        num += 1
        if num == 1:
            sel = blankimg
        elif num == 2:
            sel = selectimg
            num = 0
        game.fill(brown)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_e:
                    menu(x,y)
                elif event.key == pygame.K_DOWN:
                    if sely < length:
                        sely += 50
                elif event.key == pygame.K_UP:
                    if sely > 97:
                        sely -= 50
                elif event.key == pygame.K_RETURN:
                    for i in orderlst:
                        if sely == l2:
                            if orderlst[lengnum] == "AppleSauce":
                                if appsa.Torf:
                                    if inv[appsa.item1] > 0:
                                        inv[appsa.item1] -= 1
                                        if inv[appsa.item2] > 0:
                                            inv[appsa.item2] -= 1
                                            inv[appsa.result] += 1
                                            inventory(x,y)
                                        else:
                                            inv[appsa.item1] += 1
                                else:
                                    inv[appsa.item1] -= 1
                                    inv[appsa.result] += 1
                                    inventory(x,y)
                                l2 = 97
                                lengnum = 0
                            elif orderlst[lengnum] == "Stick":
                                if stick.Torf:
                                    if inv[stick.item1] > 0:
                                        inv[stick.item1] -= 1
                                        if inv[stick.item2] > 0:
                                            inv[stick.item2] -= 1
                                            inv[stick.result] += 1
                                            inventory(x,y)
                                        else:
                                            inv[stick.item1] += 1
                                else:
                                    inv[stick.item1] -= 1
                                    inv[stick.result] += 1
                                    inventory(x,y)
                                l2 = 97
                                lengnum = 0
                            elif orderlst[lengnum] == "Board":
                                if board.Torf:
                                    if inv[board.item1] > 0:
                                        inv[board.item1] -= 1
                                        if inv[board.item2] > 0:
                                            inv[board.item2] -= 1
                                            inv[board.result] += 1
                                            inventory(x,y)
                                        else:
                                            inv[board.item1] += 1
                                else:
                                    inv[board.item1] -= 1
                                    inv[board.result] += 1
                                    inventory(x,y)
                                l2 = 97
                                lengnum = 0
                            elif orderlst[lengnum] == "Boat":
                                if boat.Torf:
                                    if inv[boat.item1] > 0:
                                        inv[boat.item1] -= 1
                                        if inv[boat.item2] > 0:
                                            inv[boat.item2] -= 1
                                            inv[boat.result] += 1
                                            inventory(x,y)
                                        else:
                                            inv[boat.item1] += 1
                                else:
                                    inv[boat.item1] -= 1
                                    inv[boat.result] += 1
                                    inventory(x,y)
                                l2 = 97
                                lengnum = 0
                            elif orderlst[lengnum] == "Axe":
                                if axe.Torf:
                                    if inv[axe.item1] > 0:
                                        inv[axe.item1] -= 1
                                        if inv[axe.item2] > 0:
                                            inv[axe.item2] -= 1
                                            inv[axe.result] += 1
                                            inventory(x,y)
                                        else:
                                            inv[axe.item1] += 1
                                else:
                                    inv[axe.item1] -= 1
                                    inv[axe.result] += 1
                                    inventory(x,y)
                                l2 = 97
                                lengnum = 0
                            break
                        else:
                            l2 += 50
                            lengnum += 1
        hero(0,0,fullmenu)
        message("item",black,70,60,15)
        message("cost",black,300,60,15)
        length = 0
        for o in range(numrec):
            length += 50
        number = 100
        if create(appsa,number):
            number += 50
            if appsa.result not in orderlst:
                orderlst.append(appsa.result)
        else:
            length -= 50
        if create(stick,number):
            number += 50
            if stick.result not in orderlst:
                orderlst.append(stick.result)
        else:
            length -= 50
        if create(board,number):
            number += 50
            if board.result not in orderlst:
                orderlst.append(board.result)
        else:
            length -= 50
        if create(boat,number):
            number += 50
            if boat.result not in orderlst:
                orderlst.append(boat.result)
        else:
            length -= 50
        if create(axe,number):
            number += 50
            if axe.result not in orderlst:
                orderlst.append(axe.result)
        else:
            length -= 50
        hero(45,sely,sel)
        pygame.display.update()
        clock.tick(30)
def h1():
    gameExit = True
    x = position["treehouse"][0]
    y = position["treehouse"][1]
    position["treehouse"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    position['xs'] = unit
    position['ys'] = unit*2
    num = 0
    while gameExit:
        game.fill(black)
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(woodbg)
        hero(unit*4,unit*7,sandbg)
        #CHEST
        if position["thchest"][2] == False and addtree(position["thchest"][0],position["thchest"][1],x,y,img,blankimg,False) == 1:
            xchange = 0
        elif position["thchest"][2] == False and addtree(position["thchest"][0],position["thchest"][1],x,y,img,blankimg,False) == 2:
            ychange = 0
        chest("thchest",position["thchest"][0],position["thchest"][1],x,y,1,False)
        if position["thchest"][2] == False and img == avatarup and x == unit*4 and y == unit*5:
            game.blit(menuimg,(12.5,25))
            message("What a mysterious chest..",black,35,55,13)
            message("Press Enter to open.",black,85,125,11)
        #oldman
        if position["oldmanhelp"][5]:
            hero(unit*4,unit*4,avatar)
            if keys[pygame.K_RETURN]:
                num += 1
            game.blit(menuimg,(12.5,25))
            if num == 0:
                message("My sword has been stolen!",black,35,55,13)
                message("Press Enter.",black,85,125,11)
            elif num == 1:
                message("Oh, you have taken it..",black,35,55,13)
                message("Press Enter.",black,85,125,11)
            elif num == 2:
                message("Well you saved me so..",black,35,55,13)
                message("Press Enter.",black,85,125,11)
            elif num == 3:
                message("Keep it!",black,35,55,13)
                message("Press Enter.",black,85,125,11)
            elif num == 4:
                message("Maybe you can help",black,35,55,13)
                message("the people here...",black,65,125,13)
            elif num == 5:
                message("This may be of use to you.",black,35,55,13)
                message("Press Enter",black,65,125,11)
            elif num == 6:
                inv["Gold"] += 12
                message("+12 gold",black,35,55,13)
                pygame.display.update()
                time.sleep(1)
                position["oldmanhelp"][5] = False
                position["oldmanhelp"][6] = True
        if position["oldmanhelp"][6]:
            hero(unit*4,unit*4,avatar)
        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == unit*4 and y == unit*7 and img == avatardown:
            if keys[pygame.K_DOWN]:
                main()
        pygame.display.update()
        clock.tick(30)
def d1():
    gameExit = False
    x = position["Dungeon1"][0]
    y = position["Dungeon1"][1]
    position["Dungeon1"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    position["sec6"][0] = unit*6
    position['sec6'][1] = unit
    while not gameExit:
        game.fill(black)
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(stone)
        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == unit*6 and y == unit*7 and img == avatardown:
            if keys[pygame.K_DOWN]:
                position["Dungeon1"][2] = False
                position["sec6"][0] = x
                position["sec6"][1] = unit*2
                sec6()
        pygame.display.update()
        clock.tick(30)
def start():
    gameExit = True
    while gameExit:
        game.fill(brown)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    if position["treehouse"][2] == True:
                        h1()
                    elif position["sec1"][2] == True:
                        sec1()
                    elif position["sec2"][2] == True:
                        sec2()
                    elif position["sec3"][2] == True:
                        sec3()
                    elif position["sec4"][2] == True:
                        sec4()
                    elif position["sec5"][2] == True:
                        sec5()
                    elif position["sec5"][2] == True:
                        sec5()
                    else:
                        main()
        hero(13,100,titleimg)
        message("Press enter",black,140,200,11)
        pygame.display.update()
        clock.tick(30)
def inventory(x,y):
    inventoryExit = False
    num = 0
    sely = 87
    length = 57
    orderlst = []
    lengnum = 0
    l2 = 87
    for u in inv:
        if inv[u] > 0:
            length += 30
    while not inventoryExit:
        number = 50
        time.sleep(0.3)
        num += 1
        if num == 1:
            sel = blankimg
        elif num == 2:
            sel = selectimg
            num = 0
        game.fill(brown)
        orderlst = list(inv.keys())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_e:
                    menu(x,y)
                elif event.key == pygame.K_DOWN:
                    if sely < length:
                        sely += 30
                elif event.key == pygame.K_UP:
                    if sely > 87:
                        sely -= 30
                elif event.key == pygame.K_RETURN:
                    for i in orderlst:
                        if sely == l2:
                            if orderlst[lengnum] == "Apple" and health["Health"] < 10 and inv["Apple"] > 0:
                                inv["Apple"] -= 1
                                health["Health"] += 1
                            elif orderlst[lengnum] == "Water" and health["Water"] < 10 and inv["Water"] > 0:
                                inv["Water"] -= 1
                                health["Water"] += 1
                            elif orderlst[lengnum] == "AppleSauce" and health["Water"] < 10 and inv["AppleSauce"] > 0 and health["Food"] < 10:
                                inv["AppleSauce"] -= 1
                                health["Water"] += 1
                                health["Food"] += 1
                            break
                        else:
                            l2 += 30
                            lengnum += 1
        game.blit(fullmenu,(0,0))
        number = 90
        message("inventory",black,displayw/2-60,55,15)
        for z in inv:
            if inv[z] > 0:
                message(str(z)+":",black,displayw/2-70,number,10)
                number += 30
        number = 90
        for z in inv.values():
            if z > 0:
                message(str(z),black,displayw/2+70,number,10)
                number += 30
        hero(displayw/2-93,sely,sel)
        pygame.display.update()
        clock.tick(30)
def menu(x,y):
    if position["sec1"][2] == True:
        position["sec1"][0] = x
        position["sec1"][1] = y
    elif position["treehouse"][2] == True:
        position["treehouse"][0] = x
        position["treehouse"][1] = y
    elif position["sec2"][2] == True:
        position["sec2"][0] = x
        position["sec2"][1] = y
    elif position["sec3"][2] == True:
        position["sec3"][0] = x
        position["sec3"][1] = y
    elif position["sec4"][2] == True:
        position["sec4"][0] = x
        position["sec4"][1] = y
    elif position["sec5"][2] == True:
        position["sec5"][0] = x
        position["sec5"][1] = y
    elif position["sec6"][2] == True:
        position["sec6"][0] = x
        position["sec6"][1] = y
    else:
        position["xs"] = x
        position["ys"] = y
    gameExit = True
    num = 0
    sely = 247
    while gameExit:
        time.sleep(0.3)
        num += 1
        game.fill(brown)
        if num == 1:
            sel = blankimg
        elif num == 2:
            sel = selectimg
            num = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_e:
                    if position["treehouse"][2] == True:
                        h1()
                    elif position["sec1"][2] == True:
                        sec1()
                    elif position["sec2"][2] == True:
                        sec2()
                    elif position["sec3"][2] == True:
                        sec3()
                    elif position["sec4"][2] == True:
                        sec4()
                    elif position["sec5"][2] == True:
                        sec5()
                    elif position["sec6"][2] == True:
                        sec6()
                    else:
                        main()
                elif event.key == pygame.K_DOWN:
                    if sely < 247+80:
                        sely += 40
                elif event.key == pygame.K_UP:
                    if sely > 247:
                        sely -= 40
                elif event.key == pygame.K_RETURN:
                    if sely == 247:
                        inventory(x,y)
                    if sely == 247 +80:
                        save()
                        time.sleep(1)
                        message("saving..",white,10,10,12)
                    if sely == 247+40:
                        craft(x,y)
        game.blit(menu2img,(195,200))
        game.blit(menuimg,(12.5,25))
        game.blit(menu2img,(14,200))
        message("Link",black,90,230,12)
        message("drink:",black,45,270,12)
        message(str(health["Water"]),black,135,270,12)
        message("food:",black,45,310,12)
        message(str(health["Food"]),black,135,310,12)
        message("health:",black,45,350,12)
        message(str(health["Health"]),black,135,350,12)
        message("What do you want to do?",black,35,50,13)
        message("Bag",black,250,250,13)
        message("Craft",black,250,290,13)
        message("Save",black,250,330,13)
        hero(220,sely,sel)
        pygame.display.update()
        clock.tick(30)
def sec1():
    gameExit = False
    x = position["sec1"][0]
    y = position["sec1"][1]
    position["sec1"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    position['xs'] = unit*7
    position['ys'] = unit*4
    while not gameExit:
        game.fill(black)
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(sandbg)
        #Trees
        if addtree(0,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*3,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*3,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*4,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*4,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*5,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*5,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*3,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*3,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*4,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*4,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*5,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*5,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*3,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*3,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*4,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*4,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*5,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*5,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*3,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*3,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*4,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*4,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*5,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*5,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*6,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*6,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*3,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*3,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*4,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*4,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*5,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*5,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*6,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*6,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*3,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*3,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*5,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*5,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*3,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*3,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*5,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*5,x,y,img,treeimg,True) == 2:
            ychange = 0
        #CHESTTREE
        if addtree(unit*6,unit,x,y,img,blankimg,False) == 1 and position["trees162"][2] == True:
            xchange = 0
        elif addtree(unit*6,unit,x,y,img,blankimg,False) == 2 and position["trees162"][2] == True:
            ychange = 0
        if addtree(position["s1chest"][0],position["s1chest"][1],x,y,img,blankimg,False) == 1 and position["s1chest"][2] == False:
            xchange = 0
        elif addtree(position["s1chest"][0],position["s1chest"][1],x,y,img,blankimg,False) == 2 and position["s1chest"][2] == False:
            ychange = 0
        #Hero
        x += xchange
        y += ychange
        hero(unit*6,0,grass)
        hero(unit*6,unit,grass)
        hero(unit*6,unit*2,grass)
        hero(unit*6,unit,treeimg)
        hero(x,y,img)
        #CHEST
        chest("s1chest",position["s1chest"][0],position["s1chest"][1],x,y,6,False)
        if position["s1chest"][2] == False and img == avatarup and x == unit*6 and y == unit:
            game.blit(menuimg,(12.5,25))
            message("What a mysterious chest..",black,35,55,13)
            message("Press Enter to open.",black,85,125,11)

        #Cuttree
        disptree("trees162",position["trees162"][0],position["trees162"][1],x,y)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == 0 and y == unit*4 and img == avatarleft:
            if keys[pygame.K_LEFT]:
                position["sec1"][2] = False
                main()
        #sec2
        if x == unit*7 and y == unit*4 and img == avatarright:
            if keys[pygame.K_RIGHT]:
                position["sec2"][0] = 0
                position["sec2"][1] = unit*4
                position["sec1"][2] = False
                sec2()
        pygame.display.update()
        clock.tick(30)
def sec2():
    gameExit = False
    x = position["sec2"][0]
    y = position["sec2"][1]
    position["sec2"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    en2img = avatar
    position["sec1"][0] = unit*7
    position['sec1'][1] = unit*4
    tempnum = 0
    while not gameExit:
        game.fill(black)
        if img == avatarup:
            image["img"] = 0
        elif img == avatardown:
            image["img"] = 1
        elif img == avatarright:
            image["img"] = 2
        elif img == avatarleft:
            image["img"] = 3
        else:
            if image["img"] == 0:
                img = avatarup
            elif image["img"] == 1:
                img = avatardown
            elif image["img"] == 2:
                img = avatarright
            elif image["img"] == 3:
                img = avatarleft
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
                elif event.key == pygame.K_RETURN:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(sandbg)
        #Sea
        if addtree(unit*7,0,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,0,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit*2,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*2,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit*3,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*3,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit*4,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*4,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit*5,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*5,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit*6,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*6,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*7,unit*7,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*7,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,0,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,0,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit*2,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*2,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit*3,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*3,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit*4,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*4,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit*5,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*5,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit*6,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*6,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit*6,unit*7,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*7,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        #Trees
        if addtree(0,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*3,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*3,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*5,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*5,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        #enemy
        if addenemy("s2enemy33",position["s2enemy33"][0],position["s2enemy33"][1],x,y,img,en2img) == 1:
            xchange = 0
            en2img = avatarleft
        elif addenemy("s2enemy33",position["s2enemy33"][0],position["s2enemy33"][1],x,y,img,en2img) == 2:
            xchange = 0
            en2img = avatarright
        elif addenemy("s2enemy33",position["s2enemy33"][0],position["s2enemy33"][1],x,y,img,en2img) == 3:
            ychange = 0
            en2img = avatardown
        elif addenemy("s2enemy33",position["s2enemy33"][0],position["s2enemy33"][1],x,y,img,en2img) == 4:
            ychange = 0
            en2img = avatarup
        elif position["s2enemy33"][1] < unit*7 and position["s2enemy33"][1] > 0 and en2img != avatarup and position["s2enemy33"][1] < unit*7 and position["s2enemy33"][1] > 0 and en2img != avatardown:
            en2img = avatarup
        elif position["s2enemy33"][1] < unit*7 and position["s2enemy33"][1] > 0 and en2img == avatardown:
            position["s2enemy33"][1] += unit
        elif position["s2enemy33"][1] == unit*7:
            en2img = avatarup
            position["s2enemy33"][1] -= unit
        elif position["s2enemy33"][1] < unit*7 and position["s2enemy33"][1] > 0 and en2img == avatarup:
            position["s2enemy33"][1] -= unit
        elif position["s2enemy33"][1] == 0:
            en2img = avatardown
            position["s2enemy33"][1] += unit
        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == 0 and y == unit*4 and img == avatarleft:
            if keys[pygame.K_LEFT]:
                position["sec2"][2] = False
                sec1()
        #sec3
        if x == unit*7 and img == avatarright:
            if keys[pygame.K_RIGHT]:
                position["sec3"][0] = 0
                position["sec3"][1] = y
                position["sec2"][2] = False
                sec3()
        pygame.display.update()
        clock.tick(30)
def sec3():
    gameExit = False
    x = position["sec3"][0]
    y = position["sec3"][1]
    position["sec3"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    position["sec2"][0] = unit*7
    position['sec2'][1] = unit*4
    enimg = avatarright
    while not gameExit:
        game.fill(black)
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(waterimg)
        #CHEST
        if position["s3chest"][2] == False and addtree(position["s3chest"][0],position["s3chest"][1],x,y,img,blankimg,False) == 1:
            xchange = 0
        elif position["s3chest"][2] == False and addtree(position["s3chest"][0],position["s3chest"][1],x,y,img,blankimg,False) == 2:
            ychange = 0
        chest("s3chest",position["s3chest"][0],position["s3chest"][1],x,y,1,True)
        if position["s3chest"][2] == False and img == avatarup and x == unit*6 and y == unit*2 or position["s3chest"][2] == False and img == blankimg and x == unit*6 and y == unit*2:
            img = blankimg
            game.blit(menuimg,(12.5,25))
            message("What a mysterious chest..",black,35,55,13)
            message("Press Enter to open.",black,85,125,11)
        elif position["s3chest"][2] == True and img == blankimg and x == unit*6 and y == unit*2:
            img = avatarup
        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == 0 and img == avatarleft:
            if keys[pygame.K_LEFT]:
                position["sec3"][2] = False
                position["sec2"][0] = unit*7
                position["sec2"][1] = y
                sec2()
        if x == unit*7 and img == avatarright:
            if keys[pygame.K_RIGHT]:
                position["sec3"][2] = False
                position["sec4"][0] = 0
                position["sec4"][1] = y
                sec4()
        pygame.display.update()
        clock.tick(30)
def sec4():
    gameExit = False
    x = position["sec4"][0]
    y = position["sec4"][1]
    position["sec4"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    temp = 0
    position["sec3"][0] = unit*7
    position['sec3'][1] = unit*4
    while not gameExit:
        game.fill(black)
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        joinsand(sandbg)
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        #Sea
        if addtree(0,0,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,0,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit*2,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit*2,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit*3,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit*3,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit*4,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit*4,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit*5,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit*5,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit*6,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit*6,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(0,unit*7,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(0,unit*7,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,0,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,0,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit*2,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit*2,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit*3,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit*3,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit*4,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit*4,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit*5,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit*5,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit*6,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit*6,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        if addtree(unit,unit*7,x,y,img,waterimg,False) == 1 and inv["Boat"] == 0:
            xchange = 0
        elif addtree(unit,unit*7,x,y,img,waterimg,False) == 2 and inv["Boat"] == 0:
            ychange = 0
        #Shop
        hero(unit*7,unit*7,avatar)
        if addtree(unit*6,unit*6,x,y,img,woodbg,False) == 1:
            xchange = 0
        elif addtree(unit*6,unit*6,x,y,img,woodbg,False) == 2:
            ychange = 0
        if addtree(unit*6,unit*7,x,y,img,woodbg,False) == 1:
            xchange = 0
        elif addtree(unit*6,unit*7,x,y,img,woodbg,False) == 2:
            ychange = 0
        if addtree(unit*7,unit*6,x,y,img,woodbg,False) == 1:
            xchange = 0
        elif addtree(unit*7,unit*6,x,y,img,woodbg,False) == 2:
            ychange = 0
            game.blit(menuimg,(12.5,25))
            if keys[pygame.K_RETURN]:
                temp += 1
            if temp == 0:
                message("Hello! Welcome to my shop.",black,35,55,12)
                message("Enter",black,85,125,11)
            if temp == 1:
                message("You are not from around here.",black,35,55,12)
                message("Enter",black,85,125,11)
            if temp == 2:
                message("We don't get many visitors..",black,35,55,12)
                message("..the King doesn't like them.",black,35,85,12)
                message("Enter",black,85,125,11)
            if temp == 3:
                message("oh well, what would you like?",black,30,55,12)
                message("press Enter to shop",black,85,125,11)
            if temp == 4:
                temp = 0
                position["sec4"][0] = unit*7
                position["sec4"][1] = unit*5
                shop(position["s4shop77"][0],position["s4shop77"][1],"Key")


        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)

        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == 0 and img == avatarleft:
            if keys[pygame.K_LEFT]:
                position["sec4"][2] = False
                position["sec3"][0] = unit*7
                position["sec3"][1] = y
                sec3()
        if x == unit*7 and y < unit*6 and img == avatarright:
            if keys[pygame.K_RIGHT]:
                position["sec4"][2] = False
                position["sec5"][0] = 0
                position["sec5"][1] = y
                sec5()
        pygame.display.update()
        clock.tick(30)
def sec5():
    gameExit = False
    x = position["sec5"][0]
    y = position["sec5"][1]
    position["sec5"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    enimg = avatar
    en2img = avatar
    tempnum = 0
    tempnum2 = 0
    position["sec4"][0] = unit*7
    position['sec4'][1] = unit*4
    gateclosed = gatetl
    gateclosed2 = gatever
    oldmanx = position["oldmanhelp"][3]
    oldmany = position["oldmanhelp"][4]
    oldmanimg = avatar
    num = 0
    tempnum3 = 0
    while not gameExit:
        game.fill(black)
        if img == avatarup:
            image["img"] = 0
        elif img == avatardown:
            image["img"] = 1
        elif img == avatarright:
            image["img"] = 2
        elif img == avatarleft:
            image["img"] = 3
        else:
            if image["img"] == 0:
                img = avatarup
            elif image["img"] == 1:
                img = avatardown
            elif image["img"] == 2:
                img = avatarright
            elif image["img"] == 3:
                img = avatarleft
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(sandbg)
        #Old man
        hero(oldmanx,oldmany,oldmanimg)
        if addtree(unit*6,unit*6,x,y,img,gateclosed,False) == 1 and inv["Key"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*6,x,y,img,gateclosed,False) == 2 and inv["Key"] == 0:
            ychange = 0
        if addtree(unit*6,unit*7,x,y,img,gateclosed2,False) == 1 and inv["Key"] == 0:
            xchange = 0
        elif addtree(unit*6,unit*7,x,y,img,gateclosed2,False) == 2 and inv["Key"] == 0:
            ychange = 0
        if addtree(unit*7,unit*6,x,y,img,gatehor,False) == 1 and inv["Key"] == 0:
            xchange = 0
        elif addtree(unit*7,unit*6,x,y,img,gatehor,False) == 2 and inv["Key"] == 0:
            ychange = 0
        #OLD MAN HELP
        if not position["oldmanhelp"][0]:
            if not position["oldmanhelp"][2]:
                game.blit(menuimg,(12.5,25))
                message("HEY! OVER HERE!",black,35,55,13)
                message("HELP ME!",black,85,125,13)
                pygame.display.update()
                time.sleep(1)
                position["oldmanhelp"][0] = True
            if position["oldmanhelp"][2]:
                if keys[pygame.K_RETURN]:
                    num += 1
                game.blit(menuimg,(12.5,25))
                if num == 0:
                    message("Thank you for helping!",black,35,55,13)
                    message("Press enter",black,35,85,11)
                elif num == 1:
                    message("Visit my house anytime!",black,35,55,13)
                    message("Press enter",black,35,85,11)
                elif num == 2:
                    position["oldmanhelp"][0] = True
                    position["oldmanhelp"][5] = True
        if position["oldmanhelp"][0] and position["oldmanhelp"][2] and oldmanx > -unit*2:
            if oldmanx == unit*4 or oldmanx == unit*5:
                oldmanimg = avatarup
                oldmany -= unit
                position["oldmanhelp"][3] = oldmanx
                position["oldmanhelp"][4] = oldmany
            if oldmanx > -unit:
                oldmanimg = avatarleft
                oldmanx -= unit
                position["oldmanhelp"][3] = oldmanx
                position["oldmanhelp"][4] = oldmany
        #ENEMY
        if addenemy("s5enemy33",position["s5enemy33"][0],position["s5enemy33"][1],x,y,img,enimg) == 1:
            xchange = 0
            enimg = avatarleft
        elif addenemy("s5enemy33",position["s5enemy33"][0],position["s5enemy33"][1],x,y,img,enimg) == 2:
            xchange = 0
            enimg = avatarright
        elif addenemy("s5enemy33",position["s5enemy33"][0],position["s5enemy33"][1],x,y,img,enimg) == 3:
            ychange = 0
            enimg = avatardown
        elif addenemy("s5enemy33",position["s5enemy33"][0],position["s5enemy33"][1],x,y,img,enimg) == 4:
            ychange = 0
            enimg = avatarup
        elif position["s5enemy33"][0] < unit*7 and position["s5enemy33"][0] > 0 and enimg != avatarright and position["s5enemy33"][0] < unit*7 and position["s5enemy33"][0] > 0 and enimg != avatarleft:
            enimg = avatarright
        elif position["s5enemy33"][0] < unit*7 and position["s5enemy33"][0] > 0 and enimg == avatarright:
            position["s5enemy33"][0] += unit
        elif position["s5enemy33"][0] == unit*7:
            enimg = avatarleft
            position["s5enemy33"][0] -= unit
        elif position["s5enemy33"][0] < unit*7 and position["s5enemy33"][0] > 0 and enimg == avatarleft:
            position["s5enemy33"][0] -= unit
        elif position["s5enemy33"][0] == 0:
            enimg = avatarright
            position["s5enemy33"][0] += unit
        #2nd enemy
        if addenemy("s5enemy74",position["s5enemy74"][0],position["s5enemy74"][1],x,y,img,en2img) == 1:
            xchange = 0
            en2img = avatarleft
        elif addenemy("s5enemy74",position["s5enemy74"][0],position["s5enemy74"][1],x,y,img,en2img) == 2:
            xchange = 0
            en2img = avatarright
        elif addenemy("s5enemy74",position["s5enemy74"][0],position["s5enemy74"][1],x,y,img,en2img) == 3:
            ychange = 0
            en2img = avatardown
        elif addenemy("s5enemy74",position["s5enemy74"][0],position["s5enemy74"][1],x,y,img,en2img) == 4:
            ychange = 0
            en2img = avatarup
        elif position["s5enemy74"][1] < unit*7 and position["s5enemy74"][1] > 0 and en2img != avatarup and position["s5enemy74"][1] < unit*7 and position["s5enemy74"][1] > 0 and en2img != avatardown:
            en2img = avatarup
        elif position["s5enemy74"][1] < unit*7 and position["s5enemy74"][1] > 0 and en2img == avatardown:
            position["s5enemy74"][1] += unit
        elif position["s5enemy74"][1] == unit*7:
            en2img = avatarup
            position["s5enemy74"][1] -= unit
        elif position["s5enemy74"][1] < unit*7 and position["s5enemy74"][1] > 0 and en2img == avatarup:
            position["s5enemy74"][1] -= unit
        elif position["s5enemy74"][1] == 0:
            en2img = avatardown
            position["s5enemy74"][1] += unit
        #Key
        if position["oldmanhelp"][2]:
            gateclosed = gatehor
            gateclosed2 = gatetr
        if position["s5enemy74"][2] == True and position["s5enemy33"][2] == True and position["oldmanhelp"][0] and inv["Key"] == 0 and position["oldmanhelp"][2] == False:
            if tempnum3 == 1:
                inv["Key"] += 1
                plusmess(1,"Key")
                tempnum3 += 1
                gateclosed = gatehor
                gateclosed2 = gatetr
                position["oldmanhelp"][0] = False
                position["oldmanhelp"][2] = True
            else:
                tempnum3 += 1
        elif position["s5enemy74"][2] == True and position["s5enemy33"][2] == True and position["oldmanhelp"][0] and inv["Key"] == 1:
            if tempnum3 == 0:
                tempnum3 += 1
                gateclosed = gatehor
                gateclosed2 = gatetr
        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == 0 and y < unit*6 and img == avatarleft:
            if keys[pygame.K_LEFT]:
                position["sec5"][2] = False
                position["sec4"][0] = unit*7
                position["sec4"][1] = y
                sec4()
        if x == unit*7 and img == avatarright:
            if keys[pygame.K_RIGHT]:
                position["sec5"][2] = False
                position["sec6"][0] = 0
                position["sec6"][1] = y
                sec6()
        pygame.display.update()
        clock.tick(30)
def sec6():
    gameExit = False
    x = position["sec6"][0]
    y = position["sec6"][1]
    position["sec6"][2] = True
    xchange = 0
    ychange = 0
    img = avatar
    position["sec5"][0] = unit*7
    position['sec5'][1] = unit*4
    num = 0
    while not gameExit:
        game.fill(black)
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        joinsand(sandbg)
        #Cave
        if addtree(unit*7,0,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*7,0,x,y,img,rock,True) == 2:
            ychange = 0
        if addtree(unit*6,0,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*6,0,x,y,img,rock,True) == 2:
            ychange = 0
        if addtree(unit*5,0,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*5,0,x,y,img,rock,True) == 2:
            ychange = 0
        if addtree(unit*4,0,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*4,0,x,y,img,rock,True) == 2:
            ychange = 0
        if addtree(unit*7,unit,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit,x,y,img,rock,True) == 2:
            ychange = 0
        if addtree(unit*6,unit,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*6,unit,x,y,img,rock,True) == 2:
            ychange = 0
        if addtree(unit*5,unit,x,y,img,rock,True) == 1:
            xchange = 0
        elif addtree(unit*5,unit,x,y,img,rock,True) == 2:
            ychange = 0
        hero(unit*5,0,houseimg)
        #Guard
        if addtree(position["S6guard61"][0],position["S6guard61"][1],x,y,img,avatar,False) == 1:
            xchange = 0
        elif addtree(position["S6guard61"][0],position["S6guard61"][1],x,y,img,avatar,False) == 2:
            ychange = 0
            if keys[pygame.K_RETURN]:
                num += 1
            game.blit(menuimg,(12.5,25))
            img = blankimg
            if not position["S6guard61"][2]:
                if num == 0:
                    message("You can't come in here.",black,35,55,13)
                    message("Press enter",black,35,85,11)
                elif num == 1 and inv["Gold"] < 20:
                    message("SCRAM!",black,35,55,13)
                    message("Press enter",black,35,85,11)
                elif num == 2 and inv["Gold"] < 20:
                    y += unit
                    img = avatardown
                    num = 0
                elif num == 1 and inv["Gold"] >= 20:
                    message("Oh, I see you have money..",black,35,55,13)
                    message("Press enter",black,35,85,11)
                elif num >= 2 and inv["Gold"] >= 20:
                    message("20 Gold and you're in.",black,35,55,13)
                    message("y or n",black,65,105,11)
                    if keys[pygame.K_y]:
                        position["S6guard61"][0] -= unit
                        inv["Gold"] -= 20
                        img = avatarup
                        num = 0
                        position["S6guard61"][2] = True
                    elif keys[pygame.K_n]:
                        y += unit
                        img = avatardown
                        num = 0
            elif position["S6guard61"][2]:
                num = 0
                if num == 0:
                    message("Hopefully the king won't know.",black,35,55,11)
                    num = 0


        #Hero
        x += xchange
        y += ychange
        hero(x,y,img)
        #Hunger and Thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        #Exit
        if x == 0 and img == avatarleft:
            if keys[pygame.K_LEFT]:
                position["sec6"][2] = False
                position["sec5"][0] = unit*7
                position["sec5"][1] = y
                sec5()
        if x == unit*6 and img == avatarup:
            if keys[pygame.K_UP]:
                position["sec6"][2] = False
                position["Dungeon1"][0] = x
                position["Dungeon1"][1] = unit*7
                d1()
        pygame.display.update()
        clock.tick(30)
def main():
    position["treehouse"][2] = False
    x = position["xs"]
    y = position["ys"]
    position['treehouse'][0] = unit*4
    position['treehouse'][1] = unit*7
    xchange = 0
    ychange = 0
    img = avatar
    gameExit = False
    while not gameExit:
        time.sleep(0.15)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    ychange -= unit
                    img = avatarup
                elif event.key == pygame.K_DOWN:
                    ychange += unit
                    img = avatardown
                elif event.key == pygame.K_LEFT:
                    xchange -= unit
                    img = avatarleft
                elif event.key == pygame.K_RIGHT:
                    xchange += unit
                    img = avatarright
                elif event.key == pygame.K_e:
                    menu(x,y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0
        #borders
        if x == 0 and img == avatarleft:
            xchange = 0
        if x+sandw == displayw and img == avatarright:
            xchange = 0
        if y == 0 and img == avatarup:
            ychange = 0
        if y+sandw == displayh and img == avatardown:
            ychange = 0
        game.fill(black)
        joinsand(sandbg)
        #Trees
        if addtree(unit*2,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,0,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,0,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*2,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*2,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*3,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*3,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*5,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*5,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*6,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*6,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*7,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*7,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(0,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(0,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*2,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*2,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*3,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*3,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*4,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*4,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*5,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*5,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        if addtree(unit*6,unit*7,x,y,img,treeimg,True) == 1:
            xchange = 0
        elif addtree(unit*6,unit*7,x,y,img,treeimg,True) == 2:
            ychange = 0
        #hero
        hero(0,0,houseimg)
        x += xchange
        y += ychange
        hero(x,y,img)
        #Cuttree
        disptree("tree2",position["tree2"][0],position["tree2"][1],x,y)
        disptree("tree74",position["tree74"][0],position["tree74"][1],x,y)
        disptree("tree2",position["tree2"][0],position["tree2"][1],x,y)
        #house1
        if position["tree2"][2] == False and x == unit and y == unit*2 and img == avatarup:
            if keys[pygame.K_UP]:
                h1()
        #Sec1Right
        if position["tree74"][2] == False and x == unit*7 and y == unit*4 and img == avatarright:
            if keys[pygame.K_RIGHT]:
                position["sec1"][0] = 0
                position["sec1"][1] = unit*4
                sec1()
        #Hunger and thirst
        health["Hunger"] += 1
        health["Thirst"] += 1
        if health["Hunger"] == 1922:
            health["Food"] -= 1
        if health["Thirst"] == 1922 * 0.5:
            health["Water"] -= 1
        pygame.display.update()
        clock.tick(30)
start()
pygame.quit()
