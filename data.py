training_data= [
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef add(a, b):\n    return a + b\n```",
        "completion": "```python\n# Review:\n# 1. Function name is descriptive and clear.\n# 2. Consider adding type hints for better readability and type safety.\n# 3. No error handling for invalid input types.\n# 4. Overall, the function is simple and correct.\n\ndef add(a: int, b: int) -> int:\n    return a + b\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef find_max(arr):\n    max_val = arr[0]\n    for num in arr:\n        if num > max_val:\n            max_val = num\n    return max_val\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly finds the maximum value in a list.\n# 2. Initial value for max_val should be handled carefully for empty lists.\n# 3. Use built-in max function for simplicity and efficiency.\n# 4. Add type hints for better readability.\n# 5. Add error handling for empty list input.\n\ndef find_max(arr: list[int]) -> int:\n    if not arr:\n        raise ValueError('The input list is empty')\n    return max(arr)\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly calculates factorial using recursion.\n# 2. Consider adding type hints for better readability.\n# 3. Add error handling for negative inputs.\n# 4. Recursive approach can lead to maximum recursion depth exceeded error for large n.\n# 5. Consider an iterative approach for better performance.\n\ndef factorial(n: int) -> int:\n    if n < 0:\n        raise ValueError('Input must be a non-negative integer')\n    if n == 0:\n        return 1\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef reverse_string(s):\n    return s[::-1]\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly reverses a string using slicing.\n# 2. Consider adding type hints for better readability.\n# 3. Function is concise and efficient.\n# 4. No additional improvements necessary.\n\ndef reverse_string(s: str) -> str:\n    return s[::-1]\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly checks for prime numbers.\n# 2. Consider adding type hints for better readability.\n# 3. Add error handling for non-integer inputs.\n# 4. Consider using a more efficient algorithm for large numbers.\n\ndef is_prime(n: int) -> bool:\n    if not isinstance(n, int):\n        raise TypeError('Input must be an integer')\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly calculates Fibonacci numbers using recursion.\n# 2. Add type hints for better readability.\n# 3. Recursive approach can be inefficient for large n due to repeated calculations.\n# 4. Consider using memoization or an iterative approach for better performance.\n\ndef fibonacci(n: int) -> int:\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    fib = [0, 1]\n    for i in range(2, n + 1):\n        fib.append(fib[-1] + fib[-2])\n    return fib[n]\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef sum_list(arr):\n    total = 0\n    for num in arr:\n        total += num\n    return total\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly sums the elements of a list.\n# 2. Consider using the built-in sum function for simplicity and efficiency.\n# 3. Add type hints for better readability.\n# 4. Function is otherwise correct and simple.\n\ndef sum_list(arr: list[int]) -> int:\n    return sum(arr)\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef palindrome_check(s):\n    s = s.lower()\n    return s == s[::-1]\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly checks if a string is a palindrome.\n# 2. Consider adding type hints for better readability.\n# 3. Function is simple and efficient.\n# 4. No additional improvements necessary.\n\ndef palindrome_check(s: str) -> bool:\n    s = s.lower()\n    return s == s[::-1]\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly implements bubble sort algorithm.\n# 2. Consider adding type hints for better readability.\n# 3. Bubble sort is not efficient for large lists. Mention alternative algorithms like quicksort or mergesort.\n# 4. Add a docstring explaining the function.\n\ndef bubble_sort(arr: list[int]) -> list[int]:\n    \"\"\"\n    Sorts a list using bubble sort algorithm.\n    Args:\n        arr (list[int]): List of integers to be sorted.\n    Returns:\n        list[int]: Sorted list.\n    \"\"\"\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef unique_elements(arr):\n    unique_set = set()\n    unique_list = []\n    for elem in arr:\n        if elem not in unique_set:\n            unique_list.append(elem)\n            unique_set.add(elem)\n    return unique_list\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly extracts unique elements while maintaining order.\n# 2. Add type hints for better readability.\n# 3. Consider using a dictionary for better performance in Python 3.7+.\n# 4. Add a docstring explaining the function.\n\ndef unique_elements(arr: list[int]) -> list[int]:\n    \"\"\"\n    Returns a list of unique elements while maintaining order.\n    Args:\n        arr (list[int]): List of integers.\n    Returns:\n        list[int]: List of unique integers.\n    \"\"\"\n    unique_set = set()\n    unique_list = []\n    for elem in arr:\n        if elem not in unique_set:\n            unique_list.append(elem)\n            unique_set.add(elem)\n    return unique_list\n```"
    }
]

