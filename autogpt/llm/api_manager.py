from __future__ import annotations

import bittensor as bt
from types import SimpleNamespace


from autogpt.config import Config
from autogpt.llm.modelsinfo import COSTS
from autogpt.logs import logger
from autogpt.singleton import Singleton


class ApiManager(metaclass=Singleton):
    def __init__(self, user_text_prompting_pool = True):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0
        self.total_budget = 0

        self.user_text_prompting_pool = user_text_prompting_pool
        if self.user_text_prompting_pool:
            self.wallet = bt.wallet()
            self.met = bt.subtensor().metagraph(1)
            self.pprompt = bt.text_prompting_pool( keypair = self.wallet.hotkey, metagraph = self.met )

        else:
            self.llm = bt.prompting()
        

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

        cfg = Config()
        if temperature is None:
            temperature = cfg.temperature

        # While system prompts are injected/ignored, we instead convert the system role into user role
        for i, message in enumerate(messages):
            if message[ "role" ] == "system":
                messages[i][ "role" ] = "user"

        print ('\nmessages', messages )

        if self.user_text_prompting_pool:
            pass
            roles = [el["role"] for el in messages]
            messages = [el["content"] for el in messages]
            resps = self.pprompt( roles = roles, messages = messages, timeout = 24)
            
            resps = [res.completion for res in resps]

            response = max(resps, key=len)
            if len(response) == 0:
                response = "No response from the network"


        else:
            response = self.llm( content = messages )
        
        logger.debug(f"Response: {response}")
        print ('\nStart response:\n', response )
        print("End response\n")
        r = SimpleNamespace()
        r.choices = []
        r.choices.append( SimpleNamespace() )
        r.choices[0].message = { 'content': response }
        prompt_tokens = 0
        completion_tokens = 0
        self.update_cost(prompt_tokens, completion_tokens, model)
        return r

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
