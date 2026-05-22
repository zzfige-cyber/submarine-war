#!/usr/bin/env python3
"""
批量转换 figma_image/ 目录中的 PNG 图片为 WebP 格式
"""
import os
from PIL import Image
import sys

def convert_png_to_webp(input_path, output_path, quality=80):
    """
    将 PNG 图片转换为 WebP 格式
    """
    try:
        img = Image.open(input_path)
        
        # 如果是透明图片，保持透明度
        if img.mode in ('RGBA', 'LA'):
            img.save(output_path, 'WEBP', quality=quality, method=6)
        else:
            img.save(output_path, 'WEBP', quality=quality, method=6)
            
        return True
    except Exception as e:
        print(f"转换失败 {input_path}: {e}")
        return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    figma_dir = os.path.join(script_dir, '..', 'assets', 'figma_image')
    
    if not os.path.exists(figma_dir):
        print(f"目录不存在: {figma_dir}")
        return
    
    print(f"开始转换目录: {figma_dir}")
    print("-" * 60)
    
    total_size_before = 0
    total_size_after = 0
    converted_count = 0
    skipped_count = 0
    
    for filename in os.listdir(figma_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(figma_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(figma_dir, output_filename)
            
            # 检查是否已经存在 WebP 文件
            if os.path.exists(output_path):
                print(f"跳过已存在: {output_filename}")
                skipped_count += 1
                continue
            
            # 转换图片
            size_before = os.path.getsize(input_path)
            total_size_before += size_before
            
            if convert_png_to_webp(input_path, output_path, quality=80):
                size_after = os.path.getsize(output_path)
                total_size_after += size_after
                
                compression = (1 - size_after / size_before) * 100
                print(f"转换成功: {filename:50} "
                      f"{size_before/1024:7.1f}KB -> {size_after/1024:7.1f}KB "
                      f"(-{compression:.1f}%)")
                converted_count += 1
            else:
                skipped_count += 1
    
    print("-" * 60)
    print(f"转换完成:")
    print(f"  成功转换: {converted_count} 个文件")
    print(f"  跳过: {skipped_count} 个文件")
    print(f"  原始大小: {total_size_before/1024/1024:.2f}MB")
    print(f"  WebP大小: {total_size_after/1024/1024:.2f}MB")
    
    if total_size_before > 0:
        savings = (1 - total_size_after / total_size_before) * 100
        print(f"  节省空间: {savings:.1f}%")

if __name__ == "__main__":
    main()