validation_data= [
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef is_even(n):\n    return n % 2 == 0\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly checks if a number is even.\n# 2. Add type hints for better readability.\n# 3. Function is simple and efficient.\n# 4. No additional improvements necessary.\n\ndef is_even(n: int) -> bool:\n    return n % 2 == 0\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly calculates the greatest common divisor using Euclidean algorithm.\n# 2. Add type hints for better readability.\n# 3. Function is simple and efficient.\n# 4. No additional improvements necessary.\n\ndef gcd(a: int, b: int) -> int:\n    while b:\n        a, b = b, a % b\n    return a\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef count_vowels(s):\n    count = 0\n    vowels = 'aeiouAEIOU'\n    for char in s:\n        if char in vowels:\n            count += 1\n    return count\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly counts vowels in a string.\n# 2. Consider using a set for vowels for better performance.\n# 3. Add type hints for better readability.\n# 4. Add a docstring explaining the function.\n\ndef count_vowels(s: str) -> int:\n    \"\"\"\n    Counts the number of vowels in a string.\n    Args:\n        s (str): Input string.\n    Returns:\n        int: Number of vowels in the string.\n    \"\"\"\n    count = 0\n    vowels = set('aeiouAEIOU')\n    for char in s:\n        if char in vowels:\n            count += 1\n    return count\n```"
    },
    {
        "prompt": "Review this code and provide feedback: \n```python\ndef merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        left_half = arr[:mid]\n        right_half = arr[mid:]\n\n        merge_sort(left_half)\n        merge_sort(right_half)\n\n        i = j = k = 0\n\n        while i < len(left_half) and j < len(right_half):\n            if left_half[i] < right_half[j]:\n                arr[k] = left_half[i]\n                i += 1\n            else:\n                arr[k] = right_half[j]\n                j += 1\n            k += 1\n\n        while i < len(left_half):\n            arr[k] = left_half[i]\n            i += 1\n            k += 1\n\n        while j < len(right_half):\n            arr[k] = right_half[j]\n            j += 1\n            k += 1\n    return arr\n```",
        "completion": "```python\n# Review:\n# 1. Function correctly implements merge sort algorithm.\n# 2. Add type hints for better readability.\n# 3. Consider adding a helper function for merging to improve readability.\n# 4. Add a docstring explaining the function.\n\ndef merge_sort(arr: list[int]) -> list[int]:\n    \"\"\"\n    Sorts a list using merge sort algorithm.\n    Args:\n        arr (list[int]): List of integers to be sorted.\n    Returns:\n        list[int]: Sorted list.\n    \"\"\"\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        left_half = arr[:mid]\n        right_half = arr[mid:]\n\n        merge_sort(left_half)\n        merge_sort(right_half)\n\n        i = j = k = 0\n\n        while i < len(left_half) and j < len(right_half):\n            if left_half[i] < right_half[j]:\n                arr[k] = left_half[i]\n                i += 1\n            else:\n                arr[k] = right_half[j]\n                j += 1\n            k += 1\n\n        while i < len(left_half):\n            arr[k] = left_half[i]\n            i += 1\n            k += 1\n\n        while j < len(right_half):\n            arr[k] = right_half[j]\n            j += 1\n            k += 1\n    return arr\n```"
    }
]
