import subprocess
import sys

def set_full_range_flag(input_path: str, output_path: str) -> None:
    """
    Sets the H264 full range flag in the video stream without re-encoding.
    
    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to the output video file.
    """
    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-bsf:v', 'h264_metadata=video_full_range_flag=1',
        '-c:v', 'copy',
        output_path
    ]
    
    print(f"Running FFmpeg command:\n{' '.join(cmd)}")
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if process.returncode != 0:
        print(f"FFmpeg failed with error:\n{process.stderr}")
        sys.exit(1)
    else:
        print(f"Output saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Set H264 full range flag without re-encoding.")
    parser.add_argument("input_file", help="Input video filename")
    parser.add_argument("output_file", help="Output video filename")

    args = parser.parse_args()
    set_full_range_flag(args.input_file, args.output_file)
