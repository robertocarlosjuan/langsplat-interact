# lang_interface/command_parser.py
# Parses natural language commands and finds matching objects using CLIP

import torch
import clip
from PIL import Image
import numpy as np
import open3d as o3d

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Example scene labels and mock object positions (in world coordinates)
scene_objects = [
    {"label": "red chair", "position": [1.0, 0.0, 2.0]},
    {"label": "wooden table", "position": [0.0, 0.0, 0.0]},
    {"label": "blue box", "position": [-1.5, 0.0, 1.0]},
    {"label": "white sofa", "position": [2.0, 0.0, -1.0]}
]
scene_labels = [obj["label"] for obj in scene_objects]

# Mock function: Precomputed feature vectors for each object label
@torch.no_grad()
def compute_label_features(labels):
    text_tokens = clip.tokenize(labels).to(device)
    text_features = model.encode_text(text_tokens)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    return text_features

# Match command to most similar label
def match_command_to_label(command: str, label_features, labels):
    with torch.no_grad():
        cmd_feat = model.encode_text(clip.tokenize([command]).to(device))
        cmd_feat /= cmd_feat.norm(dim=-1, keepdim=True)
        sims = (cmd_feat @ label_features.T).squeeze()
        best_idx = sims.argmax().item()
        return labels[best_idx], sims[best_idx].item()

# Get position of matched object and visualize it

def get_object_position(label, scene_objects):
    for obj in scene_objects:
        if obj["label"] == label:
            return obj["position"]
    return None

def visualize_position(position, label):
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.1)
    sphere.translate(position)
    sphere.paint_uniform_color([1.0, 0.0, 0.0])  # red

    coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)
    print(f"Visualizing object '{label}' at position {position}")
    o3d.visualization.draw_geometries([sphere, coord_frame])

if __name__ == '__main__':
    label_feats = compute_label_features(scene_labels)
    test_command = "highlight the red object"
    match, score = match_command_to_label(test_command, label_feats, scene_labels)
    position = get_object_position(match, scene_objects)
    print(f"Command matched to: '{match}' (similarity: {score:.2f})")
    print(f"Object position in scene: {position}")

    if position is not None:
        visualize_position(position, match)
