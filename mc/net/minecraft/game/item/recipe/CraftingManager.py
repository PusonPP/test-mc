"""Minimal crafting manager.

This project originally implemented a sizeable subset of the classic
Minecraft crafting system.  The majority of that code referenced dozens of
items and blocks that are no longer present in this trimmed down
distribution which only contains a handful of basic blocks.  Importing the
old recipe modules attempted to access attributes such as
``items.ingotIron`` which no longer exist on :mod:`Items` and resulted in an
``AttributeError`` during start-up.

For the purposes of this kata we only require the ability to register and
look up shaped recipes.  The helper recipe modules and large predefined
recipe list have therefore been removed leaving a much smaller and safer
implementation.
"""

from mc.net.minecraft.game.item.Item import Item
from mc.net.minecraft.game.item.ItemStack import ItemStack
from mc.net.minecraft.game.item.recipe.ShapedRecipes import ShapedRecipes
from mc.net.minecraft.game.level.block.Block import Block


class CraftingManager:
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance:
            return cls.instance

        cls.instance = cls()
        return cls.instance

    def __init__(self):
        # Recipes are registered dynamically by the rest of the code base.
        # The original project populated a large list of default recipes here
        # which depended on many non-existent items.  Keeping the list empty
        # avoids those lookups while still allowing custom recipes to be
        # added by calling :meth:`addRecipe` if ever required.
        self.__recipes = []

    def addRecipe(self, stack, solution):
        slotLocations = ''
        slot = 0
        recipeWidth = 0
        recipeHeight = 0
        while isinstance(solution[slot], str):
            slots = solution[slot]
            slot += 1
            recipeHeight += 1
            recipeWidth = len(slots)
            slotLocations += slots

        slot2item = {}
        while slot < len(solution):
            slots = solution[slot]
            idx = 0
            if isinstance(solution[slot + 1], Item):
                idx = solution[slot + 1].shiftedIndex
            elif isinstance(solution[slot + 1], Block):
                idx = solution[slot + 1].blockID

            slot2item[slots] = idx
            slot += 2

        recipeItems = [0] * recipeWidth * recipeHeight
        for i in range(recipeWidth * recipeHeight):
            slot = slotLocations[i]
            if slot2item.get(ord(slot)):
                recipeItems[i] = slot2item.get(ord(slot))
            else:
                recipeItems[i] = -1

        self.__recipes.append(
            ShapedRecipes(recipeWidth, recipeHeight, recipeItems, stack)
        )

    def findMatchingRecipe(self, craftItems):
        for recipe in self.__recipes:
            if recipe.matches(craftItems):
                return recipe.getCraftingResult()

        return None
