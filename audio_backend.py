import pygame.mixer

class audio_backend:
    def __init__(self):
        '''init music player'''

        # Init pygame mixer
        pygame.mixer.init()


    def play(self, file_path:str, fade_in_ms:int=0):
        '''Load and play music'''

        # Load music file
        pygame.mixer.music.load(file_path)

        # Play music file
        pygame.mixer.music.play(fade_ms=fade_in_ms)
    
    def stop(self, fade_out_ms:int=0):
        '''Stop music'''

        # Fade out music
        pygame.mixer.music.fadeout(fade_out_ms)

        # Unload music
        pygame.mixer.music.unload()


    def pause(self):
        '''Pause music'''
        
        # Pause music
        pygame.mixer.music.pause()

    
    def unpause(self):
        '''Unpause music'''

        # Unpause music
        pygame.mixer.music.unpause()


    def is_playing(self) -> bool:
        '''Check if music is playing'''

        # Check state
        music_state = pygame.mixer.music.get_busy()

        return music_state
