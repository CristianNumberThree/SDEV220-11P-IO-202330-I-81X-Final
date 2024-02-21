import sqlite3
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf(data):
    doc = SimpleDocTemplate("database_contents.pdf", pagesize=letter)
    table_data = [list(data[0])]  # Convert tuple to list
    table_data.extend(data[1:])
    table = Table(table_data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])

def main():
    conn = sqlite3.connect("change_requests.db")
    c = conn.cursor()
    c.execute("SELECT * FROM change_requests")
    data = c.fetchall()
    conn.close()

    if data:
        generate_pdf(data)
        print("PDF generated successfully.")
    else:
        print("No data found in the database.")

if __name__ == "__main__":
    main()