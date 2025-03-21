# Detailed Code Explanation: Bidirectional Words and Numbers Converter

## Function: `word_to_num(input_text)`

This function converts text representations of numbers into actual integer values.

```python
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
```
**Purpose**: Defines the function interface and documents its behavior through docstring.

```python
    MAX_LIMIT = 10**36

    def check_limit(value: int) -> None:
        """Check if a value exceeds the maximum limit and raise an error if it does."""
        if value >= MAX_LIMIT:
            raise ValueError(
                "Number exceeds the maximum limit of 999,999,999,999,999,999,999,999,999,999,999,999 implemented"
            )
```
**Purpose**:
- Sets the maximum supported number (one undecillion)
- Creates a helper function to avoid repeating limit-checking code
- Raises an appropriate error when values exceed the maximum limit

```python
    nums_dict = {
        "zero": 0, "one": 1, "two": 2, /* ... and so on ... */ "ninety": 90,
    }

    scales_dict = {
        "hundred": 100,
        "thousand": 1000,
        /* ... and so on ... */
        "decillion": 1000000000000000000000000000000000,
    }
```
**Purpose**:
- Defines dictionaries mapping English words to their numerical values
- `nums_dict` handles basic number words (zero through ninety)
- `scales_dict` handles scale words (hundred, thousand, million, etc.)

```python
    input_text = input_text.lower().replace("-", " ").replace(",", " ")
    input_text = input_text.replace(" a ", " one ").replace("a ", "one ")
    words = input_text.split()
```
**Purpose**:
- Normalizes the input text by:
  - Converting to lowercase for consistent matching
  - Replacing hyphens and commas with spaces
  - Converting "a" to "one" (e.g., "a hundred" becomes "one hundred")
  - Splitting the text into individual words

```python
    if not words:
        return 0

    is_negative = False
    if words[0] == "negative":
        words = words[1:]
        is_negative = True
```
**Purpose**:
- Handles the special case of empty input (returns 0)
- Detects and handles negative numbers by:
  - Setting a flag if the first word is "negative"
  - Removing "negative" from the list of words to process

```python
    total_value = 0
    current_value = 0
    has_and = False
```
**Purpose**:
- Initializes tracking variables:
  - `total_value`: The running total of the number being built
  - `current_value`: The value currently being accumulated before applying a scale
  - `has_and`: Flag to indicate if "and" was just encountered (signifies addition)

```python
    i = 0
    while i < len(words):
        word = words[i]

        if word == "and":
            has_and = True
            i += 1
            continue
```
**Purpose**:
- Sets up a loop to process each word
- Handles the word "and" by:
  - Setting the `has_and` flag
  - Moving to the next word
  - The "and" itself doesn't contribute a value, but affects how later words are processed

```python
        if word in nums_dict:
            current_value += nums_dict[word]
```
**Purpose**:
- If the current word represents a basic number (e.g., "one", "twenty"), add its value to `current_value`

```python
        elif word in scales_dict:
            scale = scales_dict[word]

            if current_value == 0:
                current_value = 1
```
**Purpose**:
- Identifies and handles scale words (hundred, thousand, million, etc.)
- If no number precedes a scale word (e.g., "thousand" instead of "one thousand"), defaults to a multiplier of 1

```python
            if word == "hundred":
                current_value *= 100
```
**Purpose**:
- Special handling for "hundred" which behaves differently from other scales
- Simply multiplies the current value by 100 without resetting

```python
            else:
                if has_and:
                    check_limit(total_value + current_value * scale)
                    total_value += current_value * scale
                    current_value = 0
                    has_and = False
```
**Purpose**:
- Handles the case where "and" preceded this scale word
- For example, "one billion and one million" means 1,000,000,000 + 1,000,000
- Checks if adding this value would exceed the limit
- Adds the scaled value to the total and resets tracking variables

```python
                else:
                    if (
                        i + 1 < len(words)
                        and words[i + 1] in scales_dict
                        and scales_dict[words[i + 1]] > scale
                    ):
                        check_limit(current_value * scale * scales_dict[words[i + 1]])
                        current_value *= scale
```
**Purpose**:
- Implements look-ahead logic for consecutive scale words
- If the next word is a larger scale (e.g., "million billion"), this indicates multiplication
- For example, "one million billion" means 1,000,000 × 1,000,000,000
- Checks if this multiplication would exceed the limit
- Multiplies the current value by the current scale

```python
                    else:
                        check_limit(total_value + current_value * scale)
                        total_value += current_value * scale
                        current_value = 0
```
**Purpose**:
- Handles the normal case where we apply a scale and add to total
- For example, "one million" adds 1,000,000 to the total
- Checks if adding this value would exceed the limit
- Resets `current_value` for the next group of words

```python
        else:
            raise ValueError(f"Invalid number word: {word}")

        i += 1
```
**Purpose**:
- Raises an error if an unrecognized word is encountered
- Increments the counter to move to the next word

