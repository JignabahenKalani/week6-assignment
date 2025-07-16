from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.align import Align
import time
import os
from readme_generator.prompts import get_project_prompts
from readme_generator.readme_creator import ReadmeCreator

console = Console()

def save_to_file(content,filename):
    output_dir = 'output'
    os.makedirs(output_dir,exist_ok=True)
    with open(os.path.join(output_dir,filename),'w', encoding='utf-8') as f:
        f.write(content)

def loading_simulation(message):
    console.print(f"[bold cyan]{message}[/bold cyan]")
    for _ in track(range(10), description="Processing..."):
        time.sleep(0.3)

def main():
    console.print(Align.center(Panel("[bold blue]📄 Welcome to the README Generator[/bold blue]", subtitle="By Jigna Kalani", border_style="bold magenta")))

    project_info = get_project_prompts()

    if not project_info.get("confirm",False):
        console.print("[bold red]README generation cancelled by user.[/bold red]")
        return
    
    readme = ReadmeCreator(project_info)

    loading_simulation("Generating README....")

    readme_content = readme.generate_readme()
    save_to_file(readme_content,"README.md")

    console.print(Panel(readme_content, title="📘 README Content Preview", border_style="green"))
    console.print(Panel("[bold green]✅ README.md generated successfully in the 'output/' folder[/bold green]", border_style="green"))

if __name__ == "__main__":
    main()
