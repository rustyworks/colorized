=========
Colorized
=========

Just another stupid decorator
-----------------------------

This just a decorator to coloring your output
By add the decorator to the function, you can get the output colorized
|
|

**Available Color**

|  black
|  red
|  green
|  orange
|  blue
|  purple
|  cyan
|  dark_gray
|  light_red
|  light_green
|  yellow
|  light_blue
|  light_purple
|  light_cyan
|
|

**Example**

.. code-block:: python

  @colorized(color='light_green')
  # Just add this decorator
  def kentang(a, b):
      print('hello')
      return a + b

  print(kentang(1, 2))
