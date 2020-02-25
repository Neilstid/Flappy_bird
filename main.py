import pygame
import random
import sys
from datetime import datetime
import time


# Pipe---------------------------------------------------------------------------------------------------------
class Pipe:
    def __init__(self):
        # pipe image
        self.size_pipe = (int(parameterGame.get_size_frame_x() / 20), int(parameterGame.get_size_frame_y() / 1.25))
        self.pipes_image = pygame.image.load("pipes.png")  # load image
        self.pipes_image = pygame.transform.scale(self.pipes_image, self.size_pipe)  # transform image to be correct
        self.pipes_gap = 130

        self.list_random = []
        self.start_position_random()

        # define the upper pipe
        self.pipes_up = [GameObject(self.pipes_image, parameterGame.get_size_frame_x(),
                                    self.list_random[0] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() +
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[1] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 2 *
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[2] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 3 *
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[3] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 4 *
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[4] - self.pipes_gap, 1)]

        # define the lower pipe
        # each pipe are Gameobject, define by the image of the pipe define higher, and their position. They split screen
        # by the needed
        self.pipes_down = [GameObject(self.pipes_image, parameterGame.get_size_frame_x(),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[0], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() +
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[1], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 2 *
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[2], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 3 *
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[3], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 4 *
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[4], 1)]

        self.clear_list()  # clear unused pipes

    # redifine the pipes
    def reset(self):
        # define the upper pipe
        self.pipes_up = [GameObject(self.pipes_image, parameterGame.get_size_frame_x(),
                                    self.list_random[0] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() +
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[1] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 2 *
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[2] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 3 *
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[3] - self.pipes_gap, 1),
                         GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 4 *
                                                          (
                                                                  parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                    self.list_random[4] - self.pipes_gap, 1)]

        # define the lower pipe
        self.pipes_down = [GameObject(self.pipes_image, parameterGame.get_size_frame_x(),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[0], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() +
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[1], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 2 *
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[2], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 3 *
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[3], 1),
                           GameObject(self.pipes_image, int(parameterGame.get_size_frame_x() + 4 *
                                                            (
                                                                    parameterGame.get_size_frame_x() / parameterGame.get_number_pipe())),
                                      parameterGame.get_size_frame_y() / 2 + self.pipes_gap + self.list_random[4], 1)]

        self.clear_list()

    # clear unused pipes
    def clear_list(self):
        # for each value out of the number wanted
        for val in range(parameterGame.get_number_pipe(), len(self.pipes_up)):
            self.pipes_up.pop()  # clear last for upper
            self.pipes_down.pop()  # clear last for lower

    # return upper pipe
    def get_pipes_up(self):
        return self.pipes_up

    # return lower pipe
    def get_pipes_down(self):
        return self.pipes_down

    def get_pipe_gap(self):
        return self.pipes_gap

    def set_pipe_gap(self, gap):
        self.pipes_gap = gap

    def start_position_random(self):
        list_random = []
        for element in range(6):
            self.list_random.append(random.randint(-380 + self.get_pipe_gap(), 245 - self.get_pipe_gap()))


