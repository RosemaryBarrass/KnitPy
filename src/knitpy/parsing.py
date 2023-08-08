import math

class Pattern:
    """A class for storing pattern information.
    
    This class of objects contains the necessary attributes and methods for storing
    written pattern information.

    Attributes:
        name: A string containing the name of the written pattern.
        author: A string containing the name of the author of the original written pattern.
        spi: An float containing the number of stitches per inch for the pattern gauge.
        rpi: An float containing the number of rows per inch for the pattern gauge.
    """
    def __init__(self, name, author):
        """Initializes the instance based on pattern name and author.

        Args:
          name: A string containing the name of the written pattern.
          author: A string containing the name of the author of the original written pattern.
        """
        self.name = name
        self.author = author
    def add_pattern_gauge(self, stitches_per_inches, stitch_inches, rows_per_inches, row_inches):
        """Adds pattern gauge to pattern object.

        Takes as input the stitches per n inches, the number of n inches, the rows per
        m inches, and the number of m inches. These values are used to compute the 
        float number of stitches per inch and rows per inch for the pattern gauge. These
        values are stored as attributes `spi` and `rpi`, respectively.

        Args:
            self: A pattern object to be modified.
            stitches_per_inches: An integer number of stitches per (n) inches of the written pattern.
            stitch_inches: An integer number of inches (n) used in the gauge of the written pattern.
            rows_per_inches: An integer number of rows per (m) inches of the written pattern.
            row_inches: An integer number of inches (m) used in the gauge of the written pattern.

        Returns:
            nothing
        """
        self.spi = stitches_per_inches/stitch_inches
        self.rpi = rows_per_inches/row_inches