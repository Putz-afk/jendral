import pygame

def draw_text(screen, text, x, y, font_size=36, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def load_image(filename, colorkey=None):
    try:
        image = pygame.image.load(filename)
    except pygame.error as e:
        print(f"Cannot load image: {filename}")
        raise SystemExit(e)
    
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image

def draw_button(screen, text, x, y, width, height, color, hover_color, text_color, mouse_pos, action=None):
    button_rect = pygame.Rect(x, y, width, height)
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect)
        if pygame.mouse.get_pressed()[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, button_rect)
    
    # Draw text
    font = pygame.font.Font(None, 32)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    
    return button_rect

def draw_deck(screen, deck):
    card_amount = len(deck)
    y_pos = 200
    
    for i, card in enumerate(deck):
        card.draw(screen, i, card_amount)
    