import os
import sys
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Print the current working directory
        print(f"Current working directory: {os.getcwd()}")

        # Load the alien image and set its rect attribute.
        current_path = os.path.dirname(__file__)  # Get the current file path
        image_path = os.path.join(current_path, "images", "alien.png")
        print(f"Loading alien image from: {image_path}")  # Debugging info

        # Verify if the file exists
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            sys.exit(1)

        try:
            self.image = pygame.image.load(image_path)
            print("Alien image loaded successfully")  # Debugging info
        except pygame.error as e:
            print(f"Unable to load alien image from {image_path}: {e}")
            sys.exit(1)

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def update(self):
        """Move the alien right or left."""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)