#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from generate_sn_stories.crew import GenerateSnStories

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(topic):
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
        'language': 'português'
    }

    result_text = None
    log_messages = []
    error = None
    
    
    try:
        GenerateSnStories().crew().kickoff(inputs=inputs)
        report_path = 'output/stories.md'
        if os.path.exists(report_path):
            with open(report_path, 'r', encoding='utf-8') as f:
                result_text = f.read()
        else:
            result_text = "Processamento concluído, mas relatório não encontrado."
        log_messages.append("Processamento finalizado com sucesso.")
    except Exception as e:
            error = str(e)
            log_messages.append(f"Erro: {error}")   

    return result_text, log_messages, error

def train(topic):
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": topic,
        'current_year': str(datetime.now().year),
        'language': 'pt-br'
    }
    try:
        GenerateSnStories().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GenerateSnStories().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Quero fazer com que eu receba um pdf, identifique o conteudo e extraia as informações para associar a um incidente",
        "current_year": str(datetime.now().year),
        'language': 'pt-br'
    }
    
    try:
        GenerateSnStories().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
    