dolar : float = 3128.65

# Obtener la TRM actual desde la API de dolarapi.com
def get_trm() -> float:
    import json
    import subprocess

    global dolar

    res : subprocess.CompletedProcess = subprocess.run(["curl", "https://co.dolarapi.com/v1/trm"], capture_output=True, text=True, check=False)

    dolar = json.loads(res.stdout).get("valor")

    print(f"TRM actual: ${dolar:,.3f}")

    return dolar