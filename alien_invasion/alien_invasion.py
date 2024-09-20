import sys 
from time import sleep
import pygame 
from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

#管理游戏资源和⾏为的类
class AlienInvasion:       
    
    #初始化游戏并创建游戏资源
    def __init__(self):   
        pygame.init()                                      #初始化背景，让pygame可以正常工作
        self.clock = pygame.time.Clock()                   #创建一个Clock实例
        self.settings = Settings()                         #创建一个Settings实例
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")       #窗口大小和名字的调整
        self.stats = GameStats(self)                       #创建一个GameStats实例
        self.ship = Ship(self)                             #创建一个Ship实例
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()                               #创造外星人舰队
        #让游戏在⼀开始处于非活动状态                           
        self.game_active = False
        self.play_button = Button(self, "Play")            #创建Play按钮

    #开始游戏的主循环 
    def run_game(self):    
        while True:                          
            self._check_events()                #响应按键和⿏标事件
            if self.game_active: 
                self.ship.update()                  #更新飞船位置
                self._update_bullets()              #更新子弹位置    
                self._update_aliens()               #更新外星人位置
            self._update_screen()               #更新屏幕上的图像，并切换到新屏幕
            self.clock.tick(90)                #tick()⽅法接受⼀个参数：游戏的帧率，这⾥使⽤的值为60


    def _check_events(self):  
        #响应按键和⿏标事件              
        for event in pygame.event.get():        #使⽤pygame.event.get() 函数来访问Pygame检测到的事件
                if event.type == pygame.QUIT:   #检测玩家点击了关闭键
                   sys.exit()                   #退出游戏                
                elif event.type == pygame.KEYDOWN: 
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos() 
                    self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        #在玩家单击Play按钮时开始新游戏
        if self.play_button.rect.collidepoint(mouse_pos): 
            self.game_active = True
    

    def _check_keydown_events(self,event):
        #响应按下
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet() 
        if event.key == pygame.K_q:
            sys.exit()
    

    def _check_keyup_events(self,event): 
        #响应释放
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
         #限制子弹数量
        #if len(self.bullets) < self.settings.bullets_allowed:
            #创建新⼦弹，并将其加⼊编组bullets
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    

    def _update_bullets(self): 
        self.bullets.update()
        #删除超出窗口的子弹
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet) 
        self._check_bullet_alien_collisions()
        #print(len(self.bullets))        
    

    def _create_alien(self, x_position,y_position): 
        #创建⼀个外星⼈并将其放在当前⾏中
        new_alien = Alien(self) 
        new_alien.x = x_position 
        new_alien.y = y_position 
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)
    

    def _create_fleet(self):
        #创建⼀个外星舰队
        #外星⼈的间距为外星⼈的宽度和高度
        alien = Alien(self) 
        alien_width = alien.rect.width 
        alien_height = alien.rect.height        
        current_x = alien_width 
        current_y = alien_height
        #嵌套循环生成多行舰队
        while current_y < (self.settings.screen_height -4*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y) 
                current_x += 2 * alien_width
            #添加⼀⾏外星⼈后，重置x值并递增y值
            current_x = alien_width 
            current_y += 2 * alien_height     
    

    def _check_fleet_edges(self): 
        #在有外星⼈到达边缘时采取相应的措施
        for alien in self.aliens.sprites(): 
            if alien.check_edges(): 
                self._change_fleet_direction() 
                break
    

    def _change_fleet_direction(self): 
        #将整个外星舰队向下移动，并改变它们的⽅向
        for alien in self.aliens.sprites(): 
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1
    

    def _update_aliens(self): 
        #检查是否有外星⼈位于屏幕边缘，并更新整个外星舰队的位置
        self._check_fleet_edges()
        self.aliens.update()
        #检测外星⼈和⻜船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens): 
            self._ship_hit()
        #检查是否有外星⼈到达了屏幕的下边缘
        self._check_aliens_bottom()


    def _check_bullet_alien_collisions(self):
        #检查是否有⼦弹击中了外星⼈
        #如果是，就删除相应的⼦弹和外星⼈
        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True)
        #删除现有的⼦弹并创建⼀个新的外星舰队
        if not self.aliens: 
            self.bullets.empty() 
            self._create_fleet()
    

    def _ship_hit(self): 
        #响应⻜船和外星⼈的碰撞
        if self.stats.ships_left > 0:
            #将ships_left减1 
            self.stats.ships_left -= 1  
            #清空外星⼈列表和⼦弹列表
            self.bullets.empty() 
            self.aliens.empty() 
            #创建⼀个新的外星舰队，并将⻜船放在屏幕底部的中央
            self._create_fleet() 
            self.ship.center_ship() 
            sleep(0.5)
        else :
            self.game_active = False     
    
    
    def _check_aliens_bottom(self): 
        #检查是否有外星⼈到达了屏幕的下边缘
        for alien in self.aliens.sprites(): 
            if alien.rect.bottom >= self.settings.screen_height: 
                #像⻜船被撞到⼀样进⾏处理
                self._ship_hit() 
                break


    def _update_screen(self):                       #更新屏幕上的图像，并切换到新屏幕
        self.screen.fill(self.settings.bg_color)    #每次循环设定的背景色都填充屏幕
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet() 
        self.aliens.draw(self.screen)               #显示外星人
        self.ship.blitme()                          #在指定位置绘制⻜船 
        #如果游戏处于⾮活动状态，就绘制Play按钮
        if not self.game_active: 
            self.play_button.draw_button()
        pygame.display.flip()                       #让最近绘制的屏幕可⻅



# 创建游戏实例并运⾏游戏
if __name__ == '__main__':
    ai = AlienInvasion() 
    ai.run_game()
