import cv2
import os

# Path to folder where all videos are stored
#video_folder = "C:\Users\Shipra Shakya\OneDrive\Desktop\picture_video\videos"
#video_folder = r"C:\\Users\\Shipra Shakya\\OneDrive\\Desktop\\picture_video\\videos"
video_folder = r"D:\Wedding\GIRJESH WEDDING CINEMATIC RAW DATA"

output_folder = r"C:\Users\Shipra Shakya\OneDrive\Desktop\picture_video\GWCRD"
#output_folder = r"C:\\Users\\Shipra Shakya\\OneDrive\\Desktop\\picture_video\\pictures"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all video files in the folder
video_files = [f for f in os.listdir(video_folder) if f.endswith(('.MP4', '.avi', '.MOV'))]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    video_name = os.path.splitext(video_file)[0]

    # Create a subfolder for each video's frames
    video_output_folder = os.path.join(output_folder, video_name)
    os.makedirs(video_output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    print(f"Processing: {video_file}")

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame_filename = os.path.join(video_output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"✅ Saved {frame_count} frames from {video_file}")

print("🎉 All videos processed successfully.")