# parameters------------------------------------------------------------------------------------------------------------
class Parameters:
    def __init__(self, frame_size_x=720, frame_size_y=480, speed_of_player=10, number_of_pipe=2,
                 number_fps=100, difficulty="Medium"):
        # Window size
        self.frame_size_x = frame_size_x
        self.frame_size_y = frame_size_y
        # set the speed fo jump of the player
        self.speed_of_player = speed_of_player
        # number of pipe per screen
        self.number_of_pipe = number_of_pipe
        # number of frame per second
        self.number_fps = number_fps
        # difficulty
        self.difficulty = difficulty

    # set the frame size
    def set_frame_size(self, size_x, size_y):
        self.frame_size_x = size_x
        self.frame_size_y = size_y

    # set the speed of the player
    def set_difficulty_player(self, difficulty="Pers", speedness=0):
        if difficulty == "Easy":
            self.number_fps = 50
            pipes.set_pipe_gap(175)
            self.difficulty = difficulty
        elif difficulty == "Medium":
            self.number_fps = 100
            pipes.set_pipe_gap(130)
            self.difficulty = difficulty
        elif difficulty == "Hardcore":
            self.number_fps = 200
            pipes.set_pipe_gap(115)
            self.difficulty = difficulty
        elif difficulty == "Pers":
            self.speed_of_player = speedness

    # set the number of pipe
    def set_number_pipe(self, number):
        self.number_of_pipe = number

    # set the number of fps
    def set_number_fps(self, number):
        self.number_fps = number

    def get_size_frame_x(self):
        return self.frame_size_x

    def get_size_frame_y(self):
        return self.frame_size_y

    def get_speed_player(self):
        return self.speed_of_player

    def get_number_pipe(self):
        return self.number_of_pipe

    def get_number_fps(self):
        return self.number_fps


# parameter will be reminded in parameterGame
parameterGame = Parameters()

# Init the game---------------------------------------------------------------------------------------------------------
random.seed(datetime.now())  # define a seed

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Checks for errors encountered
check_errors = pygame.init()

# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Flappy Bird')
screen = pygame.display.set_mode((parameterGame.get_size_frame_x(), parameterGame.get_size_frame_y()))
# screen = pygame.display.set_mode((parameterGame.get_size_frame_x(), parameterGame.get_size_frame_y()),
# pygame.FULLSCREEN)

# set the icon
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)

# Define if the game is running or not
game_running = 1

# background
background = pygame.image.load("background2.png")
background = pygame.transform.scale(background, (parameterGame.get_size_frame_x(), parameterGame.get_size_frame_y()))
screen.blit(background, (0, 0))

# game over
game_over_image = pygame.image.load("gameover.png")
game_over_image = pygame.transform.scale(game_over_image, (208, 56))

# setting fps
fpsClock = pygame.time.Clock()


# Object of the game----------------------------------------------------------------------------------------------------
class GameObject:
    # Init of the class
    def __init__(self, image, width, height, speed, type_object="Pipes"):
        self.speed = speed  # speed of movement
        self.image = image  # image
        self.pos = image.get_rect().move(width, height)  # hitbox
        self.type = type_object  # type of the object

    # movement from right to left
    def move_right(self):
        self.pos = self.pos.move(-self.speed, 0)

    # movement from left to right
    def move_left(self):
        self.pos = self.pos.move(self.speed, 0)

    # movement from bottom to top
    def move_up(self):
        self.pos = self.pos.move(0, -self.speed)

    # movement from top to bottom
    def move_down(self):
        self.pos = self.pos.move(0, self.speed)

    # from top to bottom at a different speed
    def fall(self):
        self.pos = self.pos.move(0, parameterGame.get_size_frame_y() / 100)

    # test collision
    def is_collided_with(self, object_game):
        return self.pos.colliderect(object_game.pos)

    # print the object
    def render(self):
        screen.blit(self.image, self.pos)

    # test if the object has finish his sprite
    def is_ended(self):
        if self.pos.x == 0:
            return True
        else:
            return False

    # restart the object with a new y position
    def renew(self, new_pos_y):
        if self.is_ended():  # test if the sprite is finished
            self.pos = self.image.get_rect().move(parameterGame.get_size_frame_x(), new_pos_y)

    # reset the position of the player
    def reset_position(self):
        if self.type == "Player":  # verify if object is player
            self.pos = self.image.get_rect().move(100, 0)  # move to init position


# player----------------------------------------------------------------------------------------------------------------
# player image
size_player = (32, 22)  # size of the player
player_image = pygame.image.load("player.png")  # load image
player_image = pygame.transform.scale(player_image, size_player)  # resize picture

# player start
player_width = 100  # player x position start
player_height = 100  # player y position start
init_position_player = (player_width, player_height)  # start position of the player

