##  Questions...

"""
1. Is the Python Standard Library included with PyInputPlus?
2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
3. How do you distinguish between inputInt() and inputFloat()?
4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
6. If a blank input is entered three times, what does inputStr(limit=3) do?
7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

"""

## Answers...

"""
1. No, the Python Standard Library is not included with PyInputPlus. However, PyInputPlus is built on top of the standard library's input() function and provides additional features for user input validation and error handling.

-----------------------------------------------------------------------------------------



2. PyInputPlus is commonly imported with the alias 'pypi' to make it easier and quicker to refer to the library in the code. It also avoids conflicts with other libraries or modules that may have similar names or attributes.

-----------------------------------------------------------------------------------------

3. inputInt() is used to ensure that the user enters an integer value, while inputFloat() is used to ensure that the user enters a floating-point number.

-----------------------------------------------------------------------------------------

4. To ensure that the user enters a whole number between 0 and 99 using PyInputPlus, you can use the following code:

python
Copy code
import pyinputplus as pypi
num = pypi.inputInt(prompt='Enter a whole number between 0 and 99: ', min=0, max=99)
The min and max arguments ensure that the input is between 0 and 99.

-----------------------------------------------------------------------------------------

5.The keyword arguments allowRegexes and blockRegexes are used to specify regular expressions that are either allowed or blocked in user input. If allowRegexes is specified, only input that matches one of the regular expressions will be allowed. If blockRegexes is specified, any input that matches one of the regular expressions will be blocked.

-----------------------------------------------------------------------------------------

6.If a blank input is entered three times using inputStr(limit=3), the function will raise a RetryLimitException, indicating that the user has exceeded the maximum number of allowed retries.

-----------------------------------------------------------------------------------------

7.If a blank input is entered three times using inputStr(limit=3, default='hello'), the function will return the default value 'hello' after the third retry, indicating that the user has exceeded the maximum number of allowed retries.

-----------------------------------------------------------------------------------------
"""