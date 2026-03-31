import json

# 读取文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 剩余的翻译
remaining_translations = {
    "Der Spulvorgang wurde erfolgreich fertiggestellt.": "倒带过程已成功完成。",
    "Für die WLAN-Verbindung hier nach verfügbaren Netzwerken suchen und das Passwort eingeben. Funktioniert nur mit 2,4 GHz Netzwerken.": "在此搜索可用的 WLAN 网络并输入密码。仅支持 2.4 GHz 网络。",
    "Konnte nicht geladen werden.": "无法加载。",
    "Schrittweite: %@ mm": "步进：%@ 毫米",
    "Temperatur": "温度",
    "Wenn du **kostenlos** das neue Control Board V4 erhalten möchtest, kannst du den folgenden Code dafür im Store anwenden, sobald es verfügbar ist.": "如果您想**免费**获得新的 V4 控制面板，一旦有货，您可以在商店中使用以下代码。",
    "Willkommen bei LTS Control": "欢迎使用 LTS Control",
}

# 添加翻译
updated_count = 0
for key, translation in remaining_translations.items():
    if key in data['strings']:
        value = data['strings'][key]
        localizations = value.get('localizations', {})
        
        # 添加简体中文翻译
        localizations['zh-Hans'] = {
            "stringUnit": {
                "state": "translated",
                "value": translation
            }
        }
        value['localizations'] = localizations
        updated_count += 1
        print(f"✓ 已翻译：{key[:50]}... -> {translation[:40]}...")

# 保存文件
with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！添加了 {updated_count} 条翻译。")

# 统计
total_zh = sum(1 for v in data['strings'].values() 
               if 'localizations' in v and 'zh-Hans' in v['localizations'])
total_strings = len([k for k,v in data['strings'].items() if v.get('shouldTranslate') != False])
print(f"中文翻译总数：{total_zh}/{total_strings}")
print(f"完成率：{total_zh/total_strings*100:.1f}%")
