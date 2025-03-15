import re

def identify_document(text):
    if "INCOME TAX" in text or "Permanent Account Number" in text:
        return "pan"
    elif "government of india" in text or "Aadhaar" in text:
        return "aadhaar"
    elif "driving license" in text or "DL" in text:
        return "driving_license"
    elif "PASSPORT" in text or "Government of India" in text:
        return "passport"
    else:
        return "unknown"

def extract_data(text, doc_type):
    extracted_data = {}

    if doc_type == "aadhaar":
        name_pattern = re.search(r"(?:Name\s*[:\-]?\s*)(\w+\s*\w+)", text, re.IGNORECASE)
        aadhaar_pattern = re.search(r"(\d{4}\s*\d{4}\s*\d{4})", text)
        address_pattern = re.search(r"Address\s*[:\-]?\s*([\w\s,]+)", text, re.IGNORECASE)

        if name_pattern:
            extracted_data['Name'] = name_pattern.group(1)
        if aadhaar_pattern:
            extracted_data['Aadhaar Number'] = aadhaar_pattern.group(1).replace(" ", "")
        if address_pattern:
            extracted_data['Address'] = address_pattern.group(1)

    elif doc_type == "pan":
        name_pattern = re.search(r"(Name\s*[:\-]?\s*)(\w+\s*\w+)", text, re.IGNORECASE)
        pan_pattern = re.search(r"([A-Z]{5}\d{4}[A-Z]{1})", text)
        dob_pattern = re.search(r"Date\s*of\s*Birth\s*[:\-\s]*([\d]{2}/[\d]{2}/[\d]{4})", text)

        if name_pattern:
            extracted_data['Name'] = name_pattern.group(1)
        if pan_pattern:
            extracted_data['PAN Number'] = pan_pattern.group(1)
        if dob_pattern:
            extracted_data['Date of Birth'] = dob_pattern.group(1)

    elif doc_type == "driving_license":
        name_pattern = re.search(r"(?:Name\s*[:\-]?\s*)(\w+\s*\w+)", text, re.IGNORECASE)
        license_pattern = re.search(r"([A-Z0-9]{1,15})", text)
        dob_pattern = re.search(r"(?:DOB\s*[:\-]?\s*)(\d{2}/\d{2}/\d{4})", text)
        expiry_date_pattern = re.search(r"(?:Valid\s*Till\s*[:\-]?\s*)(\d{2}/\d{2}/\d{4})", text)
        dl_number_pattern = re.search(r"(?:DL\s*[A-Z0-9]{10,15}|License\s*No\s*[:\-]?\s*[A-Z0-9]{10,15})", text, re.IGNORECASE)

        if name_pattern:
            extracted_data['Name'] = name_pattern.group(1)
        if license_pattern:
            extracted_data['License Number'] = license_pattern.group(1)
        if dl_number_pattern:
            extracted_data['DL No'] = dl_number_pattern.group(1)
        if expiry_date_pattern:
            extracted_data['Expiry Date'] = expiry_date_pattern.group(1)
        if dob_pattern:
            extracted_data['Date of Birth'] = dob_pattern.group(1)

    elif doc_type == "passport":
        name_pattern = re.search(r"(?:Name\s*[:\-]?\s*)(\w+\s*\w+)", text, re.IGNORECASE)
        passport_pattern = re.search(r"(?:Passport\s*No\s*[:\-]?\s*)(\w+)", text)
        dob_pattern = re.search(r"(?:DOB\s*[:\-]?\s*)(\d{2}/\d{2}/\d{4})", text)

        if name_pattern:
            extracted_data['Name'] = name_pattern.group(1)
        if passport_pattern:
            extracted_data['Passport Number'] = passport_pattern.group(1)
        if dob_pattern:
            extracted_data['Date of Birth'] = dob_pattern.group(1)

    return extracted_data

def format_data(extracted_data):
    formatted_data = ([f"{key}: {value}" for key, value in extracted_data.items()])
    return formatted_data