# creation of the object player
player = GameObject(player_image, 100, 100, parameterGame.get_speed_player(), "Player")

# pipes-----------------------------------------------------------------------------------------------------------------
pipes = Pipe()  # create the pipes


# score-----------------------------------------------------------------------------------------------------------------
def show_score(color, font, size, score):
    score_font = pygame.font.SysFont(font, size)  # font of the text
    score_surface = score_font.render('Score : ' + str(score), True, color)  # text to print
    score_rect = score_surface.get_rect()  # hitbox
    score_rect.midtop = (parameterGame.get_size_frame_x() / 10, 15)  # position
    screen.blit(score_surface, score_rect)  # print it


# menu------------------------------------------------------------------------------------------------------------------
# set font of menu
menu_font = pygame.font.Font(None, 40)


class Option:
    hovered = False  # mouse not on
    selected = False  # parameter unselected

    def __init__(self, text, pos):
        self.text = text  # text of option
        self.pos = pos  # position of option
        self.set_rect()  # hitbox
        self.draw()  # print it

    # print the option to the screen
    def draw(self):
        self.set_rend()  # set the font to the option
        screen.blit(self.rend, self.rect)  # print the option with his hitbox

    # set the font option
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    # set the color
    def get_color(self):
        # if mouse on
        if self.hovered:
            # white
            return 255, 255, 255
        # if selected
        elif self.selected:
            # yellow
            return 255, 255, 155
        else:
            # grey
            return 100, 100, 100

    # set the hitbox
    def set_rect(self):
        self.set_rend()  # rend the text
        self.rect = self.rend.get_rect()  # create hitbox
        self.rect.topleft = self.pos  # set the pos of the hitbox


# set the menu
def menu():
    # option, with the text and their position
    options = [
        Option("NEW GAME", (parameterGame.get_size_frame_x() / 15, (parameterGame.get_size_frame_y() / 15) + 350)),
        Option("QUIT", (parameterGame.get_size_frame_x() / 15 + parameterGame.get_size_frame_x() / 3,
                        (parameterGame.get_size_frame_y() / 15) + 350)),
        Option("RESUME", (parameterGame.get_size_frame_x() / 15 + 2 * parameterGame.get_size_frame_x() / 3,
                          (parameterGame.get_size_frame_y() / 15) + 350)),
        Option("Number of pipe : ", (parameterGame.get_size_frame_x() / 15, (parameterGame.get_size_frame_y() / 10))),
        Option("1", (parameterGame.get_size_frame_x() / 15 + 250, (parameterGame.get_size_frame_y() / 10))),
        Option("2", (parameterGame.get_size_frame_x() / 15 + 275, (parameterGame.get_size_frame_y() / 10))),
        Option("3", (parameterGame.get_size_frame_x() / 15 + 300, (parameterGame.get_size_frame_y() / 10))),
        Option("4", (parameterGame.get_size_frame_x() / 15 + 325, (parameterGame.get_size_frame_y() / 10))),
        Option("5", (parameterGame.get_size_frame_x() / 15 + 350, (parameterGame.get_size_frame_y() / 10))),
        Option("Difficulty : ", (parameterGame.get_size_frame_x() / 15, (parameterGame.get_size_frame_y() / 10 + 50))),
        Option("Easy", (parameterGame.get_size_frame_x() / 15 + 175, (parameterGame.get_size_frame_y() / 10 + 50))),
        Option("Medium", (parameterGame.get_size_frame_x() / 15 + 250, (parameterGame.get_size_frame_y() / 10 + 50))),
        Option("Hardcore", (parameterGame.get_size_frame_x() / 15 + 370, (parameterGame.get_size_frame_y() / 10 + 50)))]

    while True:
        # pause the background
        pygame.event.pump()
        # black background
        screen.fill((0, 0, 0))

        # for each option
        for opt in options:
            opt.selected = False  # unselected
            # test if the parameter is selected or not
            if opt.text == parameterGame.difficulty or opt.text == str(parameterGame.get_number_pipe()):
                opt.selected = True  # if it's selected, the colour is yellow

            # test if the mouse is in the hitbox
            if opt.rect.collidepoint(pygame.mouse.get_pos()):
                opt.hovered = True  # if yes, the colour is white
                # test if there is a click on it or not
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    # see the action to do in menu_action
                    if menu_action(opt.text) == 1:
                        # if the menu_action return 1, back to the game
                        return None
            else:
                opt.hovered = False  # mouse not on
            opt.draw()  # print the option

        # update the screen
        pygame.display.update()


