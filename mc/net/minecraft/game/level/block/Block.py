"""Simplified Python implementation of the base ``Block`` class.

The original project provided this functionality as a Cython extension.
For the pared down set of blocks used in the exercises we only require a
very small subset of the original behaviour.  The implementation below
is intentionally lightweight but exposes the attributes and methods that
other modules expect.
"""


class Block:
    def __init__(self, blocks, blockId, tex=0):
        if blocks.blocksList[blockId]:
            raise RuntimeError(
                f"Slot {blockId} is already occupied by {blocks.blocksList[blockId]}"
            )
        blocks.blocksList[blockId] = self
        self.blocks = blocks
        self.blockID = blockId
        self.blockIndexInTexture = tex
        self.stepSound = blocks.soundStone
        self.blockParticleGravity = 1.0
        self._hardness = 0.0
        self._resistance = 0.0
        self._setBlockBounds(0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        blocks.opaqueCubeLookup[blockId] = self.isOpaqueCube()
        blocks.lightOpacity[blockId] = 255 if self.isOpaqueCube() else 0
        blocks.canBlockGrass[blockId] = self.renderAsNormalBlock()
        blocks.isBlockContainer[blockId] = False

    # ------------------------------------------------------------------
    def setLightOpacity(self, opacity):
        self.blocks.lightOpacity[self.blockID] = opacity
        return self

    def setLightValue(self, value):
        self.blocks.lightValue[self.blockID] = int(15.0 * value)
        return self

    def setResistance(self, resistance):
        self._resistance = resistance * 3.0
        return self

    def setHardness(self, hardness):
        self._hardness = hardness
        if self._resistance < hardness * 5.0:
            self._resistance = hardness * 5.0
        return self

    def _setTickOnLoad(self, tick):
        self.blocks.tickOnLoad[self.blockID] = tick
        return self

    def _setBlockBounds(self, minX, minY, minZ, maxX, maxY, maxZ):
        self.minX, self.minY, self.minZ = minX, minY, minZ
        self.maxX, self.maxY, self.maxZ = maxX, maxY, maxZ

    # Rendering helpers -------------------------------------------------
    def renderAsNormalBlock(self):
        return True

    def getRenderType(self):
        return 0

    def isOpaqueCube(self):
        return True

    def shouldSideBeRendered(self, world, x, y, z, layer):
        return True

    def getBlockTexture(self, face):
        return self.blockIndexInTexture

    def getBlockTextureFromSideAndMetadata(self, world, x, y, z, face):
        return self.getBlockTexture(face)

    # Game mechanics ----------------------------------------------------
    def getBlockMaterial(self):
        return 0  # corresponds to ``Material.air`` in the original code

    def quantityDropped(self, rand=None):
        return 1

    def idDropped(self):
        return self.blockID

    def blockStrength(self, player):
        return int(self._hardness * 30.0)

    def dropBlockAsItem(self, world, x, y, z):
        pass

    # Bounding boxes ----------------------------------------------------
    def getSelectedBoundingBoxFromPool(self, x, y, z):
        return (x + self.minX, y + self.minY, z + self.minZ,
                x + self.maxX, y + self.maxY, z + self.maxZ)

    def getCollisionBoundingBoxFromPool(self, x, y, z):
        return self.getSelectedBoundingBoxFromPool(x, y, z)
