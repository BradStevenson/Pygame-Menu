#!/usr/bin/env python

import pygame

pygame.display.init()
pygame.font.init()
HEIGHT_RES = 768
WIDTH_RES = 768

class Menu:
    field_list = []
    field = []
    dest_surface = pygame.Surface
    number_fields = 0
    background_color = (51, 51, 51)
    font_size = 36
    font_color =  (255, 255, 255)
    selection_color = (153, 102, 255)
    selection_position = 0
    position = (0,0)
    menu_width = 0
    menu_height = 0

    class Field:
      text = ''
    	field = pygame.Surface
    	field_rect = pygame.Rect
    	selection_rect = pygame.Rect

    def move_menu(self, top, left):
    	self.position = (top, left)

    def set_colors(self, text, selection, background):
    	self.background_color = background
    	self.font_color = text
    	self.selection_color = selection

    def get_position(self):
    	return self.selection_position

    def init(self, item_list, dest_surface):
    	self.field_list = item_list
    	self.dest_surface = dest_surface
    	self.number_fields = len(self.field_list)
    	self.create_structures()

    def draw(self, move=0):
        if move:
            self.selection_position += move 
            if self.selection_position == -1:
                self.selection_position = self.number_fields - 1
            self.selection_position %= self.number_fields
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.background_color)
        selection_rect = self.field[self.selection_position].selection_rect
        pygame.draw.rect(menu, self.selection_color, selection_rect)

        for i in xrange(self.number_fields):
            menu.blit(self.field[i].field, self.field[i].field_rect)
        self.dest_surface.blit(menu, self.position)
        return self.selection_position

    def create_structures(self):
        shift = 0
        self.menu_height = 0
        self.font = pygame.font.Font(None, self.font_size)
        for i in xrange(self.number_fields):
            self.field.append(self.Field())
            self.field[i].text = self.field_list[i]
            self.field[i].field = self.font.render(self.field[i].text, 1, self.font_color)

            self.field[i].field_rect = self.field[i].field.get_rect()
            shift = int(self.font_size * 0.2)

            height = self.field[i].field_rect.height
            self.field[i].field_rect.left = shift
            self.field[i].field_rect.top = shift + (shift * 2 + height) * i

            width = self.field[i].field_rect.width + shift*2
            height = self.field[i].field_rect.height + shift*2            
            left = self.field[i].field_rect.left - shift
            top = self.field[i].field_rect.top - shift
            if width > self.menu_width:
            	self.menu_width = width
            else:
            	width = self.menu_width
            self.field[i].selection_rect = (left, top , width, height)
            self.menu_height += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.position
        self.position = (x + mx, y + my) 

def main():
	def nop():
		pass

	# SET RESOLUTION
	screen = pygame.display.set_mode((WIDTH_RES, HEIGHT_RES))
	background = pygame.Surface((WIDTH_RES, HEIGHT_RES))
	background.fill(pygame.Color(236, 240, 241))
	screen.blit(background,(0, 0))

	menu = Menu()
	menu.init(['Start', 'Pause', 'Quit'], screen)
	# Optional to set menu colors. (Text color, Selection color, Menu-Background color)
	menu.set_colors((255, 255, 255), (26, 188, 156), (52, 73, 94))
	menu.draw()

	running = True
	while running:
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
			   	if event.key == pygame.K_UP:
			   		menu.draw(-1)
			  	elif event.key == pygame.K_DOWN:
				   	menu.draw(1)
			  	elif event.key == pygame.K_RETURN:
				   	if menu.get_position() == 2:
				   		# Do something
				   		running = False

if __name__ == "__main__":
	main()
