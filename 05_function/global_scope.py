best_superhero = "captain america"

def update_best_superhero():
    def change_best_superhero():
        global best_superhero
        best_superhero = "Ironman"
    change_best_superhero()

update_best_superhero()
print(best_superhero)

# output: Ironman