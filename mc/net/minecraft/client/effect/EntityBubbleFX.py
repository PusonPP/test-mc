from mc.net.minecraft.client.effect.EntityFX import EntityFX


class EntityBubbleFX(EntityFX):
    """Minimal placeholder bubble particle effect.

    The original game includes a bubble effect particle. The current project
    does not implement it, but some modules still attempt to import the
    class.  Providing this stub ensures those imports succeed while having no
    behaviour."""

    def __init__(self, world, x, y, z):
        super().__init__(world, x, y, z, 0.0, 0.0, 0.0)

    def renderParticle(self, t, a, xa, ya, za, xa2, ya2):
        """Render the particle. This stub intentionally does nothing."""

    def onEntityUpdate(self):
        """Update the particle each tick. This stub intentionally does nothing."""
