import pygame
import random
import sys

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Number Guess Quiz')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# フォント設定
font_path = '/System/Library/Fonts/ヒラギノ明朝 ProN.ttc'
font = pygame.font.Font(font_path, 36)

# ゲーム設定
min_num = 1
max_num = 100
number_to_guess = random.randint(min_num, max_num)
guesses_taken = 0
user_text = ''
feedback_text = ''
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(user_text)
                    guesses_taken += 1
                    if guess < number_to_guess:
                        feedback_text = 'もっと高いです。'
                    elif guess > number_to_guess:
                        feedback_text = 'もっと低いです。'
                    else:
                        feedback_text = f'おめでとうございます！ {guesses_taken} 回で正解しました。'
                        game_over = True
                except ValueError:
                    feedback_text = '数字を入力してください。'
                user_text = ''
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    screen.fill(BLACK)

    text_surface = font.render(f'{min_num} - {max_num}で数を入力: ' + user_text, True, WHITE)
    feedback_surface = font.render(feedback_text, True, GREEN if game_over else RED)
    screen.blit(text_surface, (50, 100))
    screen.blit(feedback_surface, (50, 150))

    pygame.display.flip()

pygame.quit()
