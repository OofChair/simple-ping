# python-ping

Python ping package

&nbsp;  
&nbsp;  
## README Map

- To run locally, go to [Run from command line](#run-from-command-line).
- To use the main class, skip to [The main class](#the-main-class).
- Instructions on advanced/technical documentation, go to [Documentation](#documentation).


## Run from command line
From the project's root directory, please run the following command and follow instructions:

    $ python -m ping


## The main class
With the python console and the [Ping class](ping/__init__.py), we can get things running:

    $ python
    >>> from ping import Ping
    >>> ping = Ping('localhost')
    >>> print(f'Ping avg return: {ping.avg} ms')


## Documentation
Please try from python console:

    $ python
    >>> import ping
    >>> help(ping)

Or try from command line:

    $ python -c "import ping; print(ping.__doc__)"

All documentation can be found in [docs](docs).

