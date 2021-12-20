import os
from typing import Sized
import pygame

#######TODO##########
# o 1. 레시피 북 띄우기 
# x 2. 주문 띄우기
# x 3. 납품하기
# o 4. 만든 제품 수 띄우기
# o 5. 제작화면 띄우기
# o 6. 제작화면 - 입력한 스택 보이기
# o 7. 재료 그림 그리기 

#########################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 560 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름")

#FPS
clock = pygame.time.Clock()
#########################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 작업대 만들기
worktable = pygame.image.load(os.path.join(image_path,"worktable.png"))
worktable_size = worktable.get_rect().size
worktable_height = worktable_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용
worktable_y_pos = screen_height - worktable_height

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height / 2) - (character_height / 2)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
charcter_speed = 0.6

# 상단 주문 바 만들기
orderbar = pygame.image.load(os.path.join(image_path, "orderbar.png"))
orderbar_size = orderbar.get_rect().size
orderbar_height = orderbar_size[1]
orderbar_y_pos = 0

# 주문 처리하기



# 레시피 만들기

apple_juice = ['apple', 'ice', 'sugar' , 'water'] # 사과 주스
mango_juice = ['mango', 'ice', 'sugar' , 'water'] # 망고 주스

materials = ['apple', 'mango' , 'sugar' , 'ice' ,'water']
recipes = [apple_juice, mango_juice]


# 제작 스택
buffer = [] 


# 현재 만든 제작품
num_apple = 0
num_mango = 0

maked_item = [num_apple, num_mango]


# 레시피 북 만들기
recipebook = pygame.image.load(os.path.join(image_path, "recipe_book.png"))
recipebook_size = recipebook.get_rect().size
recipebook_width = recipebook_size[0]
recipebook_height = recipebook_size[1]
recipebook_x_pos = 0
recipebook_y_pos = (screen_height / 2) - (recipebook_height / 2)


# 레시피 스크린 만들기
recipescreen = pygame.image.load(os.path.join(image_path, "recipescreen.png"))
recipescreen_size = recipescreen.get_rect().size
recipescreen_width = recipescreen_size[0]
recipescreen_height = recipescreen_size[1]
recipescreen_x_pos = (screen_width / 2) - (recipescreen_width / 2)
recipescreen_y_pos = (screen_height / 2) - (recipescreen_height / 2)


# 제작 스크린 만들기
makingscreen = pygame.image.load(os.path.join(image_path, "makingscreen.png"))
makingscreen_size = makingscreen.get_rect().size
makingscreen_width = makingscreen_size[0]
makingscreen_height = makingscreen_size[1]
makingscreen_x_pos = (screen_width / 2) - (makingscreen_width / 2)
makingscreen_y_pos = (screen_height / 2) - (makingscreen_height / 2)


# 사과주스 제작 스크린 만들기
making_apple_screen = pygame.image.load(os.path.join(image_path, "making_apple_screen.png"))
making_apple_screen_size = making_apple_screen.get_rect().size
making_apple_screen_width = making_apple_screen_size[0]
making_apple_screen_height = making_apple_screen_size[1]
making_apple_screen_x_pos = (screen_width / 2) - (making_apple_screen_width / 2)
making_apple_screen_y_pos = (screen_height / 2) - (making_apple_screen_height / 2)

# 망고주스 제작 스크린 만들기
making_mango_screen = pygame.image.load(os.path.join(image_path, "making_mango_screen.png"))
making_mango_screen_size = making_mango_screen.get_rect().size
making_mango_screen_width = making_mango_screen_size[0]
making_mango_screen_height = making_mango_screen_size[1]
making_mango_screen_x_pos = (screen_width / 2) - (making_mango_screen_width / 2)
making_mango_screen_y_pos = (screen_height / 2) - (making_mango_screen_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 30) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 15


# 게임 루프
running = True 
reading = False # 레시피 읽기

# 제작하기
making = False 
making_menu = False # 만들 레시피 고르기
making_apple = False # 사과 주스 만들기
making_mango = False # 망고 주스 만들기
delivering = False # 납품하기

