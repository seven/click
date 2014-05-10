# -*- coding: utf-8 -*-
"""
    click
    ~~~~~

    click is a simple Python module that wraps the stdlib's optparse to make
    writing command line scripts fun.  Unlike other modules it's based around
    a simple API that does not come with too much magic and is composable.

    In case optparse ever goes away from the stdlib it will be shipped by
    this module.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

# Core classes
from .core import Context, Command, MultiCommand, Group, CommandCollection, \
     Parameter, Option, Argument

# Decorators
from .decorators import pass_context, pass_obj, make_pass_decorator, \
     command, group, argument, option, confirmation_option, \
     password_option, version_option, help_option

# Types
from .types import ParamType, File, Path, Choice, IntRange, STRING, INT, \
     FLOAT, BOOL, UUID

# Utilities
from .utils import echo

# Terminal functions
from .termui import prompt, confirm, get_terminal_size, echo_via_pager

# Exceptions
from .exceptions import ClickException, UsageError, FileError, Abort

# Formatting
from .formatting import HelpFormatter, wrap_text

# Parsing
from .parser import OptionParser


__all__ = [
    # Core classes
    'Context', 'Command', 'MultiCommand', 'Group', 'CommandCollection',
    'Parameter', 'Option', 'Argument',

    # Decorators
    'pass_context', 'pass_obj', 'make_pass_decorator', 'command', 'group',
    'argument', 'option', 'confirmation_option', 'password_option',
    'version_option', 'help_option',

    # Types
    'ParamType', 'File', 'Path', 'Choice', 'IntRange', 'STRING', 'INT',
    'FLOAT', 'BOOL', 'UUID',

    # Utilities
    'echo',

    # Terminal functions
    'prompt', 'confirm', 'get_terminal_size', 'echo_via_pager',

    # Exceptions
    'ClickException', 'UsageError', 'FileError', 'Abort',

    # Formatting
    'HelpFormatter', 'wrap_text',

    # Parsing
    'OptionParser',
]
