from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import re

class MathLogicAdapter(LogicAdapter):
    """
    A logic adapter that performs basic arithmetic operations.
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        # Check if the statement contains mathematical operations
        return re.search(r'\b\d+\s*[\+\-\*/]\s*\d+\b', statement.text)

    def process(self, input_statement, additional_response_selection_parameters):
        # Extract mathematical expression from the input statement
        expression = input_statement.text
        
        try:
            # Evaluate the mathematical expression
            result = eval(expression)

            # Construct the response statement with original expression and result
            response_text = f"{expression} = {result}"
            selected_statement = Statement(text=response_text)
            selected_statement.confidence = 1.0  # Set confidence to 1 since it's a mathematical operation
        except Exception as e:
            # If evaluation fails, return the input statement
            selected_statement = input_statement
            selected_statement.confidence = 0.0  # Set confidence to 0 to indicate failure

        return selected_statement
