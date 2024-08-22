def search_email(name):
    email_directory = {
        "John": "john.doe@example.com",
        "Jane": "jane.smith@example.com",
        "Bob": "bob.johnson@example.com"
    }

    if name in email_directory:
        email = email_directory[name]
    else:
        print(f"No email found for {name}")

    return email
