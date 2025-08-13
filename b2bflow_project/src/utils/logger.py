import datetime

def log(message: str) -> None:
    """Exibe mensagens com timestamp no console."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")