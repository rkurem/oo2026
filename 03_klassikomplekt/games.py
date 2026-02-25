class Game:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def install(self, free_space, device):
        if self.size > free_space:
            return False, f"{self.name} ei saanud paigaldada, sest seadmes {device} on vaja {self.size}GB, kuid saadaval on ainult {free_space}GB"
        return True, f"{self.name} paigaldati seadmesse {device}"

    def info(self):
        return f"{self.name} ({self.size}GB)"


class GameLibrary:
    def __init__(self, device, free_space):
        self.device = device
        self.free_space = free_space
        self.games = []

    def add_game(self, game):
        success, msg = game.install(self.free_space, self.device)

        if success:
            self.games.append(game)
            self.free_space -= game.size

        return msg

    def show_games(self):
        if not self.games:
            return "\nArvutisse pole ühtegi mängu paigaldatud.\n"

        result = "\nPaigaldatud mängud:\n"
        for g in self.games:
            result += f"- {g.info()}\n"

        result += f"\nVaba ruumi alles: {self.free_space}GB"
        return result

pc = GameLibrary("PC", 180)

g1 = Game("CS2", 85)
g2 = Game("Rocket League", 30)
g3 = Game("Valorant", 50)
g4 = Game("Growtopia", 100)

print(pc.add_game(g1))
print(pc.add_game(g2))
print(pc.add_game(g3))
print(pc.add_game(g4))

print(pc.show_games())
