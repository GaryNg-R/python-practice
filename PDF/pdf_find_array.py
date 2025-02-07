import fitz  # PyMuPDF

# Open the PDF
doc = fitz.open("cat.pdf")

# Define the list of phrases to redact (including multi-word text)
words_to_redact = ["Appa", "Decreased Appetite"]

# Iterate through each page
for page_num in range(len(doc)):
    page = doc[page_num]

    print(f"\nPage {page_num + 1}:")
    
    for phrase in words_to_redact:
        # Find phrase locations in the text
        text_instances = page.search_for(phrase)

        for inst in text_instances:
            print(f"  Redacting: '{phrase}' at {inst}")  # Print coordinates
            page.add_redact_annot(inst, fill=(0, 0, 0))  # Black out the text

    # Apply all redactions on this page
    page.apply_redactions()

# Save the redacted PDF
doc.save("redacted_file.pdf")

print("\nRedaction complete. The updated file is saved as 'redacted_file.pdf'.")
