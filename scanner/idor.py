import requests 
import json
import re

def extract_id(endpoint):
    match = re.search(r"/(\d+)", endpoint)
    return int(match.group(1)) if match else None

def scan_idor(base_ulr, endpoint):
    print("[+] Checking IDOR / BOLA")
    findings = []

    object_id = extract_id(endpoint)
    if object_id is None:
        findings.append("Endpoint does not contain numeric object ID")
        return findings
    
    url_1 = base_ulr.rstrip("/") + endpoint
    url_2 = base_ulr.rstrip("/") + endpoint.replace(str(object_id), str(object_id + 1))

    try:
        r1 = requests.get(url_1, timeout=5)
        r2 = requests.get(url_2, timeout=5)

        if r1.status_code == 200 and r2.status_code == 200:
            try:
                data1 = r1.json()
                data2 = r2.json()

                if isinstance(data1, dict) and isinstance(data2, dict):
                    if set(data1.keys()) == set(data2.keys()):
                        findings.append(
                            "Possible IDOR/BOLA: indentical reponse structure for different object IDs"
                        )
            except json.JSONDecodeError:
                pass
    except requests.exceptions.RequestException:
        findings.append("Request error during IDOR check")

    return findings