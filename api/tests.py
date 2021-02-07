from django.test import TestCase
from .utilities import TranslateNumber

# Create your tests here.
# Run "python manage.py test" in the terminal to test the algorithm
class TranslatorTestCase(TestCase):
    def test_1(self):
        self.assertEqual(TranslateNumber(0).to_english(), "zero")

    def test_2(self):
        self.assertEqual(TranslateNumber(9).to_english(), "nine")

    def test_3(self):
        self.assertEqual(TranslateNumber(10).to_english(), "ten")

    def test_4(self):
        self.assertEqual(TranslateNumber(19).to_english(), "nineteen")

    def test_5(self):
        self.assertEqual(TranslateNumber(20).to_english(), "twenty")

    def test_6(self):
        self.assertEqual(TranslateNumber(21).to_english(), "twenty one")

    def test_7(self):
        self.assertEqual(TranslateNumber(100).to_english(), "one hundred")

    def test_8(self):
        self.assertEqual(TranslateNumber(101).to_english(), "one hundred one")

    def test_9(self):
        self.assertEqual(TranslateNumber(119).to_english(), "one hundred nineteen")

    def test_10(self):
        self.assertEqual(TranslateNumber(199).to_english(), "one hundred ninety nine")

    def test_11(self):
        self.assertEqual(TranslateNumber(1000).to_english(), "one thousand")

    def test_12(self):
        self.assertEqual(TranslateNumber(100000).to_english(), "one hundred thousand")

    def test_13(self):
        self.assertEqual(
            TranslateNumber(110000).to_english(), "one hundred ten thousand"
        )

    def test_14(self):
        self.assertEqual(
            TranslateNumber(100001).to_english(), "one hundred thousand one"
        )

    def test_15(self):
        self.assertEqual(TranslateNumber(10001).to_english(), "ten thousand one")

    def test_16(self):
        self.assertEqual(
            TranslateNumber(111111).to_english(),
            "one hundred eleven thousand one hundred eleven",
        )

    def test_17(self):
        self.assertEqual(
            TranslateNumber(1100001).to_english(),
            "one million one hundred thousand one",
        )

    def test_18(self):
        self.assertEqual(TranslateNumber(1000001).to_english(), "one million one")

    def test_19(self):
        self.assertEqual(
            TranslateNumber(1641083).to_english(),
            "one million six hundred fourty one thousand eighty three",
        )

    def test_20(self):
        self.assertEqual(
            TranslateNumber(1111111).to_english(),
            "one million one hundred eleven thousand one hundred eleven",
        )

    def test_21(self):
        self.assertEqual(
            TranslateNumber(11641783).to_english(),
            "eleven million six hundred fourty one thousand seven hundred eighty three",
        )

    def test_22(self):
        self.assertEqual(TranslateNumber(1000000).to_english(), "one million")

    def test_23(self):
        self.assertEqual(
            TranslateNumber(111641083).to_english(),
            "one hundred eleven million six hundred fourty one thousand eighty three",
        )

    def test_24(self):
        self.assertEqual(
            TranslateNumber(6252525).to_english(),
            "six million two hundred fifty two thousand five hundred twenty five",
        )

    def test_25(self):
        self.assertEqual(
            TranslateNumber(999999999).to_english(),
            "nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine",
        )
