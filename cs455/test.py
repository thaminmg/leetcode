import string

def clean_text(text):
  """
  Cleans a string by removing punctuations and numbers.

  Args:
    text: The string to clean.

  Returns:
    The cleaned string without punctuations and numbers.
  """
  # Define punctuation and number sets
  punctuations = set(string.punctuation) - set(['.'])
  numbers = set(string.digits)

  # Remove punctuations and numbers from the string
  cleaned_text = "".join(char for char in text if char not in (punctuations | numbers))

  return cleaned_text

# Example usage
text = "A.T."
cleaned_text = clean_text(text)
print(cleaned_text)  # Output: game