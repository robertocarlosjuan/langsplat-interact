# lang_interface/command_parser.py
# Parses natural language commands and finds matching objects using CLIP

import torch
import clip
from PIL import Image
import numpy as np

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Example scene labels (precomputed or mocked)
scene_labels = [
    "red chair", "wooden table", "blue box", "white sofa"
]

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

if __name__ == '__main__':
    label_feats = compute_label_features(scene_labels)
    test_command = "highlight the red object"
    match, score = match_command_to_label(test_command, label_feats, scene_labels)
    print(f"Command matched to: '{match}' (similarity: {score:.2f})")
