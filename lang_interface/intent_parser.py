# lang_interface/intent_parser.py
# Extracts high-level intent from a natural language command

import re

# Very basic rule-based parser for now
def parse_command(command: str):
    command = command.lower()
    
    # Define simple patterns
    move_pattern = r"move (the )?(?P<target>.+?) (?P<direction>left|right|forward|backward|up|down)"
    highlight_pattern = r"highlight (the )?(?P<target>.+)"

    match = re.match(move_pattern, command)
    if match:
        return {
            "action": "move",
            "target": match.group("target"),
            "direction": match.group("direction")
        }

    match = re.match(highlight_pattern, command)
    if match:
        return {
            "action": "highlight",
            "target": match.group("target")
        }

    return {"action": "unknown", "raw": command}


# Example usage
if __name__ == '__main__':
    examples = [
        "move the red chair left",
        "highlight the blue box",
        "move white sofa forward"
    ]

    for cmd in examples:
        result = parse_command(cmd)
        print(f"Command: '{cmd}' → Parsed: {result}")
