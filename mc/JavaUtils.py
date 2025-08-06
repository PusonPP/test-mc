import time
import random as _random
import ctypes


def getMillis():
    """Return the current time in milliseconds."""
    return int(time.time() * 1000)


def random():
    """Mimic Java's ``Math.random`` using Python's :mod:`random` module."""
    return _random.random()


class Random:
    """Minimal implementation of ``java.util.Random``.

    Only the methods required by the client code are provided.
    """

    def __init__(self, seed=None):
        self._rand = _random.Random(seed)

    def nextInt(self, n):
        return self._rand.randrange(n)

    def nextFloat(self):
        return self._rand.random()

    def nextGaussian(self):
        return self._rand.gauss(0.0, 1.0)


class _Buffer:
    """Simple buffer wrapper providing a handful of ``java.nio``-like methods.

    OpenGL specific methods are implemented as no-ops to keep the
    implementation lightweight and to avoid the need for an active GL
    context in test environments.
    """

    def __init__(self, ctype, size):
        self.buffer = (ctype * size)()
        self._pos = 0
        self._limit = size

    # Buffer manipulation -------------------------------------------------
    def clear(self):
        self._pos = 0
        return self

    def flip(self):
        self._limit = self._pos
        self._pos = 0
        return self

    def position(self, pos):
        self._pos = pos
        return self

    def limit(self, lim):
        self._limit = lim
        return self

    # Data population -----------------------------------------------------
    def put(self, value):
        self.buffer[self._pos] = value
        self._pos += 1
        return self

    def putBytes(self, data):
        for b in data:
            self.buffer[self._pos] = b
            self._pos += 1
        return self

    # OpenGL helpers (no-op stubs) ---------------------------------------
    def glLightfv(self, *args):
        pass

    def glLightModelfv(self, *args):
        pass

    def glTexImage2D(self, *args):
        pass

    def glTexSubImage2D(self, *args):
        pass


class BufferUtils:
    """Factory for typed buffers used by the rendering code."""

    @staticmethod
    def createFloatBuffer(size):
        return _Buffer(ctypes.c_float, size)

    @staticmethod
    def createByteBuffer(size):
        return _Buffer(ctypes.c_ubyte, size)

    @staticmethod
    def createIntBuffer(size):
        return _Buffer(ctypes.c_int, size)
