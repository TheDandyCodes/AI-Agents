import inspect

from Tool import Tool


def tool(func):
    """
    A decorator that creates a Tool instance from the given function.
    """
    # Get the function signature
    signature = inspect.signature(func)

    # Extract (param_name, param_type) pairs for inputs
    arguments = []
    for param in signature.parameters.values():
        annotation_name = (
            param.annotation.__name__
            if hasattr(param.annotation, "__name__")
            else str(param.annotation)
        )
        arguments.append((param.name, annotation_name))

    # Determine the return annotation
    return_annotation = signature.return_annotation
    if return_annotation is inspect._empty:
        outputs = None
    else:
        outputs = (
            return_annotation.__name__
            if hasattr(return_annotation, "__name__")
            else str(return_annotation)
        )

    # Use the function's docstring as the description (default if None)
    description = func.__doc__ or "No description available."

    # The functionname becomes the Tool name
    name = func.__name__

    # Return a new Tool instance
    return Tool(name, description, func, arguments, outputs)


if __name__ == "__main__":
    # Use the tool decorator to create a Tool instance
    # This is equivalente to: calculator = tool(calculator)
    @tool
    def calculator(a: int, b: int) -> int:
        """Add two numbers together.

        Parameters
        ----------
        a : int
            The first number to add.
        b : int
            The second number to add.

        Returns
        -------
        int
            The sum of the two numbers.
        """
        return a + b

    # Because the tool decorator "converts" the function into a Tool instance,
    # we can now call the function as a Tool instance using his properties, including the to_string method.
    print(calculator.to_string())
