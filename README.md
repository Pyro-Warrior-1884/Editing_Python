# CLI Image Editor

A simple, interactive **command-line image editor** built using **Pillow (PIL fork)**.  
This tool allows you to open images, apply multiple edits, view change history, crop specific regions, and even edit selected parts separately using a **sub-editor** — all from the terminal.

---

## Overview

This CLI-based image editor is designed for users who want a **lightweight, script-based** solution for basic image editing without using heavy graphical software.  
It provides a **menu-driven workflow**, where you can perform edits step by step, preview them, and save them to a separate file.

---

## Features

### Image Enhancements
- Adjust sharpness, contrast, brightness, and colour.
- Convert images to black and white.
- Apply Gaussian blur for smoothing effects.

### Transformations
- Rotate images at any angle.
- Resize images to custom dimensions.
- Transpose or flip images horizontally or vertically.

### Cropping and Sub-Editing
- Crop an entire image, or
- Select a region to edit separately:
  - Apply all enhancements locally.
  - Paste the edited region back into the main image.

### Change Tracking
- Every modification is recorded in a change history log.
- View a complete list of all applied edits at any time.
- Reset the image back to its original state whenever required.

### Non-Destructive Workflow
- The original image remains untouched.
- Edited images are saved separately in your chosen output directory.

---

## Requirements

- Python 3.8 or later
- Pillow (PIL fork)

Make sure Pillow is installed before running the tool.

---

## How It Works

### 1. Start the Tool
- The program runs entirely in the terminal.
- You provide:
  - The path to the folder containing your images.
  - The path where edited images should be saved.

### 2. Main Editing Menu
- After opening an image, the tool presents a menu of available operations.
- You can choose from enhancements, transformations, cropping, and history viewing.
- Multiple edits can be applied before saving.

### 3. Cropping Workflow
- When choosing to crop, you can:
  - Crop the image directly, or
  - Open the **sub-editor** to edit only the selected region.

### 4. Sub-Editor for Cropped Regions
- The sub-editor works on the selected region only.
- You can adjust sharpness, contrast, brightness, colour, convert to black and white, blur, rotate, flip, or reset the cropped region.
- Once edits are done, the modified region is pasted back into the main image.

### 5. Saving Edits
- The program saves the edited image in the specified output directory.
- The filename is automatically modified to indicate it has been edited.
- Original images remain unchanged.

### 6. Change History and Reset
- All modifications are logged.
- You can review every change made during the session.
- You can reset the image or cropped region back to its original state at any point.
