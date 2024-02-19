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
        # Check if the statement contains both an English question and a mathematical operation
        return re.search(r'\b[A-Za-z]+\b.*(\d+\s*[\+\-\*/]\s*\d+)\b', statement.text)

    def process(self, input_statement, additional_response_selection_parameters):
        # Extract English question and mathematical expression from the input statement
        match = re.search(r'\b([A-Za-z]+)\b(.*)(\d+\s*[\+\-\*/]\s*\d+)\b', input_statement.text)
        
        if match:
            question = match.group(1).strip()
            expression = match.group(3).strip()

            try:
                # Evaluate the mathematical expression
                result = eval(expression)

                # Construct the response statement with the original question and the evaluated expression
                response_text = f"{expression} is {result}"
                selected_statement = Statement(text=response_text)
                selected_statement.confidence = 1.0  # Set confidence to 1 since it's a mathematical operation
            except Exception as e:
                # If evaluation fails, return the input statement
                selected_statement = input_statement
                selected_statement.confidence = 0.0  # Set confidence to 0 to indicate failure
        else:
            # If no match is found, return the input statement
            selected_statement = input_statement
            selected_statement.confidence = 0.0  # Set confidence to 0 to indicate failure

        return selected_statement
