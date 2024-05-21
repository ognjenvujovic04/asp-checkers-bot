import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

class Button:
    def __init__(self, x, y, width, height, text, button_color, text_color, action=None, arg=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.action = action
        self.arg = arg

    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def clicked(self):
        if self.action:
            return self.action(self.arg)

def main_menu():
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((500,500))
    screen.fill(WHITE)

    font = pygame.font.Font(None, 40)
    text = font.render("Welcome to Checkers!", True, BLACK)
    text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
    screen.blit(text, text_rect)

    logo = pygame.image.load("../assets/checkers-logo.png")
    logo = pygame.transform.scale(logo, (200, 200))
    logo_rect = logo.get_rect(center=(screen.get_width() // 2, 200))
    screen.blit(logo, logo_rect)

    buttons = []
    buttons.append(Button(100, 350, 300, 50, "Jumping Mandatory", GRAY, WHITE, return_choice, 1))
    buttons.append(Button(100, 450, 300, 50, "Jumping Optional", GRAY, WHITE, return_choice, 0))

    total_button_height = sum(button.rect.height + 10 for button in buttons)
    current_y = (screen.get_height() - total_button_height) // 2

    for button in buttons:
        button.rect.y = current_y
        current_y += button.rect.height + 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_pos):
                        return button.clicked()

        for button in buttons:
            button.draw(screen)

        pygame.display.update()

def return_choice(choice):
    return choice


main_menu()
