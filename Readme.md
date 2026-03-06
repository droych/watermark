# Chaotic Image Watermarking – Implementation

This repository contains a **Python implementation of a chaotic system based fragile watermarking scheme for image tamper detection**.

The implementation reproduces the algorithm described in the research paper:


---

# Algorithm Overview

The watermarking scheme uses **two chaotic systems**:

1. **Arnold's Cat Map** – used for scrambling image pixels
2. **Logistic Map** – used for generating a chaotic watermark pattern

The watermark is embedded in the **Least Significant Bit (LSB) plane** of the scrambled image.

---

# Chaotic Maps 
## Arnold's Cat Map

The generalized Arnold Cat Map used in this implementation is:

```
[x_{n+1}]   [1   a] [x_n] mod N
[y_{n+1}] = [b ab+1][y_n]
```

where:

* `a`, `b` are positive integers
* `N` is the image dimension
* `(x_n, y_n)` are pixel coordinates before transformation

Features implemented:

* Pixel scrambling using Arnold Cat Map
* Configurable parameters `a` and `b`
* Automatic detection of the **period T**
* Periodicity verification

Example from the paper:

```
a = 1
b = 1
N = 128
```

The Arnold Cat Map period is:

```
T = 96
```

This means the image returns to its original state after 96 iterations.

---

## Logistic Map

The logistic map generates a chaotic sequence:

```
x_{k+1} = μ x_k (1 − x_k)
```

Parameters used in the implementation:

```
μ = 3.854
x0 = 0.654
```

Implementation steps:

1. Generate a chaotic sequence
2. Convert the sequence to a binary pattern
3. Reshape it into a 2D chaotic image pattern
4. Use the pattern to scramble the watermark

---

# Watermark Embedding 
The embedding process follows the **six steps described in the paper**.

1. **Scramble Host Image**

Apply Arnold Cat Map **k times** to obtain the scrambled image.

2. **Bit Plane Extraction**

Extract the **Least Significant Bit (LSB) plane** from the scrambled image.

3. **Generate Chaotic Pattern**

Generate a chaotic binary pattern using the logistic map.

4. **Create Chaotic Watermark**

XOR the watermark with the chaotic pattern:

```
Wp = Scp XOR W
```

5. **Embed Watermark**

Replace the **LSB bit-plane** with the chaotic watermark.

6. **Inverse Scrambling**

Apply Arnold Cat Map **(T − k) times** to obtain the final watermarked image.

---

# Watermark Extraction & Tamper Detection 

The extraction process reverses the embedding algorithm.

Steps:

1. Scramble the watermarked image using Arnold Cat Map **k times**
2. Extract the **LSB bit-plane**
3. Generate the same chaotic pattern using the logistic map
4. Recover the watermark using XOR
5. Compute the **absolute difference** between extracted and original watermark
6. Apply Arnold Cat Map **(T − k)** times to locate tampered regions

The resulting **tamper map highlights modified regions in the image**.


---

# Metrics

Image quality is evaluated using **Peak Signal-to-Noise Ratio (PSNR)**.

```
PSNR = 10 log10 (255² / MSE)
```

Higher PSNR indicates better visual similarity between the original and watermarked images.

---

# Project Structure

```
.
├── main.py              # Runs watermark embedding and detection
├── chaotic_maps.py      # Arnold Cat Map and Logistic Map implementation
├── watermarking.py      # Embedding and extraction algorithms
├── metrics.py           # PSNR calculation
├── host.png             # Input host image
├── watermark.png        # Binary watermark
└── README.md
```

---

# Requirements

Install dependencies:

```
pip install matplotlib pillow opencv-python
```

---

# Run the Project

```
python main.py
```

The program will:

* Embed a watermark
* Simulate image tampering
* Extract the watermark
* Detect modified regions
