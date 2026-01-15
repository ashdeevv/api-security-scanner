import requests

SENSITIVE_FIELDS = [
    "password",
    "passwd",
    "token",
    "secret",
    "api_key",
    "role",
    "is_admin",
    "email"
]

def scan_exposure(base_url, endpoint):
    print("[+] Checking Excessive Data Exposure")
    findings = []

    url = base_url.rstrip("/") + endpoint

    try:
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            try:
                data = r.json()

                if isinstance(data, dict):
                    for field in SENSITIVE_FIELDS:
                        if field in data:
                            findings.append(
                                f"Sensitive field exposed in response: {field}"
                            )
            except ValueError:
                pass
    
    except requests.exceptions.RequestException:
        findings.append("Request error during exposure check")

    return findings