"""Lightweight fallback implementation of the Cython based tessellator.

The original project used a Cython extension to stream vertex data to
OpenGL.  Building that extension adds a significant amount of complexity
and is unnecessary for the simplified test environment.  This module
provides a very small stub with the same public API so the rest of the
codebase can run without needing to compile any native extensions.  All
methods are essentially no-ops which is sufficient for non-graphical
unit tests.
"""


class Tessellator:
    def __getattr__(self, _):
        def method(*_args, **_kwargs):
            return self
        return method


# Single shared instance, mirroring the behaviour of the original module.
tessellator = Tessellator()