while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= charcter_speed # to_X = to_x -5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += charcter_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= charcter_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += charcter_speed
            elif event.key == pygame.K_q: # 레시피, 제작 화면 나가기
                reading = False
                making = False
                buffer = []
            elif event.key == pygame.K_c: # 제작 메뉴 나가고, 사과주스 만들기
                making_menu = False
                making_apple = True
                buffer = []
            elif event.key == pygame.K_v: # 제작 메뉴 나가고, 망고주스 만들기
                making_menu = False
                making_mango = True
                buffer = []
            
            # 사과주스 만들기 키보드 이벤트
            if making_apple :
                if event.key == pygame.K_w:
                    buffer.append('apple') # 사과
                elif event.key == pygame.K_a: # 물
                    buffer.append('water')
                elif event.key == pygame.K_s: # 얼음
                    buffer.append('ice')
                elif event.key == pygame.K_d: # 설탕
                    buffer.append('sugar')
                elif event.key == pygame.K_q: # 뒤로가기
                    making_apple = False
                    making = False
                    making_menu = True

            # 망고주스 만들기 키보드 이벤트
            elif making_mango :
                if event.key == pygame.K_w:
                    buffer.append('apple') # 망고
                elif event.key == pygame.K_a: # 물
                    buffer.append('water')
                elif event.key == pygame.K_s: # 얼음
                    buffer.append('ice')
                elif event.key == pygame.K_d: # 설탕
                    buffer.append('sugar')
                elif event.key == pygame.K_q: # 뒤로가기
                    making_mango = False
                    making = False
                    making_menu = True
                
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT  or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP  or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < orderbar_height -1:
        character_y_pos = orderbar_height -1
    elif character_y_pos > screen_height - worktable_height - character_height + 1:
        character_y_pos = screen_height - worktable_height - character_height + 1

    # 4. 충돌 처리

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    orderbar_rect = orderbar.get_rect()
    orderbar_rect.top = orderbar_y_pos

    recipebook_rect = recipebook.get_rect()
    recipebook_left = recipebook_x_pos
    recipebook_rect.top = recipebook_y_pos

    worktable_rect = worktable.get_rect()
    worktable_rect.top = worktable_y_pos

    # 충돌 체크
    if character_rect.colliderect(orderbar_rect):
        print("납품합니다.")
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2) - (character_height / 2)
        delivering = True
    
    elif character_rect.colliderect(recipebook_rect):
        print("레시피를 확인합니다.")
        # 레시피 북 열기
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2) - (character_height / 2)
        reading = True
        
    elif character_rect.colliderect(worktable_rect):
        print("제작을 시작합니다.")
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2) - (character_height / 2)
        making = True
        making_menu = True
    

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(worktable, (0, screen_height - worktable_height))
    screen.blit(orderbar, (0, 0))
    screen.blit(recipebook, (0, recipebook_y_pos))
    screen.blit(character,(character_x_pos, character_y_pos))

    # 만든 제품 개수 표시
    # 사과 주스
    text_applejuice = game_font.render("apple juice : " + str(num_apple), True,(0,0,0))
    screen.blit(text_applejuice , (0 , 60))

    # 망고 주스
    text_mangojuice = game_font.render("mango juice : " + str(num_mango), True, (0,0,0))
    screen.blit(text_mangojuice , (0, 80))

    # 레시피 북 열기
    if reading :
        screen.blit(recipescreen, (recipescreen_x_pos, recipescreen_y_pos))
        
    # 제작 화면 열기
    if making :
        if making_menu :
            screen.blit(makingscreen, (makingscreen_x_pos, makingscreen_y_pos))
            
        # 사과 주스 제작 화면 
        if making_apple :
            screen.blit(making_apple_screen, (making_apple_screen_x_pos, making_apple_screen_y_pos))
                              
            #레시피 스택 표시
            text_buffer = game_font.render(str(buffer), True,(0,0,0))
            screen.blit(text_buffer, (80 , 300))
            

            # 레시피 성공하면 사과주스 +1
            if buffer == apple_juice :
                num_apple += 1
                making_apple = False
                making=False
            else :
                if len(buffer) == len(apple_juice) :
                    text_wrong = game_font.render("Try again!" ,True, (255,0,0))
                    screen.blit(text_wrong, (200, 400))      
   

        # 망고 주스 제작 화면
        elif making_mango :
            screen.blit(making_mango_screen, (making_mango_screen_x_pos, making_mango_screen_y_pos))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
                    if event.key == pygame.K_w: # 망고
                        buffer.append('mango')
                    elif event.key == pygame.K_a: # 물
                        buffer.append('water')
                    elif event.key == pygame.K_s: # 얼음
                        buffer.append('ice')
                    elif event.key == pygame.K_d: # 설탕
                        buffer.append('sugar')

            # 레시피 스택 표시
            text_buffer = game_font.render(str(buffer), True,(0,0,0))
            screen.blit(text_buffer, (80 , 300))
            pygame.display.update()

            # 레시피 성공하면 망고 주스 +1
            if buffer == mango_juice :
                num_mango += 1
                making_mango = False
                making=False
            else :
                if len(buffer) == len(mango_juice) :
                    text_wrong = game_font.render("Try again!" ,True, (255,0,0) )
                    screen.blit(text_wrong, (200, 400))     


    # 납품하기
    if delivering :
        # 타이머 집어넣기
        # 시작 시간
        start_ticks = pygame.time.get_ticks() # 현재 tick을 받아옴
        # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
        # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

        timer = game_font.render(str(int(total_time - elapsed_time)), True,(0,0,0))
        # 출력할 글자, True, 글자 색상
        screen.blit(timer,(10,10))

        # 만약 시간이 0 이하이면 게임 종료
        if total_time - elapsed_time <=0:
            print("고객이 화를 내며 떠났습니다.")
            delivering = False

    pygame.display.update()

pygame.quit()