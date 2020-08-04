# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class Uint8Vector(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUint8Vector(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Uint8Vector()
        x.Init(buf, n + offset)
        return x

    # Uint8Vector
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Uint8Vector
    def Values(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Uint8Vector
    def ValuesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Uint8Vector
    def ValuesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def Uint8VectorStart(builder): builder.StartObject(1)
def Uint8VectorAddValues(builder, values): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def Uint8VectorStartValuesVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def Uint8VectorEnd(builder): return builder.EndObject()
