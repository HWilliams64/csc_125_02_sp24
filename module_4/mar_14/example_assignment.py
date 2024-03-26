class Assignment:

    def __init__(self, name: str, difficulty: float):
        """
        Constructs an assignment with the given assignment name and a float that 
        indicates the level of difficulty of the assignment.
        
        Args:
            name (str): The name of the assignment.
            difficulty (float): The level of difficulty of the assignment the 
                value will be between 0-1.
        """

        self._name = name
        self._difficulty = difficulty

    def get_name(self) -> str:
        """
        Returns the name of the assignment as specified in the constructor.
        
        Returns:
            str: The assignment name.
        """

        return self._name

    def get_difficulty(self) -> float:
        """
        Returns the level of difficulty of the assignment as specified in the 
        constructor.
        
        Returns:
            float: The assignment level of difficulty.
        """

        return self._difficulty

    def __str__(self) -> str:
        """
        Returns the name of the assignment as specified in the constructor.
        
        Returns:
            str: The assignment name.
        """

        return self.get_name()


asg_1 = Assignment("apple", .7)
assert asg_1.get_name() == "apple", "The name of the assignment is incorrect"
assert asg_1.get_difficulty() == .7, "The difficulty of the assignment is incorrect"
assert str(asg_1) == "apple", "The result of the __str__ assignment is incorrect"
