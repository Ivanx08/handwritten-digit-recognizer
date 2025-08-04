# 🔢 Handwritten Digit Recognizer

A deep learning web app that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Built using TensorFlow, deployed using Streamlit, and designed for real-time predictions through a user-friendly interface.

---

## 🚀 Live Demo

> 🌐 **Try it here**: [https://handwritten-digit-recognizer-0-9.streamlit.app](https://handwritten-digit-recognizer-0-9.streamlit.app)

> 🧠 Accuracy: ~99% (on MNIST test dataset)

---

## 📌 Project Highlights

- 🔢 Classifies digits with ~99% accuracy using a CNN
- 🧼 Includes data preprocessing, normalization, and reshaping
- 🧠 Trained and evaluated using TensorFlow + Keras
- 💾 Model exported in `.keras` format for deployment
- 🖥️ Deployed using [Streamlit Community Cloud](https://streamlit.io/cloud)
- 📓 [View Model Training Notebook (Google Colab)](https://colab.research.google.com/drive/1a3pRoHhAaRTQgCU79KeT-O9g5YZ37Cty?usp=sharing)

---

## 🧠 Model Details

- **Architecture**: 2 Conv2D layers → MaxPooling → Flatten → Dense → Softmax  
- **Loss Function**: `categorical_crossentropy`  
- **Optimizer**: `Adam`  
- **Epochs**: 10  
- **Training Accuracy**: ~99%  
- **Test Accuracy**: ~98.5%

---

## 🛠️ Tech Stack

| Tool                   | Purpose                           |
|------------------------|-----------------------------------|
| Python                 | Core programming language         |
| TensorFlow/Keras       | Deep learning model building      |
| Streamlit              | Interactive Web app framework     |
| OpenCV + Pillow        | Image handling & preprocessing    |
| NumPy                  | Data handling and transformations |
| Google Colab           | Model training & experimentation  |
| Git & GitHub           | Version control and hosting       |

---

## 📂 Project Structure

```bash
📁 handwritten-digit-recognizer
├── app.py                          # Streamlit application
├── digit_recognizer_model.keras    # Trained model
├── requirements.txt                # Python dependencies
├── setup.sh                        # Auto setup script (optional use)
├── README.md                       # Project documentation
├── digit_training.ipynb            # 📓 Google Colab notebook (also linked above)
```


---

## 🧪 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/Ivanx08/handwritten-digit-recognizer.git

# 2. Move into the project directory
cd handwritten-digit-recognizer

# 3. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate  # On Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

---

## 🧠 What I Learned

- 🧠 How to build CNNs for image classification
- 🧪 Training, evaluating, and saving models with TensorFlow
- 🎨 Integrating OpenCV with Streamlit for live image processing
- 🌐 Deploying AI models on Streamlit Cloud
- 🗂️ Writing clean code, version control, and production-readiness 

---

## 📄 License

This project is released under the **MIT License** – free to use, modify, and distribute.


---

## 🙋‍♂️ About the Author

I'm **Shivam Bhati**, an aspiring AI developer passionate about building real-world applications through hands-on projects. I enjoy translating complex deep learning ideas into accessible web apps.

> 🔗 [Connect on LinkedIn](https://www.linkedin.com/in/shivam-bhati-dev/)
