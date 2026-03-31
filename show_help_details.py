import json

with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 80)
print("📖 使用指南、技术说明和帮助信息详情")
print("=" * 80)

# 查找相关的关键翻译
categories = {
    "开源信息": ["GitHub", "github", "Open Source", "Quellcode"],
    "联系方式": ["E-Mail", "email", "info@", "Fragen", "Problemen"],
    "使用说明": ["steuern", "koppeln", "Bedienung"],
    "技术提示": ["OTA", "WLAN", "Internet", "Web Flasher"],
    "功能说明": ["Sensor", "Filament", "Motor", "Lüfter"],
}

found_items = []

for key, value in data['strings'].items():
    if 'localizations' not in value or 'zh-Hans' not in value['localizations']:
        continue
    
    zh_value = value['localizations']['zh-Hans']['stringUnit']['value']
    
    # 检查是否属于某个类别
    for category, keywords in categories.items():
        if any(kw.lower() in key.lower() for kw in keywords):
            found_items.append((category, key, zh_value))
            break

# 按类别显示
current_category = None
for category, key, zh_value in sorted(found_items, key=lambda x: x[0]):
    if category != current_category:
        print(f"\n{'='*80}")
        print(f"📁 {category}")
        print(f"{'='*80}")
        current_category = category
    
    print(f"\n🔹 原文：{key[:120]}{'...' if len(key) > 120 else ''}")
    print(f"🔸 中文：{zh_value}")
    print("-" * 80)

# 特别显示长文本说明
print("\n" + "=" * 80)
print("📋 完整的长文本说明")
print("=" * 80)

long_texts = [
    (k, v['localizations']['zh-Hans']['stringUnit']['value'])
    for k, v in data['strings'].items()
    if 'localizations' in v and 'zh-Hans' in v['localizations'] 
    and len(k) > 80
]

for key, zh_value in long_texts:
    print(f"\n【说明】{zh_value}")
    print(f"{'─'*80}")
