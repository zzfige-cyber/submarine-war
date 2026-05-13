#!/usr/bin/env python3
"""
将序列帧合并成精灵图 (Sprite Sheet)
"""

import os
import json
import math
from PIL import Image

def create_sprite_sheet(input_dir, output_name, max_width=4096):
    """
    将目录中的PNG序列帧合并成精灵图
    
    Args:
        input_dir: 输入目录路径
        output_name: 输出文件名（不含扩展名）
        max_width: 精灵图最大宽度
    """
    # 获取所有PNG文件并排序
    files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
    if not files:
        print(f"错误: 在 {input_dir} 中没有找到PNG文件")
        return
    
    print(f"找到 {len(files)} 帧")
    
    # 加载第一帧获取尺寸
    first_frame = Image.open(os.path.join(input_dir, files[0]))
    frame_width, frame_height = first_frame.size
    print(f"单帧尺寸: {frame_width}x{frame_height}")
    
    # 计算精灵图布局
    num_frames = len(files)
    frames_per_row = min(num_frames, max_width // frame_width)
    num_rows = math.ceil(num_frames / frames_per_row)
    
    sheet_width = frames_per_row * frame_width
    sheet_height = num_rows * frame_height
    
    print(f"精灵图尺寸: {sheet_width}x{sheet_height}")
    print(f"布局: {frames_per_row}列 x {num_rows}行")
    
    # 创建精灵图
    sprite_sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))
    
    # 帧数据
    frames_data = {}
    
    for idx, filename in enumerate(files):
        # 计算位置
        row = idx // frames_per_row
        col = idx % frames_per_row
        x = col * frame_width
        y = row * frame_height
        
        # 粘贴帧
        frame_path = os.path.join(input_dir, filename)
        frame = Image.open(frame_path)
        sprite_sheet.paste(frame, (x, y))
        
        # 记录帧数据
        frame_name = os.path.splitext(filename)[0]
        frames_data[frame_name] = {
            "frame": {
                "x": x,
                "y": y,
                "w": frame_width,
                "h": frame_height
            },
            "rotated": False,
            "trimmed": False,
            "spriteSourceSize": {
                "x": 0,
                "y": 0,
                "w": frame_width,
                "h": frame_height
            },
            "sourceSize": {
                "w": frame_width,
                "h": frame_height
            }
        }
    
    # 保存精灵图
    output_dir = input_dir
    sheet_path = os.path.join(output_dir, f"{output_name}.png")
    sprite_sheet.save(sheet_path, 'PNG')
    print(f"✓ 精灵图已保存: {sheet_path}")
    
    # 生成JSON数据
    json_data = {
        "frames": frames_data,
        "meta": {
            "image": f"{output_name}.png",
            "size": {
                "w": sheet_width,
                "h": sheet_height
            },
            "scale": 1
        }
    }
    
    json_path = os.path.join(output_dir, f"{output_name}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"✓ JSON数据已保存: {json_path}")
    
    # 计算节省的HTTP请求数
    original_size = sum(os.path.getsize(os.path.join(input_dir, f)) for f in files)
    new_size = os.path.getsize(sheet_path)
    print(f"\n优化效果:")
    print(f"  - 原文件数: {num_frames}")
    print(f"  - 新文件数: 2 (精灵图 + JSON)")
    print(f"  - 节省HTTP请求: {num_frames - 2} 次")
    print(f"  - 原总大小: {original_size / 1024:.1f} KB")
    print(f"  - 新大小: {new_size / 1024:.1f} KB")

if __name__ == "__main__":
    # Boss激光序列帧
    create_sprite_sheet(
        input_dir="/Users/bytedance/Desktop/vibe coding/submarine-war/assets/boss-激光",
        output_name="boss_laser_atlas",
        max_width=4096
    )
