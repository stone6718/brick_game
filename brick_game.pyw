# Version 2.1
#############################################################
# 1. 모듈

import pygame
import random
import sys

#############################################################
def main():
    #############################################################
    # 2. 기본 초기화

    pygame.init()
    score = 0 # 점수 초기화

    #############################################################
    # 3. 화면 크기 설정

    screen_width = 480 # 가로 크기
    screen_height = 640 # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))

    #############################################################
    # 4. 게임 이름 설정

    pygame.display.set_caption("벽돌 피하기 V.2")

    #############################################################
    # 5. FPS

    clock = pygame.time.Clock()

    #############################################################
    # 6. 이미지 경로설정

    brick_image = "images/brick.png"
    background_image = "images/background_paper.png"
    character_image = "images/character.png"
    ground_image = "images/ground.png"

    #############################################################
    # 7. 배경 만들기

    background = pygame.image.load(background_image).convert_alpha()

    #############################################################
    # 8. 땅 만들기

    ground = pygame.image.load(ground_image).convert_alpha()
    ground_size = ground.get_rect().size
    ground_width = ground_size[0]
    ground_height = ground_size[1]
    ground_x_pos = (screen_width / 2) - (ground_width / 2)
    ground_y_pos = screen_height - ground_height

    #############################################################
    # 9. 캐릭터 만들기

    character = pygame.image.load(character_image).convert_alpha()
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2)
    character_y_pos = screen_height - (character_height + ground_height)

    #############################################################
    # 10. 이동 좌표

    to_x = 0

    #############################################################
    # 11. 이동 속도

    character_speed = 0.6
    brick_speed = 10
    brick1_speed = 10
    brick2_speed = 10

    #############################################################
    # 12. 벽돌 만들기

    brick = pygame.image.load(brick_image).convert_alpha()
    brick_size = brick.get_rect().size
    brick_width = brick_size[0]
    brick_x_pos = random.randint(0, screen_width - brick_width)
    brick_y_pos = random.randint(random.randrange(-300,0), 0)

    brick1 = pygame.image.load(brick_image).convert_alpha()
    brick1_size = brick1.get_rect().size
    brick1_width = brick1_size[0]
    brick1_x_pos = random.randint(0, screen_width - brick1_width)
    brick1_y_pos = random.randint(random.randrange(-300,0), 0)

    brick2 = pygame.image.load(brick_image).convert_alpha()
    brick2_size = brick2.get_rect().size
    brick2_width = brick2_size[0]
    brick2_x_pos = random.randint(0, screen_width - brick2_width)
    brick2_y_pos = random.randint(random.randrange(-300,0), 0)

    #############################################################
    # 13. 폰트 정의

    game_font = pygame.font.Font(None, 40)
    gamestart_font = pygame.font.SysFont('한컴말랑말랑', 45)
    gamestart1_font = pygame.font.SysFont(None, 40)
    gameover_font = pygame.font.Font(None, 50)
    gameover1_font = pygame.font.SysFont('malgungothic', 20)

    #############################################################
    # 14. 게임 시작

    def game_start():
        gm_start = pygame.image.load(background_image).convert_alpha()

        gm_text = "벽돌 피하기 (V 2.1)"
        gm1_text = "Press Space Key To START"

        gm_text_image = gamestart_font.render(gm_text, True, (0, 0, 255))
        gm1_text_image = gamestart1_font.render(gm1_text, True, (255, 0, 0))

        gm_text_size_wedith = gm_text_image.get_rect().size[0]
        gm1_text_size_wedith = gm1_text_image.get_rect().size[0]
        gm1_text_size_height = gm1_text_image.get_rect().size[1]

        gm_text_x_pos = (screen_width / 2) - (gm_text_size_wedith / 2)
        gm1_text_x_pos = (screen_width / 2) - (gm1_text_size_wedith / 2)
        gm1_text_y_pos = (screen_height / 2) - (gm1_text_size_height / 2)

        screen.blit(gm_start, (0, 0))
        screen.blit(ground, (ground_x_pos, ground_y_pos))
        screen.blit(gm_text_image, (gm_text_x_pos, 30))
        screen.blit(gm1_text_image, (gm1_text_x_pos, gm1_text_y_pos))

        pygame.display.update()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

    #############################################################
    # 15. 게임 메인 루프 시작

    gameover = False

    running = True

    game_start()

    while running:
        dt = clock.tick(30)

    #############################################################
    # 16. 이벤트 처리 (키보드, 마우스 등)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += character_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    to_x -= character_speed
                elif event.key == pygame.K_d:
                    to_x += character_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0

    #############################################################
    # 17. 게임 캐릭터 위치 정의

        character_x_pos += to_x * dt

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        brick_y_pos += brick_speed

        if brick_y_pos > screen_height:
            brick_y_pos = random.randint(random.randrange(-300,0), 0)
            brick_x_pos = random.randint(0, screen_width - brick_width)
            score += 1
            brick_speed += 0.25

        brick1_y_pos += brick1_speed

        if brick1_y_pos > screen_height:
            brick1_y_pos = random.randint(random.randrange(-300,0), 0)
            brick1_x_pos = random.randint(0, screen_width - brick1_width)
            score += 1
            brick1_speed += 0.25
        
        brick2_y_pos += brick2_speed

        if brick2_y_pos > screen_height:
            brick2_y_pos = random.randint(random.randrange(-300,0), 0)
            brick2_x_pos = random.randint(0, screen_width - brick2_width)
            score += 1
            brick2_speed += 0.25

    #############################################################
    # 18. 충돌 처리

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        brick_rect = brick.get_rect()
        brick_rect.left = brick_x_pos
        brick_rect.top = brick_y_pos

        if character_rect.colliderect(brick_rect):
            print("충돌했어요")
            gameover = "GAME OVER"
        
        brick1_rect = brick1.get_rect()
        brick1_rect.left = brick1_x_pos
        brick1_rect.top = brick1_y_pos

        if character_rect.colliderect(brick1_rect):
            print("충돌했어요")
            gameover = "GAME OVER"

        brick2_rect = brick2.get_rect()
        brick2_rect.left = brick2_x_pos
        brick2_rect.top = brick2_y_pos

        if character_rect.colliderect(brick2_rect):
            print("충돌했어요")
            gameover = "GAME OVER"

    #############################################################
    # 19. 점수표시

        scoreboard = game_font.render(str(score), True, (110,110,110))

    #############################################################
    # 20. 게임 오버

        if gameover:
            gameover1 = "5초 뒤 게임이 다시 시작됩니다!"

            gameover_text = gameover_font.render(gameover, True, (255,0,0))
            gameover1_text = gameover1_font.render(gameover1, True, (255,0,0))

            text_size_wedith = gameover_text.get_rect().size[0]
            text_size_height = gameover_text.get_rect().size[1]
            text1_size_wedith = gameover1_text.get_rect().size[0]
            text1_size_height = gameover1_text.get_rect().size[1]

            text_x_pos = (screen_width / 2) - (text_size_wedith / 2)
            text_y_pos = (screen_height / 2) - (text_size_height / 2)
            text1_x_pos = (screen_width / 2) - (text1_size_wedith / 2)
            text1_y_pos = (screen_height / 2) - (text1_size_height / 2)

            screen.blit(gameover_text, (text_x_pos, text_y_pos - 30))
            screen.blit(gameover1_text, (text1_x_pos, text1_y_pos))
            pygame.display.update()
            pygame.time.delay(5 * 1000) # 5 초
            regame()

    #############################################################
    # 21. 화면에 그리기

        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(brick, (brick_x_pos, brick_y_pos))
        screen.blit(brick1, (brick1_x_pos, brick1_y_pos))
        screen.blit(brick2, (brick2_x_pos, brick2_y_pos))
        screen.blit(ground, (ground_x_pos, ground_y_pos))
        screen.blit(scoreboard, (20,20))

    #############################################################
    # 22. 게임 종료

        pygame.display.update() # 업데이트

    #############################################################
    # 23. 메인루프 종료

    pygame.quit()

    #############################################################
def regame():
    main()
main()
