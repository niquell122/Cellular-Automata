from copy import deepcopy

def default_rule(current_state, neighborhood):  # rule for Life Automata
    total = sum(neighborhood)
    if current_state == 1 and total < 2:  # underpopulation
        return 0

    if current_state == 1 and 2 <= total <= 3:  # proceeds to next generation
        return 1

    if current_state == 1 and total > 3:  # overpopulation
        return 0

    if current_state == 0 and total == 3:  # reproduction
        return 1
    return current_state

default_cell_grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,1,1,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


class CellularAutomata:
    def __init__(self, cells=default_cell_grid, rule=default_rule):
        # Matrix of any dimension
        self.cells = cells
        
        # Current State of the cells
        # Updated at the end of every run the transition rule
        self.snapshot = deepcopy(cells)
        
        # Dimensions of the Matrix (X x Y)
        # Columns
        self.X = len(cells[0])
        # Rows
        self.Y = len(cells)

        # Transition Rule
        self.rule = rule  

    def __str__(self):
        s = ''
        for cell_row in self.cells:
            s += str(cell_row) + '\n'
        return s


    ### Moore's Neighborhood
    ### a.k.a.
    ### Queen's Neighborhood
    def get_neighborhood(self, x, y):
        result = []        
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                result.append(self.get_cell(i, j))
        return result

    ### Edges are cyclical
    def get_cell(self, x, y):
        xmod = x % self.X
        ymod = y % self.Y
        return self.snapshot[xmod][ymod]

    ### Update every cell
    def evolve(self):
        print("Evolving. . .", end="\n")
        self.snapshot = deepcopy(self.cells)
        
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                neighborhood = self.get_neighborhood(i, j)
                self.cells[i][j] = self.rule(self.get_cell(i, j), neighborhood)
        
        self.snapshot = deepcopy(self.cells)
