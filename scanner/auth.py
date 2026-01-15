import requests

def scan_auth(base_url, endpoint):
    print("[+] Checking Broken Authentication")
    findings = []

    url = base_url.rstrip("/") + endpoint

    try:
        r = requests.get(url, timeout=5)

        # Cas suspect : accès sans auth
        if r.status_code == 200:
            findings.append(
                "Possible Broken Authentication: endpoint accessible without authentication"
            )

        # Maucaise pratique : www-Authenticate manquant 
        if r.status_code == 401 and "WWW-Authenticate" not in r.headers:
            findings.append(
                "Authentication challenge missing (WWW-Authenticate header)"
            )
    
    except requests.exceptions.RequestException:
        findings.append("Request error during authentication check")

    return findings