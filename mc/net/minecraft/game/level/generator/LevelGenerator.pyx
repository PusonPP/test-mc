# cython: language_level=3

"""Simplified level generator.

The original project shipped a very feature rich terrain generator that
created caves, ores and various biomes.  That implementation depended on a
large collection of blocks which have been removed from this kata.  To keep
the codebase small and focused we replace it with a tiny generator that
builds a flat world using only the handful of supported blocks.
"""

cimport cython

from mc.net.minecraft.game.level.World cimport World
from mc.net.minecraft.game.level.block.Blocks import blocks


@cython.final
cdef class LevelGenerator:
    """Generate a very small and simple level."""

    cdef object __guiLoading

    def __init__(self, guiLoading):
        self.__guiLoading = guiLoading

    def generate(self, str userName, int width, int depth, int height):
        """Return a world containing a flat grass surface."""
        cdef World world = World()
        cdef bytearray b = bytearray(width * depth * height)
        cdef int x, y, z, idx, ground

        ground = height // 2
        world.waterLevel = 0
        world.groundLevel = ground

        for x in range(width):
            for z in range(depth):
                for y in range(height):
                    idx = (y * depth + z) * width + x
                    if y < ground - 1:
                        b[idx] = blocks.stone.blockID
                    elif y < ground:
                        b[idx] = blocks.dirt.blockID
                    elif y == ground:
                        b[idx] = blocks.grass.blockID

        world.generate(width, height, depth, b)
        return world

