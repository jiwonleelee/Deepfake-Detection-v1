# Dataset Specifications

This repository utilizes a balanced combination of **Celeb-DF v2** and **FaceForensics++ (FF++)** datasets for deepfake detection. The dataset is constructed with a 1:1 ratio of real and fake samples to ensure unbiased training.

## 1. Data Sources & Statistics

### **Celeb-DF v2**
- **Real Videos:** 580 (only target vedios)
- **Fake Videos:** 580 (Sampled to maintain a 1:1 ratio between real and fake classes.)
- **Total:** 1,160 videos
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

### **DeeperForensics-1.0 (DF)**
- **Real Videos:** 2,000
- **Fake Videos:** 2,000 (Sampled 500 videos from each perturbation category)
    - Level 3, Level 4, Level 5, and Mix 2
    - 500 videos per category based on Target ID
- **Total:** 4,000 videos
- [GitHub Link](https://github.com/EndlessSora/DeeperForensics-1.0)
  
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

## 3. Data Integrity & Splitting Strategy

To ensure high-quality training and prevent data leakage, the following principles were applied during dataset construction:

* **1:1 Target ID Matching**: For every fake video included, its corresponding original real video (based on the same Target ID) is also included to maintain a perfect class balance.
* **Identity-aware Splitting**: Data splitting (Train/Val/Test) is performed based on **Target IDs**. All videos associated with a specific identity—both real and fake—are assigned to the same split. This prevents the model from "memorizing" an individual's facial features and ensures it learns to distinguish manipulation artifacts rather than personal identities.
