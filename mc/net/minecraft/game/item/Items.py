from mc.net.minecraft.game.item.ItemBlock import ItemBlock
from mc.net.minecraft.game.level.block.Blocks import blocks


class Items:
    def __init__(self):
        self.itemsList = [None] * 1024
        for i in range(256):
            if blocks.blocksList[i]:
                self.itemsList[i] = ItemBlock(self, i - 256)


items = Items()
