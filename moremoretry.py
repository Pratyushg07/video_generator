import cv2 as cv
import pygame
import librosa
import time
# Load the audio track
music, sr = librosa.load("background.mp3", sr=None)

# Trim or manipulate the audio track if needed

# Initialize Pygame for playing audio
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
 # Play the background music indefinitely
# Open the longer video
import cv2 as cv

# Open the video file
video = cv.VideoCapture("longer_video.mp4")

# Extract clip1 (5s to 9s)
start_frame1 = int(2 * video.get(cv.CAP_PROP_FPS))
end_frame1 = int(6.5 * video.get(cv.CAP_PROP_FPS))
video.set(cv.CAP_PROP_POS_FRAMES, start_frame1)
success1, frame1 = video.read()
clip1 = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height1 = frame1.shape[0]
new_width1 = int(height1 * 9 / 16)

while success1 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame1:
    # Calculate the x-coordinate of the top-left corner of the cropped area
    width1 = frame1.shape[1]
    x1 = int((width1 - new_width1 + 250) / 2)
    
    # Crop out the region of interest (ROI) from the frame
    cropped_frame1 = frame1[:, x1:x1+new_width1]

    # Add the cropped frame to clip1
    clip1.append(cropped_frame1)
    
    # Read the next frame
    success1, frame1 = video.read()

# Release the VideoCapture object
video.release()

# Apply blur effect and add text to the first clip
for i in range(len(clip1)):
    # Apply blur effect for the first second
    if i < 90:  # Assuming 30 frames per second
        clip1[i] = cv.GaussianBlur(clip1[i], (21, 21), 0)

    # Add text to the frame
    if i >= 15 and i < 90:  # Assuming 30 frames per second and 1-second duration for text
        text="A Robot's Tale"
        text2="of Friendship and Freedom"
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 5
        text_color = (0, 0, 0)  
        text_position = (int(new_width1 / 2) - 300, int(height1 / 2)-500)
        text_position2 = (int(new_width1 / 2) - 200, int(height1 / 2)-450)  
        cv.putText(clip1[i], text, text_position, font, font_scale, text_color, font_thickness)
        cv.putText(clip1[i], text2, text_position2, font, font_scale, text_color, font_thickness)



# Close the OpenCV windows
cv.destroyAllWindows()

# Open the longer video again for clip2 (15s to 20s)
video = cv.VideoCapture("longer_video.mp4")

# Extract clip2 (15s to 20s)
start_frame2 = int(11.2 * video.get(cv.CAP_PROP_FPS))
end_frame2 = int(12.35 * video.get(cv.CAP_PROP_FPS))
video.set(cv.CAP_PROP_POS_FRAMES, start_frame2)
success2, frame2 = video.read()
clip2 = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height2 = frame2.shape[0]
new_width2 = int(height2 * 9 / 16)

while success2 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame2:
    # Calculate the x-coordinate of the top-left corner of the cropped area
    width2 = frame2.shape[1]
    x2 = int((width2 - new_width2 + 250) / 2)
    
    # Crop out the region of interest (ROI) from the frame
    cropped_frame2 = frame2[:, x2-300:x2+new_width2-300]

    # Add the cropped frame to clip2
    clip1.append(cropped_frame2)
    
    # Read the next frame
    success2, frame2 = video.read()

# Release the VideoCapture object
video.release()



# Close the OpenCV windows
cv.destroyAllWindows()

# Open the longer video again for clip3 (16.5s to 17.5s)
video = cv.VideoCapture("longer_video.mp4")

# Extract clip3 (16.5s to 17.5s)
start_frame3 = int(16 * video.get(cv.CAP_PROP_FPS))
end_frame3 = int(18.5 * video.get(cv.CAP_PROP_FPS))
video.set(cv.CAP_PROP_POS_FRAMES, start_frame3)
success3, frame3 = video.read()
clip3 = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height3 = frame3.shape[0]
new_width3 = int(height3 * 9 / 16)

while success3 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame3:
    # Calculate the x-coordinate of the top-left corner of the cropped area
    width3 = frame3.shape[1]
    x3 = int((width3 - new_width3) / 2) # Shift the cropped frame horizontally by 200 pixels
    
    # Crop out the region of interest (ROI) from the frame
    cropped_frame3 = frame3[:, x3-200:x3+new_width3-200]

    # Add the cropped frame to clip3
    clip1.append(cropped_frame3)
    
    # Read the next frame
    success3, frame3 = video.read()

# Release the VideoCapture object
video.release()



# Close the OpenCV windows
cv.destroyAllWindows()
# # Open the longer video again for clip4 (17.5s to 18.5s)
# video = cv.VideoCapture("longer_video.mp4")

