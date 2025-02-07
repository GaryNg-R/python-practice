import fitz  # PyMuPDF

# Open the PDF
doc = fitz.open("cat.pdf")

# Define the regular expression for SSN (for example, "XXX-XX-XXXX")
ssn_regex = r"Appa"

# Iterate through each page and redact SSNs
for page_num in range(len(doc)):
    page = doc[page_num]
    text_instances = page.search_for(ssn_regex)

    print(f"\nPage {page_num + 1}:")  # Print page number

    for inst in text_instances:
        # Print the coordinates of the redaction
        print(f"  Redacting at: {inst}")

        # Redact the found instances
        page.add_redact_annot(inst, fill=(0, 0, 0))
    
    # Apply the redaction
    page.apply_redactions()

# Save the redacted PDF
doc.save("redacted_file.pdf")

print("\nRedaction complete. The updated file is saved as 'redacted_file.pdf'.")
