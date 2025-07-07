import re, subprocess
from pathlib import Path
from typing import Union

def get_ast(filepath: Path) -> str:
    try:
        result = subprocess.run(
            ["clang", "-Xclang", "-ast-dump", "-fsyntax-only", str(filepath)],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[⚠️] Clang AST extraction failed for {filepath.name}:\n{e.stderr}")
        return "null"

#def extract_features(ast: str) -> dict | None:
def extract_features(ast: str) -> Union[dict, None]:
    if not ast.strip():
        return None
        
    return {
        "num_loops": len(re.findall(r"(ForStmt|WhileStmt|DoStmt)", ast)),
        "max_nesting": max((len(l) - len(l.lstrip())) // 2 for l in ast.splitlines() if l.strip()),
        "num_branches": len(re.findall(r"(IfStmt|SwitchStmt)", ast)),
        "num_calls": len(re.findall(r"CallExpr", ast)),
        "num_funcs": len(re.findall(r"FunctionDecl", ast)),
    }
