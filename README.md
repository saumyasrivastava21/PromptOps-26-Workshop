# 🚀 PromptOps’26 — From Prompts to Production Systems

From prompts to production — building real AI systems, not just learning them.

PromptOps’26 was a 3-day intensive, hands-on AI engineering workshop conducted at Madan Mohan Malaviya University of Technology (MMMUT).

This repository contains the complete workshop implementation structured day-wise.

---

## 📌 Workshop Philosophy

The goal was simple:

Engineering with AI > Just using AI

Participants moved from prompt engineering fundamentals to deploying real production systems in just three days.

Complete lifecycle covered:

Prompting → Development → Deployment

---

# 📂 Repository Structure

```
PromptOps-26-Workshop/
│
├── PromptOps' Day1/
├── PromptOps' Day2/
├── PromptOps' Day3/
├── cursor_project/
└── README.md
```

---

# 📅 Day-wise Breakdown

---

## 🔹 PromptOps' Day1 — Prompt Engineering Foundations

Focus:
- Understanding LLM behavior
- Structured prompting
- Few-shot prompting
- Role-based prompting
- Output formatting strategies
- System-level instruction design

Tools Used:
- ChatGPT
- Claude
- GitHub Copilot

Outcome:
Participants learned how to:
- Break problems into structured prompts
- Control model outputs
- Design reproducible AI workflows

---

## 🔹 PromptOps' Day2 — Computer Vision: Face Detection System

Focus:
- Real-time Face Detection using OpenCV
- DNN-based inference using Res10 SSD model
- Google Colab + VS Code implementation

Tech Stack:
- Python
- OpenCV
- NumPy
- Pretrained Res10 SSD Model

Pipeline Architecture:

Input (Image / Webcam)
        ↓
Preprocessing (Resize + Blob Conversion)
        ↓
DNN Model Inference
        ↓
Confidence Filtering
        ↓
Bounding Box Drawing
        ↓
Face Extraction & Saving

Key Learnings:
- How pretrained models are loaded
- Confidence threshold tuning
- Real-time webcam frame processing
- Face cropping & storage pipeline

---

## 🔹 PromptOps' Day3 — From Development to Deployment

Focus:
- AI-assisted development using Cursor AI
- Code generation & debugging workflows
- Production deployment

Deployment Platform:
- Vercel

Topics Covered:
- Git-based workflow
- Production builds
- Environment setup
- Live deployment

Outcome:
Students deployed live websites publicly accessible on the internet.

---

## 💻 Cursor Project

The `cursor_project/` directory contains:

- AI-assisted frontend development
- Project scaffolding
- Structured UI components
- Production-ready web implementation

This demonstrates:
Using AI as an engineering partner — not just a code generator.

---

# 📊 Impact Metrics

- 300+ Participants
- 180+ Face Detection systems built
- 60+ Websites deployed
- 3 Days of execution-focused implementation
- Fully hands-on learning model

---

# 🛠 How to Run Face Detection Project

## 1️⃣ Install Dependencies

```bash
pip install opencv-python numpy
```

## 2️⃣ Run

```bash
python face_detect.py
```

(Ensure model files are placed correctly inside the project directory.)

---

# 🎯 Core Engineering Principles Taught

- Prompting is structured engineering
- AI is a system, not magic
- Shipping matters more than theory
- Deployment is part of learning
- Build → Test → Deploy → Iterate

---

# 🤝 Contribution

If you were a participant:

- Improve prompt workflows
- Optimize CV pipeline
- Enhance frontend system
- Add production-level features
- Raise Pull Requests

---

# 🏁 Conclusion

PromptOps’26 demonstrated that students can move from:

Learning AI → Building AI → Deploying AI

All within 3 focused execution-driven days.

This repository serves as a documentation of that engineering journey.

