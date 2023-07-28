import pygame

#Calling pygame
pygame.init()


#Screen Size
screen = pygame.display.set_mode([500, 500])

#Screen Background Color
bg = (127,127,127)
screen.fill(bg)

#Button
font = pygame.font.SysFont("Arial", 14)
text = font.render(" Increment ", True, (255,255,255))
rect = text.get_rect(topleft=(10,10))


#Message
number = 0
fontMessage = pygame.font.SysFont("Arial", 14)
textMessage = fontMessage.render(str(number), True, (255,255,255))
rectMessage = textMessage.get_rect(topleft=(100,100))

#pygame is alive
running = True

#frame rendering
while running:

    #Render Button
    screen.blit(text, rect)
    pygame.draw.rect(screen, (255,0,0),rect,2)
    
    #Render Message
    strNumber = str(number)
    textMessage=fontMessage.render(str(number), True, (255,255,255))
    screen.blit(textMessage, rectMessage)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Check Click Event
        if event.type == pygame.MOUSEBUTTONDOWN: # try print(event.pos) to get mouse clicke position
          
            
            #Check position of current mouse hover
            if rect.collidepoint(pygame.mouse.get_pos()):
                print("Increment button is pressed")  
                number += 1
            
    #reset screen to emthy for the next frame
    screen.fill(bg) # try to delete this line

  
    pygame.display.flip()
    

pygame.quit()
