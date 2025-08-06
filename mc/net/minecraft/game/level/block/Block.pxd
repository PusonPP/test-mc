# cython: language_level=3
cdef class Block:
    cdef public object blocks
    cdef public int blockID
    cdef public int blockIndexInTexture
    cdef public object stepSound
    cdef public float blockParticleGravity
    cdef public float _hardness
    cdef public float _resistance
    cdef public float minX
    cdef public float minY
    cdef public float minZ
    cdef public float maxX
    cdef public float maxY
    cdef public float maxZ