# # Extract clip4 (17.5s to 18s)
# start_frame4 = int(17 * video.get(cv.CAP_PROP_FPS))
# end_frame4 = int(18.5 * video.get(cv.CAP_PROP_FPS))
# video.set(cv.CAP_PROP_POS_FRAMES, start_frame4)
# success4, frame4 = video.read()
# clip4 = []

# # Calculate the new width for cropping to a 9:16 aspect ratio
# height4 = frame4.shape[0]
# new_width4 = int(height4 * 9 / 16)

# while success4 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame4:
#     # Calculate the x-coordinate of the top-left corner of the cropped area
#     width4 = frame4.shape[1]
#     x4 = int((width4 - new_width4) / 2)   # Shift the cropped frame back horizontally by 200 pixels
    
#     # Crop out the region of interest (ROI) from the frame
#     cropped_frame4 = frame4[:, x4+50:x4+new_width4+50]

#     # Add the cropped frame to clip4
#     clip4.append(cropped_frame4)
    
#     # Read the next frame
#     success4, frame4 = video.read()

# # Release the VideoCapture object
# video.release()

# # Display clip4
# for frame in clip4:
#     cv.imshow("Clip 4", frame)
#     cv.waitKey(30)  # Adjust the waitKey value to control playback speed (e.g., 30 milliseconds)
    
#     # Press 'q' to quit the loop
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # Close the OpenCV windows
# cv.destroyAllWindows()



# Open the longer video again for clip5 (51s to 54s)
video = cv.VideoCapture("longer_video.mp4")

# Extract clip5 (51s to 54s)
start_frame5 = int(51 * video.get(cv.CAP_PROP_FPS))
end_frame5 = int(52.5 * video.get(cv.CAP_PROP_FPS))
video.set(cv.CAP_PROP_POS_FRAMES, start_frame5)
success5, frame5 = video.read()
clip5 = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height5 = frame5.shape[0]
new_width5 = int(height5 * 9 / 16)

# Initialize variables for leftward shift
shift_per_sec = 50  # Pixels to shift per second
shift_per_frame = shift_per_sec / video.get(cv.CAP_PROP_FPS)  # Pixels to shift per frame

# Calculate the initial x-coordinate of the top-left corner of the cropped area
width5 = frame5.shape[1]
x5 = int((width5 - new_width5) / 2)  # Initial x-coordinate
current_x5 = x5

while success5 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame5:
    # Crop out the region of interest (ROI) from the frame
    cropped_frame5 = frame5[:, current_x5+150:current_x5+new_width5+150]

    # Add the cropped frame to clip5
    clip1.append(cropped_frame5)

    # Update the x-coordinate for the next frame (leftward shift)
    current_x5 -= int(shift_per_frame)

    # Read the next frame
    success5, frame5 = video.read()

# Release the VideoCapture object
video.release()


# Open the longer video again for clip5b (52s to 54s)
video = cv.VideoCapture("longer_video.mp4")

# Extract clip5b (52s to 54s)
start_frame5b = int(1 * 60 * video.get(cv.CAP_PROP_FPS) + 52 * video.get(cv.CAP_PROP_FPS))
end_frame5b = int(1 * 60 * video.get(cv.CAP_PROP_FPS) + 53.5 * video.get(cv.CAP_PROP_FPS))
video.set(cv.CAP_PROP_POS_FRAMES, start_frame5b)
success5b, frame5b = video.read()
clip5b = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height5b = frame5b.shape[0]
new_width5b = int(height5b * 9 / 16)

# Initialize variables for left-to-right movement
shift_per_sec = 50  # Pixels to shift per second
shift_per_frame = shift_per_sec / video.get(cv.CAP_PROP_FPS)  # Pixels to shift per frame

# Calculate the initial x-coordinate of the top-left corner of the cropped area
width5b = frame5b.shape[1]
x5b = int((width5b - new_width5b) / 2)  # Initial x-coordinate
current_x5b = x5b

while success5b and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame5b:
    # Apply left-to-right movement
    current_x5b += int(shift_per_frame)

    # Crop out the region of interest (ROI) from the frame
    cropped_frame5b = frame5b[:, current_x5b:current_x5b+new_width5b]

    # Add the cropped frame to clip5b
    clip1.append(cropped_frame5b)

    # Read the next frame
    success5b, frame5b = video.read()

# Release the VideoCapture object
video.release()



# Close the OpenCV windows
cv.destroyAllWindows()

# Open the longer video again for clip6 (2:00 to 2:05)
video = cv.VideoCapture("longer_video.mp4")

# Extract clip6 (2:00 to 2:05)
start_frame6 = int(2 * 60 * video.get(cv.CAP_PROP_FPS))  # Convert 2 minutes to frames
end_frame6 = int((2 * 60 + 4) * video.get(cv.CAP_PROP_FPS))  # Convert 2 minutes 5 seconds to frames
video.set(cv.CAP_PROP_POS_FRAMES, start_frame6)
success6, frame6 = video.read()
clip6 = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height6 = frame6.shape[0]
new_width6 = int(height6 * 9 / 16)

