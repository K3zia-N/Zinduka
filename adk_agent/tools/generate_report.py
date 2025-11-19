# chatbot/adk_agent/tools/generate_report.py
def generate_report(form_data: dict) -> str:
    """
    Minimal demo: produce a plain-text 'report' and return its first chars.
    Replace with a Vertex AI call to generate a lawful formatted report,
    then save to cloud storage and return a download link.
    """
    name = form_data.get("name")
    date = form_data.get("date")
    location = form_data.get("location")
    narrative = form_data.get("narrative", "")

    report = (
        f"LEGAL REPORT FORM\n"
        f"Name: {name}\nDate: {date}\nLocation: {location}\n\nIncident Narrative:\n{narrative}\n"
    )
    # For demo, return truncated content (in real app produce PDF and store)
    return report
