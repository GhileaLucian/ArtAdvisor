# 🧠 Pre-trained Deep Learning Models

This directory contains the serialized PyTorch model weights used for inference in ArtAdvisor:

1. `model_stil_efficientnet.pth` — Art Movement / Style Classifier (EfficientNet Backbone)
2. `model_autor.pth` — Classical Painter Identification Model (27+ artists)
3. `model_licenta_definitiv.pth` — Dual-Stream Emotion Ensemble (EfficientNet-B2 + Vision Transformer ViT-B/16)

> **Note on Model Weights:** Due to GitHub's file size limits (>100MB), production weights can be downloaded from the release assets or cloud storage repository. The application includes graceful fallbacks for local architecture inspection and testing when weights are not present.
