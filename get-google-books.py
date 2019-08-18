import click
import requests

__author__ = 'GG'

@click.group()
def main():
    """
    Simple CLI fro quering books on Google
    """
    pass

@main.command()
@click.argument('query')
def search(query):
    """This seatch return query from Goovle Books"""
    url_format = 'https://www.googleapis.com/books/v1/volumes'
    query = '+'.join(query.split())

    query_params = {
        'q': query
    }

    response = request.get(url_format, params=query_params)

    click.echo(response.json()['items'])


@main.command()
@click.argument('id')
def get(id):
    """This resitmn a particular boo kfrom the given id"""
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
    click.echo()

    response = requests.get(url_format.format(id))
    click.echo(response.json())

if __name__ == '__main__':
    main()

