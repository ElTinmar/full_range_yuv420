# Full-Range YUV420 Video Fix

This project provides a simple fix for videos encoded with full-range YUV420 but **missing the proper metadata flag**. Without this flag, many decoders (including OpenCV and FFmpeg) incorrectly assume **limited-range (TV range)** and display washed-out colors or incorrect contrast.

---

## What's the Problem?

Most video decoders assume that YUV420 video uses **limited range** by default:
- Luma (Y): 16–235
- Chroma (U/V): 16–240

However, some videos are encoded with **full range (0–255)** but **lack the `video_full_range_flag`** in the H.264 stream metadata. This causes tools like OpenCV to:
- Apply incorrect YUV → RGB conversion
- Show reduced contrast or clipped blacks/whites

---

## The Solution

This script uses **FFmpeg's `h264_metadata` bitstream filter** to inject the missing full-range flag **without re-encoding** the video.

### What it does:
- Parses the input H.264 stream
- Sets `video_full_range_flag=1` in the Sequence Parameter Set (SPS)
- Outputs a corrected video with proper full-range decoding behavior

---

## Setup

This project includes a Conda environment file for easy setup:

```bash
conda env create -f full_range_yuv420.yml
```

## Usage

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=color_range -of default=noprint_wrappers=1:nokey=1 input.avi
unknown
```

```bash
conda activate full_range_yuv420
python set_full_range.py input.avi output_fixed.avi
```

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=color_range -of default=noprint_wrappers=1:nokey=1 output_fixed.avi
pc
```