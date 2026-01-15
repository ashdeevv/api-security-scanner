# 🔐 OWASP API Security Scanner (Python)

Passive and educational **API security scanner** based on the **OWASP API Top 10**.  
This tool is designed for **learning, API security assessments and cybersecurity portfolios**.

⚠️ **Educational use only**  
No exploitation, no bruteforce, no intrusive testing.

---

## 🎯 Purpose

The goal of this project is to:
- Understand **modern API security risks**
- Learn how **API vulnerabilities are detected logically**
- Build a **professional cybersecurity portfolio project**
- Apply **OWASP API Top 10 methodology**

---

## 🚀 Features

- **API1 – Broken Object Level Authorization (IDOR / BOLA)**
- **API2 – Broken Authentication (logical detection)**
- **API3 – Excessive Data Exposure**
- **API7 – Security Misconfiguration**
- Passive HTTP analysis (status codes, headers, JSON structure)
- Clean CLI interface
- JSON / HTML / PDF report generation

---

## 📁 Project Structure

api-security-scanner/
│
├── main.py # CLI entry point
├── report.py # Report generation (JSON / HTML / PDF)
├── requirements.txt
├── scanner/
│ ├── init.py
│ ├── idor.py # API1 – IDOR / BOLA
│ ├── auth.py # API2 – Broken Authentication
│ ├── exposure.py # API3 – Excessive Data Exposure
│ └── misconfig.py # API7 – Security Misconfiguration
│
└── tests/
└── test_idor.py

yaml
Copier le code

---

## ⚙️ Installation

