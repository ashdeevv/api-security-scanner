import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Strict-Transport-Security"
]

def scan_misconfig(base_url, endpoint):
    print("[+] Checking Securit Misconfigurations")
    findings = []

    url = base_url.rstrip("/") + endpoint

    try:
        r = requests.get(url, timeout=5)

        # Headers de sécurité manquants
        for header in SECURITY_HEADERS:
            if header not in r.headers:
                findings.append(f"Missing security header: {header}")
        
        # CORS trop permissif 
        if r.headers.get("Access-Control-Allow-Origin") == "*":
            findings.append("CORS misconfiguration: Access-Control-Allow-Origin set to '*'")

        # Mode debug exposé (heuristique)
        if "debug" in r.text.lower():
            findings.append("Debug information possibly exposed")
    
    except requests.exceptions.RequestException:
        findings.append("Request error during misconfiguration check")
    
    return findings