from exercises_utils.exercise import Exercise

class Variables(Exercise):
    """
    Class for representing the Variables exercise.
    """
    
    id = "variables"
    total_score = 10
    
    def _get_exercises(self, _locals: dict) -> list[str]:
        """
        Returns the exercises.
        """
    
        _exercises = [
            # Exercise 1: Declare a variable 'name' and assign your name to it.
            "type(_locals['name']) == str",
            
            # Exercise 2: Create two variables, 'length' and 'width', and calculate the area of a rectangle.
            "_locals['area'] == _locals['length'] * _locals['width']",
            
            # Exercise 3: Define a variable 'radius' and calculate the area of a circle.
            "_locals['circle_area'] == _locals['pi'] * _locals['radius'] ** 2",
            
            # Exercise 4: Swap the values of two variables, 'a' and 'b'.
            # TODO: check if the values were actually swapped
            "_locals['a'] != _locals['b']",
            
            # Exercise 5: Convert a temperature in Celsius to Fahrenheit using a variable.
            "_locals['fahrenheit'] == _locals['celsius'] * 9 / 5 + 32",
            
            # Exercise 6: Create a variable 'greeting' and assign a string greeting of your choice.
            "type(_locals['greeting']) == str",
            
            # Exercise 7: Concatenate two strings using variables 'first_name' and 'last_name'.
            "_locals['full_name'] == _locals['first_name'] + ' ' + _locals['last_name']",
            
            # Exercise 8: Increment a variable 'counter' by 1.
            # TODO: check if the value was actually incremented
            "type(_locals['counter']) == int",
            
            # Exercise 9: Determine if a number is even or odd using a variable 'num'.
            "_locals['num_odd'] == _locals['num'] % 2 != 0",
            
            # Exercise 10: Calculate the average of three numbers using variables 'num1', 'num2', and 'num3'.
            "_locals['average'] == (_locals['num1'] + _locals['num2'] + _locals['num3']) / 3",
        ]
        
        return _exercises