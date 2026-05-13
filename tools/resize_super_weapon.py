#!/usr/bin/env python3
"""
压缩超级武器精灵图分辨率
保持游戏内显示尺寸不变（通过缩放实现）
"""

from PIL import Image
import json
import os

BASE_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 原始文件
original_path = os.path.join(ASSETS_DIR, "超级武器动态皮肤", "super_weapon_atlas.png")
# 输出文件
output_path = os.path.join(ASSETS_DIR, "超级武器动态皮肤", "super_weapon_atlas_resized.webp")

# 目标尺寸：将8824x2838压缩到约50%（4412x1419）
# 这样可以大幅减少文件大小，同时保持显示质量
TARGET_WIDTH = 4412
TARGET_HEIGHT = 1419

def resize_sprite_sheet():
    """压缩精灵图分辨率"""
    print("=" * 60)
    print("超级武器精灵图分辨率压缩")
    print("=" * 60)
    
    with Image.open(original_path) as img:
        original_size = os.path.getsize(original_path)
        original_dim = img.size
        
        print(f"\n原始尺寸: {original_dim[0]}x{original_dim[1]}")
        print(f"原始大小: {original_size / 1024 / 1024:.2f} MB")
        
        # 计算缩放比例
        scale = TARGET_WIDTH / original_dim[0]
        new_width = TARGET_WIDTH
        new_height = int(original_dim[1] * scale)
        
        print(f"\n目标尺寸: {new_width}x{new_height}")
        print(f"缩放比例: {scale:.2%}")
        
        # 使用LANCZOS重采样算法进行高质量缩放
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # 保存为WebP格式，质量70
        resized_img.save(output_path, 'WEBP', quality=70, method=6)
        
        new_size = os.path.getsize(output_path)
        print(f"\n压缩后大小: {new_size / 1024 / 1024:.2f} MB")
        print(f"节省空间: {(original_size - new_size) / 1024 / 1024:.2f} MB")
        print(f"压缩率: {(1 - new_size/original_size) * 100:.1f}%")
        
        return scale

def update_sprite_data(scale):
    """更新精灵图数据中的帧坐标"""
    print("\n" + "=" * 60)
    print("更新精灵图数据坐标")
    print("=" * 60)
    
    # 原始JSON数据
    original_data = {
        "frames": {
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00000.png":
                {"frame": {"x": 0, "y": 0, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00001.png":
                {"frame": {"x": 2206, "y": 0, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00002.png":
                {"frame": {"x": 4412, "y": 0, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00003.png":
                {"frame": {"x": 6618, "y": 0, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00004.png":
                {"frame": {"x": 0, "y": 946, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00005.png":
                {"frame": {"x": 2206, "y": 946, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00006.png":
                {"frame": {"x": 4412, "y": 946, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00007.png":
                {"frame": {"x": 6618, "y": 946, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00008.png":
                {"frame": {"x": 0, "y": 1892, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00009.png":
                {"frame": {"x": 2206, "y": 1892, "w": 2206, "h": 946}},
            "jimeng-2026-04-25-4892-二次元动画风格，少女喊出fire，少女的头发随风飘动，背景有漫画感的速度线条移动_00010.png":
                {"frame": {"x": 4412, "y": 1892, "w": 2206, "h": 946}},
        },
        "meta": {
            "image": "super_weapon_atlas_resized.webp",
            "size": {"w": TARGET_WIDTH, "h": TARGET_HEIGHT}
        }
    }
    
    # 更新所有坐标
    for key in original_data["frames"]:
        frame = original_data["frames"][key]["frame"]
        frame["x"] = int(frame["x"] * scale)
        frame["y"] = int(frame["y"] * scale)
        frame["w"] = int(frame["w"] * scale)
        frame["h"] = int(frame["h"] * scale)
    
    # 更新meta尺寸
    original_data["meta"]["size"]["w"] = TARGET_WIDTH
    original_data["meta"]["size"]["h"] = TARGET_HEIGHT
    
    # 输出新的JSON（用于手动更新game.html）
    print("\n更新后的精灵图数据（请复制到game.html中）:")
    print("-" * 60)
    print(json.dumps(original_data, ensure_ascii=False))
    print("-" * 60)
    
    return original_data

if __name__ == '__main__':
    scale = resize_sprite_sheet()
    update_sprite_data(scale)
    
    print("\n" + "=" * 60)
    print("完成！")
    print(f"新文件: {output_path}")
    print("请更新game.html中的superWeaponSprite路径和superWeaponSpriteData数据")
    print("=" * 60)
