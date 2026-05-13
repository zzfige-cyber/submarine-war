#!/usr/bin/env python3
"""
Boss激光序列帧转精灵图工具
将 /assets/boss-激光动画/ 中的41帧序列帧转换为精灵图
"""

from PIL import Image
import json
import os

def create_boss_laser_atlas():
    # 序列帧目录
    frames_dir = "/Users/bytedance/Desktop/vibe coding/submarine-war/assets/boss-激光动画"
    output_dir = "/Users/bytedance/Desktop/vibe coding/submarine-war/assets/boss-激光"
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有帧文件（按顺序）
    frame_files = []
    for i in range(41):  # 00000 - 00040
        filename = f"4月28日_1_{i:05d}.png"
        filepath = os.path.join(frames_dir, filename)
        if os.path.exists(filepath):
            frame_files.append(filepath)
        else:
            print(f"警告: 文件不存在 {filename}")
    
    if not frame_files:
        print("错误: 没有找到任何帧文件")
        return
    
    print(f"找到 {len(frame_files)} 帧")
    
    # 读取第一帧获取尺寸
    first_frame = Image.open(frame_files[0])
    frame_width, frame_height = first_frame.size
    print(f"单帧尺寸: {frame_width}x{frame_height}")
    
    # 计算精灵图布局 (每行6帧，共7行)
    frames_per_row = 6
    num_rows = (len(frame_files) + frames_per_row - 1) // frames_per_row
    
    atlas_width = frame_width * frames_per_row
    atlas_height = frame_height * num_rows
    
    print(f"精灵图尺寸: {atlas_width}x{atlas_height}")
    print(f"布局: {frames_per_row}列 x {num_rows}行")
    
    # 创建精灵图
    atlas = Image.new('RGBA', (atlas_width, atlas_height), (0, 0, 0, 0))
    
    # 帧数据
    frames_data = {}
    
    # 将每帧粘贴到精灵图
    for idx, frame_path in enumerate(frame_files):
        row = idx // frames_per_row
        col = idx % frames_per_row
        
        x = col * frame_width
        y = row * frame_height
        
        frame = Image.open(frame_path)
        atlas.paste(frame, (x, y))
        
        # 记录帧数据
        frame_name = os.path.basename(frame_path)
        frames_data[frame_name] = {
            "frame": {
                "x": x,
                "y": y,
                "w": frame_width,
                "h": frame_height
            }
        }
        
        print(f"处理帧 {idx+1}/{len(frame_files)}: {frame_name} -> ({x}, {y})")
    
    # 保存精灵图
    atlas_path = os.path.join(output_dir, "boss_laser_atlas.png")
    atlas.save(atlas_path, "PNG")
    print(f"\n精灵图已保存: {atlas_path}")
    
    # 保存JSON数据
    atlas_data = {
        "frames": frames_data,
        "meta": {
            "image": "boss_laser_atlas.png",
            "size": {
                "w": atlas_width,
                "h": atlas_height
            }
        }
    }
    
    json_path = os.path.join(output_dir, "boss_laser_atlas.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(atlas_data, f, ensure_ascii=False, indent=2)
    print(f"JSON数据已保存: {json_path}")
    
    # 生成嵌入代码
    print("\n=== 嵌入代码 ===")
    print(f"// Boss激光精灵图数据直接嵌入")
    print(f"assets.bossLaserSpriteData = {json.dumps(atlas_data, ensure_ascii=False, separators=(',', ':'))};")
    print(f"console.log('Boss激光精灵图数据已嵌入');")
    
    return atlas_path, json_path

if __name__ == "__main__":
    create_boss_laser_atlas()
