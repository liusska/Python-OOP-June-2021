from unittest import TestCase, main

from .custom_list import CustomList


class TestsCustomList(TestCase):
    def setUp(self):
        self.custom_list = CustomList(1, 2 , 3)

    def test_init(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)

    def test_append_add_element_at_the_end(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertNotEqual(5, self.custom_list._CustomList__values[-1])
        self.custom_list.append(5)
        self.assertEqual([1, 2, 3, 5], self.custom_list._CustomList__values)
        self.assertEqual(5, self.custom_list._CustomList__values[-1])

    def test_add_works_if_the_list_is_empty(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.append(5)
        self.assertEqual([5], cl._CustomList__values)

    def test_append_without_value_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.custom_list.append()
        self.assertIn("append()", str(ex.exception))

    def test_append_not_return_value(self):
        result = self.custom_list.append(5)
        self.assertIsNone(result)

    def test_remove_element(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.remove(0)
        self.assertEqual([2, 3], self.custom_list._CustomList__values)
        self.assertEqual(2, self.custom_list._CustomList__values[0])

    def test_remove_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.remove(100)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_remove_returns_the_removed_element(self):
        el = self.custom_list.remove(0)
        self.assertIsNotNone(1)
        self.assertEqual(1, el)

    def test_get_returns_element_on_the_given_index(self):
        el = self.custom_list.get(0)
        self.assertIsNotNone(el)
        self.assertEqual(1, el)

    def test_get_with_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.get(100)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_extend_append_iterable_to_values(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.extend([100, 200])
        self.assertEqual([1, 2, 3, 100, 200], self.custom_list._CustomList__values)
        self.custom_list.extend((100, 200))
        self.assertEqual([1, 2, 3, 100, 200, 100, 200], self.custom_list._CustomList__values)
        self.custom_list.extend({5, 6})
        self.assertEqual([1, 2, 3, 100, 200, 100, 200, 5, 6], self.custom_list._CustomList__values)

    def test_extend_appends_iterable_to_values_with_empty_values(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.extend([1, 2])
        self.assertEqual([1, 2], cl._CustomList__values)

    def test_extend_non_iterable_as_arg_should_work(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.extend(5)
        self.assertEqual([1, 2, 3, 5], self.custom_list._CustomList__values)

    def test_extend_returns_new_list_modifies_old_one(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        result = self.custom_list.extend([100, 200])
        self.assertEqual([1, 2, 3, 100, 200], self.custom_list._CustomList__values)
        self.assertEqual([1, 2, 3, 100, 200], result)
        self.assertNotEqual(id(self.custom_list._CustomList__values), id(result))

    def test_insert_adds_element_to_specific_index_shift_others_to_right(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(5, self.custom_list._CustomList__values[0])
        self.assertEqual(1, self.custom_list._CustomList__values[1])

    def test_insert_adds_element_to_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.insert(100, 5)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_insert_returns_all_values_with_same_ref(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        result = self.custom_list.insert(0, 100)
        self.assertEqual([100, 1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(id(self.custom_list._CustomList__values), id(result))

    def test_pop_remove_last_element_and_return_it(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(3, self.custom_list._CustomList__values[-1])
        res = self.custom_list.pop()
        self.assertEqual([1, 2], self.custom_list._CustomList__values)
        self.assertEqual(2, self.custom_list._CustomList__values[-1])
        self.assertIsNotNone(res)
        self.assertEqual(3, res)

    def test_pop_with_empty_values_raises(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        with self.assertRaises(IndexError) as ex:
            cl.pop()
        self.assertEqual("No elements in list", str(ex.exception))

    def test_clear_removes_all_elements_in_list(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomList__values)

    def test_clear_works_with_no_values_in_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.clear()
        self.assertEqual([], cl._CustomList__values)

    def test_index_returns_index(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        result = self.custom_list.index(1)
        self.assertIsNotNone(result)
        self.assertEqual(0, result)

    def test_index_raises_when_value_not_found(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertIsNotNone(100, self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index(100)
        self.assertEqual("Element is not in the list", str(ex.exception))

    def test_count_returns_count_of_element_requested(self):
        self.assertEqual(1, self.custom_list._CustomList__values.count(1))
        result = self.custom_list.count(1)
        self.assertIsNotNone(result)
        self.assertEqual(1, result)

    def test_count_returns_zero_if_element_is_not_presented(self):
        self.assertEqual(0, self.custom_list._CustomList__values.count(0))
        result = self.custom_list.count(0)
        self.assertIsNotNone(result)
        self.assertEqual(0, result)

    def test_reversed_return_new_list_with_reversed_values(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        result = self.custom_list.reverse()
        self.assertEqual([3, 2, 1], result)
        self.assertNotEqual(id(result), id(self.custom_list._CustomList__values))

    def test_copy_returns_same_element_different_list(self):
        result = self.custom_list.copy()
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertNotEqual(id(result), id(self.custom_list._CustomList__values))


if __name__ == '__main__':
    main()