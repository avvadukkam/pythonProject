import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import speech_recognition as sr
from pydub import AudioSegment


class AudioRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Recorder App")

        self.recording = False
        self.paused = False
        self.audio_format = tk.StringVar(value="wav")

        # Create GUI elements
        self.start_stop_button = ttk.Button(root, text="Start Recording", command=self.start_stop_recording)
        self.start_stop_button.pack(pady=10)

        self.pause_resume_button = ttk.Button(root, text="Pause Recording", command=self.pause_resume_recording,
                                              state=tk.DISABLED)
        self.pause_resume_button.pack(pady=5)

        formats = ["wav", "flac", "aac", "mp3"]
        self.format_menu = ttk.OptionMenu(root, self.audio_format, *formats)
        self.format_menu.pack(pady=5)

        self.status_label = ttk.Label(root, text="Status: Idle")
        self.status_label.pack(pady=10)

        # Initialize recognizer and microphone
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def start_stop_recording(self):
        if not self.recording:
            self.recording = True
            self.paused = False
            self.start_stop_button.config(text="Stop Recording")
            self.pause_resume_button.config(text="Pause Recording", state=tk.NORMAL)
            self.status_label.config(text="Status: Recording...")

            try:
                self.record_audio()
            except Exception as e:
                print(f"Error starting recording: {e}")
        else:
            self.recording = False
            self.start_stop_button.config(text="Start Recording")
            self.pause_resume_button.config(text="Pause Recording", state=tk.DISABLED)
            self.status_label.config(text="Status: Stopped")

            # Prompt user for file save location
            self.save_audio()

    def pause_resume_recording(self):
        if self.paused:
            self.paused = False
            self.pause_resume_button.config(text="Pause Recording")
            self.status_label.config(text="Status: Recording...")
        else:
            self.paused = True
            self.pause_resume_button.config(text="Resume Recording")
            self.status_label.config(text="Status: Paused")

    def record_audio(self):
        with self.microphone as source:
            while self.recording:
                try:
                    if not self.paused:
                        audio_data = self.recognizer.listen(source)
                        if self.recording and not self.paused:
                            # Handle audio data as needed (currently not saving directly here)
                            pass
                except Exception as e:
                    print(f"Error recording audio: {e}")
                    break

    def save_audio(self):
        try:
            audio_data = self.recognizer.listen(self.microphone)
            if audio_data:
                audio_format = self.audio_format.get()
                filename = filedialog.asksaveasfilename(defaultextension=f".{audio_format}", filetypes=[
                    (f"{audio_format.upper()} files", f"*.{audio_format}")])

                if filename:
                    if audio_format == "wav":
                        with open(filename, "wb") as file:
                            file.write(audio_data.get_wav_data())
                    elif audio_format == "flac":
                        with open(filename, "wb") as file:
                            file.write(audio_data.get_flac_data())
                    elif audio_format == "aac":
                        # Convert to AAC using pydub
                        audio_segment = AudioSegment.from_wav(
                            sr.AudioData(audio_data.get_wav_data(), self.recognizer.sample_rate,
                                         self.recognizer.sample_width))
                        audio_segment.export(filename, format="aac")
                    elif audio_format == "mp3":
                        # Convert to MP3 using pydub
                        audio_segment = AudioSegment.from_wav(
                            sr.AudioData(audio_data.get_wav_data(), self.recognizer.sample_rate,
                                         self.recognizer.sample_width))
                        audio_segment.export(filename, format="mp3")
        except Exception as e:
            print(f"Error saving audio: {e}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorderApp(root)
    app.run()
