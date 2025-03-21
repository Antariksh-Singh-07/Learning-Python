def word_to_num(input_text: str) -> int:
    """
    Convert a number written in words to its numerical value.

    Args:
        input_text (str): The number in words (e.g., "six hundred and ninety-six thousand nine hundred and sixty-nine")

    Returns:
        int: The numerical value of the input number

    Raises:
        ValueError: If the input contains invalid number words or exceeds the maximum limit implemented
    """
    MAX_LIMIT = 10**36

    def check_limit(value: int) -> None:
        """Check if a value exceeds the maximum limit and raise an error if it does."""
        if value >= MAX_LIMIT:
            raise ValueError(
                "Number exceeds the maximum limit of 999,999,999,999,999,999,999,999,999,999,999,999 implemented"
            )

    nums_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    scales_dict = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000,
        "trillion": 1000000000000,
        "quadrillion": 1000000000000000,
        "quintillion": 1000000000000000000,
        "sextillion": 1000000000000000000000,
        "septillion": 1000000000000000000000000,
        "octillion": 1000000000000000000000000000,
        "nonillion": 1000000000000000000000000000000,
        "decillion": 1000000000000000000000000000000000,
    }

    input_text = input_text.lower().replace("-", " ").replace(",", " ")
    input_text = input_text.replace(" a ", " one ").replace("a ", "one ")
    words = input_text.split()

    if not words:
        return 0

    is_negative = False
    if words[0] in ["negative", "minus"]:
        words = words[1:]
        is_negative = True

    total_value = 0
    current_value = 0
    has_and = False

    i = 0
    while i < len(words):
        word = words[i]

        if word == "and":
            has_and = True
            i += 1
            continue

        if word in nums_dict:
            current_value += nums_dict[word]

        elif word in scales_dict:
            scale = scales_dict[word]

            if current_value == 0:
                current_value = 1

            if word == "hundred":
                current_value *= 100
            else:
                if has_and:
                    check_limit(total_value + current_value * scale)
                    total_value += current_value * scale
                    current_value = 0
                    has_and = False
                else:
                    if (
                        i + 1 < len(words)
                        and words[i + 1] in scales_dict
                        and scales_dict[words[i + 1]] > scale
                    ):
                        check_limit(current_value * scale * scales_dict[words[i + 1]])
                        current_value *= scale
                    else:
                        check_limit(total_value + current_value * scale)
                        total_value += current_value * scale
                        current_value = 0
        else:
            raise ValueError(f"Invalid number word: {word}")

        i += 1

    if current_value > 0:
        check_limit(total_value + current_value)
        total_value += current_value

    if is_negative:
        total_value = -total_value

    return total_value


def num_to_word(input_num: int) -> str:
    """
    Convert a numerical value to its word representation.

    Args:
        input_num (int): The number to convert to words

    Returns:
        str: The word representation of the input number

    Raises:
        ValueError: If the number exceeds the maximum limit implemented
    """
    MAX_LIMIT = 10**36

    def check_limit(value: int) -> None:
        """Check if a value exceeds the maximum limit and raise an error if it does."""
        if abs(value) >= MAX_LIMIT:
            raise ValueError(
                "Number exceeds the maximum limit of 999,999,999,999,999,999,999,999,999,999,999,999 implemented"
            )

    check_limit(input_num)

    if input_num == 0:
        return "zero"

    ones = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    scales = [
        "",
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion",
        "quintillion",
        "sextillion",
        "septillion",
        "octillion",
        "nonillion",
        "decillion",
    ]

    def process_chunks(n: int, scale_idx: int) -> str:
        """
        Process each chunk of three digits and convert to words with appropriate scale.

        Args:
            n (int): A three-digit chunk to convert (0-999)
            scale_idx (int): Index in the scales list to determine magnitude (thousand, million, etc.)

        Returns:
            str: Word representation of this chunk with its scale
        """
        if n == 0:
            return ""

        hundred = n // 100
        remainder = n % 100

        word_representation = ""
        if hundred > 0:
            word_representation += f"{ones[hundred]} hundred "
            if remainder > 0:
                word_representation += "and "

        if remainder > 0:
            if remainder < 20:
                word_representation += ones[remainder]
            else:
                word_representation += tens[remainder // 10]
                if remainder % 10 > 0:
                    word_representation += f"-{ones[remainder % 10]}"

        if word_representation and scale_idx:
            word_representation += f" {scales[scale_idx]}"

        return word_representation

    is_negative = False
    if input_num < 0:
        is_negative = True
        input_num = -input_num

    chunks = []
    while input_num > 0:
        chunks.append(input_num % 1000)
        input_num //= 1000

    if not chunks:
        return "zero"

    word_chunks = []
    for i, chunk in enumerate(chunks):
        chunk_word = process_chunks(chunk, i)
        if chunk_word:
            word_chunks.append(chunk_word)

    result = " ".join(reversed(word_chunks))

    if is_negative:
        result = f"negative {result}"

    return result


def convert_user_input(user_input: str) -> str:
    """
    Converts user input into either words or numbers as required.

    Args:
        user_input (str): User input to be converted

    Returns:
        str: The converted user input or an Error message if the conversion fails
    """
    user_input = user_input.strip()

    try:
        num_value = int(user_input)
        return num_to_word(num_value)
    except ValueError:
        try:
            return word_to_num(user_input)
        except ValueError as error:
            return f"Error: {error}"


def main():
    print("\nBidirectional Words and Numbers Converter\n")

    while True:
        user_input = input(
            "Input the Word(s)/Number(s) you want to convert (or 'quit' to exit): "
        )

        if user_input.lower() in ("quit", "exit", "q", "e"):
            print("\nThank you for using the converter. Goodbye!")
            break

        result = convert_user_input(user_input)
        print(f"\nResult: {result}")
        print("\n" + "*-----" * 10 + "*\n")


if __name__ == "__main__":
    main()
