# scene_engine/object_manager.py
# Handles object state and spatial manipulation

class SceneObject:
    def __init__(self, label, position):
        self.label = label
        self.position = position  # [x, y, z]

    def move(self, direction_vector):
        self.position = [p + d for p, d in zip(self.position, direction_vector)]
        print(f"Moved '{self.label}' to {self.position}")


class ObjectManager:
    def __init__(self, objects):
        self.objects = {obj.label: obj for obj in objects}

    def get_position(self, label):
        obj = self.objects.get(label)
        return obj.position if obj else None

    def move_object(self, label, direction):
        direction_map = {
            "left": [-0.5, 0, 0],
            "right": [0.5, 0, 0],
            "forward": [0, 0, 0.5],
            "backward": [0, 0, -0.5],
            "up": [0, 0.5, 0],
            "down": [0, -0.5, 0]
        }
        direction_vector = direction_map.get(direction.lower())
        if label in self.objects and direction_vector:
            self.objects[label].move(direction_vector)
        else:
            print(f"Invalid label '{label}' or direction '{direction}'")


# Example usage
if __name__ == '__main__':
    from copy import deepcopy
    scene_objects = [
        SceneObject("red chair", [1.0, 0.0, 2.0]),
        SceneObject("wooden table", [0.0, 0.0, 0.0]),
        SceneObject("blue box", [-1.5, 0.0, 1.0]),
        SceneObject("white sofa", [2.0, 0.0, -1.0])
    ]

    manager = ObjectManager(scene_objects)
    print("Initial position:", manager.get_position("red chair"))
    manager.move_object("red chair", "left")
    print("After move:", manager.get_position("red chair"))
