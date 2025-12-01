import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=5):
    """
    Extract frames from a video at a specified frame rate.

    Args:
        video_path (str): Path to the video file.
        output_folder (str): Folder to save extracted frames.
        frame_rate (int): Extract 1 frame every 'frame_rate' seconds.
    """
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"❌ ERROR: Cannot open video file {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get FPS of the video
    frame_interval = fps * frame_rate     # Capture every 'frame_rate' seconds

    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"✅ Extracted {saved_count} frames from {video_path} to {output_folder}")

# Define paths
video_dirs = {
    "train": "C:/Users/SHRUTI/Desktop/emergency_vechicle/videos/videos_training",
    "val": "C:/Users/SHRUTI/Desktop/emergency_vechicle/videos/videos_val"
}
output_dirs = {
    "train": "C:/Users/SHRUTI/Desktop/emergency_vechicle/images/train",
    "val": "C:/Users/SHRUTI/Desktop/emergency_vechicle/images/val"
}

# Extract frames for both training and validation videos
for split in ["train", "val"]:
    video_folder = video_dirs[split]
    output_folder = output_dirs[split]

    # Ensure video folder exists
    if not os.path.exists(video_folder):
        print(f"⚠️ WARNING: Video folder not found: {video_folder}")
        continue

    for video_file in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_file)
        
        # Ignore folders
        if not os.path.isfile(video_path):
            continue  # Skip directories

        # Process only video files
        if video_file.lower().endswith(('.mp4', '.avi', '.mov')):  
            extract_frames(video_path, output_folder, frame_rate=5)
