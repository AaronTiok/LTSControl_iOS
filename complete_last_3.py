import json

# 读取文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 最后 3 个字符串的精确翻译 (包含不间断空格\xa0)
last_translations = {
    "Der Respooler stoppt anhand der übertragenen Menge. Empfohlen, wenn die obere Spule größer als 1\u00a0kg ist.": 
        "Respooler 根据传输的量停止。建议当上线轴大于 1 千克时使用。",
    
    "Der Respooler stoppt anhand des Filament Sensors, sobald die obere Spule leer ist. Empfohlen, wenn Filament zwischen zwei 1\u00a0kg Spulen übertragen wird.": 
        "当上线轴空时，Respooler 会通过耗材传感器停止。建议在两个 1 千克线轴之间传输耗材时使用。",
    
    "Für genauere Zeitangaben bzw. Respool-Mengen die benötigte Dauer für eine 1\u00a0kg Spule bei 80\u00a0% Geschwindigkeit messen und hier anpassen.": 
        "为获得更精确的时间或倒带量，请测量并在此处调整 80% 速度下 1 千克线轴所需的时间。",
}

# 添加翻译
added_count = 0
not_found_count = 0

for key, translation in last_translations.items():
    if key not in data['strings']:
        print(f"✗ 未找到：{key[:60]}...")
        not_found_count += 1
        continue
        
    value = data['strings'][key]
    localizations = value.get('localizations', {})
    
    # 检查是否已有中文翻译
    if 'zh-Hans' in localizations:
        print(f"✓ 已有中文：{key[:60]}...")
        continue
    
    # 添加简体中文翻译
    localizations['zh-Hans'] = {
        "stringUnit": {
            "state": "translated",
            "value": translation
        }
    }
    value['localizations'] = localizations
    added_count += 1
    print(f"✓ 已翻译：{key[:60]}...")

# 保存文件
with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！添加了 {added_count} 条翻译。")

# 最终统计
total_zh = sum(1 for v in data['strings'].values() 
               if 'localizations' in v and 'zh-Hans' in v['localizations'])
total_strings = len([k for k,v in data['strings'].items() if v.get('shouldTranslate') != False])
print(f"中文翻译总数：{total_zh}/{total_strings}")
print(f"完成率：{total_zh/total_strings*100:.1f}%")

if total_zh == total_strings:
    print("\n🎉 恭喜！所有 161 个字符串都已 100% 翻译成中文!")
    print("✅ iOS 应用现在支持完整的中文界面!")
else:
    print(f"\n还剩 {total_strings - total_zh} 条未翻译")
