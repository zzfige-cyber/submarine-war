#!/usr/bin/env python3
"""
合成完整的logo图片
将标题、闪电、英文文字等图层合成为一张图片
"""

from PIL import Image, ImageDraw, ImageFont
import os

ASSETS_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war/assets"
FIGMA_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war/.figma/image"

def create_complete_logo():
    # 创建画布 (528x345 根据设计稿)
    canvas = Image.new('RGBA', (528, 345), (0, 0, 0, 0))
    
    # 加载主标题图片
    title_img = Image.open(f"{FIGMA_DIR}/mo5mb30f-gssqlze.png")
    # 调整大小
    title_img = title_img.resize((477, 297), Image.Resampling.LANCZOS)
    
    # 粘贴标题 (位置根据设计稿: left: 20, top: 0)
    canvas.paste(title_img, (20, 0), title_img)
    
    # 绘制橙色闪电
    draw = ImageDraw.Draw(canvas)
    # 闪电路径 (根据设计稿调整)
    lightning_points = [
        (195, 149), (477, 5), (272, 148), (333, 148), 
        (0, 334), (253, 149), (195, 149)
    ]
    draw.polygon(lightning_points, fill=(255, 94, 0, 255))
    # 闪电黑色描边
    draw.line(lightning_points, fill=(0, 0, 0, 255), width=5)
    
    # 添加英文文字
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 45)
    except:
        font = ImageFont.load_default()
    
    # 绘制英文文字 (位置: left: 102, top: 276)
    draw.text((102, 276), "submarinewarfare", fill=(175, 175, 175, 255), font=font)
    
    # 保存
    canvas.save(f"{ASSETS_DIR}/logo.png")
    print("✓ logo.png 合成完成")

if __name__ == "__main__":
    create_complete_logo()
