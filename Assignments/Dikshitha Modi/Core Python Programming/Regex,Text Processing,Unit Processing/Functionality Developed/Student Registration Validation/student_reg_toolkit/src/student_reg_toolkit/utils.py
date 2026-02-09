def normalize_name(name):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return " ".join(part.capitalize() for part in name.strip().split())

def unique_preserve_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


# Comprehension practice helpers (from Use Case 1)
mock_emails = [
    "alice@univ.edu",
    "bob@univ.edu",
    "charlie@college.org",
    "david@state.edu",
    "eve@gradschool.net",
]


def extract_usernames(emails):
    return [email.split("@")[0] for email in emails]


def filter_edu(emails):
    return [email for email in emails if email.endswith(".edu")]


def domain_types_map(emails):
    return {email.split("@")[0]: email.split(".")[-1] for email in emails}


def edu_domain_mapping(emails):
    return {email.split("@")[0]: email.split(".")[-1] for email in emails if email.endswith(".edu")}


if __name__ == "__main__":
    print("Original Emails:", mock_emails)
    print("\nExtracted Usernames:", extract_usernames(mock_emails))
    print("Emails with .edu domain:", filter_edu(mock_emails))
    print("Usernames to Domain Types:", domain_types_map(mock_emails))
    print("Usernames to .edu Domain Types:", edu_domain_mapping(mock_emails))
