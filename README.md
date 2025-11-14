Autonomous Helmet Detection

A Computer Vision System for Enhancing Road Safety

About

Autonomous Helmet Detection is a computer vision project designed to identify whether motorcycle riders are wearing helmets in real time. Using the power of YOLO and OpenCV, this system aims to support road safety initiatives by automatically detecting helmet compliance from images or video streams.

This project integrates modern deep-learning models and a user-friendly interface built with PyQt5 and Streamlit. The model is optimized and executed using ONNX Runtime for fast and efficient inference.

Features

Real-time helmet detection using YOLO

Video and image input support

High-accuracy object detection

Lightweight ONNX runtime for faster inference

GUI using PyQt5

Web interface using Streamlit

Easy-to-run and extendable codebase

Tech Stack

YOLO – Object detection model

OpenCV – Image/video processing

PyQt5 – Desktop application UI

Streamlit – Web interface

ONNX Runtime – Efficient model inference

lxml – XML parsing and annotation handling

Project Structure
Autonomous-Helmet-Detection/
│── models/                # YOLO ONNX model files
│── src/                   # Main source code
│   ├── detection.py       # Helmet detection logic
│   ├── utils.py           # Helper functions
│   ├── gui_app.py         # PyQt5 interface
│   └── web_app.py         # Streamlit app
│── data/                  # Images, videos, annotations
│── requirements.txt       # Dependencies
│── README.md              # Project description

Installation

Clone the repository

git clone https://github.com/your-username/Autonomous-Helmet-Detection.git
cd Autonomous-Helmet-Detection


Install dependencies

pip install -r requirements.txt

Usage
Run PyQt5 Desktop App
python src/gui_app.py

Run Streamlit Web App
streamlit run src/web_app.py

Direct Detection Script
python src/detection.py --source path_to_image_or_video

Dataset

You may use:

Custom collected images

Public datasets such as:

Helmet Detection Dataset

Safety Helmet Wearing Dataset (SHWD)
Add images and annotations in the data/ folder.

Results

Accurate helmet vs. no-helmet classification

Fast inference using ONNX

Works on both live camera feeds and offline videos

(You can add your results, screenshots, or GIFs here)

Contribution

Pull requests are welcome! Feel free to open issues for new features or bug reports.

📄 License

This project is licensed under the MIT License (or any license you choose).
