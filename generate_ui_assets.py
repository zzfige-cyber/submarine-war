#!/usr/bin/env python3
"""生成技能配置界面所需的UI素材"""

from PIL import Image, ImageDraw
import os

def create_circle_button(size, color, border_color=None, border_width=0):
    """创建圆形按钮"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制圆形背景
    draw.ellipse([0, 0, size-1, size-1], fill=color)
    
    # 绘制边框
    if border_color and border_width > 0:
        draw.ellipse([0, 0, size-1, size-1], outline=border_color, width=border_width)
    
    return img

def create_minus_button(enabled=True):
    """创建减号按钮"""
    size = 34
    if enabled:
        # 可用状态：灰色背景
        bg_color = (217, 217, 217, 255)  # #d9d9d9
        minus_color = (34, 34, 34, 255)  # #222222
    else:
        # 不可用状态：更浅的灰色
        bg_color = (217, 217, 217, 255)
        minus_color = (153, 153, 153, 255)  # #999999
    
    img = create_circle_button(size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # 绘制减号
    line_y = size // 2
    line_padding = 10
    draw.line([(line_padding, line_y), (size - line_padding, line_y)], 
              fill=minus_color, width=3)
    
    return img

def create_plus_button(enabled=True):
    """创建加号按钮"""
    size = 34
    if enabled:
        # 可用状态：亮绿色背景
        bg_color = (217, 250, 5, 255)  # #d9fa05
        plus_color = (34, 34, 34, 255)  # #222222
    else:
        # 不可用状态：灰色背景
        bg_color = (217, 217, 217, 255)  # #d9d9d9
        plus_color = (153, 153, 153, 255)  # #999999
    
    img = create_circle_button(size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # 绘制加号
    center = size // 2
    line_padding = 9
    line_width = 3
    
    # 水平线
    draw.line([(line_padding, center), (size - line_padding, center)], 
              fill=plus_color, width=line_width)
    # 垂直线
    draw.line([(center, line_padding), (center, size - line_padding)], 
              fill=plus_color, width=line_width)
    
    return img

def create_skill_bg():
    """创建技能配置界面背景"""
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), (239, 239, 239))  # #efefef
    draw = ImageDraw.Draw(img)
    
    # 绘制蓝色海洋区域（右侧）
    ocean_color = (0, 150, 220)  # 海洋蓝
    
    # 绘制波浪形状的海岸线
    points = []
    # 左上角开始
    points.append((0, 0))
    points.append((800, 0))
    # 波浪曲线
    for x in range(800, 1000, 20):
        y = 100 + int(50 * ((x - 800) / 200))
        points.append((x, y))
    points.append((1100, 200))
    points.append((width, 200))
    points.append((width, height))
    points.append((0, height))
    
    draw.polygon(points, fill=ocean_color)
    
    # 绘制深蓝色的海水下半部分
    deep_ocean_color = (0, 100, 180)
    draw.rectangle([0, height//2, width, height], fill=deep_ocean_color)
    
    return img

def main():
    assets_dir = '/Users/bytedance/Desktop/vibe coding/submarine-war/assets'
    
    # 生成按钮素材
    create_minus_button(enabled=False).save(os.path.join(assets_dir, 'btn_minus_disabled.png'))
    create_minus_button(enabled=True).save(os.path.join(assets_dir, 'btn_minus_enabled.png'))
    create_plus_button(enabled=False).save(os.path.join(assets_dir, 'btn_plus_disabled.png'))
    create_plus_button(enabled=True).save(os.path.join(assets_dir, 'btn_plus_enabled.png'))
    
    # 生成背景
    create_skill_bg().save(os.path.join(assets_dir, 'skill_bg.png'))
    
    print("UI素材生成完成！")

if __name__ == '__main__':
    main()
