from __future__ import print_function
import sys

class Writer:

  def __init__(self):
    return None

  def add_args(self, parser):
    return parser

  def write(self, args, docs):
    print(docs, file=sys.stdout)

