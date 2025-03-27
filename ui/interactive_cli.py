# ui/interactive_cli.py
# Command-line interface to test natural language interaction with 3D scene

from lang_interface.command_parser import compute_label_features, match_command_to_label
from lang_interface.intent_parser import parse_command
from scene_engine.object_manager import SceneObject, ObjectManager
from lang_interface.command_parser import visualize_position

# Define initial scene objects
scene_objects = [
    SceneObject("red chair", [1.0, 0.0, 2.0]),
    SceneObject("wooden table", [0.0, 0.0, 0.0]),
    SceneObject("blue box", [-1.5, 0.0, 1.0]),
    SceneObject("white sofa", [2.0, 0.0, -1.0])
]

labels = [obj.label for obj in scene_objects]
label_feats = compute_label_features(labels)
manager = ObjectManager(scene_objects)

print("Type commands like 'highlight the red chair' or 'move blue box forward'. Type 'exit' to quit.\n")

while True:
    command = input(">> ")
    if command.strip().lower() == "exit":
        break

    intent = parse_command(command)
    if intent["action"] == "highlight":
        matched_label, _ = match_command_to_label(intent["target"], label_feats, labels)
        position = manager.get_position(matched_label)
        if position:
            visualize_position(position, matched_label)
        else:
            print("Could not find object to highlight.")

    elif intent["action"] == "move":
        matched_label, _ = match_command_to_label(intent["target"], label_feats, labels)
        manager.move_object(matched_label, intent["direction"])

    else:
        print("Unrecognized command. Try again.")
