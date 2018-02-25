=========
Colorized
=========

Just another stupid decorator
-----------------------------

This just a decorator to coloring your output
By add the decorator to the function, you can get the output colorized


**Available Color**
'black': Color.BLACK,
'red': Color.RED,
'green': Color.GREEN,
'orange': Color.ORANGE,
'blue': Color.BLUE,
'purple': Color.PURPLE,
'cyan': Color.CYAN,
'dark_gray': Color.DARK_GRAY,
'light_red': Color.LIGHT_RED,
'light_green': Color.LIGHT_GREEN,
'yellow': Color.YELLOW,
'light_blue': Color.LIGHT_BLUE,
'light_purple': Color.LIGHT_PURPLE,
'light_cyan': Color.LIGHT_CYAN,
'no_color': Color.NO_COLOR,


**Example**
.. code-block:: python

  @colorized(color='light_green')
  def kentang(a, b):
      print('hello')
      return a + b

  print(kentang(1, 2))
