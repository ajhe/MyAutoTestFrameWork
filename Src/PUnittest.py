# coding=utf-8

from Utils.Decorator import my_unittest_assertion
import unittest

class PUnittest(unittest.TestCase):

    Exc_Stack = []

    def raise_exc(self):
        if self.Exc_Stack:
            exc_text = ', AssertionError: '.join(str(x) for x in self.Exc_Stack)
            self.Exc_Stack = []
            raise AssertionError(exc_text)


    # 判断first 和 second是否一致
    @my_unittest_assertion
    def assertEqual(self, first, second, msg=None):
        super(PUnittest, self).assertEqual(first, second, msg=msg)

    # 判断first 和 second 是否不一致
    @my_unittest_assertion
    def assertNotEqual(self, first, second, msg=None):
        super(PUnittest, self).assertNotEqual(first, second, msg=msg)

    # 判断 expr 是否为False
    @my_unittest_assertion
    def assertFalse(self, expr, msg=None):
        super(PUnittest, self).assertFalse(expr, msg=msg)

    # 判断 expr 是否为True
    @my_unittest_assertion
    def assertTrue(self, expr, msg=None):
        super(PUnittest, self).assertTrue(expr, msg=msg)

    # 判断first 和 second 是否几乎相等，规则如下
    # 注:places与delta不能同时存在，否则出异常
    # 若 first == second，则直接输入正确，不判断下面的过程
    # 若 delta有数，places为空，判断first与second的差的绝对值是否<=delta，满足则正确，否则错误
    # 若 delta为空，places有数，判断second与first的差的绝对值,取小数places位，等于0则正确，否则错误
    # 若 delta为空，places为空，默认赋值places=7判断
    @my_unittest_assertion
    def assertAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        super(PUnittest, self).assertAlmostEqual(first, second, places=places, msg=msg, delta=delta)

    # 判断实际（actual）是否超出预期（expected)，也就是说actual是否是expected的子集
    @my_unittest_assertion
    def assertDictContainsSubset(self, expected, actual, msg=None):
        super(PUnittest, self).assertDictContainsSubset(expected, actual, msg=msg)

    # 判断字典1和字典2是否一致
    @my_unittest_assertion
    def assertDictEqual(self, d1, d2, msg=None):
        super(PUnittest, self).assertDictEqual(d1, d2, msg=msg)

    # 判断member是否在container里面
    @my_unittest_assertion
    def assertIn(self, member, container, msg=None):
        super(PUnittest, self).assertIn(member, container, msg=msg)

    # 判断member是否不在container里面
    @my_unittest_assertion
    def assertNotIn(self, member, container, msg=None):
        super(PUnittest, self).assertNotIn(member, container, msg=msg)

    # 判断expr1是不是expr2
    @my_unittest_assertion
    def assertIs(self, expr1, expr2, msg=None):
        super(PUnittest, self).assertIs(expr1, expr2, msg=msg)

    # 判断expr1是不是不是expr2
    @my_unittest_assertion
    def assertIsNot(self, expr1, expr2, msg=None):
        super(PUnittest, self).assertIsNot(expr1, expr2, msg=msg)

    # 判断是否为空（None）
    def assertIsNone(self, obj, msg=None):
        super(PUnittest, self).assertIsNone(obj, msg=msg)

    # 判断是否不为空
    @my_unittest_assertion
    def assertIsNotNone(self, obj, msg=None):
        super(PUnittest, self).assertIsNotNone(obj, msg=msg)

    # 判断obj是否为cls的实例
    @my_unittest_assertion
    def assertIsInstance(self, obj, cls, msg=None):
        super(PUnittest, self).assertIsInstance(obj, cls, msg=msg)

    # 判断obj是否不是cls的实例
    @my_unittest_assertion
    def assertNotIsInstance(self, obj, cls, msg=None):
        super(PUnittest, self).assertNotIsInstance(obj, cls, msg=msg)

    # 判断 a 是否大于 b
    @my_unittest_assertion
    def assertGreater(self, a, b, msg=None):
        super(PUnittest, self).assertGreater(a, b, msg=msg)
        
    # 判断a 是否小于 b
    @my_unittest_assertion
    def assertLess(self, a, b, msg=None):
        super(PUnittest, self).assertLess(a, b, msg=msg)
    
    # 判断a 是否大于等于 b
    @my_unittest_assertion
    def assertGreaterEqual(self, a, b, msg=None):
        super(PUnittest, self).assertGreaterEqual(a, b, msg=msg)
        
    # 判断a 是否小于等于b
    @my_unittest_assertion
    def assertLessEqual(self, a, b, msg=None):
        super(PUnittest, self).assertLessEqual(a, b, msg=msg)





if __name__ == '__main__':

    class TestPUnittest(PUnittest):

        def test_equal(self):
            self.assertEqual(1,2)
            self.assertEqual(1,1)
            self.assertEqual('s','s')
            self.assertAlmostEqual(9,2)
            self.raise_exc()

        def test_in(self):
            self.assertIn(1,[2])
            self.assertIn(1,[1,2,'1'])
            self.assertIn(1,['1'])
            self.assertIs(1,1)
            self.raise_exc()


    unittest.main()







