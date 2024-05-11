#!/usr/bin/env python
from agencia_noticias.crew import AgenciaNoticiasCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Inteligência artificial aplicada a gestão de obras industriais com BIM 4D e Advanced Work Packaging (AWP)'
    }
    AgenciaNoticiasCrew().crew().kickoff(inputs=inputs)