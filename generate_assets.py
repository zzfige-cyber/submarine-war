#!/usr/bin/env python3
"""
生成像素风格游戏素材
使用简单的几何图形创建复古像素风格的精灵
"""

from PIL import Image, ImageDraw
import os

ASSETS_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war/assets"

def create_player_ship():
    """创建玩家战舰 - 蓝色科幻风格"""
    img = Image.new('RGBA', (210, 84), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 主体 - 深蓝色
    draw.rectangle([20, 30, 190, 70], fill=(42, 100, 160, 255))
    # 高光
    draw.rectangle([25, 32, 185, 40], fill=(74, 158, 255, 255))
    # 舰桥
    draw.rectangle([85, 15, 125, 35], fill=(26, 58, 92, 255))
    draw.rectangle([90, 18, 120, 28], fill=(42, 100, 160, 255))
    # 推进器
    draw.rectangle([5, 40, 20, 60], fill=(255, 107, 74, 200))
    # 细节
    draw.rectangle([40, 45, 170, 55], fill=(26, 58, 92, 255))
    
    img.save(f"{ASSETS_DIR}/player_ship.png")
    print("✓ player_ship.png")

def create_player_ship_armor():
    """创建装甲版战舰 - 灰色厚重风格"""
    img = Image.new('RGBA', (210, 84), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 主体 - 深灰色装甲
    draw.rectangle([15, 25, 195, 75], fill=(90, 100, 110, 255))
    # 装甲板
    draw.rectangle([20, 30, 190, 45], fill=(122, 138, 154, 255))
    draw.rectangle([20, 50, 190, 70], fill=(70, 80, 90, 255))
    # 舰桥
    draw.rectangle([80, 10, 130, 30], fill=(50, 60, 70, 255))
    # 装甲细节
    draw.rectangle([30, 35, 60, 65], fill=(60, 70, 80, 255))
    draw.rectangle([150, 35, 180, 65], fill=(60, 70, 80, 255))
    
    img.save(f"{ASSETS_DIR}/player_ship_armor.png")
    print("✓ player_ship_armor.png")

def create_player_ship_turbo():
    """创建高速版战舰 - 红色流线型"""
    img = Image.new('RGBA', (210, 84), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 主体 - 红色
    draw.rectangle([25, 32, 185, 68], fill=(200, 60, 40, 255))
    # 流线型高光
    draw.rectangle([30, 35, 180, 42], fill=(255, 107, 74, 255))
    # 舰桥
    draw.rectangle([90, 18, 120, 35], fill=(150, 40, 25, 255))
    # 火焰推进器
    draw.rectangle([0, 38, 25, 62], fill=(255, 150, 50, 230))
    draw.rectangle([0, 42, 15, 58], fill=(255, 200, 100, 255))
    
    img.save(f"{ASSETS_DIR}/player_ship_turbo.png")
    print("✓ player_ship_turbo.png")

def create_submarine():
    """创建敌方潜艇 - 棕色复古风格"""
    img = Image.new('RGBA', (240, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 主体 - 棕色
    draw.ellipse([10, 30, 230, 100], fill=(139, 69, 19, 255))
    # 高光
    draw.arc([15, 32, 225, 95], 200, 340, fill=(160, 82, 45, 255), width=8)
    # 潜望镜
    draw.rectangle([160, 5, 175, 40], fill=(80, 80, 80, 255))
    draw.ellipse([155, 0, 180, 15], fill=(100, 100, 100, 255))
    # 窗户
    draw.ellipse([40, 50, 70, 80], fill=(100, 200, 255, 200))
    draw.ellipse([90, 50, 120, 80], fill=(100, 200, 255, 200))
    
    img.save(f"{ASSETS_DIR}/submarine.png")
    print("✓ submarine.png")

def create_gold_submarine():
    """创建金色潜艇 - 金色稀有风格"""
    img = Image.new('RGBA', (240, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 主体 - 金色
    draw.ellipse([10, 30, 230, 100], fill=(255, 215, 0, 255))
    # 高光
    draw.arc([15, 32, 225, 95], 200, 340, fill=(255, 236, 139, 255), width=8)
    # 潜望镜
    draw.rectangle([160, 5, 175, 40], fill=(180, 150, 50, 255))
    draw.ellipse([155, 0, 180, 15], fill=(255, 236, 74, 255))
    # 宝石窗户
    draw.ellipse([40, 50, 70, 80], fill=(255, 100, 100, 230))
    draw.ellipse([90, 50, 120, 80], fill=(100, 255, 100, 230))
    # 装饰条纹
    draw.arc([20, 35, 220, 95], 45, 135, fill=(255, 180, 0, 255), width=4)
    
    img.save(f"{ASSETS_DIR}/gold_submarine.png")
    print("✓ gold_submarine.png")

def create_missile():
    """创建导弹 - 红色火箭"""
    img = Image.new('RGBA', (120, 45), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 弹体
    draw.rectangle([20, 15, 100, 35], fill=(200, 50, 50, 255))
    # 弹头
    draw.polygon([(100, 15), (120, 25), (100, 35)], fill=(150, 30, 30, 255))
    # 尾翼
    draw.polygon([(20, 15), (0, 5), (20, 25)], fill=(100, 100, 100, 255))
    draw.polygon([(20, 35), (0, 45), (20, 25)], fill=(100, 100, 100, 255))
    # 火焰
    draw.polygon([(0, 20), (-15, 25), (0, 30)], fill=(255, 150, 50, 200))
    
    img.save(f"{ASSETS_DIR}/missile.png")
    print("✓ missile.png")

def create_mine():
    """创建水雷 - 蓝色球体带引信"""
    img = Image.new('RGBA', (60, 90), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 主体球
    draw.ellipse([5, 30, 55, 80], fill=(50, 100, 200, 255))
    # 高光
    draw.ellipse([10, 35, 30, 50], fill=(100, 150, 255, 200))
    # 引信
    draw.rectangle([25, 10, 35, 35], fill=(80, 80, 80, 255))
    # 引信顶部
    draw.ellipse([22, 5, 38, 18], fill=(150, 50, 50, 255))
    # 装饰刺
    draw.polygon([(30, 30), (25, 20), (35, 20)], fill=(40, 80, 160, 255))
    
    img.save(f"{ASSETS_DIR}/mine.png")
    print("✓ mine.png")

def create_explosion():
    """创建爆炸效果 - 橙黄色火焰"""
    img = Image.new('RGBA', (240, 240), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 外圈火焰
    draw.ellipse([20, 20, 220, 220], fill=(255, 150, 50, 200))
    # 中圈
    draw.ellipse([50, 50, 190, 190], fill=(255, 200, 50, 230))
    # 内圈
    draw.ellipse([80, 80, 160, 160], fill=(255, 255, 100, 255))
    # 核心
    draw.ellipse([100, 100, 140, 140], fill=(255, 255, 255, 255))
    
    img.save(f"{ASSETS_DIR}/explosion.png")
    print("✓ explosion.png")

def create_powerup_hp():
    """创建HP道具 - 红色心形"""
    img = Image.new('RGBA', (60, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 心形
    draw.polygon([(30, 50), (5, 25), (5, 15), (15, 5), (25, 5), (30, 15), (35, 5), (45, 5), (55, 15), (55, 25)], fill=(255, 50, 50, 255))
    draw.ellipse([5, 5, 30, 30], fill=(255, 50, 50, 255))
    draw.ellipse([30, 5, 55, 30], fill=(255, 50, 50, 255))
    # 高光
    draw.ellipse([12, 12, 22, 22], fill=(255, 150, 150, 200))
    
    img.save(f"{ASSETS_DIR}/powerup_hp.png")
    print("✓ powerup_hp.png")

def create_powerup_range():
    """创建范围道具 - 绿色爆炸图标"""
    img = Image.new('RGBA', (60, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 外圈
    draw.ellipse([5, 5, 55, 55], fill=(50, 200, 50, 255))
    # 内圈
    draw.ellipse([15, 15, 45, 45], fill=(100, 255, 100, 255))
    # 中心爆炸图案
    draw.polygon([(30, 20), (35, 30), (45, 30), (38, 38), (42, 48), (30, 42), (18, 48), (22, 38), (15, 30), (25, 30)], fill=(255, 255, 100, 255))
    
    img.save(f"{ASSETS_DIR}/powerup_range.png")
    print("✓ powerup_range.png")

def create_background():
    """创建深海背景 - 渐变蓝色"""
    img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景
    for y in range(1080):
        ratio = y / 1080
        r = int(26 + (6 - 26) * ratio)
        g = int(58 + (18 - 58) * ratio)
        b = int(92 + (32 - 92) * ratio)
        draw.line([(0, y), (1920, y)], fill=(r, g, b, 255))
    
    img.save(f"{ASSETS_DIR}/background.png")
    print("✓ background.png")

def create_cockpit_frame():
    """创建座舱边框 - 科技风格"""
    img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 边框
    draw.rectangle([0, 0, 1919, 1079], outline=(42, 100, 160, 255), width=20)
    # 角落装饰
    draw.rectangle([0, 0, 100, 100], fill=(42, 100, 160, 200))
    draw.rectangle([1820, 0, 1920, 100], fill=(42, 100, 160, 200))
    draw.rectangle([0, 980, 100, 1080], fill=(42, 100, 160, 200))
    draw.rectangle([1820, 980, 1920, 1080], fill=(42, 100, 160, 200))
    # 内部线条
    draw.rectangle([30, 30, 1890, 1050], outline=(74, 158, 255, 150), width=2)
    
    img.save(f"{ASSETS_DIR}/cockpit_frame.png")
    print("✓ cockpit_frame.png")

def create_skill_buttons():
    """创建技能点按钮 - 加减号按钮（使用2倍尺寸抗锯齿）"""
    scale = 2  # 2倍超采样
    final_size = 34
    size = final_size * scale
    
    # 减号按钮 - 可点击状态（黑底 + 黄绿色图标 #d9fa05）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 圆形背景 - 黑色
    draw.ellipse([0, 0, size-1, size-1], fill=(34, 34, 34, 255))
    # 减号 - 黄绿色
    bar_width = 16 * scale
    bar_height = 4 * scale
    x1 = (size - bar_width) // 2
    y1 = (size - bar_height) // 2
    draw.rectangle([x1, y1, x1 + bar_width, y1 + bar_height], fill=(217, 250, 5, 255))
    # 缩放到目标尺寸
    img = img.resize((final_size, final_size), Image.Resampling.LANCZOS)
    img.save(f"{ASSETS_DIR}/btn_minus_enabled.png")
    print("✓ btn_minus_enabled.png")
    
    # 减号按钮 - 不可点击状态（灰底 + 灰色图标）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 圆形背景 - 灰色
    draw.ellipse([0, 0, size-1, size-1], fill=(217, 217, 217, 255))
    # 减号 - 浅灰色
    draw.rectangle([x1, y1, x1 + bar_width, y1 + bar_height], fill=(180, 180, 180, 255))
    # 缩放到目标尺寸
    img = img.resize((final_size, final_size), Image.Resampling.LANCZOS)
    img.save(f"{ASSETS_DIR}/btn_minus_disabled.png")
    print("✓ btn_minus_disabled.png")
    
    # 加号按钮 - 可点击状态（黑底 + 黄绿色图标 #d9fa05）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 圆形背景 - 黑色
    draw.ellipse([0, 0, size-1, size-1], fill=(34, 34, 34, 255))
    # 加号 - 黄绿色
    draw.rectangle([x1, y1, x1 + bar_width, y1 + bar_height], fill=(217, 250, 5, 255))
    draw.rectangle([y1, x1, y1 + bar_height, x1 + bar_width], fill=(217, 250, 5, 255))
    # 缩放到目标尺寸
    img = img.resize((final_size, final_size), Image.Resampling.LANCZOS)
    img.save(f"{ASSETS_DIR}/btn_plus_enabled.png")
    print("✓ btn_plus_enabled.png")
    
    # 加号按钮 - 不可点击状态（灰底 + 灰色图标）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 圆形背景 - 灰色
    draw.ellipse([0, 0, size-1, size-1], fill=(217, 217, 217, 255))
    # 加号 - 浅灰色
    draw.rectangle([x1, y1, x1 + bar_width, y1 + bar_height], fill=(180, 180, 180, 255))
    draw.rectangle([y1, x1, y1 + bar_height, x1 + bar_width], fill=(180, 180, 180, 255))
    # 缩放到目标尺寸
    img = img.resize((final_size, final_size), Image.Resampling.LANCZOS)
    img.save(f"{ASSETS_DIR}/btn_plus_disabled.png")
    print("✓ btn_plus_disabled.png")

if __name__ == "__main__":
    print("生成像素风格游戏素材...")
    print("-" * 40)
    
    create_player_ship()
    create_player_ship_armor()
    create_player_ship_turbo()
    create_submarine()
    create_gold_submarine()
    create_missile()
    create_mine()
    create_explosion()
    create_powerup_hp()
    create_powerup_range()
    create_background()
    create_cockpit_frame()
    create_skill_buttons()
    
    print("-" * 40)
    print("✓ 所有素材生成完成！")
