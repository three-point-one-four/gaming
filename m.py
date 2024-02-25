import pygame
import random

dsp = pygame.display
img = pygame.image
eve = pygame.event
fnt = pygame.font

# init
pygame.init()
screen = dsp.set_mode((650, 750))
dsp.set_caption('2048')
dsp.set_icon(img.load('logo.png'))
ya_hei_ui = fnt.SysFont('Microsoft YaHei UI', 50, True)
blank = img.load('blank.png')
colors = {'1': [[255, 0, 0], [255, 255, 255]], '2': [[255, 128, 0], [255, 255, 255]],
          '4': [[255, 255, 0], [0, 0, 0]], '8': [[128, 255, 0], [0, 0, 0]],
          '16': [[0, 255, 0], [0, 0, 0]], '32': [[0, 255, 128], [0, 0, 0]],
          '64': [[0, 255, 255], [0, 0, 0]], '128': [[0, 128, 255], [255, 255, 255]],
          '256': [[0, 0, 255], [255, 255, 255]], '512': [[128, 128, 255], [0, 0, 0]],
          '1024': [[255, 255, 255], [0, 0, 0]]}

# pygame.key.set_repeat(1, 1)
xys = []
blocks = [0, 0, 0, 0, 0, 0, 0, 0, [1, [50, 450]], 0, 0, 0, [1, [50, 600]], 0, 0, 0]
# pygame.draw.rect(screen, colors['1'][0], [50, 600, 100, 100], 0)

while True:
    dsp.update()
    screen.fill('#eeeebb')
    title = ya_hei_ui.render('２０４８', True, 'Black')
    screen.blit(title, (50, 50))
    for x in range(0, 4):
        for y in range(0, 4):
            screen.blit(blank, (50 + x * 150, 150 + y * 150))
            xys.append([50 + x * 150, 150 + y * 150])

    for item in range(len(blocks)):
        if blocks[item] != 0:
            pygame.draw.rect(screen, colors[str(blocks[item][0])][0], [blocks[item][1][0], blocks[item][1][1], 100, 100], 0)
            num = ya_hei_ui.render(str(blocks[item][0]), True, colors[str(blocks[item][0])][1])
            screen.blit(num, (blocks[item][1][0], blocks[item][1][1]))

    for event in eve.get():
        if event.type == pygame.QUIT:
            dsp.quit()
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_UP:
                for k in range(4):
                    for i in range(len(blocks)):
                        block_go = True
                        for j in range(len(blocks)):
                            if blocks[i] != 0 and blocks[j] != 0:
                                if blocks[i][1][1] - 150 == blocks[j][1][1] and blocks[i][1][0] == blocks[j][1][0]:
                                    block_go = False
                                    if blocks[i][0] == blocks[j][0]:
                                        blocks[j] = 0
                                        blocks[i] = [blocks[i][0] * 2,
                                                                   [blocks[i][1][0],
                                                                    blocks[i][1][1] - 150]]
                        if blocks[i] != 0:
                            if 149 > blocks[i][1][1] - 150:
                                block_go = False
                        if block_go:
                            if blocks[i] != 0:
                                blocks[i] = [blocks[i][0], [blocks[i][1][0],
                                                                                        blocks[i][1][1]
                                                                                        - 150]]
                rl = []
                fl = []
                for m in range(len(blocks)):
                    if blocks[m] == 0:
                        rl.append(m)
                    else:
                        fl.append(m)
                rl1 = random.choice(rl)
                blocks[rl1] = [blocks[random.choice(fl)][0], [(rl1 % 4 + 1) * 150 + 50, rl1 // 4 * 150 + 150]]
                print(blocks)
