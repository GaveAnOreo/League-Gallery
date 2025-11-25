import sys
import pygame
from time import sleep
from ai_car import AICar
from power_up import PowerUp
from obstacle import Obstacle

def is_position_valid(new_rect, group):
    """Check if the new object's position does not collide with existing objects."""
    for obj in group:
        if new_rect.colliderect(obj.rect):
            return False
    return True

def spawn_ai_car(settings, screen, ai_cars):
    """Spawn a single AI car at a random position, ensuring no overlap."""
    max_attempts = 100  # Maximum attempts to find a valid position
    for _ in range(max_attempts):
        ai_car = AICar(screen, settings)
        if is_position_valid(ai_car.rect, ai_cars):
            ai_cars.add(ai_car)
            break

def spawn_power_up(settings, screen, power_ups, ai_cars, obstacles):
    """Spawn a power-up at a random position, ensuring no overlap with AI cars or obstacles."""
    max_attempts = 100  # Maximum attempts to find a valid position
    for _ in range(max_attempts):
        power_up = PowerUp(screen, settings)
        if (is_position_valid(power_up.rect, power_ups) and
            is_position_valid(power_up.rect, ai_cars) and
            is_position_valid(power_up.rect, obstacles)):
            power_ups.add(power_up)
            break

def spawn_obstacle(settings, screen, obstacles, ai_cars):
    """Spawn an obstacle at a random position, ensuring no overlap with AI cars or other obstacles."""
    max_attempts = 100  # Maximum attempts to find a valid position
    for _ in range(max_attempts):
        obstacle = Obstacle(screen, settings)
        if is_position_valid(obstacle.rect, obstacles) and is_position_valid(obstacle.rect, ai_cars):
            obstacles.add(obstacle)
            break

