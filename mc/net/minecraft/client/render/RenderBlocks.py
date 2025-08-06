"""Minimal stub for the original Cython ``RenderBlocks`` helper."""


class RenderBlocks:
    def __init__(self, tessellator, world=None):
        self.tessellator = tessellator
        self.world = world

    def renderBlockOnInventory(self, block):
        pass

    def renderBlockAllFaces(self, block, x, y, z):
        pass
