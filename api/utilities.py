class TranslateNumber:
    # takes an int and returns a string
    def __init__(self, original_number):
        self.original_number = original_number
        self.translation = []
        self.ones = {
            "0": "",
            "1": "one",
            "01": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
        }
        self.teens = {
            "00": "",
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
        }
        self.tens = {
            "2": "twenty",
            "3": "thirty",
            "4": "fourty",
            "5": "fifty",
            "6": "sixty",
            "7": "seventy",
            "8": "eighty",
            "9": "ninety",
        }

        self.large = {
            # number of digits
            "2": "",
            "3": "hundred",
            "4": "thousand",
            "5": "thousand",
            "6": "hundred",
            "7": "million",
            "8": "million",
            "9": "hundred",
            "10": "billion",
        }

    def to_english(self):
        if self.original_number == 0 or self.original_number == "0":
            return "zero"
        if (
            self.original_number == 1000000000000
            or self.original_number == "1000000000000"
        ):
            return "!!! ONE TRILLION !!!"
        if self.original_number < 1000000000000 and self.original_number >= 1000000000:
            self.billion(self.original_number // 1000000000)
            # extract rightmost 7 digits
            cur_number = self.original_number % 1000000000
            cur_number = cur_number // 1000000
            self.million(cur_number)
        if self.original_number >= 1000000 and self.original_number < 1000000000:
            self.million(self.original_number // 1000000)
        self.to_english_recursive(self.original_number % 1000000)
        solution = " ".join([number for number in self.translation if number])
        # print(" ".join(solution_list))
        return solution

    def to_english_recursive(self, number):
        if number == 0 or number == "0":
            return "zero"
        # No number was given
        if not number:
            return None

        num_str = str(number)
        num_int = int(number)
        size = len(num_str)

        # Numbers of length 1
        if size == 1:
            self.translation.append(self.ones[num_str])
            return " ".join(self.translation)

        # Numbers of length 2
        if size % 3 == 2:
            first_2_digits = "".join(num_str[0:2])
            first_digit = num_str[0]
            second_digit = num_str[1]

            if first_digit == "0":
                # print(self.translation)
                self.translation.append(self.large[str(size)])
                self.to_english_recursive(num_str[1:])
                return " ".join(self.translation)

            if int(first_2_digits) < 20:
                self.translation.append(self.teens[first_2_digits])
                self.translation.append(self.large[str(size)])
                self.to_english_recursive(num_str[2:])
                return " ".join(self.translation)
            else:
                self.translation.append(self.tens[num_str[0]])
                self.translation.append(self.ones[num_str[1]])
                self.translation.append(self.large[str(size)])
                self.to_english_recursive(num_str[2:])
                return " ".join(self.translation)

        # Numbers of length 3
        if size % 3 == 0 or size % 3 == 1:
            digit_0 = num_str[0]
            if digit_0 == "0":
                self.to_english_recursive(num_str[1:])
                return " ".join(self.translation)
            self.translation.append(self.ones[digit_0])
            self.translation.append(self.large[str(size)])
            self.to_english_recursive(num_str[1:])
            return " ".join(self.translation)

    # THE PATTERN CHANGES FOR NUMBERS >= 1000000 !!!
    def million(self, number):
        mil_number = number
        print("mil_number", mil_number)

        # Numbers of length 1
        if len(str(mil_number)) == 1:
            self.translation.append(self.ones[str(mil_number)])
            if str(mil_number) != "0":
                self.translation.append("million")
            return " ".join(self.translation)

        # Numbers of length 2
        if len(str(mil_number)) == 2:
            if int(mil_number) < 20:
                if int(mil_number) > 9:
                    self.translation.append(self.teens[str(mil_number)])
                    self.translation.append("million")
                else:
                    self.translation.append(self.ones[str(mil_number)[0]])
                    self.translation.append("million")
                return " ".join(self.translation)
            else:
                self.translation.append(self.tens[str(mil_number)[0]])
                self.translation.append(self.ones[str(mil_number)[1]])
                self.translation.append("million")
                return " ".join(self.translation)

        # Numbers of length 3
        if len(str(mil_number)) == 3:
            self.translation.append(self.ones[str(mil_number)[0]])
            self.translation.append(self.large[str(len(str(mil_number)))])
            self.million(str(mil_number)[1:])
            return " ".join(self.translation)

    # >= BILLION !!! ===> STIL NEEDS WORK ===> NOT FINISHED YET!
    def billion(self, number):
        bil_number = number
        print("bil_number", bil_number)

        # Numbers of length 1
        if len(str(bil_number)) == 1:
            self.translation.append(self.ones[str(bil_number)])
            self.translation.append("billion")
            return " ".join(self.translation)

        # Numbers of length 2
        if len(str(bil_number)) == 2:
            if int(bil_number) < 20:
                if int(bil_number) > 9:
                    self.translation.append(self.teens[str(bil_number)])
                    self.translation.append("billion")
                else:
                    self.translation.append(self.ones[str(bil_number)[0]])
                    self.translation.append("billion")
                return " ".join(self.translation)
            else:
                self.translation.append(self.tens[str(bil_number)[0]])
                self.translation.append(self.ones[str(bil_number)[1]])
                self.translation.append("billion")
                return " ".join(self.translation)

        # Numbers of length 3
        if len(str(bil_number)) == 3:
            self.translation.append(self.ones[str(bil_number)[0]])
            self.translation.append(self.large[str(len(str(bil_number)))])
            self.billion(str(bil_number)[1:])
            return " ".join(self.translation)
