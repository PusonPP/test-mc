from mc.net.minecraft.game.level.block.Block import Block
from mc.net.minecraft.game.level.block.BlockGrass import BlockGrass
from mc.net.minecraft.game.level.block.BlockDirt import BlockDirt
from mc.net.minecraft.game.level.block.BlockLog import BlockLog
from mc.net.minecraft.game.level.block.BlockStone import BlockStone
from mc.net.minecraft.game.level.block.StepSound import StepSound


class Blocks:
    def __init__(self):
        self.blocksList = [None] * 256
        self.tickOnLoad = [False] * 256
        self.opaqueCubeLookup = [False] * 256
        self.lightOpacity = [0] * 256
        self.canBlockGrass = [False] * 256
        self.isBlockContainer = [False] * 256
        self.lightValue = [0] * 256

        # Footstep sounds for the small set of supported blocks
        self.soundWood = StepSound('wood', 1.0, 1.0)
        self.soundGrass = StepSound('grass', 1.0, 1.0)
        self.soundStone = StepSound('stone', 1.0, 1.0)
        self.soundPowderFootstep = self.soundStone

        self.stone = BlockStone(self, 1, 1).setHardness(1.0).setResistance(10.0)
        self.stone.stepSound = self.soundStone

        self.grass = BlockGrass(self, 2).setHardness(0.6)
        self.grass.stepSound = self.soundGrass

        self.dirt = BlockDirt(self, 3, 2).setHardness(0.5)
        self.dirt.stepSound = self.soundGrass

        self.cobblestone = Block(self, 4, 16).setHardness(1.5).setResistance(10.0)
        self.cobblestone.stepSound = self.soundStone

        self.planks = Block(self, 5, 4).setHardness(1.5).setResistance(5.0)
        self.planks.stepSound = self.soundWood

        self.wood = BlockLog(self, 17).setHardness(2.5)
        self.wood.stepSound = self.soundWood


blocks = Blocks()
