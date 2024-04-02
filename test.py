from generate import revise

def neighbors(self, var):
        """Given a variable, return set of overlapping variables."""
        return set(
            v for v in self.variables
            if v != var and self.overlaps[v, var]
        )

overlaps = {
    ("1", "2"): (1, 0),
    ("2", "3"): (3, 1),
    ("3", "4"): (3, 1)
}
x = "2"
y = "3"

domains = {
    "1": ["back", "camp", "cody", "pete", "dent", "kpmg"],
    "2": ["make", "andy", "oldy", "duke", "game", "king", "play"],
    "3": ['pete', 'kgnu']
}
################

def ac3(arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # define queue based on whether arcs is empty or not

        print(f'arcs: {arcs}')

        if arcs is None:
            queue = []
            for x in domains:
                for y in domains:
                    if x != y:
                        queue.append((x, y))
        else:
            queue = arcs

        print(f'queue: {queue}')

        while queue:
            # dequeue an arc to check
            check = queue[0]
            queue.remove(check)
            x, y = (check[0].i, check[0].j), (check[1].i, check[1].j)

            print(f'x:{x}; y:{y}')

            # check for revision and add neighbors
            if not domains[0]:
                return False
            elif revise(x, y):
                neighbors = neighbors(x)
                for neighbor in neighbors:
                    if neighbor != y:
                        queue.append((x, neighbor))
            
            print(f'updated queue: {queue}')
        
        return True    


