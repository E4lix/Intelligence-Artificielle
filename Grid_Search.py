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

    def up(self):
        self.pos -= (1,0)

    def down(self):
        self.pos += (1,0)

    def left(self):
        self.pos -= (0,1)

    def right(self):
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
