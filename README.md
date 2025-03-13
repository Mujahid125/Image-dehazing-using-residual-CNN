# Image Dehazing using Residual-Based Deep CNN  

## 📌 Project Overview  
This project focuses on **removing haze from images using a Residual-Based Deep Convolutional Neural Network (CNN)**. Haze reduces visibility and degrades image quality, affecting various applications like autonomous driving, surveillance, and remote sensing. Our model enhances image clarity by learning to predict haze-free images from hazy inputs.  

## 📷 Sample Results  
| Hazy Image | Dehazed Image |
|------------|--------------|
| ![Hazy Image](path/to/hazy_sample.jpg) | ![Dehazed Image](path/to/dehazed_sample.jpg) |

## ⚙️ How It Works  
1. **Preprocessing:**  
   - Input images are resized and normalized.  
   - Data augmentation techniques are applied to improve model performance.  

2. **Model Architecture:**  
   - The model is based on a **deep CNN with residual connections**, which helps in learning fine details while avoiding vanishing gradients.  
   - It takes a hazy image as input and predicts a clear, dehazed version.  

3. **Training Process:**  
   - The model is trained on a dataset of hazy and clear image pairs.  
   - Loss function: **Mean Squared Error (MSE) or Structural Similarity Index (SSIM) loss** to measure image quality improvement.  
   - Optimizer: **Adam optimizer** is used for fast convergence.  

4. **Inference:**  
   - A new hazy image is fed into the trained model.  
   - The model predicts a haze-free image with improved visibility.  

## 🛠️ Installation and Setup  
### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/yourusername/Image-Dehazing-CNN.git
cd Image-Dehazing-CNN
