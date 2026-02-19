# Python Text Portrait Generator 🎨

A custom Python script that takes any image and redraws it using thousands of characters. I built this because generic apps are boring. I wanted a way to turn a photo into something more meaningful—using words instead of just pixels. Step by step, logic by logic, para eyyable ang result! 🤙

![Result Example](Video Project.mp4) 

## ⚡ How It Works
1. **Scans** the image pixel by pixel (X and Y coordinates).
2. **Calculates** brightness to determine the shading.
3. **Replaces** pixels with looping text characters (e.g., "I Love You").
4. **Generates** a high-resolution text portrait.

## 🛠️ Requirements
* Python 3.x
* Pillow Library (`pip install pillow`)

## 🚀 How to Run
1. Place your image in the same folder.
2. Rename your image to `sample.jpg` OR change the `IMAGE_PATH` variable in the code.
3. Run the script:
   `python drawing.py`

## 📝 Roadmap
- [x] V1.0: Basic Black & White Rendering
- [ ] V2.0: Full RGB Color Support (In Development)

---
*Created with ❤️ and Python.*
