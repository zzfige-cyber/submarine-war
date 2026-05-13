#!/usr/bin/env python3
"""
激进压缩方案 - 尽量压缩图片体积但不改变游戏内显示尺寸
使用WebP格式 + 较低质量 + 尺寸优化
"""

import os
import json
from PIL import Image
import shutil

# 配置 - 激进压缩参数
CONFIG = {
    'webp_quality': 60,  # 降低质量到60 (原来75)
    'webp_method': 6,    # 最大压缩 effort
    'png_compress_level': 9,  # 最高PNG压缩
    'max_dimension': None,  # 不限制最大尺寸，保持原尺寸
}

# 项目根目录
BASE_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def get_display_size(filename):
    """
    获取游戏内实际显示尺寸
    根据文件名返回对应的显示尺寸
    """
    name_lower = filename.lower()
    
    # Boss激光 - 游戏内显示608x1080
    if 'boss' in name_lower and 'laser' in name_lower:
        return (608, 1080)
    
    # 超级武器 - 根据游戏代码估算
    if 'super' in name_lower and 'weapon' in name_lower:
        return (400, 400)  # 估算值
    
    # 导弹尾焰 - 根据游戏代码
    if 'missile' in name_lower and 'tail' in name_lower:
        return (100, 200)  # 估算值
    
    # 爆炸效果
    if 'explosion' in name_lower:
        return (200, 200)
    
    # 水花效果
    if 'splash' in name_lower or 'bubble' in name_lower:
        return (150, 150)
    
    # 背景图保持原尺寸
    if 'bg' in name_lower or 'background' in name_lower:
        return None
    
    return None

def compress_image(input_path, output_path, filename):
    """
    压缩单张图片，保持显示尺寸不变
    """
    try:
        with Image.open(input_path) as img:
            original_size = os.path.getsize(input_path)
            original_mode = img.mode
            original_size_dim = img.size
            
            # 转换为RGB/RGBA（WebP需要）
            if img.mode in ('RGBA', 'P'):
                if img.mode == 'P':
                    img = img.convert('RGBA')
                has_alpha = True
            else:
                img = img.convert('RGB')
                has_alpha = False
            
            # 获取目标显示尺寸（但这里我们不改变尺寸，只压缩质量）
            display_size = get_display_size(filename)
            
            # 策略1: 优先使用WebP格式（最佳压缩比）
            webp_path = output_path.rsplit('.', 1)[0] + '.webp'
            
            if has_alpha:
                img.save(webp_path, 'WEBP', 
                        quality=CONFIG['webp_quality'], 
                        method=CONFIG['webp_method'],
                        lossless=False)
            else:
                img.save(webp_path, 'WEBP', 
                        quality=CONFIG['webp_quality'], 
                        method=CONFIG['webp_method'],
                        lossless=False)
            
            webp_size = os.path.getsize(webp_path)
            
            # 策略2: 同时尝试优化PNG（某些情况PNG可能更小）
            if has_alpha:
                png_path = output_path.rsplit('.', 1)[0] + '_opt.png'
                img.save(png_path, 'PNG', compress_level=CONFIG['png_compress_level'])
                png_size = os.path.getsize(png_path)
                
                # 选择更小的格式
                if png_size < webp_size:
                    os.remove(webp_path)
                    shutil.move(png_path, output_path)
                    final_size = png_size
                    format_used = 'PNG'
                else:
                    os.remove(png_path)
                    shutil.move(webp_path, output_path)
                    final_size = webp_size
                    format_used = 'WebP'
            else:
                # 无透明通道，WebP通常更好
                shutil.move(webp_path, output_path)
                final_size = webp_size
                format_used = 'WebP'
            
            savings = original_size - final_size
            savings_pct = (savings / original_size) * 100 if original_size > 0 else 0
            
            return {
                'success': True,
                'original_size': original_size,
                'final_size': final_size,
                'savings': savings,
                'savings_pct': savings_pct,
                'format': format_used,
                'original_dim': original_size_dim,
                'mode': original_mode
            }
            
    except Exception as e:
        return {'success': False, 'error': str(e)}

