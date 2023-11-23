import typer
import asyncio
import subprocess
from rich import print
from typing_extensions import Annotated
from emm.query.query import Query
from emm.ui.selector import get_user_choice
from emm.utils.config import Config

app = typer.Typer()


@app.command()
def main(
    query: Annotated[
        str, typer.Argument(
            help="Things to ask about ..."
        )] = "Nothing",
    chat: Annotated[
        bool, typer.Option(help="Use chat mode")] = False,
    set_auth: Annotated[
        str, typer.Argument(
            help="Set OpenAI API key")] = None,
):
    """
    Generate the correct command for a given system and shell.
    \n
    --chat: enable chat mode.
    --set_auth: set OpenAI API key.
    """
    if set_auth:
        Config().write_config({"openai_key": set_auth})
        print(
            "OpenAI API key set to: ",
            Config().get_config_value("openai_key")
        )
        return
    if chat:
        print("chat mode under construction")
    else:
        if (query == "Nothing"):
            print("Hi, I am a command line assistant.")
            print("Please tell me how can I help :-)")
        else:
            print("[blue underline]Searching for the correct command ...")
            res = asyncio.run(Query().get_res(query))
            cmd = get_user_choice(res)
            subprocess.run(
                cmd, check=True,
                text=True, shell=True
            )


if __name__ == "__main__":
    typer.run(main)
