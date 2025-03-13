# Image Dehazing using Residual-Based Deep CNN  

## 📌 Project Overview  
This project focuses on **removing haze from images using a Residual-Based Deep Convolutional Neural Network (CNN)**. Haze reduces visibility and degrades image quality, affecting various applications like autonomous driving, surveillance, and remote sensing. Our model enhances image clarity by learning to predict haze-free images from hazy inputs.  

## 📷 Sample Results  
| Hazy Image | Dehazed Image |
|------------|--------------|
| ![Hazy Image] 01_hazy.png| ![Dehazed Image] |

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

pip install -r requirements.txt


python dehaze.py --input images/hazy.jpg --output results/dehazed.jpg

python train.py --data path/to/dataset


Image-Dehazing-CNN/
│── data/                 # Training dataset  
│── models/               # Saved model checkpoints  
│── images/               # Sample input images  
│── results/              # Dehazed output images  
│── src/                  # Model architecture & training scripts  
│   │── model.py          # CNN Model definition  
│   │── train.py          # Training script  
│   │── dehaze.py         # Inference script  
│── requirements.txt      # Required dependencies  
│── README.md             # Project documentation  


📊 Performance Metrics
PSNR (Peak Signal-to-Noise Ratio): Measures the quality improvement in dehazed images.
SSIM (Structural Similarity Index): Evaluates structural changes before and after dehazing.

🖼️ Dataset
The model was trained on the RESIDE dataset, which contains a variety of hazy and corresponding clear images.
Custom datasets can also be used by placing hazy images in data/hazy/ and clear images in data/clear/.

📢 Future Improvements
Implement GAN-based dehazing for better texture restoration.
Optimize the model for real-time video dehazing.
Extend support for different atmospheric conditions.

🤝 Contributing
If you’d like to contribute, feel free to fork the repository and submit a pull request.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

✨ Acknowledgments
NIT Warangal – Internship guidance under Dr. J Ravi Kumar
RESIDE Dataset – Used for training the model


---

### 🔹 What’s Covered in the README?  
✔ **Project Explanation**  
✔ **How It Works**  
✔ **Installation & Setup**  
✔ **Dataset Information**  
✔ **Performance Metrics**  
✔ **Future Scope**  
✔ **License & Contribution**  

This README ensures that anyone visiting your **GitHub repository** understands your project and can easily set it up. Let me know if you need any modifications! 🚀
