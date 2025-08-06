from mc.net.minecraft.game.level.block.Blocks import blocks


class Session:
    registeredBlocksList = (
        blocks.stone,
        blocks.cobblestone,
        blocks.dirt,
        blocks.planks,
        blocks.wood,
        blocks.leaves,
        blocks.grass,
    )
    print(len(registeredBlocksList))

    def __init__(self, username, sessionId):
        self.username = username
        self.sessionId = sessionId
