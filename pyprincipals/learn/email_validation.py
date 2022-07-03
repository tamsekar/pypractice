def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."

    # your code here
    for char in string:
        if char not in valid:
            return True
    return False


def is_valid(email):
    if email.count("@") != 1:
        return False

    prefix, domain = email.split("@")

    if len(prefix) == 0:
        return False

    if domain.count(".") != 1:
        return False

    domain_name, extension = domain.split(".")

    if len(domain_name) == 0 or len(extension) == 0:
        return False

    if has_invalid_characters(prefix) or has_invalid_characters(domain):
        return False

    return True


emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com",
    "test@example.co.uk",
    "test@dev.gmail.com",
    "hello+world@gmail.com",
    "UPPERCASE@example.com"
]

for email in emails:
    if is_valid(email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")