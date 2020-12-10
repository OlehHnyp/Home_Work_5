def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    This function evaluate could you drive
    to the nearest pump if you have
    <fuel_left> gallons of fuel, your car runs
    about <mpg> miles per gallon and
    distance to pymp is <distance_to_pump>
    miles
    Input parametrs: distance_to_pump,
    mpg, fuel_left
    Output: boolean value
    """

    return mpg*fuel_left >= distance_to_pump