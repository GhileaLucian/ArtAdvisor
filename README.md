# 🎨 ArtAdvisor · Multimodal AI & Narrative Art Interpretation Assistant

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c.svg)](https://pytorch.org/)
[![Vision Transformer](https://img.shields.io/badge/ViT-ViT--B%2F16-8A2BE2.svg)](https://huggingface.co/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o%20%7C%20TTS-412991.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

An end-to-end multimodal AI application developed as a **Bachelor Thesis Project** at the **Technical University of Cluj-Napoca (TUCN)**.

ArtAdvisor combines **computer vision**, **dual-stream deep neural networks**, and **multimodal generative LLMs** to classify classical artworks, predict affective and aesthetic dimensions, interpret visual attention through **Grad-CAM**, and synthesize rich contextual narratives in real time.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Input Layer
        UserImg["User Artwork Upload (JPG, PNG)"]
        Cropper["Interactive Region Cropping & Image Optimizer"]
    end

    subgraph Deep Learning Inference Engine
        subgraph Style Classification
            StyleNet["EfficientNet Backbone"]
            StylePred["Art Movement / Style (10 movements)"]
        end

        subgraph Author Identification
            AuthorNet["EfficientNet + Dropout Head"]
            AuthorPred["Master Painter (27+ artists)"]
        end

        subgraph Affective Dimension
            ViT["Vision Transformer (ViT-B/16)"]
            EffNet["EfficientNet-B2 Backbone"]
            Ensemble["Dual-Stream Feature Fusion"]
            EmoPred["Plutchik Emotion Taxonomy (14 classes)"]
        end

        subgraph Explainable AI
            GradCAM["Grad-CAM Saliency Maps & Heatmap Overlays"]
        end
    end

    subgraph Multimodal Generative Layer
        PromptEngine["Prompt Engineering & Aesthetic Synthesis"]
        LLM["OpenAI GPT-4o API"]
        TTS["OpenAI Audio Synthesis (Text-to-Speech)"]
        Chat["Artist Persona Interactive Q&A"]
    end

    subgraph Export and Reporting
        PDF["Executive Academic PDF Dossier (ReportLab)"]
        Radar["Emotion Distribution Radar Chart"]
    end

    UserImg --> Cropper
    Cropper --> StyleNet --> StylePred
    Cropper --> AuthorNet --> AuthorPred
    Cropper --> ViT & EffNet --> Ensemble --> EmoPred
    Cropper --> GradCAM

    StylePred & AuthorPred & EmoPred & GradCAM --> PromptEngine
    PromptEngine --> LLM --> TTS
    LLM --> Chat
    EmoPred --> Radar
    LLM & Radar & GradCAM & StylePred & AuthorPred --> PDF
```

---

## 📊 Curated Datasets & Machine Learning Methodology

The underlying models were trained on an aggregated and curated dataset of **14,000 classical art images**:
* **WikiArt Collection & ArtEmis Benchmark:** Cleaned, validated, and normalized across metadata distributions.
* **10 Art Movements:** Baroque, Impressionism, Post-Impressionism, Surrealism, Expressionism, Realism, Romanticism, Symbolism, Art Nouveau, Renaissance.
* **30 Classical Painters:** Van Gogh, Monet, Rembrandt, Da Vinci, Picasso, Dalí, Renoir, Cézanne, Goya, Rubens, Beksiński, etc.
* **14 Affective Categories (Plutchik-Inspired):** Sadness, Trust, Fear, Disgust, Anger, Anticipation, Happiness, Love, Surprise, Optimism, Gratitude, Pessimism, Regret, Agreeableness.

---

## ✨ Key Capabilities

1. **Dual-Stream Feature Fusion:** Combines convolutional localized spatial representations (EfficientNet-B2) with global contextual attention mechanisms (Vision Transformer ViT-B/16).
2. **Explainable AI (XAI):** Generates Grad-CAM activation heatmaps highlighting the exact compositional regions influencing model predictions.
3. **Adaptive Narrative Generation:** Translates technical model outputs into dynamic, engaging natural language across multiple stylistic tones (Poetic, Academic/Analytical, Curatorial).
4. **Interactive Artist Personas:** Conversational chat interface simulating historical masters (Van Gogh, Da Vinci, Monet, Picasso) powered by prompt-engineered LLM personas.
5. **Academic PDF Generation:** Programmatically compiles downloadable evaluation dossiers complete with visual heatmaps, prediction rankings, and generated narrative critiques.
6. **Audio Synthesis (TTS):** Narrates visual interpretations using synchronized speech synthesis.

---

## 🚀 Quick Start Guide

### Prerequisites
* Python 3.10 or 3.11 recommended.
* Virtual environment tool (`venv` or `conda`).
* OpenAI API Key (optional, required for generative narratives and chat).

### 1. Clone the Repository
```bash
git clone https://github.com/GhileaLucian/ArtAdvisor.git
cd ArtAdvisor
```

### 2. Set Up Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure API Secrets
Create a `.streamlit/secrets.toml` file (copied from `.streamlit/secrets.toml.example`):
```toml
OPENAI_API_KEY = "sk-proj-your-api-key-here"
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🗂️ Project Structure

```
ArtAdvisor/
├── app.py                     # Streamlit application entry point & layout
├── config.py                  # Global configurations & artist personas
├── predict.py                 # Unified inference pipeline & preprocessing
├── requirements.txt           # Python package dependencies
├── predictors/                # PyTorch deep learning predictors
│   ├── style_predictor.py     # Art movement classifier & Grad-CAM
│   ├── author_predictor.py    # Painter identification model
│   └── emotion_predictor.py   # Dual-stream EfficientNet + ViT ensemble
├── ui_components/             # Modular Streamlit tab interfaces
│   ├── analysis_tab.py        # Core artwork analysis interface
│   ├── gallery_tab.py         # Curated masterpiece exploration
│   ├── search_tab.py          # Multimodal semantic search
│   └── artist_chat_tab.py     # Interactive LLM artist persona dialogs
├── utils/                     # Supporting utilities
│   ├── ai_services.py         # OpenAI GPT-4o narrative & audio synthesis
│   ├── data_management.py     # Metadata persistence & user feedback
│   ├── pdf_generator_advanced.py # Automated PDF report compiler
│   ├── visualizations.py      # Radar charts & affective distribution plots
│   └── emotion_database.json  # Affective taxonomy definitions
├── models/                    # Model serialization directory
└── static/                    # CSS stylesheets, branding & assets
```

---

## 👤 Author

**Dan Lucian Ghilea**  
*MSc Student in Applied Informatics in Complex Systems · Technical University of Cluj-Napoca (TUCN)*  
* **LinkedIn:** [linkedin.com/in/lucian-ghilea](https://linkedin.com/in/lucian-ghilea)  
* **Email:** [danlucianghilea@gmail.com](mailto:danlucianghilea@gmail.com)  
* **GitHub:** [@GhileaLucian](https://github.com/GhileaLucian)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
