import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from player_car import PlayerCar
import game_functions as gf

def run_game():
    # Initialize pygame and reduce sound delay
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    
    # Initialize game settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Dodge & Drive")
    
    # Initialize game elements
    play_button = Button(screen, "Play")
    stats = GameStats(settings)
    sb = Scoreboard(screen, settings, stats)
    player_car = PlayerCar(screen, settings)
    
    # Initialize sprite groups
    ai_cars = Group()
    power_ups = Group()
    obstacles = Group()
    
    # Load background music (but don't play it yet)
    pygame.mixer.music.load('assets/sounds/background_music.wav')
    
    # Game loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        gf.check_events(player_car, play_button, stats)
        
        if stats.game_active:
            # Start background music if it's not already playing
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)  # Loop indefinitely
            
            player_car.update()
            gf.update_ai_cars(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles)
            gf.update_power_ups(settings, screen, stats, sb, player_car, power_ups, ai_cars, obstacles)
            gf.update_obstacles(settings, screen, stats, sb, player_car, obstacles, ai_cars, power_ups)
            
            if stats.lives <= 0:
                print("Player has lost all lives!")  # Debug statement
                stats.game_active = False
                pygame.mixer.music.stop()  # Stop background music when the game is over
                restart = gf.show_game_over(screen, settings, stats, sb)
                if restart:
                    stats.reset_stats()  # Reset stats
                    sb.prep_score()      # Update score display
                    sb.prep_level()      # Update level display
                    ai_cars.empty()
                    power_ups.empty()
                    obstacles.empty()
                    player_car.center_car()
                    stats.game_active = True
        
        gf.update_screen(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles, play_button)

if __name__ == "__main__":
    run_game()