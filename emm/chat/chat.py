from rich.console import Console
from openai import AsyncOpenAI
from emm.utils.sysinfo import SysInfo
from emm.utils.config import Config


class Chat():
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
                f"Please answer the query, if the query involves "
                f"system/platform dependent response, "
                f"please adjust the response according to the system/platform."
            )
        }

    @property
    def message_system(self):
        return {
            "role": "system",
            "content": (
                "You are a command line assistant,"
                "Please answer the query of the user "
                "in a proper way so it can be displayed "
                "in the terminal properly."
            )
        }

    async def get_res(self, query):
        current_query = {
            "role": "user",
            "content": (
                f"Answer the query: \"{query}\" "
            )
        }
        console = Console()
        with console.status("[bold blue]Loading...", spinner="dots"):
            completion = await self.client.chat.completions.create(
                model=self.model_v,
                messages=[
                    self.message_system,
                    self.message_assistant_sysinfo,
                    current_query
                ]
            )
        res = (completion.choices[0].message.content)
        return res
