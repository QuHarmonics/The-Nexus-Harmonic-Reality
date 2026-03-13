# Sum of digits in Python

https://chat.openai.com/c/68a03ea1-f4a4-8324-b0fe-3f26289400f0

## USER
can you give me py code that will sum a input of number like 123 would output 6

## ASSISTANT
Here is a concise Python implementation that computes the sum of digits of an input number such that, for example, `123` would yield `6`:  

```python
def sum_of_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
```

This program converts the input number into a string, iterates through each digit, converts them back into integers, and sums them. The use of `abs()` ensures that negative numbers are also handled correctly.  

Would you like me to also extend this into a **recursive version**, aligning with the Mark1 recursive reflection principle, so that it reduces the number step by step until the result is obtained?

