#!/usr/bin/env python3
"""
压缩Boss激光精灵图分辨率到50%
保持游戏内显示尺寸608x1080不变
"""

from PIL import Image
import json
import os

BASE_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 使用原始PNG文件进行压缩（质量更好）
original_path = os.path.join(ASSETS_DIR, "boss-激光", "boss_laser_atlas.png")
output_path = os.path.join(ASSETS_DIR, "boss-激光", "boss_laser_atlas_resized.webp")

def resize_sprite_sheet():
    """压缩精灵图分辨率到50%"""
    print("=" * 60)
    print("Boss激光精灵图分辨率压缩")
    print("=" * 60)
    
    with Image.open(original_path) as img:
        original_size = os.path.getsize(original_path)
        original_dim = img.size
        
        print(f"\n原始尺寸: {original_dim[0]}x{original_dim[1]}")
        print(f"原始大小: {original_size / 1024 / 1024:.2f} MB")
        
        # 计算50%缩放后的尺寸
        new_width = original_dim[0] // 2
        new_height = original_dim[1] // 2
        scale = 0.5
        
        print(f"\n目标尺寸: {new_width}x{new_height}")
        print(f"缩放比例: {scale:.0%}")
        print(f"单帧尺寸: {608//2}x{1080//2} (304x540)")
        
        # 使用LANCZOS重采样算法进行高质量缩放
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # 保存为WebP格式，质量75
        resized_img.save(output_path, 'WEBP', quality=75, method=6)
        
        new_size = os.path.getsize(output_path)
        print(f"\n压缩后大小: {new_size / 1024 / 1024:.2f} MB")
        print(f"节省空间: {(original_size - new_size) / 1024 / 1024:.2f} MB")
        print(f"压缩率: {(1 - new_size/original_size) * 100:.1f}%")
        
        return scale

def generate_new_sprite_data(scale):
    """生成新的精灵图数据（坐标都乘以scale）"""
    print("\n" + "=" * 60)
    print("生成新的精灵图数据")
    print("=" * 60)
    
    # 原始帧数据（从game.html中提取的）
    frames_data = {}
    frame_width = 608
    frame_height = 1080
    cols = 6  # 每行6帧
    
    for i in range(41):  # 0-40共41帧
        frame_num = f"{i:05d}"
        filename = f"4月28日_1_{frame_num}.png"
        
        row = i // cols
        col = i % cols
        
        x = col * frame_width
        y = row * frame_height
        
        frames_data[filename] = {
            "frame": {
                "x": int(x * scale),
                "y": int(y * scale),
                "w": int(frame_width * scale),
                "h": int(frame_height * scale)
            }
        }
    
    new_data = {
        "frames": frames_data,
        "meta": {
            "image": "boss_laser_atlas_resized.webp",
            "size": {
                "w": int(3648 * scale),
                "h": int(7560 * scale)
            }
        }
    }
    
    # 输出JSON字符串（用于复制到game.html）
    json_str = json.dumps(new_data, ensure_ascii=False, separators=(',', ':'))
    
    print("\n更新后的精灵图数据（请复制到game.html中）:")
    print("-" * 60)
    print(f"assets.bossLaserSpriteData = {json_str};")
    print("-" * 60)
    
    return new_data

if __name__ == '__main__':
    scale = resize_sprite_sheet()
    generate_new_sprite_data(scale)
    
    print("\n" + "=" * 60)
    print("完成！")
    print(f"新文件: {output_path}")
    print("请更新game.html中的bossLaserSprite路径和bossLaserSpriteData数据")
    print("=" * 60)