def find_large_images():
    """找出所有需要压缩的图片"""
    images = []
    
    for root, dirs, files in os.walk(ASSETS_DIR):
        # 跳过原始序列帧文件夹
        if '序列帧' in root or '序列帧-夜晚' in root:
            continue
        if 'boss-激光动画' in root:
            continue
            
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                # 跳过已经压缩过的
                if '_compressed' in file or '_opt' in file:
                    continue
                    
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath)
                
                # 只处理大于100KB的文件
                if size > 100 * 1024:
                    images.append({
                        'path': filepath,
                        'filename': file,
                        'size': size,
                        'size_mb': size / (1024 * 1024)
                    })
    
    # 按大小排序
    images.sort(key=lambda x: x['size'], reverse=True)
    return images

def main():
    print("=" * 70)
    print("激进图片压缩方案")
    print("策略: WebP质量60 + 最大压缩 effort")
    print("=" * 70)
    
    # 找出大文件
    images = find_large_images()
    
    if not images:
        print("没有找到需要压缩的图片")
        return
    
    print(f"\n找到 {len(images)} 个需要压缩的图片文件:\n")
    
    total_original = 0
    total_final = 0
    results = []
    
    for idx, img_info in enumerate(images, 1):
        print(f"[{idx}/{len(images)}] 处理: {img_info['filename']}")
        print(f"    路径: {img_info['path']}")
        print(f"    原始大小: {img_info['size_mb']:.2f} MB")
        
        # 生成输出路径
        base, ext = os.path.splitext(img_info['path'])
        output_path = base + '_compressed.webp'
        
        # 压缩
        result = compress_image(img_info['path'], output_path, img_info['filename'])
        
        if result['success']:
            total_original += result['original_size']
            total_final += result['final_size']
            
            print(f"    压缩后: {result['final_size']/1024/1024:.2f} MB")
            print(f"    节省: {result['savings']/1024/1024:.2f} MB ({result['savings_pct']:.1f}%)")
            print(f"    格式: {result['format']}")
            print(f"    尺寸: {result['original_dim']}")
            
            results.append({
                'original': img_info['path'],
                'compressed': output_path,
                'result': result
            })
        else:
            print(f"    压缩失败: {result['error']}")
        
        print()
    
    # 汇总
    print("=" * 70)
    print("压缩汇总")
    print("=" * 70)
    print(f"原始总大小: {total_original/1024/1024:.2f} MB")
    print(f"压缩后总大小: {total_final/1024/1024:.2f} MB")
    print(f"总节省: {(total_original-total_final)/1024/1024:.2f} MB")
    print(f"压缩率: {((total_original-total_final)/total_original)*100:.1f}%")
    print("=" * 70)
    
    # 保存结果报告
    report = {
        'config': CONFIG,
        'summary': {
            'total_original_mb': total_original / (1024 * 1024),
            'total_final_mb': total_final / (1024 * 1024),
            'total_savings_mb': (total_original - total_final) / (1024 * 1024),
            'savings_percentage': ((total_original - total_final) / total_original) * 100 if total_original > 0 else 0
        },
        'files': results
    }
    
    report_path = os.path.join(BASE_DIR, 'tools', 'compression_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n详细报告已保存到: {report_path}")
    
    # 输出替换建议
    print("\n" + "=" * 70)
    print("替换建议（在game.html中替换以下路径）:")
    print("=" * 70)
    for r in results:
        orig = r['original'].replace(BASE_DIR + '/', '')
        comp = r['compressed'].replace(BASE_DIR + '/', '')
        print(f"  {orig}")
        print(f"    → {comp}")
        print()

if __name__ == '__main__':
    main()
