# cython: language_level=3
# cython: cdivision=True

from mc.net.minecraft.client.render.Tessellator cimport Tessellator
from mc.net.minecraft.game.level.block.Block cimport Block
from mc.net.minecraft.game.level.World cimport World
from pyglet import gl

cdef class RenderBlocks:
    def __init__(self, Tessellator t, World world=None):
        self.__tessellator = t
        self.__blockAccess = world
        self.__overrideBlockTexture = -1
        self.__flipTexture = False

    def renderBlockAllFacesHit(self, Block block, int x, int y, int z, int tex):
        self.__overrideBlockTexture = tex
        self.renderBlockByRenderType(block, x, y, z)
        self.__overrideBlockTexture = -1

    def renderBlockAllFaces(self, Block block, int x, int y, int z):
        self.__flipTexture = True
        self.renderBlockByRenderType(block, x, y, z)
        self.__flipTexture = False

    cdef bint renderBlockByRenderType(self, Block block, int x, int y, int z):
        cdef bint layerOk = False
        cdef float b
        if self.__flipTexture or block.shouldSideBeRendered(self.__blockAccess, x, y - 1, z, 0):
            b = block.getBlockBrightness(self.__blockAccess, x, y - 1, z)
            self.__tessellator.setColorOpaque_F(0.5 * b, 0.5 * b, 0.5 * b)
            self.__renderBlockBottom(
                block, x, y, z,
                block.getBlockTextureFromSideAndMetadata(self.__blockAccess, x, y, z, 0)
            )
            layerOk = True
        if self.__flipTexture or block.shouldSideBeRendered(self.__blockAccess, x, y + 1, z, 1):
            b = block.getBlockBrightness(self.__blockAccess, x, y + 1, z)
            self.__tessellator.setColorOpaque_F(b, b, b)
            self.__renderBlockTop(
                block, x, y, z,
                block.getBlockTextureFromSideAndMetadata(self.__blockAccess, x, y, z, 1)
            )
            layerOk = True
        if self.__flipTexture or block.shouldSideBeRendered(self.__blockAccess, x, y, z - 1, 2):
            b = block.getBlockBrightness(self.__blockAccess, x, y, z - 1)
            self.__tessellator.setColorOpaque_F(0.8 * b, 0.8 * b, 0.8 * b)
            self.__renderBlockNorth(
                block, x, y, z,
                block.getBlockTextureFromSideAndMetadata(self.__blockAccess, x, y, z, 2)
            )
            layerOk = True
        if self.__flipTexture or block.shouldSideBeRendered(self.__blockAccess, x, y, z + 1, 3):
            b = block.getBlockBrightness(self.__blockAccess, x, y, z + 1)
            self.__tessellator.setColorOpaque_F(0.8 * b, 0.8 * b, 0.8 * b)
            self.__renderBlockSouth(
                block, x, y, z,
                block.getBlockTextureFromSideAndMetadata(self.__blockAccess, x, y, z, 3)
            )
            layerOk = True
        if self.__flipTexture or block.shouldSideBeRendered(self.__blockAccess, x - 1, y, z, 4):
            b = block.getBlockBrightness(self.__blockAccess, x - 1, y, z)
            self.__tessellator.setColorOpaque_F(0.6 * b, 0.6 * b, 0.6 * b)
            self.__renderBlockWest(
                block, x, y, z,
                block.getBlockTextureFromSideAndMetadata(self.__blockAccess, x, y, z, 4)
            )
            layerOk = True
        if self.__flipTexture or block.shouldSideBeRendered(self.__blockAccess, x + 1, y, z, 5):
            b = block.getBlockBrightness(self.__blockAccess, x + 1, y, z)
            self.__tessellator.setColorOpaque_F(0.6 * b, 0.6 * b, 0.6 * b)
            self.__renderBlockEast(
                block, x, y, z,
                block.getBlockTextureFromSideAndMetadata(self.__blockAccess, x, y, z, 5)
            )
            layerOk = True
        return layerOk

    cdef float __shouldSideBeRendered(self, int x, int y, int z):
        return 0.0

    cdef __renderBlockBottom(self, Block block, float x, float y, float z, int tex):
        cdef int xt
        cdef float u0, u1, v0, v1, x0, x1, y0, z0, z1
        if self.__overrideBlockTexture >= 0:
            tex = self.__overrideBlockTexture
        xt = (tex & 15) << 4
        tex &= 240
        u0 = xt / 256.0
        u1 = (xt + 15.99) / 256.0
        v0 = tex / 256.0
        v1 = (tex + 15.99) / 256.0
        x0 = x + block.minX
        x1 = x + block.maxX
        y0 = y + block.minY
        z0 = z + block.minZ
        z1 = z + block.maxZ
        self.__tessellator.addVertexWithUV(x0, y0, z1, u0, v1)
        self.__tessellator.addVertexWithUV(x0, y0, z0, u0, v0)
        self.__tessellator.addVertexWithUV(x1, y0, z0, u1, v0)
        self.__tessellator.addVertexWithUV(x1, y0, z1, u1, v1)

    cdef __renderBlockTop(self, Block block, float x, float y, float z, int tex):
        cdef int xt
        cdef float u0, u1, v0, v1, x0, x1, y1, z0, z1
        if self.__overrideBlockTexture >= 0:
            tex = self.__overrideBlockTexture
        xt = (tex & 15) << 4
        tex &= 240
        u0 = xt / 256.0
        u1 = (xt + 15.99) / 256.0
        v0 = tex / 256.0
        v1 = (tex + 15.99) / 256.0
        x0 = x + block.minX
        x1 = x + block.maxX
        y1 = y + block.maxY
        z0 = z + block.minZ
        z1 = z + block.maxZ
        self.__tessellator.addVertexWithUV(x1, y1, z1, u1, v1)
        self.__tessellator.addVertexWithUV(x1, y1, z0, u1, v0)
        self.__tessellator.addVertexWithUV(x0, y1, z0, u0, v0)
        self.__tessellator.addVertexWithUV(x0, y1, z1, u0, v1)

    cdef __renderBlockNorth(self, Block block, int x, int y, int z, int tex):
        cdef int xt
        cdef float u0, u1, v0, v1, x0, x1, y0, y1, z0
        if self.__overrideBlockTexture >= 0:
            tex = self.__overrideBlockTexture
        xt = (tex & 15) << 4
        tex &= 240
        u0 = xt / 256.0
        u1 = (xt + 15.99) / 256.0
        if block.minY >= 0.0 and block.maxY <= 1.0:
            v0 = (tex + block.minY * 15.99) / 256.0
            v1 = (tex + block.maxY * 15.99) / 256.0
        else:
            v0 = tex / 256.0
            v1 = (tex + 15.99) / 256.0
        x0 = x + block.minX
        x1 = x + block.maxX
        y0 = y + block.minY
        y1 = y + block.maxY
        z0 = z + block.minZ
        self.__tessellator.addVertexWithUV(x0, y1, z0, u1, v0)
        self.__tessellator.addVertexWithUV(x1, y1, z0, u0, v0)
        self.__tessellator.addVertexWithUV(x1, y0, z0, u0, v1)
        self.__tessellator.addVertexWithUV(x0, y0, z0, u1, v1)

    cdef __renderBlockSouth(self, Block block, int x, int y, int z, int tex):
        cdef int xt
        cdef float u0, u1, v0, v1, x0, x1, y0, y1, z1
        if self.__overrideBlockTexture >= 0:
            tex = self.__overrideBlockTexture
        xt = (tex & 15) << 4
        tex &= 240
        u0 = xt / 256.0
        u1 = (xt + 15.99) / 256.0
        if block.minY >= 0.0 and block.maxY <= 1.0:
            v0 = (tex + block.minY * 15.99) / 256.0
            v1 = (tex + block.maxY * 15.99) / 256.0
        else:
            v0 = tex / 256.0
            v1 = (tex + 15.99) / 256.0
        x0 = x + block.minX
        x1 = x + block.maxX
        y0 = y + block.minY
        y1 = y + block.maxY
        z1 = z + block.maxZ
        self.__tessellator.addVertexWithUV(x0, y1, z1, u0, v0)
        self.__tessellator.addVertexWithUV(x0, y0, z1, u0, v1)
        self.__tessellator.addVertexWithUV(x1, y0, z1, u1, v1)
        self.__tessellator.addVertexWithUV(x1, y1, z1, u1, v0)

    cdef __renderBlockWest(self, Block block, int x, int y, int z, int tex):
        cdef int xt
        cdef float u0, u1, v0, v1, x0, y0, y1, z0, z1
        if self.__overrideBlockTexture >= 0:
            tex = self.__overrideBlockTexture
        xt = (tex & 15) << 4
        tex &= 240
        u0 = xt / 256.0
        u1 = (xt + 15.99) / 256.0
        if block.minY >= 0.0 and block.maxY <= 1.0:
            v0 = (tex + block.minY * 15.99) / 256.0
            v1 = (tex + block.maxY * 15.99) / 256.0
        else:
            v0 = tex / 256.0
            v1 = (tex + 15.99) / 256.0
        x0 = x + block.minX
        y0 = y + block.minY
        y1 = y + block.maxY
        z0 = z + block.minZ
        z1 = z + block.maxZ
        self.__tessellator.addVertexWithUV(x0, y1, z1, u1, v0)
        self.__tessellator.addVertexWithUV(x0, y1, z0, u0, v0)
        self.__tessellator.addVertexWithUV(x0, y0, z0, u0, v1)
        self.__tessellator.addVertexWithUV(x0, y0, z1, u1, v1)

    cdef __renderBlockEast(self, Block block, int x, int y, int z, int tex):
        cdef int xt
        cdef float u0, u1, v0, v1, x1, y0, y1, z0, z1
        if self.__overrideBlockTexture >= 0:
            tex = self.__overrideBlockTexture
        xt = (tex & 15) << 4
        tex &= 240
        u0 = xt / 256.0
        u1 = (xt + 15.99) / 256.0
        if block.minY >= 0.0 and block.maxY <= 1.0:
            v0 = (tex + block.minY * 15.99) / 256.0
            v1 = (tex + block.maxY * 15.99) / 256.0
        else:
            v0 = tex / 256.0
            v1 = (tex + 15.99) / 256.0
        x1 = x + block.maxX
        y0 = y + block.minY
        y1 = y + block.maxY
        z0 = z + block.minZ
        z1 = z + block.maxZ
        self.__tessellator.addVertexWithUV(x1, y0, z1, u0, v1)
        self.__tessellator.addVertexWithUV(x1, y0, z0, u1, v1)
        self.__tessellator.addVertexWithUV(x1, y1, z0, u1, v0)
        self.__tessellator.addVertexWithUV(x1, y1, z1, u0, v0)

    def renderBlockOnInventory(self, Block block):
        if block.getRenderType() == 0:
            gl.glTranslatef(-0.5, -0.5, -0.5)
            self.__tessellator.startDrawingQuads()
            self.__tessellator.setNormal(0.0, -1.0, 0.0)
            self.__renderBlockBottom(block, 0.0, 0.0, 0.0, block.getBlockTexture(0))
            self.__tessellator.draw()
            self.__tessellator.startDrawingQuads()
            self.__tessellator.setNormal(0.0, 1.0, 0.0)
            self.__renderBlockTop(block, 0.0, 0.0, 0.0, block.getBlockTexture(1))
            self.__tessellator.draw()
            self.__tessellator.startDrawingQuads()
            self.__tessellator.setNormal(0.0, 0.0, -1.0)
            self.__renderBlockNorth(block, 0, 0, 0, block.getBlockTexture(2))
            self.__tessellator.draw()
            self.__tessellator.startDrawingQuads()
            self.__tessellator.setNormal(0.0, 0.0, 1.0)
            self.__renderBlockSouth(block, 0, 0, 0, block.getBlockTexture(3))
            self.__tessellator.draw()
            self.__tessellator.startDrawingQuads()
            self.__tessellator.setNormal(-1.0, 0.0, 0.0)
            self.__renderBlockWest(block, 0, 0, 0, block.getBlockTexture(4))
            self.__tessellator.draw()
            self.__tessellator.startDrawingQuads()
            self.__tessellator.setNormal(1.0, 0.0, 0.0)
            self.__renderBlockEast(block, 0, 0, 0, block.getBlockTexture(5))
            self.__tessellator.draw()
            gl.glTranslatef(0.5, 0.5, 0.5)
