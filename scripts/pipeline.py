import pandas as pd
from pathlib import Path
from tqdm import tqdm

#from scripts.extract_features import get_ast, extract_features
#from scripts.benchmark_runner import compile_and_time
from extract_features import get_ast, extract_features
from benchmark_runner import compile_and_time


SRC_DIR = Path("c_sources")
FLAGS = ["-O1", "-O2", "-O3", "-O2 -funroll-loops"]
rows = []

def main():
    for cfile in tqdm(SRC_DIR.glob("*.c")):
        print(f"\n🔍 Processing: {cfile.name}")
        ast = get_ast(cfile)
        feats = extract_features(ast)
        if not feats:
            print(f"[⚠️] Skipping {cfile.name} due to empty or failed AST parse.")
            continue

        feats["loc"] = sum(1 for _ in open(cfile))

        for flag in FLAGS:
            runtime = compile_and_time(cfile, flag)
            if runtime is not None:
                print(f"✅ {cfile.name} [{flag}] — {runtime:.2f} ms")
                rows.append({
                    **feats,
                    "flags": flag,
                    "runtime_ms": runtime,
                    "file": cfile.name
                })
            else:
                print(f"[⚠️] Skipped runtime for {cfile.name} with {flag}")

    df = pd.DataFrame(rows)
    df.to_csv("dataset.csv", index=False)
    print("\n✅ Dataset saved to dataset.csv")

if __name__ == "__main__":
    main()
