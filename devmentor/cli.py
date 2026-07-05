import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from devmentor.memory import DevMemory
from devmentor.router import AIRouter


app = typer.Typer(help="DevMentor AI - Your Memory-Powered CLI Agent", add_completion=False)
console = Console()
memory = DevMemory()
router = AIRouter()

@app.command()
def chat(query: str):
    """Ask DevMentor a question."""
    console.print(f"[bold blue]User:[/] {query}")
    
    # 1. Get memory context
    with console.status("[dim]Retrieving Hindsight memory...[/dim]", spinner="dots"):
        context = memory.retrieve_context(query)
    
    if context:
        console.print("[dim italic]🧠 Recalled relevant context from previous sessions.[/dim italic]")

    # 2. Ask Groq
    with console.status("[dim]Querying Groq...[/dim]", spinner="dots"):
        result = router.process_query(query, context)
    
    # 3. Display result using Rich
    console.print(Panel(result["answer"], title=f"DevMentor ({result['model']})", border_style="green"))
    console.print(f"[dim]⚡ Responded in {result['latency']}ms[/dim]")

@app.command()
def remember(content: str):
    """Manually add a memory to Hindsight."""
    memory.store(content)
    console.print(f"[bold green]✔ Remembered:[/] {content}")
    
