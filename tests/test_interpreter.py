
from unezespanol.interpreter import UnezInterpreter

def test_interpretar_devuelve_respuesta():
    interpreter = UnezInterpreter()
    resultado = interpreter.interpretar("Hola")
    assert resultado == "Interpretado: Hola"

def test_interpretar_entrada_vacia():
    interpreter = UnezInterpreter()
    resultado = interpreter.interpretar("")
    assert resultado == "Entrada vacía"
