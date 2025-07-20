import os
import json
from PIL import Image

# 设置路径
image_folder = "C:\ZJK\Guochuang\minor data/bc\images"  # 你的图片目录路径
output_folder = "C:\ZJK\Guochuang\minor data/bc\output_annotations"
log_file = os.path.join(output_folder, "annotated_images.txt")

# 创建输出文件夹和日志文件
os.makedirs(output_folder, exist_ok=True)
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        pass

def get_annotated_images():
    """获取已标注的图片列表"""
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

def mark_image_as_annotated(image_file):
    """标记图片为已标注"""
    with open(log_file, 'a') as f:
        f.write(f"{image_file}\n")

# 获取所有图片和已标注图片
all_images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
annotated_images = get_annotated_images()
unannotated_images = [img for img in all_images if img not in annotated_images]

print(f"发现 {len(all_images)} 张图片，其中 {len(annotated_images)} 张已标注，{len(unannotated_images)} 张待标注")

# 遍历未标注图片进行标注
for image_file in unannotated_images:
    image_path = os.path.join(image_folder, image_file)

    # 显示图片（操作系统默认查看器）
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"无法打开图片 {image_file}: {str(e)}")
        continue

    print(f"\n标注图像: {image_file}")
    print("请依次输入下列性状信息（直接输入选项）：")

    # 获取用户输入的性状信息
    traits = {
        "外叶颜色": input("外叶颜色（黄绿色 / 浅绿色 / 中等绿色 / 深绿色 / 灰绿色）："),
        "光泽度": input("光泽度（弱 / 中 / 强）："),
        "叶缘波状程度": input("叶缘波状程度（弱 / 中 / 强）："),
        "叶缘锯齿": input("叶缘锯齿（全缘 / 圆齿 / 锯齿 / 重齿）："),
        "泡状突起大小": input("泡状突起大小（无 / 小 / 中 / 大）："),
        "泡状突起数量": input("泡状突起数量（少 / 中 / 多）："),
        "叶脉鲜明程度": input("叶脉鲜明程度（不明显 / 明显）："),
        "外叶数量": input("外叶数量（少 / 中 / 多）："),
        "外叶形状": input("外叶形状（近圆形 / 宽倒卵形 / 倒卵形 / 长倒卵形 / 长圆形）："),
        "外叶长度": input("外叶长度（短 / 中 / 长）："),
        "外叶宽度": input("外叶宽度（窄 / 中 / 宽）："),
        "中肋颜色": input("中肋颜色（白色 / 绿白色 / 浅绿色 / 绿色）："),
        "中肋长度": input("中肋长度（短 / 中 / 长）："),
        "中肋宽度": input("中肋宽度（窄 / 中 / 宽）："),
        "中肋厚度": input("中肋厚度（薄 / 中 / 厚）："),
        "叶球形状": input("叶球形状（球形 / 头球形 / 筒形 / 长筒形 / 炮弹形）："),
        "叶球高度": input("叶球高度（极矮 / 矮 / 中 / 高 / 极高）："),
        "叶球宽度": input("叶球宽度（小 / 中 / 大）："),
        "叶球类型": input("叶球类型（开放 / 半开放 / 闭合）："),
        "抱合类型": input("抱合类型（拧抱 / 合抱 / 叠抱）："),
        "顶部形状": input("顶部形状（尖 / 圆 / 平）："),
        "上部颜色": input("上部颜色（白色 / 黄色 / 绿色）："),
        "上部绿色程度": input("上部绿色程度（浅 / 中 / 深）："),
        "紧实度": input("紧实度（松 / 中 / 紧）："),
        "叶片数量": input("叶片数量（少 / 中 / 多）：")
    }

    # 构造描述段落
    description = (
        f"这是一颗大白菜，外叶呈{traits['外叶颜色']}，带有{traits['光泽度']}光泽，"
        f"叶缘波状程度{traits['叶缘波状程度']}，边缘呈现{traits['叶缘锯齿']}状。"
        f"叶面分布着{traits['泡状突起大小']}的泡状突起，数量{traits['泡状突起数量']}，"
        f"叶脉{traits['叶脉鲜明程度']}。外叶数量{traits['外叶数量']}，整体形状为{traits['外叶形状']}，"
        f"叶片长度{traits['外叶长度']}，宽度{traits['外叶宽度']}。中肋为{traits['中肋颜色']}，长度{traits['中肋长度']}，"
        f"宽度{traits['中肋宽度']}，厚度{traits['中肋厚度']}。\n\n"
        f"叶球形状为{traits['叶球形状']}，整体高度{traits['叶球高度']}，宽度{traits['叶球宽度']}，"
        f"属于{traits['叶球类型']}类型，叶片呈{traits['抱合类型']}状。顶部形状{traits['顶部形状']}，"
        f"叶球上部为{traits['上部颜色']}，绿色程度{traits['上部绿色程度']}，紧实度{traits['紧实度']}，"
        f"内部叶片数量{traits['叶片数量']}。整体来看，这颗大白菜性状协调，结构紧凑，具备良好的农艺性状。"
    )

    # 构造 conversations JSON 结构
    data = {
        "conversations": [
            {
                "role": "user",
                "value": f"描述这张图片 <|vision_start|>./images/{image_file}<|vision_end|>"
            },
            {
                "role": "assistant",
                "value": description
            }
        ]
    }

    # 保存标注为 JSON 文件
    json_filename = os.path.splitext(image_file)[0] + ".json"
    json_path = os.path.join(output_folder, json_filename)
    
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        # 标记图片为已标注
        mark_image_as_annotated(image_file)
        print(f"{image_file} 标注已成功保存到 {json_path}")
    except Exception as e:
        print(f"保存 {image_file} 的标注时出错: {str(e)}")
    finally:
        # 关闭图片文件
        img.close()

# 统计完成情况
annotated_images = get_annotated_images()
unannotated_images = [img for img in all_images if img not in annotated_images]
print(f"\n✅ 标注完成!")
print(f"总图片数: {len(all_images)}")
print(f"已标注: {len(annotated_images)}")
print(f"未标注: {len(unannotated_images)}")
if unannotated_images:
    print("未标注的图片:")
    for img in unannotated_images:
        print(f"  - {img}")