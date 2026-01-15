import argparse
from scanner.idor import scan_idor
from scanner.auth import scan_auth
from scanner.exposure import scan_exposure
from scanner.misconfig import scan_misconfig
from report import generate_report

def main():
    parser = argparse.ArgumentParser(
        description="OWASP API Top 10 - Security Scanner (passive & educational)"
    )
    parser.add_argument("--url", required=True, help="Base API URL")
    parser.add_argument("--endpoint", required=True, help="Endpoint with object ID")
    parser.add_argument(
        "--output",
        default="report.json",
        help="Output report file (json | html | pdf)"
    )

    args = parser.parse_args()

    print("\n[+] API Security Scan Started\n")

    results = {
        "idor": scan_idor(args.url, args.endpoint),
        "auth": scan_auth(args.url, args.endpoint),
        "exposure": scan_exposure(args.url, args.endpoint),
        "misconfiguration": scan_misconfig(args.url, args.endpoint)
    }

    generate_report(args.output, results)

    print("\n[+] Scan completed")
    print(f"📄 Report generated: {args.output}")

if __name__ == "__main__":
    main()