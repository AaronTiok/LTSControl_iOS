import json

# 读取文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 完整的长文本翻译
long_translations = {
    "Da das V3 Control Board nur in begrenzter Stückzahl verkauft wurde und wir nicht mehr produzieren, wird es keine Updates mehr geben. Wir empfehlen dir, auf das V4 Control Board umzusteigen.": 
        "由于 V3 控制面板限量销售且我们不再生产，将不再有更新。我们建议您升级到 V4 控制面板。",
    
    "Das OTA-Update ist fehlgeschlagen. Stelle sicher, dass das verbundene Board über 50% Akku hat und versuche es erneut.": 
        "OTA 更新失败。请确保连接的主板电量超过 50%,然后重试。",
    
    "Der High-Speed Modus erhöht die Geschwindigkeit des Motors. Auto-Stopp funktioniert in diesem Modus jedoch weniger präzise.": 
        "高速模式会提高电机转速。但在此模式下自动停止功能精度会降低。",
    
    "Der Lüfter schaltet sich standardmäßig 10 Sekunden nach stoppen des Respoolers automatisch aus. Wenn du diese Funktion deaktivierst, läuft der Lüfter dauerhaft.": 
        "风扇默认在 Respooler 停止 10 秒后自动关闭。如果禁用此功能，风扇将持续运行。",
    
    "Der Quellcode sowie alle weiteren Dateien sind Open Source und können auf GitHub eingesehen werden.": 
        "源代码及所有其他文件均为开源，可在 GitHub 查看。",
    
    "Der Respooler hat automatisch angehalten. Überprüfe, ob der Motor blockiert ist oder das Filament klemmt.": 
        "Respooler 已自动停止。请检查电机是否卡住或耗材是否卡住。",
    
    "Der Respooler stoppt anhand der übertragenen Menge. Empfohlen, wenn die Spule gleichmäßig gefüllt ist.": 
        "Respooler 根据传输的量停止。建议在线轴均匀填充时使用。",
    
    "Der Respooler stoppt anhand des Filament Sensors, sobald die obere Spule voll ist.": 
        "当上线轴满时，Respooler 会通过耗材传感器停止。",
    
    "Die Empfindlichkeit hängt vom Netzteil ab. Wenn der Motor zu oft stoppt, reduziere die Empfindlichkeit.": 
        "灵敏度取决于电源。如果电机停止太频繁，请降低灵敏度。",
    
    "Für genauere Zeitangaben bzw. Respool-Mengen die benötigte Dauer für eine volle Umdrehung kalibrieren.": 
        "校准完整旋转所需的时间以获得更精确的时间或倒带量。",
    
    "Für OTA-Updates muss das Board mit dem lokalen WLAN verbunden sein. Alle Geräte müssen im selben Netzwerk sein.": 
        "OTA 更新需要主板连接到本地 WLAN。所有设备必须在同一网络中。",
    
    "Passe die Motorstärke an, wenn der Motor heiß wird oder vibriert. Auch bei schlechter Verbindung zum Board sollte die Stärke reduziert werden.": 
        "如果电机过热或振动，请调整电机强度。如果与主板连接不良，也应降低强度。",
    
    "Sende bei Fragen, Problemen oder Anregungen gerne eine E-Mail an info@lts-design.com": 
        "如有任何问题、问题或建议，请发送电子邮件至 info@lts-design.com",
    
    "Stelle die Endanschläge links und rechts so ein, dass die Filamentführung sicher zwischen den Anschlägen liegt.": 
        "调整左右终点限位器，确保耗材引导装置安全位于限位器之间。",
    
    "Stelle sicher, dass das Board eingeschaltet ist und starte die Kopplung erneut.": 
        "请确保主板已开启并重新配对。",
    
    "Um das Respooler Board mit der App zu steuern, musst du es zuerst mit deinem Gerät koppeln.": 
        "要使用应用控制 Respooler 主板，你必须先将其与设备配对。",
    
    "Update verfügbar (%@ → %@)": "更新可用 (%@ → %@)",
    
    "Wähle die Variante deines Respoolers. Abhängig davon werden dir die verschiedenen Funktionen zur Verfügung gestellt.": 
        "选择您的 Respooler 变体。根据不同变体会提供不同功能。",
    
    "Wenn der Sensor deaktiviert ist, wird nicht auf den Verlust von Filament geachtet.": 
        "如果传感器被禁用，将不会检测耗材丢失。",
    
    "Wenn dir die App gefällt, kannst du hier eine kleine Spende leisten. Es dauert nur wenige Sekunden.": 
        "如果您喜欢这个应用，可以在这里留下小额打赏。只需几秒钟。",
}

# 添加翻译
added_count = 0
skipped_count = 0

for key, translation in long_translations.items():
    if key not in data['strings']:
        print(f"✗ 未找到键：{key[:40]}...")
        continue
        
    value = data['strings'][key]
    localizations = value.get('localizations', {})
    
    # 检查是否已有中文翻译
    if 'zh-Hans' in localizations:
        print(f"✓ 已有中文：{key[:40]}...")
        skipped_count += 1
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
    print(f"✓ 已翻译：{key[:50]}...")

# 保存文件
with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！添加了 {added_count} 条翻译，跳过 {skipped_count} 条。")

# 统计
total_zh = sum(1 for v in data['strings'].values() 
               if 'localizations' in v and 'zh-Hans' in v['localizations'])
total_strings = len([k for k,v in data['strings'].items() if v.get('shouldTranslate') != False])
print(f"中文翻译总数：{total_zh}/{total_strings}")
print(f"完成率：{total_zh/total_strings*100:.1f}%")
