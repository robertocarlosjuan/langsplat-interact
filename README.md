# LangSplat-Interact

**LangSplat-Interact** is an experimental extension of [LangSplat](https://github.com/minghanqin/LangSplat) that enables dynamic interaction with 3D scenes using natural language commands. It explores how users can issue textual instructions to manipulate and query elements within a 3D Gaussian Splatting scene in real-time.

---

## ✨ Project Goal

To build a prototype system that:
- Understands and parses natural language commands
- Maps those commands to 3D operations (e.g., highlighting, moving objects)
- Interacts with LangSplat’s language-embedded 3D Gaussians

---

## 📦 Features

-  **Open-vocabulary querying** within 3D scenes using LangSplat
-  **Natural language command interface** (e.g., "highlight the red chair", "move the box to the left")
-  **NLP parsing + scene grounding** pipeline using CLIP or LLaVA
-  Scene manipulation: highlight, tag, or relocate objects

---

## 🧠 Background

This project builds on LangSplat’s ability to embed language features in 3D scenes via Gaussian Splatting. We aim to push this further by adding:
- Language-driven **interaction**, not just querying
- **Scene manipulation**, such as dynamic updates to object positions
- Exploration of **robot-human interaction** or AR/VR interfaces

---

## 📁 Repo Structure (WIP)
```
langsplat-interact/
├── lang_interface/         # NLP models & parser
├── scene_engine/           # Scene controller & manipulation APIs
├── ui/                     # Simple UI for command input (streamlit or CLI)
├── langsplat_core/         # Wrapper or forked module of LangSplat
├── examples/               # Test scenes and sample commands
└── README.md
```

---

## 🛠️ Setup (To be developed)
```bash
conda create -n langsplat-interact python=3.10
conda activate langsplat-interact
# Install dependencies
```

---

## 🚀 Example Commands (Planned)
- "Highlight all the chairs."
- "Move the red object to the right."
- "What is in front of the robot?"

---

## 🤝 Contributions
Open to feedback, ideas, and PRs — especially on language parsing and real-time interaction!

---

## 📚 References
- [LangSplat (Qin et al. 2023)](https://arxiv.org/abs/2312.16084)
- [CLIP (Radford et al.)](https://openai.com/research/clip)
- [Segment Anything (SAM)](https://github.com/facebookresearch/segment-anything)

---

## 🧭 Motivation
This project is inspired by the vision of seamless interaction with 3D environments — bridging the gap between language, perception, and action. It’s particularly relevant to robotics, AR/VR, and sim-to-real workflows.

> Built with ❤️ by a student researcher passionate about 3D vision and interactive AI. Work in progress!
