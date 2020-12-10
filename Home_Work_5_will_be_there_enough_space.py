def enough(cap, on, wait):
    """
    This function let you know is
    there enough space on the bus
    for waiting people
    Input parameters: cap, on, wait
    Output: 0 if enough or if not
    enough integer number of extra
    waiting people"""

    return 0 if cap-on >= wait else wait - (cap-on)