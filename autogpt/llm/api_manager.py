from __future__ import annotations

import openai
import bittensor as bt

from types import SimpleNamespace
from autogpt.config import Config
from autogpt.llm.modelsinfo import COSTS
from autogpt.logs import logger
from autogpt.singleton import Singleton


class ApiManager(metaclass=Singleton):
    def __init__(self ):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0
        self.total_budget = 0

    def reset(self):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0
        self.total_budget = 0.0

    def create_chat_completion(
        self,
        messages: list,  # type: ignore
        model: str | None = None,
        temperature: float = None,
        max_tokens: int | None = None,
        deployment_id=None,
    ) -> str:
        """
        Create a chat completion and update the cost.
        Args:
        messages (list): The list of messages to send to the API.
        model (str): The model to use for the API call.
        temperature (float): The temperature to use for the API call.
        max_tokens (int): The maximum number of tokens for the API call.
        Returns:
        str: The AI's response.
        """

        for i, message in enumerate(messages):
            if message[ "role" ] == "system":
                messages[i][ "role" ] = "user"

        print ('\n\nmessages', messages )


        responses = bt.prompt( content = messages, return_all = True )
        print("\n\nALL responses", responses, "\n\n")
        response = self.pick_response(responses)
        
        logger.debug(f"Response: {response}")
        print ('\n\nStart response:\n', response )
        print("End response\n")

        return_val = SimpleNamespace()
        return_val.choices = []
        return_val.choices.append( SimpleNamespace() )
        return_val.choices[0].message = { 'content': response }
        return return_val

    def pick_response(self, responses):
        """
        Simple algorithm for picking the best response from the network
        
        Args:
        responses (list): A list of strings with the responses from the network
        """
        for res in responses:
            res=res.strip()
            if not "Here is my inquiry: In the context of Fourier" in res and len(res) > 1:
                return res.replace("That is a great question!", "")
        return "No response given"

    def update_cost(self, prompt_tokens, completion_tokens, model):
        """
        Update the total cost, prompt tokens, and completion tokens.

        Args:
        prompt_tokens (int): The number of tokens used in the prompt.
        completion_tokens (int): The number of tokens used in the completion.
        model (str): The model used for the API call.
        """
        self.total_prompt_tokens += prompt_tokens
        self.total_completion_tokens += completion_tokens
        self.total_cost += (
            prompt_tokens * COSTS[model]["prompt"]
            + completion_tokens * COSTS[model]["completion"]
        ) / 1000
        logger.debug(f"Total running cost: ${self.total_cost:.3f}")

    def set_total_budget(self, total_budget):
        """
        Sets the total user-defined budget for API calls.

        Args:
        total_budget (float): The total budget for API calls.
        """
        self.total_budget = total_budget

    def get_total_prompt_tokens(self):
        """
        Get the total number of prompt tokens.

        Returns:
        int: The total number of prompt tokens.
        """
        return self.total_prompt_tokens

    def get_total_completion_tokens(self):
        """
        Get the total number of completion tokens.

        Returns:
        int: The total number of completion tokens.
        """
        return self.total_completion_tokens

    def get_total_cost(self):
        """
        Get the total cost of API calls.

        Returns:
        float: The total cost of API calls.
        """
        return self.total_cost

    def get_total_budget(self):
        """
        Get the total user-defined budget for API calls.

        Returns:
        float: The total budget for API calls.
        """
        return self.total_budget
