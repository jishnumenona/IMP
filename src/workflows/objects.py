import json
import os



class Prop:
    """
    This class represents a prop used in an interactive music performance.

    Attributes:
        id: The unique identifier of the prop.
        network_details: Dictionary containing network configuration for communication (e.g., MQTT).
        sensor_settings: Dictionary containing sensor data configuration for the prop.
    """

    def __init__(self, prop_id):
        self.id = prop_id
        self.network_details = {}
        self.sensor_settings = {}

    def to_dict(self):
        """
        Converts the prop object to a dictionary representation.
        """
        return {
            "id": self.id,
            "network_details": self.network_details,
            "sensor_settings": self.sensor_settings,
        }

    def load_from_dict(self, data):
        """
        Loads the prop data from a dictionary.
        """
        self.id = data["id"]
        self.network_details = data["network_details"]
        self.sensor_settings = data["sensor_settings"]


class Song:
    """
    This class represents a single song within a performance.

    Attributes:
        performance: The performance object this song belongs to.
        name: The name of the song.
        config: A dictionary containing song-specific settings.
        props: A dictionary of prop objects, indexed by prop IDs.
    """

    def __init__(self, performance, name):
        self.performance = performance
        self.name = name
        self.config = None
        self.props = {}

    def load_config(self):
        """
        Loads the song configuration file and creates prop objects.
        """
        config_path = os.path.join(self.performance.workspace_path, self.name, "song_config.json")
        if not os.path.isfile(config_path):
            self.config = {}
        else:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        for prop_id in self.config["props"]:
            prop = Prop(prop_id)
            prop.load_from_dict(self.config["props"][prop_id])
            self.props[prop_id] = prop

    def save_config(self):
        """
        Saves the song configuration to a file.
        """
        config_path = os.path.join(self.performance.workspace_path, self.name, "song_config.json")
        with open(config_path, "w") as f:
            prop_data = {}
            for prop in self.props.values():
                prop_data[prop.id] = prop.to_dict()
            self.config["props"] = prop_data
            json.dump(self.config, f, indent=4)

    def add_prop(self, prop):
        """
        Adds a prop to the song and updates the configuration file.
        """
        self.props[prop.id] = prop
        self.save_config()

    def edit_prop(self, prop_id, data):
        """
        Edits the settings of a prop and updates the configuration file.
        """
        if prop_id not in self.props:
            raise ValueError(f"Prop with ID '{prop_id}' does not exist.")
        self.props[prop_id].load_from_dict(data)
        self.save_config()

    def remove_prop(self, prop_id):
        """
        Removes a prop from the song and updates the configuration file.
        """
        if prop_id not in self.props:
            raise ValueError(f"Prop with ID '{prop_id}' does not exist.")
        del self.props[prop_id]
        self.save_config()

    def get_prop(self, prop_id):
        """
        Returns the prop object with a specific ID.
        """
        if prop_id not in self.props:
            raise ValueError(f"Prop with ID '{prop_id}' does not exist.")
        return self.props[prop_id]

    # ... other song methods ...
class Performance:
    """
    This class represents an interactive music performance. It handles configuration,
    song management, initialization, execution, and logging.

    Attributes:
        workspace_path: The path to the workspace folder for this performance.
        performance_config: A dictionary containing global performance settings.
        songs: A dictionary of song objects, indexed by song names.
    """

    def __init__(self, workspace_path):
        self.workspace_path = workspace_path
        self.performance_config = None
        self.songs = {}

    def load_config(self):
        """
        Loads the performance configuration file.
        """
        config_path = os.path.join(self.workspace_path, "performance_config.json")
        if not os.path.isfile(config_path):
            self.performance_config = {}
        else:
            with open(config_path, "r") as f:
                self.performance_config = json.load(f)

    def save_config(self):
        """
        Saves the performance configuration to a file.
        """
        config_path = os.path.join(self.workspace_path, "performance_config.json")
        with open(config_path, "w") as f:
            json.dump(self.performance_config, f, indent=4)

    def update_song_in_performance_config(self, song_name):
        """
        Updates the performance configuration to reflect the new song.
        """
        if song_name not in self.performance_config["songs"]:
            self.performance_config["songs"].append(song_name)
        self.save_config()

    def load_songs(self):
        """
        Loads all songs from their respective sub-folders and stores them in a dictionary.
        """
        for song_folder in os.listdir(self.workspace_path):
            if os.path.isdir(os.path.join(self.workspace_path, song_folder)):
                song = Song(self, song_folder)
                song.load_config()
                self.songs[song.name] = song

    def create_song(self, name):
        """
        Creates a new song with the specified name and initializes its directory structure.

        Args:
            name: The name of the new song.
        """
        song_folder = os.path.join(self.workspace_path, name)
        os.makedirs(song_folder)
        song = Song(self, name)
        self.songs[name] = song
        self.update_song_in_performance_config(name)
        song.save_config()

def edit_song_config(self, song_name, data):
    """
    Updates the configuration of an existing song and saves it to the file.

    Args:
        song_name: The name of the song to edit.
        data: A dictionary containing the updated configuration data.
    """
    if song_name not in self.songs:
        raise ValueError(f"Song '{song_name}' does not exist.")
    self.songs[song_name].config.update(data)
    self.songs[song_name].save_config()

