import os
from src import config
from src.models import model_parser


def auto(xml_location):
    manager = model_parser.new(xml_location)

