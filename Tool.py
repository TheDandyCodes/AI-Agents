class Tool:
    """
    A class representing a reusable piece of code (Tool).
    
    Attributes:
        name (str): Name of the tool.
        description (str): A textual description of what the tool does.
        func (callable): The function this tool wraps.
        arguments (list): A list of argument.
        outputs (str or list): The return type(s) of the wrapped function.
    """
    def __init__(self,
                 name: str,
                 description: str,
                 func: callable,
                 arguments: list,
                 outputs: list):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        """
        Return a string representation of the tool, 
        including its name, description, arguments, and outputs.
        """

        args_str = ', '.join([f"{arg}: {type}" for arg, type in self.arguments])

        return (f"Tool name: {self.name}",
                f"Description: {self.description}",
                f"Arguments: {args_str}",
                f"Outputs: {self.outputs}")
    
    def __call__(self, *args, **kwds):
        """
        Invoke the underlying function (callable) with provided arguments.
        """
        return self.func(*args, **kwds)
    
if __name__ == "__main__":

    def calculator(a: int, b: int) -> int:
        """Calculate the sum of two numbers.

        Parameters
        ----------
        a : int
            The first number.
        b : int
            The second number.

        Returns
        -------
        int
            The sum of the two numbers.
        """
        return a + b
    
    tool = Tool("my_tool", "A tool that does something", calculator, [("arg1", int), ("arg2", str)], [int])
    print(tool.to_string())
