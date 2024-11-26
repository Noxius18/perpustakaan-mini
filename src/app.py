import click

@click.option('-h', help='Output Pertama')
def hello():
    click.echo("Hello Click in Python!")

if __name__== "__main__":
    hello()