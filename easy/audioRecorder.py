import tkinter as tk
import pyaudio
import wave
import threading
import time
from datetime import datetime

class AudioRecorderApp:
    def __init__(self, master):
        self.master = master
        self.record_button = tk.Button(self.master, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack(pady=20)

        self.pause_button = tk.Button(self.master, text="Pause Recording", command=self.toggle_pause, state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        self.duration_label = tk.Label(self.master, text="Duration: 0:00")
        self.duration_label.pack(pady=10)

        self.is_recording = False
        self.is_paused = False
        self.record_thread = None
        self.start_time = 0
        self.pause_time = 0
        self.total_paused_time = 0  # Total time paused

        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []

    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        if not self.is_paused:
            self.start_time = time.time() - self.total_paused_time  # Start time adjusted to account for total paused time
        else:
            self.start_time += time.time() - self.pause_time  # Resume from where we paused

        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                                      frames_per_buffer=1024)
        self.frames = []

        self.record_button.config(text="Stop Recording")
        self.pause_button.config(state=tk.NORMAL)
        self.is_recording = True

        self.update_duration()

        self.record_thread = threading.Thread(target=self.record_audio)
        self.record_thread.start()

    def record_audio(self):
        while self.is_recording:
            if not self.is_paused:
                data = self.stream.read(1024)
                self.frames.append(data)
            else:
                time.sleep(0.1)

    def toggle_pause(self):
        if not self.is_paused:
            self.pause_recording()
        else:
            self.resume_recording()

    def pause_recording(self):
        self.is_paused = True
        self.pause_button.config(text="Resume Recording")
        self.pause_time = time.time()

    def resume_recording(self):
        self.is_paused = False
        self.pause_button.config(text="Pause Recording")
        self.total_paused_time += time.time() - self.pause_time  # Add paused time to total
        self.update_duration()

    def stop_recording(self):
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"recorded_audio_{current_time}.wav"

        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        self.record_button.config(text="Start Recording")
        self.pause_button.config(text="Pause Recording", state=tk.DISABLED)
        self.duration_label.config(text="Duration: 0:00")

    def update_duration(self):
        if self.is_recording and not self.is_paused:
            elapsed_time = time.time() - self.start_time - self.total_paused_time
            mins = int(elapsed_time // 60)
            secs = int(elapsed_time % 60)
            self.duration_label.config(text=f"Duration: {mins}:{secs:02}")
            self.master.after(1000, self.update_duration)  # Schedule the next update after 1 second

    def mainloop(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Audio Recorder")
    app = AudioRecorderApp(root)
    app.mainloop()
