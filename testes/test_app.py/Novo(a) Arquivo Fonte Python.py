import pytest
from unittest.mock import patch
from src.app import main


def test_fluxo_basico():
    # Simula entradas do usuário:
    # 1 = adicionar tarefa
    # "Estudar" = nome
    # "30" = tempo
    # 2 = listar tarefas
    # 5 = sair
    entradas = ["1", "Estudar", "30", "2", "5"]

    with patch("builtins.input", side_effect=entradas):
        with patch("builtins.print") as mock_print:
            main()

            assert mock_print.called