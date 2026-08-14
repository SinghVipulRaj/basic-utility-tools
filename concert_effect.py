import numpy as np
import os
from pydub import AudioSegment
from scipy.signal import lfilter
from tqdm.notebook import tqdm # Import tqdm for progress bar
from google.colab import files # Import files for uploading


def _load_audio(input_path):
    """Loads the audio file."""
    return AudioSegment.from_file(input_path)

def _apply_low_pass_filter(sound):
    """Applies a low-pass filter to simulate distance."""
    return sound.low_pass_filter(8000)

def _apply_reverb(left_samples, right_samples, sample_rate):
    """Applies concert hall reverb using a feedback delay line."""
    delay_seconds = 0.045  # 45ms delay for a large room feel
    delay_samples = int(sample_rate * delay_seconds)
    decay_factor = 0.35    # How fast the stadium echo dies out

    b = [1.0]
    a = [1.0] + [0.0] * (delay_samples - 1) + [-decay_factor]

    left_hall = lfilter(b, a, left_samples)
    right_hall = lfilter(b, a, right_samples)
    return left_hall, right_hall

def _apply_haas_effect(left_hall, right_hall, sample_rate):
    """Haas effect for speaker placement illusion."""
    haas_delay_samples = int(sample_rate * 0.020)
    right_hall_shifted = np.roll(right_hall, haas_delay_samples)
    right_hall_shifted[:haas_delay_samples] = 0  # Zero out the initial shift gap
    return left_hall, right_hall_shifted

def _rebuild_stereo_and_export(left_hall, right_hall, sample_rate, output_path):
    """Rebuilds stereo channels and exports the final audio."""
    left_hall_int = np.clip(left_hall, -32768, 32767).astype(np.int16)
    right_hall_int = np.clip(right_hall, -32768, 32767).astype(np.int16)

    processed_left = AudioSegment(left_hall_int.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
    processed_right = AudioSegment(right_hall_int.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)

    concert_stereo = AudioSegment.from_mono_audiosegments(processed_left, processed_right)
    concert_stereo.export(output_path, format="mp3", bitrate="320k")

def apply_concert_effect(input_path, output_path):
    stages = [
        "Loading audio",
        "Applying low-pass filter",
        "Processing channels (Reverb)",
        "Applying Haas effect",
        "Rebuilding stereo and Exporting audio"
    ]

    with tqdm(total=len(stages), desc="Applying Concert Effect") as pbar:
        # 1. Load the original audio file
        sound = _load_audio(input_path)
        pbar.update(1)
        pbar.set_postfix_str(stages[0] + " complete")

        # 2. Distance Logic: Apply a low-pass filter
        sound = _apply_low_pass_filter(sound)
        pbar.update(1)
        pbar.set_postfix_str(stages[1] + " complete")

        # Split the audio into raw arrays for digital signal processing
        left_channel, right_channel = sound.split_to_mono()
        left_samples = np.array(left_channel.get_array_of_samples(), dtype=np.float32)
        right_samples = np.array(right_channel.get_array_of_samples(), dtype=np.float32)
        sample_rate = sound.frame_rate

        # 3. Venue Reflection Logic: Create micro-delays
        left_hall, right_hall = _apply_reverb(left_samples, right_samples, sample_rate)
        pbar.update(1)
        pbar.set_postfix_str(stages[2] + " complete")

        # 4. Speaker Placement Logic: The Haas Effect
        left_hall_processed, right_hall_processed = _apply_haas_effect(left_hall, right_hall, sample_rate)
        pbar.update(1)
        pbar.set_postfix_str(stages[3] + " complete")

        # 5. Rebuild stereo and export
        _rebuild_stereo_and_export(left_hall_processed, right_hall_processed, sample_rate, output_path)
        pbar.update(1)
        pbar.set_postfix_str(stages[4] + " complete")
        print("Concert environment processing complete!")

  # --- User Interaction for File Selection and Loop ---
while True:
    print("\n--- Ready for new audio file ---")
    print("Please upload an MP3 file to apply the concert effect.")
    uploaded = files.upload()

    if uploaded:
        input_audio_filename = list(uploaded.keys())[0]
        print(f"Uploaded file: {input_audio_filename}")

        # Automatically generate output filename
        base_filename = os.path.splitext(input_audio_filename)[0]
        output_audio_filename = f"concert_{base_filename}.mp3"
        print(f"Processed audio will be saved as: {output_audio_filename}")

        # Run the concert effect script with user-provided files
        apply_concert_effect(input_audio_filename, output_audio_filename)

        # Provide download button for the converted audio
        print(f"\nDownloading '{output_audio_filename}'...")
        files.download(output_audio_filename)
        print("Download initiated!")

        print("Terminating. Thank you!")
        break
    else:
        print("No file uploaded. Terminating.")
        break
