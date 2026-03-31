import json

# 读取文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 精确的完整翻译
final_translations = {
    "Da das V3 Control Board nur in begrenzter Stückzahl verkauft wurde und nicht alle Funktionen unterstützt, wird es dafür **keine weiteren Firmware-Updates** mehr geben.\n\nAlle momentan vorhandenen Funktionen bleiben bestehen.": 
        "由于 V3 控制面板限量销售且不支持所有功能，将**不再有固件更新**。\n\n所有现有功能将保持不变。",
    
    "Das OTA-Update ist fehlgeschlagen. Stelle sicher, dass das verbundene WLAN über eine funktionierende Internetverbindung verfügt.": 
        "OTA 更新失败。请确保连接的 WLAN 具有正常的互联网连接。",
    
    "Der High-Speed Modus erhöht die Geschwindigkeit des Motors. Auto-Stopp ist dabei nicht verfügbar.": 
        "高速模式会提高电机转速。此模式下不可使用自动停止功能。",
    
    "Der Lüfter schaltet sich standardmäßig 10 Sekunden nach stoppen des Respoolers aus.": 
        "风扇默认在 Respooler 停止 10 秒后关闭。",
    
    "Der Quellcode sowie alle weiteren Dateien sind Open Source und können auf [GitHub](https://github.com/LukasT03/LTS-Respooler) heruntergeladen werden.": 
        "源代码及所有其他文件均为开源，可在 [GitHub](https://github.com/LukasT03/LTS-Respooler) 下载。",
    
    "Der Respooler hat automatisch angehalten. Überprüfe, ob der Motor blockiert ist.": 
        "Respooler 已自动停止。请检查电机是否卡住。",
    
    "Der Respooler stoppt anhand der übertragenen Menge. Empfohlen, wenn die obere Spule größer als 1 kg ist.": 
        "Respooler 根据传输的量停止。建议当上线轴大于 1 千克时使用。",
    
    "Der Respooler stoppt anhand des Filament Sensors, sobald die obere Spule leer ist. Empfohlen, wenn Filament zwischen zwei 1 kg Spulen übertragen wird.": 
        "当上线轴空时，Respooler 会通过耗材传感器停止。建议在两个 1 千克线轴之间传输耗材时使用。",
    
    "Die Empfindlichkeit hängt vom Netzteil ab. Wenn der Motor zu oft stoppt, verringere die Empfindlichkeit in den Einstellungen.": 
        "灵敏度取决于电源。如果电机停止太频繁，请在设置中降低灵敏度。",
    
    "Für genauere Zeitangaben bzw. Respool-Mengen die benötigte Dauer für eine 1 kg Spule bei 80 % Geschwindigkeit messen und hier anpassen.": 
        "为获得更精确的时间或倒带量，请测量并在此处调整 80% 速度下 1 千克线轴所需的时间。",
    
    "Für OTA-Updates muss das Board mit dem lokalen WLAN verbunden sein. Alternativ dazu kann auch der Web Flasher auf der LTS Design Webseite genutzt werden.": 
        "OTA 更新需要主板连接到本地 WLAN。或者也可以使用 LTS Design 网站上的 Web Flasher。",
    
    "Passe die Motorstärke an, wenn der Motor heiß wird oder vibriert. Auch ein schwaches Netzteil kann die Stärke beeinflussen.": 
        "如果电机过热或振动，请调整电机强度。电源不足也会影响强度。",
    
    "Sende bei Fragen, Problemen oder Anregungen gerne eine E-Mail an info@lts-design.com.": 
        "如有任何问题、问题或建议，请发送电子邮件至 info@lts-design.com。",
    
    "Stelle die Endanschläge links und rechts so ein, dass die Filamentführung gerade so die Seiten berührt.": 
        "调整左右终点限位器，使耗材引导装置刚好接触侧面。",
    
    "Stelle sicher, dass das Board eingeschaltet ist und starte die Kopplung über den Button unten.": 
        "请确保主板已开启，然后通过下方按钮开始配对。",
    
    "Um das Respooler Board mit der App zu steuern, musst du es zuerst mit deinem %@ verbinden.": 
        "要使用应用控制 Respooler 主板，你必须先将其与你的 %@ 配对。",
    
    "Wähle die Variante deines Respoolers. Abhängig davon werden dir die verfügbaren Einstellungen angezeigt. Die Auswahl wird auf dem Board gespeichert und kann jederzeit in den Einstellungen geändert werden.": 
        "选择您的 Respooler 变体。根据不同变体会显示可用设置。选择将保存在主板上，并可随时在设置中更改。",
    
    "Wähle die Variante deines Respoolers. Abhängig davon werden dir die verfügbaren Einstellungen angezeigt. Die Auswahl wird auf dem Board gespeichert.": 
        "选择您的 Respooler 变体。根据不同变体会显示可用设置。选择将保存在主板上。",
    
    "Wenn der Sensor deaktiviert ist, wird nicht auf den Verlust von Filament reagiert.": 
        "如果传感器被禁用，将不会对耗材丢失做出反应。",
    
    "Wenn dir die App gefällt, kannst du hier eine kleine Spende leisten. Es werden dadurch keine zusätzlichen Funktionalitäten freigeschaltet.": 
        "如果您喜欢这个应用，可以在这里留下小额打赏。这不会解锁任何额外功能。",
}

# 添加翻译
added_count = 0
not_found_count = 0

for key, translation in final_translations.items():
    if key not in data['strings']:
        print(f"✗ 未找到：{key[:50]}...")
        not_found_count += 1
        continue
        
    value = data['strings'][key]
    localizations = value.get('localizations', {})
    
    # 检查是否已有中文翻译
    if 'zh-Hans' in localizations:
        print(f"✓ 已有中文：{key[:50]}...")
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

print(f"\n完成！添加了 {added_count} 条翻译。")

# 统计
total_zh = sum(1 for v in data['strings'].values() 
               if 'localizations' in v and 'zh-Hans' in v['localizations'])
total_strings = len([k for k,v in data['strings'].items() if v.get('shouldTranslate') != False])
print(f"中文翻译总数：{total_zh}/{total_strings}")
print(f"完成率：{total_zh/total_strings*100:.1f}%")

if total_zh == total_strings:
    print("🎉 恭喜！所有字符串都已翻译成中文!")
else:
    print(f"还剩 {total_strings - total_zh} 条未翻译")
