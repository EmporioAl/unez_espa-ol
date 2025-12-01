
class UnezInterpreter:
    """Interpreta instrucciones y devuelve un resultado."""

    def interpretar(self, texto: str) -> str:
        if not texto:
            return "Entrada vacía"
        return f"Interpretado: {texto}"
