from api.forms.model import Forms


def retrieve_contacts():
    """List all saved contacts"""
    form = Forms()
    data = form.retrieve_saved_contacts()
    formatted_data = []
    for doc in data:
        doc.pop("_id")
        formatted_data.append(doc)

    return formatted_data
