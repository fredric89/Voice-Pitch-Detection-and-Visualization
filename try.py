import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import tempfile
import os

st.title("Voice Pitch Detection and Visualization")
st.markdown("Developed by Group 2, National University")

st.sidebar.header("Upload Settings")
audio_file = st.sidebar.file_uploader("Upload a pre-recorded voice file (WAV/MP3)", type=["wav", "mp3"])

if audio_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        tmp_file.write(audio_file.read())
        tmp_path = tmp_file.name

    # Load the audio using librosa
    y, sr = librosa.load(tmp_path, sr=None, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)

    st.audio(audio_file, format='audio/wav')
    st.write(f"**Duration:** {duration:.2f} seconds")
    st.write(f"**Sampling Rate:** {sr} Hz")

    # Pitch detection using YIN
    f0 = librosa.yin(y, fmin=50, fmax=1000, sr=sr, frame_length=2048)
    times = librosa.times_like(f0, sr=sr)

    # Plot waveform and pitch contour
    fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(10, 6))
    librosa.display.waveshow(y, sr=sr, ax=ax[0], alpha=0.6)
    ax[0].set(title='Audio Waveform')
    ax[0].label_outer()

    ax[1].plot(times, f0, label='Estimated Pitch (Hz)', color='r')
    ax[1].set(title='Pitch Over Time', xlabel='Time (s)', ylabel='Pitch (Hz)')
    ax[1].grid(True)
    ax[1].legend()

    st.pyplot(fig)

    os.unlink(tmp_path)  # Clean up the temporary file

else:
    st.info("Please upload a voice recording to begin pitch detection.")

st.markdown("---")
st.markdown("**Note:** This tool uses the YIN algorithm for pitch estimation. Results may vary with background noise or overlapping voices.")
