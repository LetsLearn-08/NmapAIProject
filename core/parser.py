def parse_output(raw_output):
    """
    Parses raw Nmap output into a cleaner format.
    Filters out empty lines and irrelevant headers.
    Highlights open ports with a green dot.
    """
    lines = raw_output.splitlines()
    parsed = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Starting") or line.startswith("Nmap done"):
            continue
        if "open" in line:
            parsed.append("🟢 " + line)
        else:
            parsed.append(line)

    return "\n".join(parsed)