# Initialize variables for dynamic shifting
shift_per_sec = 50  # Pixels to shift per second
shift_per_frame = shift_per_sec / video.get(cv.CAP_PROP_FPS)  # Pixels to shift per frame

current_x6 = int((frame6.shape[1] - new_width6) / 2)  # Initial x-coordinate of the top-left corner of the cropped area

while success6 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame6:
    # Crop out the region of interest (ROI) from the frame
    cropped_frame6 = frame6[:, current_x6:current_x6+new_width6]

    # Add the cropped frame to clip6
    clip1.append(cropped_frame6)

    # Update the x-coordinate for the next frame
    current_x6 -= int(shift_per_frame)

    # Read the next frame
    success6, frame6 = video.read()

# Release the VideoCapture object
video.release()



# Close the OpenCV windows
cv.destroyAllWindows()
# Open the longer video again for clip7 (3:27 to 3:34)
video = cv.VideoCapture("longer_video.mp4")

# Extract clip7 (3:27 to 3:34)
start_frame7 = int(3 * 60 * video.get(cv.CAP_PROP_FPS) + 27 * video.get(cv.CAP_PROP_FPS))
end_frame7 = int(3 * 60 * video.get(cv.CAP_PROP_FPS) + 34.2 * video.get(cv.CAP_PROP_FPS))
video.set(cv.CAP_PROP_POS_FRAMES, start_frame7)
success7, frame7 = video.read()
clip7 = []

# Calculate the new width for cropping to a 9:16 aspect ratio
height7 = frame7.shape[0]
new_width7 = int(height7 * 9 / 16)

# Initialize variables for leftward shift after 2.5 seconds
shift_start_frame = int(3 * 60 * video.get(cv.CAP_PROP_FPS) + 2.5 * video.get(cv.CAP_PROP_FPS))  # Start shifting after 2.5 seconds
shift_per_sec = 50  # Pixels to shift per second
shift_per_frame = shift_per_sec / video.get(cv.CAP_PROP_FPS)  # Pixels to shift per frame
shift_duration = 0.5 * video.get(cv.CAP_PROP_FPS)  # Duration of leftward shift in frames

# Calculate the initial x-coordinate of the top-left corner of the cropped area
width7 = frame7.shape[1]
x7 = int((width7 - new_width7) / 2)  # Initial x-coordinate
current_x7 = x7

frame_count = 0

while success7 and video.get(cv.CAP_PROP_POS_FRAMES) < end_frame7:
    # Apply leftward shift for the first 0.5 seconds
    if video.get(cv.CAP_PROP_POS_FRAMES) >= shift_start_frame and frame_count < shift_duration:
        current_x7 -= int(shift_per_frame)
    else:
        # Apply rightward shift for the remaining duration
        current_x7 += int(shift_per_frame)

    # Crop out the region of interest (ROI) from the frame
    cropped_frame7 = frame7[:, current_x7-50:current_x7+new_width7-50]

    # Add the cropped frame to clip7
    clip1.append(cropped_frame7)

    # Read the next frame
    success7, frame7 = video.read()
    frame_count += 1

pygame.mixer.music.play(-1) 
# Release the VideoCapture object
video.release()
# Display clip1
for frame in clip1:
    cv.imshow("Clip 1", frame)
    cv.waitKey(30)  # Adjust the waitKey value to control playback speed (e.g., 30 milliseconds)
    
    # Press 'q' to quit the loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



# Close the OpenCV windows
cv.destroyAllWindows()

pygame.mixer.music.play(-1)  # Play the background music indefinitely

# Define the output video file name and properties
output_video = "output_video_with_music.mp4"
fps = 30  # Frames per second
frame_width = clip1[0].shape[1]
frame_height = clip1[0].shape[0]
video_writer = cv.VideoWriter(output_video, cv.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

# Write each frame to the output video
for frame in clip1:
    video_writer.write(frame)

# Release the VideoWriter object
video_writer.release()

# Stop playing the background music
pygame.mixer.music.stop()

# Combine the video and audio tracks
video_with_audio = cv.VideoCapture(output_video)
fourcc = cv.VideoWriter_fourcc(*'mp4v')
output_video_with_audio = cv.VideoWriter("output_video_with_audio.mp4", fourcc, fps, (frame_width, frame_height))

# Check if video is opened
if not video_with_audio.isOpened():
    print("Error: Could not open video file.")

# Get video frame rate
frame_rate = int(video_with_audio.get(cv.CAP_PROP_FPS))

# Iterate through each frame in the video
while True:
    # Read a frame from the video
    ret, frame = video_with_audio.read()

    # If frame is not read correctly, break the loop
    if not ret:
        break

    # Write the frame to the output video
    output_video_with_audio.write(frame)

# Release the video capture and video writer objects
video_with_audio.release()
output_video_with_audio.release()