# action if menu is clicked
def menu_action(menu_name):
    if menu_name == "NEW GAME":
        # reset the pos of the player
        player.reset_position()
        # reset the pipes
        pipes.reset()
        # restart game
        game()
    elif menu_name == "QUIT":
        # quit
        exit()
        pygame.quit()
    elif menu_name == "RESUME":
        # back to the game
        return 1
    elif menu_name == "1":
        # set num of pipe to 1 and restart
        parameterGame.set_number_pipe(1)  # set num of pipes to 1
        player.reset_position()  # reset position of the player
        pipes.reset()  # reset pipes
        game()  # restart game
    # same  with number of pipe = 2
    elif menu_name == "2":
        parameterGame.set_number_pipe(2)
        player.reset_position()
        pipes.reset()
        game()
    # same  with number of pipe = 3
    elif menu_name == "3":
        parameterGame.set_number_pipe(3)
        player.reset_position()
        pipes.reset()
        game()
    # same  with number of pipe = 4
    elif menu_name == "4":
        parameterGame.set_number_pipe(4)
        player.reset_position()
        pipes.reset()
        game()
    # same  with number of pipe = 5
    elif menu_name == "5":
        parameterGame.set_number_pipe(5)
        player.reset_position()
        pipes.reset()
        game()
    # set difficulty to easy
    elif menu_name == "Easy":
        parameterGame.set_difficulty_player("Easy")  # change difficulty in parameter (change then all the parameter)
        # reset of the game
        player.reset_position()  # reset the position of the player
        pipes.reset()  # reset the pipes
        game()  # restart the game
    # set difficulty to medium
    elif menu_name == "Medium":
        # same than higher
        parameterGame.set_difficulty_player("Medium")
        # reset of the game
        player.reset_position()
        pipes.reset()
        game()
    # set difficulty to hardcore
    elif menu_name == "Hardcore":
        parameterGame.set_difficulty_player("Hardcore")
        # reset of the game
        player.reset_position()
        pipes.reset()
        game()


# game------------------------------------------------------------------------------------------------------------------
def game():
    pipes_up = pipes.get_pipes_up()  # get the list of upper pipes
    pipes_down = pipes.get_pipes_down()  # get the list of lower pipes

    score_player = 0  # set the score of the player to 0
    while game_running:

        # movement of object
        player.fall()
        # move each active pipes to the left
        for num_pipe in range(parameterGame.get_number_pipe()):
            pipes_up[num_pipe].move_right()  # move the object to the left
            pipes_down[num_pipe].move_right()  # move the object to the left

        # random number for the height of pipes
        new_pos = random.randint(-380 + pipes.get_pipe_gap(), 245 - pipes.get_pipe_gap())
        # if the pipe has finished
        if pipes_up[0].is_ended():
            # reset pos of the object
            pipes_up[0].renew(new_pos - pipes.get_pipe_gap())  # generate new upper pipe
            # generate new lower pipe
            pipes_down[0].renew((parameterGame.get_size_frame_y() / 2) + pipes.get_pipe_gap() + new_pos)

            # put the first element in the end
            # By this way we can only test if pipes_up[0] and player have collision and player
            pipes_up.append(pipes_up.pop(0))
            pipes_down.append(pipes_down.pop(0))

            # add 1 to score
            score_player += 1

        # check collision
        if player.is_collided_with(pipes_up[0]):
            game_over(score_player)
        if player.is_collided_with(pipes_down[0]):
            game_over(score_player)

        # check if player is still in screen
        # check top screen
        if player.pos.y <= 0:
            game_over(score_player)
        # check bottom screen
        if player.pos.y >= parameterGame.get_size_frame_y():
            game_over(score_player)

        # check event
        for event in pygame.event.get():
            # if player leave
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # if it's escape
                if event.key == pygame.K_ESCAPE:
                    # draw menu
                    menu()

        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.move_up()

        # screen update
        screen.blit(background, (0, 0))
        screen.blit(player.image, player.pos)

        # print pipes
        for num_pipe in range(parameterGame.get_number_pipe()):
            screen.blit(pipes_up[num_pipe].image, pipes_up[num_pipe].pos)
            screen.blit(pipes_down[num_pipe].image, pipes_down[num_pipe].pos)

        # show the score of the player
        show_score(black, "times", 20, score_player)

        # update the screen
        pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(parameterGame.get_number_fps())


