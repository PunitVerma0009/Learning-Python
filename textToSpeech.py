import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
l=["Rahul","Sahil","Sunny","Nishant"]
for i in l:
    speaker.speak(f"hello to {i}")