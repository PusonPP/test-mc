from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
from glob import glob

import numpy
from pathlib import Path

flags = {'define_macros': [('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]}


def make_extension(name, path, include_numpy=False):
    """Return an :class:`Extension` if source exists, otherwise ``None``."""
    base = Path(path)
    src = base.with_suffix('.pyx')
    if not src.exists():
        src = base.with_suffix('.py')
        if not src.exists():
            return None
    kwargs = dict(**flags)
    if include_numpy:
        kwargs['include_dirs'] = [numpy.get_include()]
    return Extension(name=name, sources=[str(src)], **kwargs)


ext_specs = [
    ('mc.JavaUtils', 'mc/JavaUtils', True),
    ('mc.net.minecraft.game.entity.Entity', 'mc/net/minecraft/game/entity/Entity', True),
    ('mc.net.minecraft.game.entity.EntityLiving', 'mc/net/minecraft/game/entity/EntityLiving', True),
    ('mc.net.minecraft.game.entity.AILiving', 'mc/net/minecraft/game/entity/AILiving', True),
    ('mc.net.minecraft.game.physics.AxisAlignedBB', 'mc/net/minecraft/game/physics/AxisAlignedBB', False),
    ('mc.net.minecraft.client.gui.FontRenderer', 'mc/net/minecraft/client/gui/FontRenderer', False),
    ('mc.net.minecraft.client.render.Frustum', 'mc/net/minecraft/client/render/Frustum', True),
    ('mc.net.minecraft.client.render.WorldRenderer', 'mc/net/minecraft/client/render/WorldRenderer', True),
    ('mc.net.minecraft.client.render.Tessellator', 'mc/net/minecraft/client/render/Tessellator', True),
    ('mc.net.minecraft.client.render.RenderBlocks', 'mc/net/minecraft/client/render/RenderBlocks', True),
    ('mc.net.minecraft.client.render.RenderGlobal', 'mc/net/minecraft/client/render/RenderGlobal', True),
    ('mc.net.minecraft.client.render.texture.TextureFX', 'mc/net/minecraft/client/render/texture/TextureFX', False),
    ('mc.net.minecraft.client.render.texture.TextureFlamesFX', 'mc/net/minecraft/client/render/texture/TextureFlamesFX', True),
    ('mc.net.minecraft.client.render.texture.TextureGearsFX', 'mc/net/minecraft/client/render/texture/TextureGearsFX', True),
    ('mc.net.minecraft.client.render.texture.TextureLavaFX', 'mc/net/minecraft/client/render/texture/TextureLavaFX', True),
    ('mc.net.minecraft.client.render.texture.TextureWaterFX', 'mc/net/minecraft/client/render/texture/TextureWaterFX', True),
    ('mc.net.minecraft.client.render.texture.TextureWaterFlowFX', 'mc/net/minecraft/client/render/texture/TextureWaterFlowFX', True),
    ('mc.net.minecraft.game.level.World', 'mc/net/minecraft/game/level/World', True),
    ('mc.net.minecraft.game.level.EntityMap', 'mc/net/minecraft/game/level/EntityMap', True),
    ('mc.net.minecraft.game.level.EntityMapSlot', 'mc/net/minecraft/game/level/EntityMapSlot', True),
    ('mc.net.minecraft.game.level.generator.LevelGenerator', 'mc/net/minecraft/game/level/generator/LevelGenerator', True),
    ('mc.net.minecraft.game.level.generator.noise.NoiseGeneratorDistort', 'mc/net/minecraft/game/level/generator/noise/NoiseGeneratorDistort', False),
    ('mc.net.minecraft.game.level.generator.noise.NoiseGeneratorOctaves', 'mc/net/minecraft/game/level/generator/noise/NoiseGeneratorOctaves', True),
    ('mc.net.minecraft.game.level.generator.noise.NoiseGeneratorPerlin', 'mc/net/minecraft/game/level/generator/noise/NoiseGeneratorPerlin', True),
    ('mc.net.minecraft.game.level.block.Block', 'mc/net/minecraft/game/level/block/Block', True),
    ('mc.net.minecraft.game.level.block.BlockFluid', 'mc/net/minecraft/game/level/block/BlockFluid', True),
    ('mc.net.minecraft.game.level.block.BlockFlowing', 'mc/net/minecraft/game/level/block/BlockFlowing', True),
    ('mc.net.minecraft.game.level.block.BlockFire', 'mc/net/minecraft/game/level/block/BlockFire', True),
]

extensions = [ext for ext in (make_extension(*spec) for spec in ext_specs) if ext]

setup(
    name='minecraft-python',
    version='0.31.20100131',
    author='pythonengineer',
    description='A project that seeks to recreate every old Minecraft version in Python using Pyglet and Cython.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='BSD',
    url='https://github.com/pythonengineer/minecraft-python',
    download_url='https://pypi.org/project/minecraft-python',
    project_urls={
        'Source': 'https://github.com/pythonengineer/minecraft-python',
        'Tracker': 'https://github.com/pythonengineer/minecraft-python/issues',
    },
    python_requires='>=3.9',
    keywords='minecraft pyglet cython sandbox game classic',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Games/Entertainment',
    ],
    exclude_package_data={
        '': ['*.c', '*.html', '*.pyc'],
    },
    package_data={
        '': ['*.png', '*.ogg', '*.md3', '*.MD3', '*.dll'],
    },
    packages=find_packages(),
    ext_modules=cythonize(extensions, annotate=False, language_level=3),
    include_package_data=True,
    zip_safe=False,
)
