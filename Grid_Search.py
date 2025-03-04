# Librairies
import random

# Dimension de la grille
GRID_SIZE = 5

# Type des cellules
EMPTY = "E"
OBSTACLE = "O"
REWARD = "R"
AGENT = "A"

# Position des éléments
reward_pos = []
obstacle_pos = []

# Création de la matrice tableau
class Matrix:
    # Initialisation d'une variable de type Matrix
    def __init__(self, dimension=5):
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
        self.valid_move = []
        self.action = None
        self.possible_move = ["up", "down", "left", "right"]

    def get_adjacent_positions(self):
        r, c = self.pos

        # Filtrer les positions valides
        if self.pos - (1,0) != OBSTACLE:
            self.valid_move.append("up")
        if self.pos + (1,0) != OBSTACLE:
            self.valid_move.append("down")
        if self.pos - (0,1) != OBSTACLE:
            self.valid_move.append("left")
        if self.pos + (0,1) != OBSTACLE:
            self.valid_move.append("right")

        return self.valid_move

    def decide_action(self):
        if self.pos - (1,0) == REWARD:
            self.action = "up"
        elif self.pos + (1,0) == REWARD:
            self.action = "down"
        elif self.pos - (0,1) == REWARD:
            self.action = "left"
        elif self.pos + (0,1) == REWARD:
            self.action = "right"
        else:
            self.action = random.choice(self.possible_move)
            while self.action not in self.valid_move:
                self.action = random.choice(self.possible_move)

        return self.action

    def move(self, action):
        if action == "up":
            self.pos -= (1,0)
        if action == "down":
            self.pos += (1,0)
        if action == "left":
            self.pos -= (0,1)
        if action == "right":
            self.pos += (0, 1)

# Création de la grille test avec une récompense et quelques obstacles
def create_grid():
    grille = Matrix(5)
    # Placement de la récompense
    a = random.randint(0,4)
    b = random.randint(0, 4)
    grille.m[a][b] = REWARD
    reward_pos.append((a,b))

    # Placement des Obstacles
    for i in range(15):
        x = a
        y = b
        while (x,y) in reward_pos:
            x = random.randint(0, 4)
            y = random.randint(0, 4)

        grille.m[x][y] = OBSTACLE
        obstacle_pos.append((x,y))
    return grille

# Programme Principal
GrilleJeu = create_grid()
GrilleJeu.afficher_matrice()

print(reward_pos)
print(obstacle_pos)