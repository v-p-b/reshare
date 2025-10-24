from reshare.helpers import *
from reshare import *
import unittest


class TestBuilders(unittest.TestCase):
    def test_py_constructors(self):
        self.assertTrue(isinstance(ResharePy("test"), Reshare))

        content = ReshDataTypeContentPrimitivePy()
        name = "primitive_test"
        size = 1
        self.assertEqual(content.type, "PRIMITIVE")

        primitive_type = ReshDataTypePy("test_primitive", content, name, size)
        self.assertTrue(isinstance(primitive_type, ReshDataType))

        pointer_type = ReshDataTypePy(
            name="test_pointer",
            content=ReshDataTypeContentPointerPy(target_type=primitive_type),
            size=8,
        )
        self.assertIsNotNone(pointer_type)

        array_type = ReshDataTypePy(
            name="test_array[4]",
            content=ReshDataTypeContentArrayPy(base_type=pointer_type, length=4),
            size=32,
        )
        self.assertIsNotNone(array_type)

        struct_type = ReshDataTypePy(
            name="test_struct",
            content=ReshDataTypeContentStructurePy(
                members=[pointer_type, primitive_type]
            ),
            size=9,
        )
        self.assertIsNotNone(struct_type)

        union_type = ReshDataTypePy(
            name="test_union",
            content=ReshDataTypeContentUnionPy(members=[pointer_type, primitive_type]),
            size=8,
        )
        self.assertIsNotNone(union_type)

        function_type = ReshDataTypePy(
            name="test_function",
            content=ReshDataTypeContentFunctionPy(
                arguments=[],
                calling_convention="__stdcall",
                return_type=ReshTypeSpec(
                    type_name="test_pointer", embedded_type=pointer_type
                ),
            ),
            size=8,
        )
        self.assertIsNotNone(function_type)

    def test_resh_type_magic(self):
        arg0 = ReshFunctionArgumentPy(
            name="param0",
            type="test_pointer",
        )
        self.assertTrue(isinstance(arg0.type, ReshTypeSpec))

        arg1 = ReshFunctionArgumentPy(
            name="param1",
            type=None,
        )
        self.assertTrue(isinstance(arg0.type, ReshTypeSpec))

        arg2 = ReshFunctionArgumentPy(
            name="param2",
            type=ReshTypeSpec(type_name="test_pointer", embedded_type=None),
        )
        self.assertTrue(isinstance(arg0.type, ReshTypeSpec))

        content = ReshDataTypeContentFunctionPy(
            arguments=[arg0, arg1, arg2],
            calling_convention="__stdcall",
            return_type="test_pointer",
        )
        self.assertTrue(isinstance(content.return_type, ReshTypeSpec))


if __name__ == "__main__":
    unittest.main()
