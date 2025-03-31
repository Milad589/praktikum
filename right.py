import ast
import operator

def compute_expression(expression):
    """Parst und berechnet einen mathematischen Ausdruck sicher."""
    
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod
    }

    def evaluate(node):
        """Rekursiv den Ausdruck auswerten."""
        if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return allowed_operators[type(node.op)](left, right)
        elif isinstance(node, ast.Num):  # Wenn es eine Zahl ist
            return node.n
        else:
            raise ValueError("Ungültiger Ausdruck")

    try:
    
        tree = ast.parse(expression, mode='eval')
        
        return evaluate(tree.body)
    except Exception:
        raise ValueError("Fehlerhafte Eingabe")