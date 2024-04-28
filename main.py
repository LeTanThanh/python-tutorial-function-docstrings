if __name__ == "__main__":
  # Introduction to the help() function

  """
  Python provides a built-in function called help that allows you to show the documentation of a function.

  The following examples shows the documentation of the print() function:

  help(print)

  Output:

  print(...)
    print(value, ,,. sep = " ", end = "\n", file = sys.stdout, flush = False )

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:   a file-like object (stream); default to the current sys.stdout.
    sep:    string inserted between values, default a space.
    end:    string appended after the last value, default a newline.
    flush:  whether to forcibly flush the stream.
  """

  # Using docstrings to document functions

  def add(a, b):
    """Add two arguments
    Arguments:
      a: an integer
      b: an integer
    Returns:
      The sum of the two arguments
    """
    return a + b

  print(add.__doc__)
