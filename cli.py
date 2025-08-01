from typer import Typer
from commands.init_database.main import init_database
from commands.init_database.test_connection import test_db_connection
import asyncio

app = Typer()


@app.command("init_database")
def cmd_init_database():
    print("Initializing database")
    asyncio.run(init_database())


@app.command("run_test")
def cmd_run_test():
    print("Running tests")
    # TODO: Add test execution logic here
    print("Tests executed successfully")

@app.command("test_connection")
def cmd_test_connection():
    asyncio.run(test_db_connection())

if __name__ == "__main__":
    app()
