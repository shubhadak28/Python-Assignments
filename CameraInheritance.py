class Camera:
    def camera_features(self):
        return "Camera: 108MP, Night Mode, Optical Zoom"

class MP:
    def music_player(self):
        return "Music Player: Supports MP3, WAV, Bluetooth audio"

class SP(Camera, MP):  # Multiple Inheritance
    def smart_features(self):
        return "Smartphone: 5G, Touchscreen, Face Unlock"

# Create object of SP
s = SP()

# Access methods from all parent classes
print(s.camera_features())
print(s.music_player())
print(s.smart_features())
