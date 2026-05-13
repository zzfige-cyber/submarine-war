#!/usr/bin/env python3
"""
图片压缩工具 - 方案1：激进优化
压缩所有大文件，保持显示尺寸不变
"""

from PIL import Image
import os
import glob

def compress_image(input_path, output_path, quality=85, max_size=None):
    """
    压缩图片
    - quality: JPEG/WebP 质量 (1-100)
    - max_size: 最大尺寸限制 (宽, 高)，None表示保持原尺寸
    """
    try:
        img = Image.open(input_path)
        original_size = os.path.getsize(input_path)
        
        # 转换为 RGB 模式（去除透明通道，如果不需要的话）
        if img.mode in ('RGBA', 'LA', 'P'):
            # 保持透明通道，使用 PNG 格式
            if max_size:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            img.save(output_path, 'PNG', optimize=True)
        else:
            # 无透明通道，使用 WebP 格式获得更好压缩
            if max_size:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # 尝试 WebP 格式
            webp_path = output_path.replace('.png', '.webp')
            img.save(webp_path, 'WEBP', quality=quality, method=6)
            
            # 如果 WebP 更小，使用 WebP
            webp_size = os.path.getsize(webp_path)
            
            # 也保存压缩后的 PNG 作为后备
            img.save(output_path, 'PNG', optimize=True)
            png_size = os.path.getsize(output_path)
            
            if webp_size < png_size:
                return webp_path, original_size, webp_size
            else:
                os.remove(webp_path)
                return output_path, original_size, png_size
        
        new_size = os.path.getsize(output_path)
        return output_path, original_size, new_size
    except Exception as e:
        print(f"错误: {input_path} - {e}")
        return None, 0, 0

def compress_sprite_atlas(input_path, output_dir, quality=75):
    """压缩精灵图，保持尺寸不变"""
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_compressed{ext}")
    
    return compress_image(input_path, output_path, quality=quality)

def main():
    base_dir = "/Users/bytedance/Desktop/vibe coding/submarine-war/assets"
    
    # 需要压缩的大文件列表
    files_to_compress = [
        # 超大文件
        ("超级武器动态皮肤/super_weapon_atlas.png", 75),
        ("boss-激光/boss_laser_atlas.png", 75),
        ("导弹尾焰动画/精灵图测试/atlas (1).png", 75),
        
        # 大背景图
        ("figma_image/screenshot_470_6.png", 85),
        ("figma_image/screenshot_470_11.png", 85),
        ("figma_image/screenshot_470_25.png", 85),
        ("figma_image/screenshot_259_1523.png", 85),
        ("figma_image/screenshot_331_247.png", 85),
        ("figma_image/screenshot_571_3.png", 85),
        ("skill_bg.png", 80),
        
        # 中等文件
        ("figma_image/screenshot_211_477.png", 85),
        ("figma_image/screenshot_474_216.png", 85),
        ("figma_image/screenshot_513_177.png", 85),
        ("figma_image/screenshot_508_118.png", 85),
        ("figma_image/screenshot_254_1433.png", 85),
        ("figma_image/screenshot_261_1545.png", 85),
        ("figma_image/screenshot_254_1370.png", 85),
        ("figma_image/screenshot_605_123.png", 85),
        ("figma_image/screenshot_512_165.png", 85),
        ("figma_image/screenshot_618_158.png", 85),
    ]
    
    total_original = 0
    total_compressed = 0
    
    print("=" * 60)
    print("开始压缩图片资源...")
    print("=" * 60)
    
    for rel_path, quality in files_to_compress:
        input_path = os.path.join(base_dir, rel_path)
        if not os.path.exists(input_path):
            print(f"跳过 (不存在): {rel_path}")
            continue
        
        output_dir = os.path.dirname(input_path)
        result = compress_sprite_atlas(input_path, output_dir, quality)
        
        if result[0]:
            output_path, orig_size, new_size = result
            ratio = (1 - new_size / orig_size) * 100
            total_original += orig_size
            total_compressed += new_size
            
            print(f"✓ {rel_path}")
            print(f"  原始: {orig_size/1024/1024:.2f}MB → 压缩: {new_size/1024/1024:.2f}MB (节省 {ratio:.1f}%)")
    
    print("=" * 60)
    print("压缩完成!")
    print(f"总原始大小: {total_original/1024/1024:.2f}MB")
    print(f"总压缩大小: {total_compressed/1024/1024:.2f}MB")
    print(f"总节省: {(1 - total_compressed/total_original)*100:.1f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()
