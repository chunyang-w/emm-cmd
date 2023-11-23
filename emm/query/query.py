from rich.console import Console
from openai import AsyncOpenAI
from emm.utils.sysinfo import SysInfo
from emm.utils.config import Config


class Query():
    def __init__(self, params={
        "model_version": "gpt-3.5-turbo-1106"
    }):
        self.client = AsyncOpenAI(
            api_key=self.auth_key
        )
        self.sysinfo = SysInfo().info
        self.model_v = params["model_version"]

    @property
    def auth_key(self):
        return Config().get_config_value(
            "openai_key"
        )

    @property
    def message_assistant_sysinfo(self):
        return {
            "role": "assistant",
            "content": (
                f"The system information is: {self.sysinfo}/n"
                f"Your shell is: {self.sysinfo['shell']}/n"
                f"powershell is in use: {self.sysinfo['using_powershell']}/n"
                f"You should always return response in the format: /n"
                f"0. a json object containing a list of json objects, the key for that list should always be 'commands'/n"  # noqa
                f"1. a json object containing json objects, /n"
                f"2. each sub object has 2 entries: command and description/n"
                f"4. the key 'command' will map the value of the correct command /n" # noqa
                f"4. the key 'description' will map the value of the describing and explaining the command in a succinct way/n" # noqa

                f"You should always follow these rules: \n"
                f"1. ensure the most correct command is first in the list\n"
                f"2. You should aim for give at least 3 commands\n"
                f"3. You should provide commands which are normally used\n"
                f"4. You should provide commands which are easy to remember\n"
                f"5. You should provide commands which exceed the user's expectation\n" # noqa
                f"6. You should ensure the structure of the returned object is consistent even when the number of suggestions is changing\n" # noqa
            )
        }

    @property
    def message_system(self):
        return {
            "role": "system",
            "content": (
                "You are a command line assistant,"
                "You can provide correct commands "
                "adapted to specific operating systems "
                "and shells."
            )
        }

    async def get_res(self, query):
        current_query = {
            "role": "user",
            "content": (
                f"provide command to achieve \"{query}\" "
                f"for given system&shell."
            )
        }
        console = Console()
        with console.status("[bold blue]Loading...", spinner="dots"):
            completion = await self.client.chat.completions.create(
                model=self.model_v,
                response_format={
                    "type": "json_object",
                },
                messages=[
                    self.message_system,
                    self.message_assistant_sysinfo,
                    current_query
                ]
            )
        res = completion.choices[0].message.content
        return res
