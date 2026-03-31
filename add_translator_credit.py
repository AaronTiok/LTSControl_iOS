import json

# 读取文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 更新中文版权信息，添加翻译人员信息
key = "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, Deutschland, info@lts-design.com"

if key in data['strings']:
    value = data['strings'][key]
    
    # 更新中文翻译，添加翻译人员信息
    if 'localizations' in value and 'zh-Hans' in value['localizations']:
        old_value = value['localizations']['zh-Hans']['stringUnit']['value']
        new_value = old_value + "\n翻译：抖音 十月工坊 Aarontiok"
        
        value['localizations']['zh-Hans']['stringUnit']['value'] = new_value
        
        print("✓ 已更新中文版权信息:")
        print(f"  原文：{old_value}")
        print(f"  新译：{new_value}")
    else:
        print("✗ 未找到中文翻译")
else:
    print("✗ 未找到版权信息键")

# 保存文件
with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✅ 文件已保存!")

# 验证更新
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
zh_value = data['strings'][key]['localizations']['zh-Hans']['stringUnit']['value']
print(f"\n📋 最终显示的中文版权信息:")
print(f"   {zh_value}")
