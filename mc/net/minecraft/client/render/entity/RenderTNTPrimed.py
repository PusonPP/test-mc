from mc.net.minecraft.client.render.entity.Render import Render
from mc.net.minecraft.client.render.RenderBlocks import RenderBlocks
from mc.net.minecraft.client.render.Tessellator import tessellator
from mc.net.minecraft.game.level.block.Blocks import blocks
from pyglet import gl


class RenderTNTPrimed(Render):
    """Simple renderer for primed TNT entities.

    The original project expected a dedicated renderer for the TNT entity
    but the module was missing which prevented the game from starting due to
    an import failure inside ``RenderManager``.  This implementation mirrors
    the behaviour of other renderers by using ``RenderBlocks`` to draw a block
    model.  If a specific TNT block is unavailable in ``Blocks`` we fall back
    to rendering cobblestone so that the entity can still be displayed and the
    import succeeds.
    """

    def __init__(self):
        super().__init__()
        self._shadowSize = 0.5
        self.__renderBlocks = RenderBlocks(tessellator)

    def doRender(self, entity, xd, yd, zd, yaw, a):
        gl.glPushMatrix()
        gl.glTranslatef(xd, yd, zd)
        self._loadTexture('terrain.png')
        # Use TNT block if available, otherwise fall back to cobblestone
        block = getattr(blocks, 'tnt', None) or blocks.cobblestone
        self.__renderBlocks.renderBlockOnInventory(block)
        gl.glPopMatrix()
