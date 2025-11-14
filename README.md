#  Autonomous Helmet Detection

A Computer Vision System for Enhancing Road Safety

## About

**Autonomous Helmet Detection** is a computer vision project designed to
identify whether motorcycle riders are wearing helmets in real time.
Using **YOLO** and **OpenCV**, this system aims to support road safety
initiatives by automatically detecting helmet compliance from images or
video streams.

This project integrates **PyQt5**, **Streamlit**, **ONNX Runtime**, and
**lxml** for model execution, interface, and annotation handling.

## Features

-   Real-time helmet detection using YOLO\
-   Video and image input support\
-   High-accuracy object detection\
-   Fast inference using ONNX Runtime\
-   GUI using PyQt5\
-   Web interface using Streamlit\
-   Extendable and clean codebase

## Tech Stack

-   YOLO\
-   OpenCV\
-   PyQt5\
-   Streamlit\
-   ONNX Runtime\
-   lxml

## Project Structure

    Autonomous-Helmet-Detection/
    │── models/                # YOLO ONNX model files
    │── src/                   # Source code
    │── data/                  # Images, videos, annotations
    │── requirements.txt       # Dependencies
    │── README.md

## Installation

``` bash
git clone https://github.com/your-username/Autonomous-Helmet-Detection.git
cd Autonomous-Helmet-Detection
pip install -r requirements.txt
```

## Usage

### Run PyQt5 App

``` bash
python src/gui_app.py
```

### Run Streamlit App

``` bash
streamlit run src/web_app.py
```

### Run Detection Script

``` bash
python src/detection.py --source path_to_image_or_video
```

## Results

Add your output images, metrics, or screenshots here.

## Contribution

Pull requests and suggestions are welcome.

## License

MIT License
