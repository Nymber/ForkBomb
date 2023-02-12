import pygame, settings, sys, backgroundSystem
class Login():

    # default function when Level is instansialized
    def __init__(self, surface):
        self.screen = surface
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
        self.Data = list()
        self.Data = [settings.username, settings.password, settings.money, settings.power, settings.power, settings.memory, settings.connection, settings.power, settings.bitcoin]
        self.timeout = 0
        self.username_input_box = pygame.Rect(500, 50, 40, 32)
        self.password_input_box = pygame.Rect(500, 100, 40, 32)
        self.color_passive = pygame.Color('blue')
        self.color_active = pygame.Color('black')
        self.surface_text = settings.font.render(str(self.Data), True, "blue")
        self.previous_time = pygame.time.get_ticks()
        backgroundSystem.player(self)
        self.display_surface = surface
        self.world_shift = 0
        
    def run(self):
        
        for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.username_input_box.collidepoint(event.pos):
                        settings.active_user = not settings.active_user
                    elif self.password_input_box.collidepoint(event.pos):
                        settings.active_pass = not settings.active_pass
                    else:
                        settings.active_pass = False
                        settings.active_user = False
                if event.type == pygame.KEYDOWN:
                    if settings.active_user:
                        if event.key == pygame.K_RETURN:
                            if settings.password != '':
                                settings.user_txt = ''
                                print("Username: " + settings.username)
                                return True
                            else:
                                settings.msg = "Need Password!"
                        elif event.key == pygame.K_BACKSPACE:
                            settings.user_txt = settings.user_txt[:-1]
                        else:
                            settings.user_txt += event.unicode
                        settings.username = settings.user_txt
                            
                    elif settings.active_pass:
                        if event.key == pygame.K_RETURN:
                            if settings.username != '':
                                settings.user_pass = ''
                                print(print("Password: " + settings.password))
                                return True
                            else:
                                settings.msg = "Need Username!"
                        elif event.key == pygame.K_BACKSPACE:
                            settings.user_pass = settings.user_pass[:-1]
                        else:
                            settings.user_pass += event.unicode
                        settings.password = settings.user_pass
                        
        self.color_user = self.color_active if settings.active_user else self.color_passive
        self.color_pass = self.color_active if settings.active_pass else self.color_passive
        user_surface = settings.font.render(settings.user_txt, True, self.color)
        pass_surface = settings.font.render(settings.user_pass, True, self.color)
        
        # Resize the box if the text is too long.
        user_width = max(200, user_surface.get_width()+10)
        pass_width = max(200, pass_surface.get_width()+10)
        
        self.username_input_box.w = user_width
        self.password_input_box.w = pass_width
        
        self.screen.fill("grey", self.username_input_box)
        self.screen.fill("grey", self.password_input_box)
        
        # Blit the text.
        self.screen.blit(user_surface, (self.username_input_box.x+5, self.username_input_box.y+5))
        self.screen.blit(pass_surface, (self.password_input_box.x+5, self.password_input_box.y+5))
        
        msg_surface = settings.font.render(settings.msg, True, self.color)
        self.screen.blit(msg_surface, ((500,5)))
        
        user_text = settings.font.render("Username:", True, "black")
        self.screen.blit(user_text, ((425,50)))
        user_pass = settings.font.render("Password:", True, "black")
        self.screen.blit(user_pass, ((425,100)))
        
        # Blit the input_box rect.
        pygame.draw.rect(self.screen, self.color_user, self.username_input_box, 2)
        pygame.draw.rect(self.screen, self.color_pass, self.password_input_box, 2)
        