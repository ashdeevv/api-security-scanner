import json
from datetime import datetime
from fpdf import FPDF

def generate_report(filename, results):
    data = {
        "tool": "OWASP API Security Scanner",
        "version": "1.1",
        "date": datetime.now().strftime("%d/%m/%Y"),
        "results": results
    }

    if filename.endswith(".json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    elif filename.endswith(".html"):
        with open(filename, "w") as f:
            f.write("<html><body>")
            f.write("<h1>API Security Scan Report</h1>")
            f.write(f"<p><b>Date:</b> {data['date']}</p>")

            for k, v in results.items():
                f.write(f"<h2>{k.upper()}</h2><ul>")
                if v:
                    for i in v:
                        f.write(f"<li>{i}</li>")
                else:
                    f.write("<li>No issue detected</li>")
                f.write("</ul>")

            f.write("</body></html>")

    elif filename.endswith(".pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(0, 10, "API Security Scan Report", ln=True)
        pdf.cell(0, 10, f"Date: {data['date']}", ln=True)
        pdf.ln(5)

        for k, v in results.items():
            pdf.cell(0, 10, k.upper(), ln=True)
            if v:
                for i in v:
                    pdf.multi_cell(0, 8, "- " + i)
            else:
                pdf.multi_cell(0, 8, "No issue detected")
            pdf.ln(2)

        pdf.output(filename)