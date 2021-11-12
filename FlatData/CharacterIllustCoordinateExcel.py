# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterIllustCoordinateExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterIllustCoordinateExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterIllustCoordinateExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterIllustCoordinateExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterIllustCoordinateExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterIllustCoordinateExcel
    def CharacterBodyCenterX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # CharacterIllustCoordinateExcel
    def CharacterBodyCenterY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # CharacterIllustCoordinateExcel
    def DefaultScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # CharacterIllustCoordinateExcel
    def MinScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # CharacterIllustCoordinateExcel
    def MaxScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(6)
def CharacterIllustCoordinateExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def CharacterIllustCoordinateExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddCharacterBodyCenterX(builder, CharacterBodyCenterX): builder.PrependFloat32Slot(1, CharacterBodyCenterX, 0.0)
def CharacterIllustCoordinateExcelAddCharacterBodyCenterX(builder, CharacterBodyCenterX):
    """This method is deprecated. Please switch to AddCharacterBodyCenterX."""
    return AddCharacterBodyCenterX(builder, CharacterBodyCenterX)
def AddCharacterBodyCenterY(builder, CharacterBodyCenterY): builder.PrependFloat32Slot(2, CharacterBodyCenterY, 0.0)
def CharacterIllustCoordinateExcelAddCharacterBodyCenterY(builder, CharacterBodyCenterY):
    """This method is deprecated. Please switch to AddCharacterBodyCenterY."""
    return AddCharacterBodyCenterY(builder, CharacterBodyCenterY)
def AddDefaultScale(builder, DefaultScale): builder.PrependFloat32Slot(3, DefaultScale, 0.0)
def CharacterIllustCoordinateExcelAddDefaultScale(builder, DefaultScale):
    """This method is deprecated. Please switch to AddDefaultScale."""
    return AddDefaultScale(builder, DefaultScale)
def AddMinScale(builder, MinScale): builder.PrependFloat32Slot(4, MinScale, 0.0)
def CharacterIllustCoordinateExcelAddMinScale(builder, MinScale):
    """This method is deprecated. Please switch to AddMinScale."""
    return AddMinScale(builder, MinScale)
def AddMaxScale(builder, MaxScale): builder.PrependFloat32Slot(5, MaxScale, 0.0)
def CharacterIllustCoordinateExcelAddMaxScale(builder, MaxScale):
    """This method is deprecated. Please switch to AddMaxScale."""
    return AddMaxScale(builder, MaxScale)
def End(builder): return builder.EndObject()
def CharacterIllustCoordinateExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)