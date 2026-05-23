"""
REST API Client CLI — Typer-based starter
Usage:
    python main.py --help
    python main.py get /users
    python main.py post /users --data '{"name": "Alice"}'
    python main.py delete /users/1 --confirm
"""

import json
import sys
from enum import Enum
from pathlib import Path
from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.json import JSON
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(
    name="apicli",
    help="A production-grade REST API client CLI.",
    add_completion=True,
    rich_markup_mode="rich",
)
console = Console()
err_console = Console(stderr=True, style="bold red")


# Config — loaded from ~/.apicli/config.json

CONFIG_PATH = Path.home() / ".apicli" / "config.json"
DEFAULT_CONFIG = {"base_url": "https://jsonplaceholder.typicode.com", "timeout": 10}


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return {**DEFAULT_CONFIG, **json.loads(CONFIG_PATH.read_text())}
    return DEFAULT_CONFIG


def save_config(cfg: dict) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))


#http header

def build_client(cfg: dict) -> httpx.Client:
    return httpx.Client(
        base_url=cfg["base_url"],
        timeout=cfg["timeout"],
        headers={"Accept": "application/json"},
        follow_redirects=True,
    )


def parse_data(data: Optional[str]) -> Optional[dict]:
    if data is None:
        return None
    try:
        return json.loads(data)
    except json.JSONDecodeError as exc:
        err_console.print(f"[!] Invalid JSON: {exc}")
        raise typer.Exit(code=1)


def parse_headers(headers: list[str]) -> dict:
    """Parse 'Key:Value' strings into a dict."""
    result = {}
    for h in headers:
        if ":" not in h:
            err_console.print(f"[!] Bad header format (expected Key:Value): {h}")
            raise typer.Exit(code=1)
        k, _, v = h.partition(":")
        result[k.strip()] = v.strip()
    return result


def display_response(resp: httpx.Response, raw: bool = False) -> None:
    status_color = "green" if resp.status_code < 400 else "red"
    console.print(
        f"\n[bold]Status:[/bold] [{status_color}]{resp.status_code} {resp.reason_phrase}[/{status_color}]"
        f"  [dim]{resp.elapsed.total_seconds():.3f}s[/dim]"
    )

    if raw:
        console.print(resp.text)
        return

    try:
        body = resp.json()
        if isinstance(body, list):
            _render_list(body)
        else:
            console.print(Panel(JSON(json.dumps(body, indent=2)), title="Response"))
    except Exception:
        console.print(resp.text)


def _render_list(items: list) -> None:
    if not items or not isinstance(items[0], dict):
        console.print(items)
        return
    table = Table(show_header=True, header_style="bold cyan", expand=True)
    cols = list(items[0].keys())
    for col in cols:
        table.add_column(col, overflow="fold")
    for item in items:
        table.add_row(*[str(item.get(c, "")) for c in cols])
    console.print(table)


#comands

@app.command()
def get(
    path: str = typer.Argument(..., help="Endpoint path, e.g. /users/1"),
    params: list[str] = typer.Option([], "--param", "-p", help="Query params as key=value"),
    headers: list[str] = typer.Option([], "--header", "-H", help="Extra headers as Key:Value"),
    raw: bool = typer.Option(False, "--raw", help="Print raw response text"),
):
    """Send a GET request."""
    cfg = load_config()
    query = dict(p.split("=", 1) for p in params if "=" in p)
    with build_client(cfg) as client:
        resp = client.get(path, params=query, headers=parse_headers(headers))
    display_response(resp, raw=raw)


@app.command()
def post(
    path: str = typer.Argument(..., help="Endpoint path"),
    data: Optional[str] = typer.Option(None, "--data", "-d", help="JSON body as string"),
    file: Optional[Path] = typer.Option(None, "--file", "-f", help="Path to a JSON file"),
    headers: list[str] = typer.Option([], "--header", "-H", help="Extra headers as Key:Value"),
):
    """Send a POST request with a JSON body."""
    cfg = load_config()
    if file:
        body = json.loads(file.read_text())
    else:
        body = parse_data(data)
    with build_client(cfg) as client:
        resp = client.post(path, json=body, headers=parse_headers(headers))
    display_response(resp)


@app.command()
def put(
    path: str = typer.Argument(...),
    data: Optional[str] = typer.Option(None, "--data", "-d"),
    file: Optional[Path] = typer.Option(None, "--file", "-f"),
    headers: list[str] = typer.Option([], "--header", "-H"),
):
    """Send a PUT request."""
    cfg = load_config()
    body = json.loads(file.read_text()) if file else parse_data(data)
    with build_client(cfg) as client:
        resp = client.put(path, json=body, headers=parse_headers(headers))
    display_response(resp)


@app.command()
def patch(
    path: str = typer.Argument(...),
    data: Optional[str] = typer.Option(None, "--data", "-d"),
    headers: list[str] = typer.Option([], "--header", "-H"),
):
    """Send a PATCH request."""
    cfg = load_config()
    with build_client(cfg) as client:
        resp = client.patch(path, json=parse_data(data), headers=parse_headers(headers))
    display_response(resp)


@app.command()
def delete(
    path: str = typer.Argument(...),
    confirm: bool = typer.Option(False, "--confirm", help="Skip confirmation prompt"),
    headers: list[str] = typer.Option([], "--header", "-H"),
):
    """Send a DELETE request."""
    if not confirm:
        typer.confirm(f"Delete {path}?", abort=True)
    cfg = load_config()
    with build_client(cfg) as client:
        resp = client.delete(path, headers=parse_headers(headers))
    display_response(resp)




config_app = typer.Typer(help="Manage CLI configuration.")
app.add_typer(config_app, name="config")


@config_app.command("set")
def config_set(
    base_url: Optional[str] = typer.Option(None, "--base-url", help="API base URL"),
    timeout: Optional[int] = typer.Option(None, "--timeout", help="Request timeout in seconds"),
):
    """Update configuration values."""
    cfg = load_config()
    if base_url:
        cfg["base_url"] = base_url
    if timeout:
        cfg["timeout"] = timeout
    save_config(cfg)
    console.print(f"[green]Config saved to {CONFIG_PATH}[/green]")


@config_app.command("show")
def config_show():
    """Display current configuration."""
    cfg = load_config()
    console.print(Panel(JSON(json.dumps(cfg, indent=2)), title=f"Config ({CONFIG_PATH})"))




if __name__ == "__main__":
    app()