def check_events(player_car, play_button, stats):
    """Handle keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Movement keys (WASD and Arrow Keys)
            if event.key in (pygame.K_a, pygame.K_LEFT):
                player_car.moving_left = True
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                player_car.moving_right = True
            elif event.key in (pygame.K_w, pygame.K_UP):
                player_car.moving_up = True
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                player_car.moving_down = True
            # Spacebar to start the game
            elif event.key == pygame.K_SPACE and not stats.game_active:
                stats.game_active = True
                pygame.mixer.music.play(-1)  # Start background music
        elif event.type == pygame.KEYUP:
            # Movement keys (WASD and Arrow Keys)
            if event.key in (pygame.K_a, pygame.K_LEFT):
                player_car.moving_left = False
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                player_car.moving_right = False
            elif event.key in (pygame.K_w, pygame.K_UP):
                player_car.moving_up = False
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                player_car.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not stats.game_active and play_button.rect.collidepoint(mouse_x, mouse_y):
                stats.game_active = True
                pygame.mixer.music.play(-1)  # Start background music

def update_screen(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles, play_button):
    """Update all visuals on the screen."""
    screen.blit(settings.bg_image, (0, 0))
    player_car.blitme()
    
    for ai_car in ai_cars:
        ai_car.blitme()
    for power_up in power_ups:
        power_up.blitme()
    for obstacle in obstacles:
        obstacle.blitme()
    
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
    
    pygame.display.flip()

def update_ai_cars(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles):
    """Update AI cars and handle collisions."""
    current_time = pygame.time.get_ticks()
    if current_time - settings.last_ai_spawn > settings.ai_spawn_delay:
        spawn_ai_car(settings, screen, ai_cars)
        settings.last_ai_spawn = current_time
    
    ai_cars.update()
    
    # Remove off-screen AI cars
    for ai_car in ai_cars.copy():
        if ai_car.rect.top > settings.screen_height:
            ai_cars.remove(ai_car)
    
    # Check collisions
    if pygame.sprite.spritecollideany(player_car, ai_cars):
        handle_crash(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles)

def update_power_ups(settings, screen, stats, sb, player_car, power_ups, ai_cars, obstacles):
    """Update power-ups and handle collisions."""
    current_time = pygame.time.get_ticks()
    if current_time - settings.last_power_up_spawn > settings.power_up_spawn_delay:
        spawn_power_up(settings, screen, power_ups, ai_cars, obstacles)
        settings.last_power_up_spawn = current_time
    
    power_ups.update()
    
    # Remove off-screen power-ups
    for power_up in power_ups.copy():
        if power_up.rect.top > settings.screen_height:
            power_ups.remove(power_up)
    
    # Check collisions (remove only collided power-ups)
    collided_power_ups = pygame.sprite.spritecollide(player_car, power_ups, True)
    for _ in collided_power_ups:
        stats.score += settings.power_up_points  # Always give 10 points (no combo multiplier)
        sb.prep_score()
        pygame.mixer.Sound('assets/sounds/power_up.wav').play()
        
        # Level progression (increase threshold to 100 points per level)
        if stats.score >= stats.level * 100:  # Level up every 100 points
            stats.increase_level()
            sb.prep_level()

def update_obstacles(settings, screen, stats, sb, player_car, obstacles, ai_cars, power_ups):
    """Update obstacles and handle collisions."""
    current_time = pygame.time.get_ticks()
    if current_time - settings.last_obstacle_spawn > settings.obstacle_spawn_delay:
        spawn_obstacle(settings, screen, obstacles, ai_cars)
        settings.last_obstacle_spawn = current_time
    
    obstacles.update()
    
    # Remove off-screen obstacles
    for obstacle in obstacles.copy():
        if obstacle.rect.top > settings.screen_height:
            obstacles.remove(obstacle)
    
    # Check collisions
    if pygame.sprite.spritecollideany(player_car, obstacles):
        handle_crash(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles)

def handle_crash(settings, screen, stats, sb, player_car, ai_cars, power_ups, obstacles):
    """Handle player crash with AI car/obstacle."""
    if stats.lives > 0:
        stats.lives -= 1
        sb.prep_lives()
        
        # Play crash sound
        crash_sound = pygame.mixer.Sound(settings.crash_sound_path)
        crash_sound.play()
        
        # Clear all entities
        ai_cars.empty()
        power_ups.empty()
        obstacles.empty()
        
        # Reset player position
        player_car.center_car()
        
        # Reset spawn timers
        settings.last_ai_spawn = pygame.time.get_ticks()
        settings.last_power_up_spawn = pygame.time.get_ticks()
        settings.last_obstacle_spawn = pygame.time.get_ticks()
        
        # Reset combo multiplier
        settings.combo_multiplier = 1
        
        sleep(0.5)
    else:
        # Play game over sound
        print("Game over sound should play now!")  # Debug statement
        try:
            game_over_sound = pygame.mixer.Sound(settings.game_over_sound_path)
            game_over_sound.set_volume(1.0)  # Set volume to maximum
            game_over_sound.play()
        except Exception as e:
            print(f"Error playing game over sound: {e}")  # Debug statement
        
        # Stop background music
        pygame.mixer.music.stop()
        
        # Reset level and score when the game is over
        stats.reset_stats()  # Reset level to 1 and score to 0
        sb.prep_score()      # Update score display
        sb.prep_level()      # Update level display
        stats.game_active = False

def show_game_over(screen, settings, stats, sb):
    """Display game over screen and handle restart/quit."""
    print("Showing game over screen!")  # Debug statement
    font = pygame.font.SysFont(None, 74)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (settings.screen_width // 2 - 150, settings.screen_height // 2 - 50))
    
    score_font = pygame.font.SysFont(None, 48)
    score_text = score_font.render(f"Final Score: {stats.score}", True, (255, 255, 255))
    screen.blit(score_text, (settings.screen_width // 2 - 120, settings.screen_height // 2 + 20))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_r, pygame.K_SPACE):  # Allow spacebar to restart
                    stats.reset_stats()  # Reset stats
                    sb.prep_score()      # Update score display
                    sb.prep_level()      # Update level display
                    
                    # Restart background music
                    pygame.mixer.music.play(-1)
                    
                    return True  # Restart
                elif event.key == pygame.K_q:
                    return False  # Quit