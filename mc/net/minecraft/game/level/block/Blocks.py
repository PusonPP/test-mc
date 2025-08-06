from mc.net.minecraft.game.level.block.Block import Block
from mc.net.minecraft.game.level.block.BlockGrass import BlockGrass
from mc.net.minecraft.game.level.block.BlockDirt import BlockDirt
from mc.net.minecraft.game.level.block.BlockLeaves import BlockLeaves
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

        self.soundWoodFootstep = StepSound('wood', 1.0, 1.0)
        self.soundGravelFootstep = StepSound('gravel', 1.0, 1.0)
        self.soundGrassFootstep = StepSound('grass', 1.0, 1.0)
        # ``Block`` defaults to using ``soundPowderFootstep`` during
        # initialisation.  The original project expected the ``Blocks``
        # container to always provide this attribute but it was never
        # defined which caused an ``AttributeError`` during start up.
        #
        # No unique powder footstep sounds exist in the bundled
        # resources, so we simply alias the powder sound to the stone
        # step sound so that the default reference is always valid.
        self.soundStoneFootstep = StepSound('stone', 1.0, 1.0)
        self.soundPowderFootstep = self.soundStoneFootstep

        self.stone = BlockStone(self, 1, 1).setHardness(1.0).setResistance(10.0)
        self.stone.stepSound = self.soundStoneFootstep

        self.grass = BlockGrass(self, 2).setHardness(0.6)
        self.grass.stepSound = self.soundGrassFootstep

        self.dirt = BlockDirt(self, 3, 2).setHardness(0.5)
        self.dirt.stepSound = self.soundGravelFootstep

        self.cobblestone = Block(self, 4, 16).setHardness(1.5).setResistance(10.0)
        self.cobblestone.stepSound = self.soundStoneFootstep

        self.planks = Block(self, 5, 4).setHardness(1.5).setResistance(5.0)
        self.planks.stepSound = self.soundWoodFootstep

        self.wood = BlockLog(self, 17).setHardness(2.5)
        self.wood.stepSound = self.soundWoodFootstep

        self.leaves = BlockLeaves(self, 18, 22).setHardness(0.2).setLightOpacity(1)
        self.leaves.stepSound = self.soundGrassFootstep


blocks = Blocks()
