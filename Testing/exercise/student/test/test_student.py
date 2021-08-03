from project.student import Student

from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("John", {"Python": ["Basic", "Fundamentals"]})

    def test_init(self):
        self.assertEqual("John", self.student.name)
        self.assertEqual({"Python": ["Basic", "Fundamentals"]}, self.student.courses)

    def test_init_with_empty_courses(self):
        student = Student("John")
        self.assertEqual("John", student.name)
        self.assertEqual({}, student.courses)

    def test_added_notes_in_not_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", "...")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_added_notes(self):
        result = self.student.add_notes("Python", "Advanced")
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_if_not_existing_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.student.leave_course("Python")
        self.assertEqual("Course has been removed", result)

    def test_enroll_added_notes(self):
        result = self.student.enroll("Python", "Advanced")
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_added_course_notes_y(self):
        result = self.student.enroll("Java", "Fundamentals", "Y")
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_added_course_notes_empty_string(self):
        result = self.student.enroll("Java", ["Inheritance", "SOLID"])
        self.assertEqual(2, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["Java"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_course(self):
        result = self.student.enroll("Java", "Fundamentals", "notes")
        self.assertEqual(2, len(self.student.courses))
        self.assertEqual(0, len(self.student.courses["Java"]))
        self.assertEqual("Course has been added.", result)


if __name__ == '__main__':
    main()