from mqtt_client import MqttClient
from pygame_handler import PygameHandler
from audio_player import AudioPlayer
from visual_cues import VisualCues
from utils import config

def main():
    # Initialize components
    mqtt_client = MqttClient()
    pygame_handler = PygameHandler()
    audio_player = AudioPlayer()
    visual_cues = VisualCues()

    # Start background music and audio cues
    audio_player.start_music()

    # Start MQTT loop and process messages
    mqtt_client.connect(config.MQTT_HOST, config.MQTT_PORT)
    mqtt_client.subscribe(config.MQTT_TOPIC)
    mqtt_client.on_message = lambda client, userdata, msg: pygame_handler.handle_message(msg)
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()
