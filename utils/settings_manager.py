import os
import json

class SettingsManager:
    def __init__(self, filename="settings.json"):
        self.filename = filename
        self.default_settings = {
            "music_volume": 7,
            "sfx_volume": 5,
            "difficulty": "Medium",
            "fullscreen": False
        }
        self.settings = self.load_settings()
        
    def load_settings(self):
        """Load settings from JSON file, or return defaults if file doesn't exist."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    return json.load(f)
            else:
                return self.default_settings.copy()
        except Exception as e:
            print(f"Error loading settings: {e}")
            return self.default_settings.copy()
            
    def save_settings(self, settings=None):
        """Save settings to JSON file."""
        if settings:
            self.settings = settings
            
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.settings, f, indent=4)
            print("Settings saved successfully")
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False
            
    def get_setting(self, key, default=None):
        """Get a specific setting value."""
        return self.settings.get(key, default)
        
    def update_setting(self, key, value):
        """Update a specific setting value and save it."""
        self.settings[key] = value
        return self.save_settings()
        
    def reset_to_defaults(self):
        """Reset all settings to defaults."""
        self.settings = self.default_settings.copy()
        return self.save_settings()