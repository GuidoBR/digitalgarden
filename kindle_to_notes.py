import pandas as pd

def convert_excel_to_html(excel_file):
    # Read the spreadsheet using pandas
    df = pd.read_csv(excel_file)

    # Create HTML string with blockquote elements
    html_content = "\n"

    for index, row in df.iterrows():
        note = row['Anotação']  # Assuming 'Anotação' is the column name containing Kindle notes
        blockquote = f"<blockquote name='note_{index}'>{note}</blockquote>\n"
        html_content += blockquote


    return html_content

if __name__ == "__main__":
    # Replace 'your_kindle_notes.xlsx' with the actual file name
    excel_file = 'kindle.csv'

    # Convert Excel to HTML
    result_html = convert_excel_to_html(excel_file)

    # Write the HTML content to a file
    with open('kindle_notes.html', 'w', encoding='utf-8') as html_file:
        html_file.write(result_html)

    print("Conversion complete. HTML file created: 'kindle_notes.html'")

