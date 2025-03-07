# Librairies
import random
import keyboard
import time

# Dimension de la grille
GRID_SIZE = 5

# Type des cellules
EMPTY = "E"
OBSTACLE = "O"
REWARD = "R"
AGENT = "A"

# Création de la matrice tableau
class Matrix:
    # Initialisation d'une variable de type Matrix
    def __init__(self, dimension):
        self.N = dimension
        self.m = [[EMPTY for i in range(dimension)] for j in  range(dimension)]

    # Représentation de la matrice en sortie
    def __str__(self):
        return f"Matrix({repr(self.m)})"

    # Représentation Classique de la matrice
    def afficher_matrice(self):
        for i in range(self.N):
            print(self.m[i])

# Création de la classe Agent
class Agent:
    def __init__(self, starting_pos):
        self.pos = starting_pos

    # Fonction donnant les cases valides internes à la grille (exclus le débordement mais pas les cases à obstacles)
    def get_adjacent_positions(self):
        r, c = self.pos

        moves = {"up": (r - 1, c),
                 "down": (r + 1, c),
                 "left": (r, c - 1),
                 "right": (r, c + 1)}

        # Filtrer les déplacements valides
        possible_move = {direction: pos for direction, pos in moves.items()
                           if 0 <= pos[0] < GRID_SIZE and 0 <= pos[1] < GRID_SIZE}

        # # Filtrer les positions valides
        # if self.pos - (1,0) != OBSTACLE:
        #     self.valid_move.append("up")
        # if self.pos + (1,0) != OBSTACLE:
        #     self.valid_move.append("down")
        # if self.pos - (0,1) != OBSTACLE:
        #     self.valid_move.append("left")
        # if self.pos + (0,1) != OBSTACLE:
        #     self.valid_move.append("right")

        return possible_move

    # Fonction renvoyant la présence ou non d'obstacles et de récompense sur les ces adjacentes
    def perceive(self, grid):
        perceptions = {}
        possible_move = self.get_adjacent_positions()

        for direction, pos in possible_move.items():
            perceptions[direction] = grid.m[pos[0]][pos[1]]

        return perceptions

    # Fonction décidant du déplacement en fonction des obstacles et de la récompense
    def decide_action(self, perceptions):
        for direction, cell in perceptions.items():
            if cell == REWARD:
                return direction

        valid_moves = [direction for direction, cell in perceptions.items()
                           if cell == EMPTY]

        if valid_moves:
            return random.choice(valid_moves)
        else:
            return None

        # if self.pos - (1,0) == REWARD:
        #     self.action = "up"
        # elif self.pos + (1,0) == REWARD:
        #     self.action = "down"
        # elif self.pos - (0,1) == REWARD:
        #     self.action = "left"
        # elif self.pos + (0,1) == REWARD:
        #     self.action = "right"
        # else:
        #     self.action = random.choice(self.possible_move)
        #     while self.action not in self.valid_move:
        #         self.action = random.choice(self.possible_move)

    def move(self, action):
        if action is None:
            return

        r, c = self.pos
        if action == "up":
            self.pos = (r - 1, c)
        if action == "down":
            self.pos = (r + 1, c)
        if action == "left":
            self.pos = (r, c - 1)
        if action == "right":
            self.pos = (r, c + 1)

        # if action == "up":
        #     self.pos -= (1,0)
        # if action == "down":
        #     self.pos += (1,0)
        # if action == "left":
        #     self.pos -= (0,1)
        # if action == "right":
        #     self.pos += (0, 1)

# Création de la grille test avec une récompense et quelques obstacles
def create_grid():
    grille = Matrix(GRID_SIZE)
    REWARD_POS = []
    OBSTACLE_POS = []

    # Placement de la récompense
    a = random.randint(0,4)
    b = random.randint(0, 4)
    grille.m[a][b] = REWARD
    REWARD_POS.append((a, b))

    # Placement des Obstacles
    for i in range(15):
        x = a
        y = b
        while (x,y) in REWARD_POS:
            x = random.randint(0, 4)
            y = random.randint(0, 4)

        grille.m[x][y] = OBSTACLE
        OBSTACLE_POS.append((x, y))
    return grille, REWARD_POS, OBSTACLE_POS

# Affichage dynamique de la grille
def print_grid(grille, agentPos):
    for i in range(GRID_SIZE):
        row = ""
        for j in range(GRID_SIZE):
            if(i,j) == agentPos:
                row += f"{AGENT} \t"
            else:
                row += f"{grille.m[i][j]} \t"
        print(row)
    print()

# Boucle du Jeu
def update_grid():
    AgentTest = Agent((0,0))
    while not keyboard.is_pressed("esc"):
        pass

# Programme Principal
GrilleJeu, REWARD_POS, OBSTACLE_POS = create_grid()
AgentTest = Agent((0,0))

print_grid(GrilleJeu, AgentTest.pos)
print(f"Position de la récompense : {REWARD_POS}")
print(f"Position des obstacles : {OBSTACLE_POS}")

while not(REWARD_POS[0] == AgentTest.pos):
    time.sleep(3)
    AgentTest.get_adjacent_positions()
    Vision = AgentTest.perceive(GrilleJeu)
    Action = AgentTest.decide_action(Vision)
    AgentTest.move(Action)
    print_grid(GrilleJeu, AgentTest.pos)
    print(REWARD_POS[0])
    print(AgentTest.pos)

print("Fin du Jeu !")
