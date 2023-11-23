import json
from rich import print
from rich.console import Console
from rich.table import Table
from InquirerPy import inquirer


def display_options_with_table(choices):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Command", style="dim")
    table.add_column("Description")

    for choice in choices:
        table.add_row(
            choice["name"],
            choice["description"],
            end_section=True
        )

    console.print(table)


def get_user_choice(choices):
    choices = json.loads(choices)
    choices = choices["commands"]
    num_choices = len(choices)

    cmd_choices = [
        c["command"]
        for c in choices
    ]

    des_choices = [
        c["description"]
        for c in choices
    ]

    choice_all = [
        {
            "name": cmd_choices[i],
            "value": cmd_choices[i],
            "description": des_choices[i]
        }
        for i in range(num_choices)
    ]

    print(f"[bold green]Done![/bold green] {num_choices} commands found, showing command descriptions:")  # noqa
    display_options_with_table(choice_all)
    print()
    cmd = inquirer.select(
        message="Choose command to run:",
        choices=choice_all,
        instruction="(Use arrow keys to navigate)",
        multiselect=False,
    ).execute()
    print(f"[bold green]Running command:[/bold green] {cmd}")

    return cmd
