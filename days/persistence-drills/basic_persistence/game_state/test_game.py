from game import Game

game = Game("Geetha")
game.move(5,3)
game.level_up()
game.increase_score(100)

print("Before saving:")
print(game)

# save game state
game.save_state("game_save.pkl")

# load game state
restored_game = Game.load_state("game_save.pkl")

print("\nAfter restoring:")
print(restored_game)