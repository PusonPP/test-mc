from mc.net.minecraft.game.level.block.Block import Block


class BlockFire(Block):
    """Minimal stand-in for the original ``BlockFire`` implementation.

    The project only uses the block as a reference for locating the fire
    texture in the terrain atlas.  The real game contains extensive logic
    for spreading and extinguishing fire which isn't needed for rendering
    the title screen, so this class intentionally keeps behaviour to the
    bare minimum required by the rest of the code base.
    """

    def __init__(self, blocks, block_id=51, tex=15):
        super().__init__(blocks, block_id, tex)

    # Fire is a non-solid block that shouldn't render like normal cubes.
    def isOpaqueCube(self):
        return False

    def renderAsNormalBlock(self):
        return False
