# cython: language_level=3

cimport cython

from mc.net.minecraft.client.render.Tessellator cimport Tessellator
from mc.net.minecraft.game.level.block.Block cimport Block
from mc.net.minecraft.game.level.World cimport World

@cython.final
cdef class RenderBlocks:
    cdef Tessellator __tessellator
    cdef World __blockAccess
    cdef int __overrideBlockTexture
    cdef bint __flipTexture

    cdef bint renderBlockByRenderType(self, Block block, int x, int y, int z)
    cdef float __shouldSideBeRendered(self, int x, int y, int z)
    cdef __renderBlockBottom(self, Block block, float x, float y, float z, int tex)
    cdef __renderBlockTop(self, Block block, float x, float y, float z, int tex)
    cdef __renderBlockNorth(self, Block block, int x, int y, int z, int tex)
    cdef __renderBlockSouth(self, Block block, int x, int y, int z, int tex)
    cdef __renderBlockWest(self, Block block, int x, int y, int z, int tex)
    cdef __renderBlockEast(self, Block block, int x, int y, int z, int tex)
