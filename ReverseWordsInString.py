'''Reverse Words in a String
Given a string, reverse the order of words (words separated by spaces). Remove leading/trailing spaces and reduce multiple spaces to single.
Sample: " hello world " → "world hello"
Hint: split by whitespace or iterate from end.'''

a = "hello world"

print(' '.join(a.split()[::-1]))
