import typer
import asyncio
import subprocess

from rich import print
from typing_extensions import Annotated

from emm.utils.config import Config
from emm.query.query import Query
from emm.chat.chat import Chat
from emm.ui.selector import get_user_choice
from emm.ui.answer import get_user_answer
from emm.config import __version__
from art import text2art

app = typer.Typer()


@app.command()
def main(
    query: Annotated[
        str, typer.Argument(
            help="Things to ask about ..."
        )] = "Nothing",
    chat: Annotated[
        bool, typer.Option(help="Use chat mode")] = False,
    version: Annotated[
        bool, typer.Option(help="show version")] = False,
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
    if version:
        print(text2art("EMM-CMD"))
        print("emm v", __version__)
        return
    if set_auth:
        Config().write_config({"openai_key": set_auth})
        return
    if chat:
        res = asyncio.run(Chat().get_res(query))
        get_user_answer(res)
    else:
        if (query == "Nothing"):
            print(text2art("EMM-CMD"))
            print("[blue bold]EMM-CMD: A command line assistant.")
            print("[green bold]Try:")
            print("\temm \"how to list all files in this dir\"")
            print()
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
