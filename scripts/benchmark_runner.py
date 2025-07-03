import subprocess
from pathlib import Path
from typing import Union

BUILD_DIR = Path("build")
BUILD_DIR.mkdir(exist_ok=True)

def compile_and_time(cfile: Path, flags: str) -> Union[float, None]:
    exe = BUILD_DIR / f"{cfile.stem}_{flags.replace(' ', '_')}"
    
    try:
        subprocess.run(
            f"gcc {cfile} {flags} -o {exe}",
            shell=True, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print(f"[❌] GCC Compilation failed for {cfile.name} with flags '{flags}':\n{e.stderr.decode()}")
        return None

    try:
        proc = subprocess.run(
            f"/usr/bin/time -v {exe}",
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10
        )
        for line in proc.stderr.decode().splitlines():
            if "User time (seconds):" in line:
                return float(line.split(":")[1].strip()) * 1000  # ms
    except subprocess.TimeoutExpired:
        print(f"[⏱️] Execution timed out for {exe}")
    except subprocess.CalledProcessError as e:
        print(f"[💥] Runtime error: {e.stderr.decode()}")
    except Exception as e:
        print(f"[‼️] Unexpected execution error: {e}")
    
    return None