# Game Over
def game_over(score):
    game_over_object = GameObject(game_over_image, parameterGame.get_size_frame_x() / 2 - 104,
                                  parameterGame.get_size_frame_y() / 2 - 28, 0, "Text")
    screen.blit(game_over_object.image, game_over_object.pos)

    options = [
        Option("NEW GAME", (parameterGame.get_size_frame_x() / 15, (parameterGame.get_size_frame_y() / 15) + 350)),
        Option("QUIT", (parameterGame.get_size_frame_x() / 15 + 2 * parameterGame.get_size_frame_x() / 3,
                        (parameterGame.get_size_frame_y() / 15) + 350))]
    while True:
        pygame.event.pump()
        # black background

        for opt in options:
            opt.selected = False  # unselected
            # test if the parameter is selected or not
            if opt.text == parameterGame.difficulty or opt.text == str(parameterGame.get_number_pipe()):
                opt.selected = True  # if it's selected, the colour is yellow

            # test if the mouse is in the hitbox
            if opt.rect.collidepoint(pygame.mouse.get_pos()):
                opt.hovered = True  # if yes, the colour is white
                # test if there is a click on it or not
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    # see the action to do in menu_action
                    if menu_action(opt.text) == 1:
                        # if the menu_action return 1, back to the game
                        return None
            else:
                opt.hovered = False  # mouse not on
            opt.draw()  # print the option

        # update the screen
        pygame.display.update()


# starting screen
def start_game():
    # put background
    screen.blit(background, (0, 0))
    # put player
    screen.blit(player.image, player.pos)

    # print instruction
    options = [
        Option("PRESS SPACE TO START", (parameterGame.get_size_frame_x() / 15,
                                        (parameterGame.get_size_frame_y() / 15) + 350))]
    while True:
        pygame.event.pump()  # freeze background

        for opt in options:  # for each option
            opt.selected = False  # unselected
            # test if the parameter is selected or not
            if opt.text == parameterGame.difficulty or opt.text == str(parameterGame.get_number_pipe()):
                opt.selected = True  # if it's selected, the colour is yellow

            # test if the mouse is in the hitbox
            if opt.rect.collidepoint(pygame.mouse.get_pos()):
                opt.hovered = True  # if yes, the colour is white
                # test if there is a click on it or not
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    # see the action to do in menu_action
                    if menu_action(opt.text) == 1:
                        # if the menu_action return 1, back to the game
                        return None
            else:
                opt.hovered = False  # mouse not on

            for event in pygame.event.get():
                # if player leave
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Whenever a key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # if it's escape
                    if event.key == pygame.K_ESCAPE:
                        # draw menu
                        menu()
                    if event.key == pygame.K_SPACE:
                        # start game
                        game()

            opt.draw()  # print the option

        # update the screen
        pygame.display.update()


start_game()  # print starting screen
pygame.quit()
