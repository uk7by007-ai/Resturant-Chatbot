"""
Voice Handler - Speech Recognition and Text-to-Speech
"""

import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from pathlib import Path

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.temp_dir = tempfile.gettempdir()
    
    def listen(self, timeout=5, phrase_time_limit=10):
        """
        Listen to microphone and convert speech to text
        
        Args:
            timeout: Seconds to wait for speech to start
            phrase_time_limit: Maximum seconds for the phrase
        
        Returns:
            dict with 'success' and 'text' or 'error'
        """
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listen for audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
                
                # Convert speech to text using Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                
                return {
                    "success": True,
                    "text": text
                }
                
        except sr.WaitTimeoutError:
            return {
                "success": False,
                "error": "No speech detected. Please try again."
            }
        except sr.UnknownValueError:
            return {
                "success": False,
                "error": "Could not understand audio. Please speak clearly."
            }
        except sr.RequestError as e:
            return {
                "success": False,
                "error": f"Speech recognition service error: {str(e)}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error: {str(e)}"
            }
    
    def speak(self, text, lang='en', slow=False):
        """
        Convert text to speech and save as audio file
        
        Args:
            text: Text to convert to speech
            lang: Language code (default: 'en')
            slow: Speak slowly if True
        
        Returns:
            dict with 'success' and 'audio_path' or 'error'
        """
        try:
            # Generate speech
            tts = gTTS(text=text, lang=lang, slow=slow)
            
            # Save to temporary file
            audio_path = os.path.join(self.temp_dir, "response.mp3")
            tts.save(audio_path)
            
            return {
                "success": True,
                "audio_path": audio_path
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Text-to-speech error: {str(e)}"
            }
    
    def test_microphone(self):
        """Test if microphone is available"""
        try:
            mic_list = sr.Microphone.list_microphone_names()
            if len(mic_list) > 0:
                return {
                    "success": True,
                    "message": f"Found {len(mic_list)} microphone(s)",
                    "microphones": mic_list
                }
            else:
                return {
                    "success": False,
                    "message": "No microphones found"
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error testing microphone: {str(e)}"
            }
