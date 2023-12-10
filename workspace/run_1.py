from workflows.objects import Performance, Song, Prop

# Define workspace path
workspace_path = "/path/to/your/workspace"

# Create a new performance object
performance = Performance(workspace_path)

# Create two songs
song1 = Song(performance, "song1")
song2 = Song(performance, "song2")

# Create three props for each song
prop1_song1 = Prop("prop1_song1")
prop2_song1 = Prop("prop2_song1")
prop3_song1 = Prop("prop3_song1")
song1.add_prop(prop1_song1)
song1.add_prop(prop2_song1)
song1.add_prop(prop3_song1)

prop1_song2 = Prop("prop1_song2")
prop2_song2 = Prop("prop2_song2")
prop3_song2 = Prop("prop3_song2")
song2.add_prop(prop1_song2)
song2.add_prop(prop2_song2)
song2.add_prop(prop3_song2)

# Save song configurations
song1.save_config()
song2.save_config()

# Update performance configuration
performance.update_song_in_performance_config(song1.name)
performance.update_song_in_performance_config(song2.name)
performance.save_config()

# Start the performance
# (implement this function based on your specific requirements)
performance.start()

# ... perform other actions
