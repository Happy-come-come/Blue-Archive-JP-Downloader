# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EquipmentExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EquipmentExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEquipmentExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EquipmentExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EquipmentExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def EquipmentCategory_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def Rarity_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def Wear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EquipmentExcel
    def MaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def RecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def TierInit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def NextTierEquipment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def StackableMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def Icon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EquipmentExcel
    def ImageName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EquipmentExcel
    def Tags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EquipmentExcel
    def TagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EquipmentExcel
    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentExcel
    def TagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # EquipmentExcel
    def CraftQuality(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentExcel
    def ShopCategory(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EquipmentExcel
    def ShopCategoryAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EquipmentExcel
    def ShopCategoryLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentExcel
    def ShopCategoryIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # EquipmentExcel
    def ShortcutTypeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(16)
def EquipmentExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def EquipmentExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddEquipmentCategory_(builder, EquipmentCategory_): builder.PrependInt32Slot(1, EquipmentCategory_, 0)
def EquipmentExcelAddEquipmentCategory_(builder, EquipmentCategory_):
    """This method is deprecated. Please switch to AddEquipmentCategory_."""
    return AddEquipmentCategory_(builder, EquipmentCategory_)
def AddRarity_(builder, Rarity_): builder.PrependInt32Slot(2, Rarity_, 0)
def EquipmentExcelAddRarity_(builder, Rarity_):
    """This method is deprecated. Please switch to AddRarity_."""
    return AddRarity_(builder, Rarity_)
def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(3, LocalizeEtcId, 0)
def EquipmentExcelAddLocalizeEtcId(builder, LocalizeEtcId):
    """This method is deprecated. Please switch to AddLocalizeEtcId."""
    return AddLocalizeEtcId(builder, LocalizeEtcId)
def AddWear(builder, Wear): builder.PrependBoolSlot(4, Wear, 0)
def EquipmentExcelAddWear(builder, Wear):
    """This method is deprecated. Please switch to AddWear."""
    return AddWear(builder, Wear)
def AddMaxLevel(builder, MaxLevel): builder.PrependInt32Slot(5, MaxLevel, 0)
def EquipmentExcelAddMaxLevel(builder, MaxLevel):
    """This method is deprecated. Please switch to AddMaxLevel."""
    return AddMaxLevel(builder, MaxLevel)
def AddRecipeId(builder, RecipeId): builder.PrependInt32Slot(6, RecipeId, 0)
def EquipmentExcelAddRecipeId(builder, RecipeId):
    """This method is deprecated. Please switch to AddRecipeId."""
    return AddRecipeId(builder, RecipeId)
def AddTierInit(builder, TierInit): builder.PrependInt64Slot(7, TierInit, 0)
def EquipmentExcelAddTierInit(builder, TierInit):
    """This method is deprecated. Please switch to AddTierInit."""
    return AddTierInit(builder, TierInit)
def AddNextTierEquipment(builder, NextTierEquipment): builder.PrependInt64Slot(8, NextTierEquipment, 0)
def EquipmentExcelAddNextTierEquipment(builder, NextTierEquipment):
    """This method is deprecated. Please switch to AddNextTierEquipment."""
    return AddNextTierEquipment(builder, NextTierEquipment)
def AddStackableMax(builder, StackableMax): builder.PrependInt32Slot(9, StackableMax, 0)
def EquipmentExcelAddStackableMax(builder, StackableMax):
    """This method is deprecated. Please switch to AddStackableMax."""
    return AddStackableMax(builder, StackableMax)
def AddIcon(builder, Icon): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(Icon), 0)
def EquipmentExcelAddIcon(builder, Icon):
    """This method is deprecated. Please switch to AddIcon."""
    return AddIcon(builder, Icon)
def AddImageName(builder, ImageName): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(ImageName), 0)
def EquipmentExcelAddImageName(builder, ImageName):
    """This method is deprecated. Please switch to AddImageName."""
    return AddImageName(builder, ImageName)
def AddTags(builder, Tags): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(Tags), 0)
def EquipmentExcelAddTags(builder, Tags):
    """This method is deprecated. Please switch to AddTags."""
    return AddTags(builder, Tags)
def StartTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EquipmentExcelStartTagsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTagsVector(builder, numElems)
def AddCraftQuality(builder, CraftQuality): builder.PrependInt64Slot(13, CraftQuality, 0)
def EquipmentExcelAddCraftQuality(builder, CraftQuality):
    """This method is deprecated. Please switch to AddCraftQuality."""
    return AddCraftQuality(builder, CraftQuality)
def AddShopCategory(builder, ShopCategory): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(ShopCategory), 0)
def EquipmentExcelAddShopCategory(builder, ShopCategory):
    """This method is deprecated. Please switch to AddShopCategory."""
    return AddShopCategory(builder, ShopCategory)
def StartShopCategoryVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EquipmentExcelStartShopCategoryVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartShopCategoryVector(builder, numElems)
def AddShortcutTypeId(builder, ShortcutTypeId): builder.PrependInt64Slot(15, ShortcutTypeId, 0)
def EquipmentExcelAddShortcutTypeId(builder, ShortcutTypeId):
    """This method is deprecated. Please switch to AddShortcutTypeId."""
    return AddShortcutTypeId(builder, ShortcutTypeId)
def End(builder): return builder.EndObject()
def EquipmentExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)