```python
    if current_value > 0:
        check_limit(total_value + current_value)
        total_value += current_value

    if is_negative:
        total_value = -total_value

    return total_value
```
**Purpose**:
- Adds any remaining value to the total (handles words without scale at the end)
- Applies the negative sign if needed
- Returns the final calculated number

## Function: `num_to_word(input_num)`

This function converts integer values to their English word representation.

```python
def num_to_word(input_num: int) -> str:
    """
    Convert a numerical value to its word representation.
    """
    MAX_LIMIT = 10**36

    def check_limit(value: int) -> None:
        """Check if a value exceeds the maximum limit and raise an error if it does."""
        if abs(value) >= MAX_LIMIT:
            raise ValueError(
                "Number exceeds the maximum limit of 999,999,999,999,999,999,999,999,999,999,999,999 implemented"
            )
```
**Purpose**:
- Sets the maximum limit and defines a helper function for limit checking
- Uses `abs()` to handle negative numbers properly

```python
    check_limit(input_num)

    if input_num == 0:
        return "zero"
```
**Purpose**:
- Checks if the input number exceeds the maximum limit
- Handles the special case of zero

```python
    ones = ["", "one", "two", /* ... and so on ... */ "nineteen"]
    tens = ["", "", "twenty", /* ... and so on ... */ "ninety"]
    scales = ["", "thousand", "million", /* ... and so on ... */ "decillion"]
```
**Purpose**:
- Defines lists for different numerical components:
  - `ones`: Numbers 1-19 (including teens)
  - `tens`: Multiples of 10 (twenty through ninety)
  - `scales`: Scale words for powers of 1000

```python
    def process_chunks(n: int, scale_idx: int) -> str:
        """Process each chunk of three digits and convert to words with appropriate scale."""
        if n == 0:
            return ""

        hundred = n // 100
        remainder = n % 100

        word_representation = ""
        if hundred > 0:
            word_representation += f"{ones[hundred]} hundred "
            if remainder > 0:
                word_representation += "and "
```
**Purpose**:
- Defines a helper function to process each chunk of three digits (e.g., 123 in 123,456,789)
- Extracts the hundreds digit (e.g., 1 in 123)
- Adds the word "hundred" if needed
- Adds "and" if there are remaining digits after the hundreds

```python
        if remainder > 0:
            if remainder < 20:
                word_representation += ones[remainder]
            else:
                word_representation += tens[remainder // 10]
                if remainder % 10 > 0:
                    word_representation += f"-{ones[remainder % 10]}"
```
**Purpose**:
- Handles the remainder after the hundreds place:
  - For numbers under 20, uses the `ones` list directly
  - For larger numbers, combines a tens word and a ones word with a hyphen
  - For example, "twenty-three" for 23

```python
        if word_representation and scale_idx:
            word_representation += f" {scales[scale_idx]}"

        return word_representation
```
**Purpose**:
- Adds the appropriate scale word if needed (thousand, million, etc.)
- Returns the complete word representation for this chunk

```python
    is_negative = False
    if input_num < 0:
        is_negative = True
        input_num = -input_num
```
**Purpose**:
- Checks if the number is negative
- Makes the number positive for processing

```python
    chunks = []
    while input_num > 0:
        chunks.append(input_num % 1000)
        input_num //= 1000
```
**Purpose**:
- Breaks the number into chunks of three digits
- For example, 123,456,789 becomes [789, 456, 123]

```python
    if not chunks:
        return "zero"

    word_chunks = []
    for i, chunk in enumerate(chunks):
        chunk_word = process_chunks(chunk, i)
        if chunk_word:
            word_chunks.append(chunk_word)
```
**Purpose**:
- Processes each chunk using the helper function
- The index `i` determines which scale word to use
- Only adds non-empty chunks to the result

```python
    result = " ".join(reversed(word_chunks))

    if is_negative:
        result = f"negative {result}"

    return result
```
**Purpose**:
- Reverses and joins the chunks (since they were built in reverse order)
- Adds "negative" at the beginning if needed
- Returns the complete word representation

## Function: `convert_user_input(user_input)`

This function determines whether to convert from words to numbers or vice versa.

```python
def convert_user_input(user_input: str) -> str:
    """
    Converts user input into either words or numbers as required.
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
```
**Purpose**:
- Removes leading/trailing whitespace
- First tries to parse the input as an integer:
  - If successful, converts the number to words
  - If not, assumes input is words and tries to convert to a number
- Provides user-friendly error messages if both conversions fail

## Function: `main()`

This function implements the interactive interface for the converter.

```python
def main():
    print("\nWords to Numbers & Numbers to Words Converter !!!\n")

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
```
**Purpose**:
- Displays a welcome message
- Creates an infinite loop to accept user input repeatedly
- Provides an exit mechanism ("quit", "exit", "q", or "e")
- Calls `convert_user_input()` to process each input
- Displays the result with formatting

```python
if __name__ == "__main__":
    main()
```
**Purpose**:
- Runs the `main()` function only when the script is executed directly
- Allows the code to be imported as a module without automatically running