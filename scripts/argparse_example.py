# coding: utf-8

""" Demonstration of the built-in argparse package """

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
import sys
from argparse import ArgumentParser
import logging

if __name__ == "__main__":
    # create logger
    logger = logging.getLogger(__name__)
    
    # define a handler to write log messages to stdout
    sh = logging.StreamHandler(stream=sys.stdout)
    
    # define the format for the log messages, here: "level name: message"
    formatter = logging.Formatter("[%(levelname)s]: %(message)s")
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    
    # create a parser object for understanding command-line arguments
    parser = ArgumentParser(description="Describe the script")
    
    # add two boolean arguments: 'verbose' for dumping debug messages and
    #   highers, and 'quiet' for restricting to just error messages
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", 
                        default=False, help="Be chatty! (default = False)")
    parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", 
                        default=False, help="Be quiet! (default = False)")
    
    # add a required, integer argument
    parser.add_argument("-f", dest="field_id", required=True, type=int, 
                        help="Field ID")
    parser.add_argument("-p", dest="plot", action="store_true", default=False,
                        help="Generate a plot or not")
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    elif args.quiet:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)
        
    logger.debug("Here's a debug message")
    logger.info("Here's an info message")
    logger.warning("Here's a warning message")
    logger.error("Here's an error message")
