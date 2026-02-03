# Dataset Specifications

This repository utilizes a balanced combination of **Celeb-DF v2** and **FaceForensics++ (FF++)** datasets for deepfake detection. The dataset is constructed with a 1:1 ratio of real and fake samples to ensure unbiased training.

## 1. Data Sources & Statistics

### **Celeb-DF v2**
- **Real Videos:** 890
- **Fake Videos:** 890 (Sampled to maintain a 1:1 ratio between real and fake classes.)
- **Total:** 1,780 videos
- [GitHub Link](https://github.com/yuezunli/celeb-deepfakeforensics)

### **FaceForensics++ (FF++)**
- **Real Videos:** 1,000
- **Fake Videos:** 1,000 (Sampled 250 videos from each of the 4 manipulation methods)
    - Deepfakes (DF): 250
    - Face2Face (F2F): 250
    - FaceSwap (FS): 250
    - NeuralTextures (NT): 250
- **Total:** 2,000 videos
- [GitHub Link](https://github.com/ondyari/FaceForensics)

---

## 2. Preprocessing Pipeline (Offline)

To optimize training efficiency and focus on facial artifacts, the following offline preprocessing steps were performed:

### **Frame Extraction**
- **Sampling Rate:** 15 frames per video.
- Uniform sampling was applied across the duration of each video to capture temporal variations.

### **Face Detection & Alignment**
- **Detection:** Facial regions were identified using the `InsightFace` library.
- **Alignment:** Detected faces were aligned to normalize head poses across different samples.
- **Cropping:** Identified face areas were cropped with a predefined margin to include peripheral artifacts.

### **Normalization & Resizing**
- **Resolution:** All cropped face images were resized to **256x256 pixels**.
- **Color Space:** Converted to RGB format for backbone model compatibility.

---
