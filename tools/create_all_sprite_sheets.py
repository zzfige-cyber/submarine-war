#!/usr/bin/env python3
"""
批量转换所有序列帧动画为精灵图
"""

import os
import sys
import json
from PIL import Image
import math

def create_sprite_sheet(input_dir, output_dir, name, pattern=None, frame_files=None):
    """
    创建精灵图
    
    Args:
        input_dir: 输入目录
        output_dir: 输出目录
        name: 输出文件名
        pattern: 文件名匹配模式（可选）
        frame_files: 指定帧文件列表（可选）
    """
    # 获取所有帧文件
    if frame_files is None:
        if pattern:
            frame_files = sorted([f for f in os.listdir(input_dir) if pattern in f and f.endswith('.png')])
        else:
            frame_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
    
    if not frame_files:
        print(f"警告: {input_dir} 中没有找到帧文件")
        return None
    
    print(f"处理 {name}: 找到 {len(frame_files)} 帧")
    
    # 加载所有帧
    frames = []
    for frame_file in frame_files:
        frame_path = os.path.join(input_dir, frame_file)
        img = Image.open(frame_path)
        frames.append((frame_file, img))
    
    # 获取帧尺寸
    frame_width = frames[0][1].width
    frame_height = frames[0][1].height
    
    # 计算网格布局
    num_frames = len(frames)
    cols = math.ceil(math.sqrt(num_frames))
    rows = math.ceil(num_frames / cols)
    
    # 创建精灵图
    sprite_sheet_width = frame_width * cols
    sprite_sheet_height = frame_height * rows
    sprite_sheet = Image.new('RGBA', (sprite_sheet_width, sprite_sheet_height), (0, 0, 0, 0))
    
    # 创建 JSON 数据
    sprite_data = {
        "frames": {},
        "meta": {
            "image": f"{name}_atlas.png",
            "size": {"w": sprite_sheet_width, "h": sprite_sheet_height}
        }
    }
    
    # 填充精灵图
    for idx, (frame_name, frame_img) in enumerate(frames):
        col = idx % cols
        row = idx // cols
        
        x = col * frame_width
        y = row * frame_height
        
        sprite_sheet.paste(frame_img, (x, y))
        
        # 添加帧数据
        sprite_data["frames"][frame_name] = {
            "frame": {"x": x, "y": y, "w": frame_width, "h": frame_height}
        }
    
    # 保存精灵图
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{name}_atlas.png")
    sprite_sheet.save(output_path, 'PNG')
    print(f"  保存精灵图: {output_path} ({sprite_sheet_width}x{sprite_sheet_height})")
    
    # 保存 JSON 数据（紧凑格式）
    json_path = os.path.join(output_dir, f"{name}_atlas_compact.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sprite_data, f, ensure_ascii=False, separators=(',', ':'))
    print(f"  保存 JSON: {json_path}")
    
    return sprite_data

def main():
    base_dir = "/Users/bytedance/Desktop/vibe coding/submarine-war"
    
    # 1. 爆炸序列帧 (10帧)
    print("\n=== 1. 爆炸序列帧 ===")
    create_sprite_sheet(
        os.path.join(base_dir, "assets/潜艇爆炸素材"),
        os.path.join(base_dir, "assets/潜艇爆炸素材"),
        "explosion",
        pattern="boom-"
    )
    
    # 2. 超级武器动态皮肤 (11帧)
    print("\n=== 2. 超级武器动态皮肤 ===")
    create_sprite_sheet(
        os.path.join(base_dir, "assets/超级武器动态皮肤"),
        os.path.join(base_dir, "assets/超级武器动态皮肤"),
        "super_weapon",
        pattern="jimeng-"
    )
    
    # 3. 导弹发射气泡特效 (4帧)
    print("\n=== 3. 导弹发射气泡特效 ===")
    create_sprite_sheet(
        os.path.join(base_dir, "assets/导弹发射-序列帧"),
        os.path.join(base_dir, "assets/导弹发射-序列帧"),
        "missile_bubble",
        pattern="导弹发射气泡-"
    )
    
    # 4. 海面浪花特效 - 白天 (13帧)
    print("\n=== 4. 海面浪花特效 - 白天 ===")
    # 按数字顺序排序
    splash_files = sorted([f for f in os.listdir(os.path.join(base_dir, "assets/海面浪花特效")) if f.endswith('.png')],
                         key=lambda x: int(x.replace('.png', '')))
    create_sprite_sheet(
        os.path.join(base_dir, "assets/海面浪花特效"),
        os.path.join(base_dir, "assets/海面浪花特效"),
        "water_splash",
        frame_files=splash_files
    )
    
    # 5. 海面浪花特效 - 夜晚 (13帧)
    print("\n=== 5. 海面浪花特效 - 夜晚 ===")
    create_sprite_sheet(
        os.path.join(base_dir, "assets/海面浪花特效-夜晚"),
        os.path.join(base_dir, "assets/海面浪花特效-夜晚"),
        "water_splash_night",
        pattern="10"
    )
    
    print("\n=== 所有精灵图创建完成! ===")

if __name__ == "__main__":
    main()