```bash
git clone https://github.com/ashdeevv/api-security-scanner.git
cd api-security-scanner
pip install -r requirements.txt
▶️ Usage
bash
Copier le code
python3 main.py --url https://api.example.com --endpoint /users/1
Generate reports
bash
Copier le code
python3 main.py --url https://api.example.com --endpoint /users/1 --output report.json
python3 main.py --url https://api.example.com --endpoint /users/1 --output report.html
python3 main.py --url https://api.example.com --endpoint /users/1 --output report.pdf
📄 Example Report (JSON)
json
Copier le code
{
  "tool": "OWASP API Security Scanner",
  "version": "1.1",
  "summary": {
    "total_checks": 4,
    "total_findings": 2
  },
  "results": {
    "idor": ["Possible IDOR/BOLA detected"],
    "auth": [],
    "exposure": ["Sensitive field exposed: role"],
    "misconfiguration": []
  }
}
🧠 Methodology
Passive analysis only

No authentication bypass

No data modification

No denial of service

Logical comparison of responses

OWASP API Top 10 aligned

🎓 Use Cases
Cybersecurity learning

OWASP API Top 10 understanding

API security awareness

Junior pentest / SOC portfolio

Secure API development mindset

🧪 Testing
Unit tests are included to validate core logic.

bash
Copier le code
pytest
📜 License
MIT License

📌 Disclaimer
This tool is provided for educational purposes only.
Unauthorized testing against systems you do not own or have permission to test is strictly prohibited.

👤 Author
Ashdeevv
Cybersecurity & Pentest • Python Developer

yaml
Copier le code

---

## ✅ Pourquoi ce README est “pro”

✔ clair  
✔ lisible par un recruteur  
✔ vocabulaire entreprise  
✔ pas de zone grise légale  
✔ bien structuré  
✔ facilement maintenable  

👉 **C’est exactement ce qu’on attend d’un projet sérieux.**

---

### 🚀 Suite possible
Si tu veux, on peut :
- ajouter des **badges GitHub**
- créer une **release v1.0**
- préparer un **pitch entretien**
- connecter ce projet à ton **framework de pentest**

Dis-moi 🔐💼






Vous avez dit :

readme avec ça 

ChatGPT a dit :
Parfait 👌
Je te fais un README parfaitement aligné avec ce que tu as réellement codé (structure, modules, mock API, rapports).
👉 Aucun bullshit, 100 % cohérent avec ta capture.

Copie-colle tel quel dans README.md.

markdown
Copier le code
# 🔐 API Security Scanner (OWASP API Top 10)

Passive and educational **API security scanner** written in Python, aligned with the **OWASP API Top 10**.  
This project focuses on **logical detection**, **safe analysis**, and **professional reporting**.

⚠️ Educational & defensive use only  
No exploitation, no bruteforce, no intrusive testing.

---

## 🎯 Project Goals

- Learn **modern API security risks**
- Apply **OWASP API Top 10 methodology**
- Detect common API issues using **passive techniques**
- Build a **professional cybersecurity portfolio project**
- Generate **audit-ready reports** (JSON / HTML / PDF)

---

## 🚀 Features

- **API1 – Broken Object Level Authorization (IDOR / BOLA)**
- **API2 – Broken Authentication (logical detection)**
- **API3 – Excessive Data Exposure**
- **API7 – Security Misconfiguration**
- Passive HTTP analysis (status codes, headers, JSON structure)
- Clean CLI interface
- JSON / HTML / PDF report generation
- Local mock API for safe testing

---

## 📁 Project Structure

api-security-scanner/
│
├── main.py # CLI entry point
├── report.py # Report generation (JSON / HTML / PDF)
├── requirements.txt
│
├── scanner/
│ ├── init.py
│ ├── idor.py # API1 – IDOR / BOLA
│ ├── auth.py # API2 – Broken Authentication
│ ├── exposure.py # API3 – Excessive Data Exposure
│ └── misconfig.py # API7 – Security Misconfiguration
│
├── mock_api/
│ └── app.py # Vulnerable API for local testing
│
└── tests/
└── test_idor.py # Unit tests

yaml
Copier le code

---

## ⚙️ Installation

```bash
git clone https://github.com/ashdeevv/api-security-scanner.git
cd api-security-scanner
pip install -r requirements.txt
▶️ Usage
Basic scan
bash
Copier le code
python3 main.py --url https://api.example.com --endpoint /users/1
Generate reports
bash
Copier le code
python3 main.py --url https://api.example.com --endpoint /users/1 --output report.json
python3 main.py --url https://api.example.com --endpoint /users/1 --output report.html
python3 main.py --url https://api.example.com --endpoint /users/1 --output report.pdf
🧪 Local Testing with Mock API
A vulnerable API is included to safely test the scanner.

Start the mock API
bash
Copier le code
pip install flask
python3 mock_api/app.py
The API will be available at:

cpp
Copier le code
http://(ip exemple):5000
Scan the mock API
bash
Copier le code
python3 main.py --url http://ip:5000 --endpoint /users/1
Expected detections:

IDOR (BOLA)

Excessive data exposure (email, role)

Missing security headers

📄 Example Report (JSON)
json
Copier le code
{
  "tool": "OWASP API Security Scanner",
  "version": "1.1",
  "summary": {
    "total_checks": 4,
    "total_findings": 2
  },
  "results": {
    "idor": ["Possible IDOR/BOLA detected"],
    "auth": [],
    "exposure": ["Sensitive field exposed: role"],
    "misconfiguration": []
  }
}
🧠 Detection Methodology
Passive analysis only

No authentication bypass

No data modification

No denial of service

Logical comparison of responses

Header and JSON structure inspection

Fully aligned with OWASP API Top 10

🧪 Testing
Unit tests validate core logic.

bash
Copier le code
pytest
🎓 Use Cases
Cybersecurity learning

OWASP API Top 10 practice

API security awareness

Junior pentest / SOC portfolio

Secure API development mindset

📜 License
MIT License

📌 Disclaimer
This tool is provided for educational purposes only.
Do not use it against systems you do not own or have explicit permission to test.

👤 Author
ashdeevv
Cybersecurity • Pentesting • Python