import json
import sys

# 完整的中文翻译字典
zh_translations = {
    # 基础 UI
    "App": "应用",
    "Bluetooth": "蓝牙",
    "Board Firmware": "主板固件",
    "Board not connected": "主板未连接",
    "Board Update": "主板更新",
    "Board Version: %@": "主板版本：%@",
    "Off": "关闭",
    "On: %lld %%": "开启：%lld %%",
    "Show Changes": "显示更改",
    "Auto-Stop": "自动停止",
    "Auto-Stop Sensitivity": "自动停止灵敏度",
    "Auto-Stop!": "自动停止!",
    "Notifications": "通知",
    "Settings": "设置",
    "About": "关于",
    "Cancel": "取消",
    "OK": "确定",
    "Delete": "删除",
    "Remove": "移除",
    "Save": "保存",
    "Start": "开始",
    "Stop": "停止",
    "Pause": "暂停",
    "Resume": "继续",
    "Connect": "连接",
    "Disconnect": "断开连接",
    "Connected": "已连接",
    "Not Connected": "未连接",
    "Version": "版本",
    "Update": "更新",
    "Download": "下载",
    "Install": "安装",
    "Installing": "正在安装",
    "Complete": "完成",
    "Error": "错误",
    "Warning": "警告",
    "Success": "成功",
    "Loading": "加载中",
    "Retry": "重试",
    "Back": "返回",
    "Next": "下一步",
    "Previous": "上一步",
    "Done": "完成",
    "Close": "关闭",
    "Open": "打开",
    "Enable": "启用",
    "Disable": "禁用",
    
    # 重量
    "0,5 kg": "0.5 千克",
    "0,25 kg": "0.25 千克",
    "1,0 kg": "1.0 千克",
    
    # 说明文字
    "Make sure the Respooler Board is turned on and the latest firmware is installed.": "请确保 Respooler 主板已开启并安装了最新的固件。",
    "If you encounter connectivity issues, please remove the saved device and initialize a new connection.": "如果遇到连接问题，请移除已保存的设备并重新建立连接。",
    "Stopping works based on the dynamically calculated progress. Accuracy may vary by material.": "自动停止功能基于动态计算的进度。精度可能因材料而异。",
    
    # 版权
    "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, Deutschland, info@lts-design.com": "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, 德国，info@lts-design.com",
    "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, Germany, info@lts-design.com": "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, 德国，info@lts-design.com",
    
    # 德语原文的翻译
    "Achte darauf, dass das Respooler Board eingeschaltet ist und die aktuelle Firmware installiert wurde.": "请确保 Respooler 主板已开启并安装了最新的固件。",
    "An: %lld %%": "开启：%lld %%",
    "Änderungen anzeigen": "显示更改",
    "Aus": "关闭",
    "Auswählen (%lld)": "选择 (%lld)",
    "Auto-Stopp Empfindlichkeit": "自动停止灵敏度",
    "Bei Verbindungsproblemen das gespeicherte Gerät entfernen und die Verbindung neu aufbauen.": "如果遇到连接问题，请移除已保存的设备并重新建立连接。",
    "Benachrichtigungen": "通知",
    "Board nicht verbunden": "主板未连接",
    "Celsius": "摄氏度",
    "Chip: %@": "芯片：%@",
    "Dauer: %lldm %llds": "时长：%lld分%lld秒",
    "Der Auto-Stopp stoppt den Motor bei Widerstand.": "自动停止功能会在遇到阻力时停止电机。",
    "Der High-Speed Modus erhöht die Geschwindigkeit des Motors.": "高速模式会提高电机转速。",
    "Der Lüfter schaltet sich standardmäßig 10 Sekunden nach dem Stoppen des Motors aus.": "风扇默认在电机停止 10 秒后关闭。",
    "Der Quellcode sowie alle weiteren Dateien sind Open Source.": "源代码及所有其他文件均为开源。",
    "Der Respooler hat automatisch angehalten. Überprüfe das Filament und starte den Motor erneut.": "Respooler 已自动停止。请检查耗材并重新启动电机。",
    "Der Respooler stoppt anhand der übertragenen Menge bzw. des Winkels.": "Respooler 会根据传输的量或角度停止。",
    "Der Respooler stoppt anhand des Filament Sensors, wenn kein Filament mehr erkannt wird.": "当不再检测到耗材时，Respooler 会通过耗材传感器停止。",
    "Der Spulvorgang wurde erfolgreich fertiggestellt.": "倒带过程已成功完成。",
    "Die Empfindlichkeit hängt vom Netzteil ab. Wenn der Motor zu heiß wird, reduziere die Stärke.": "灵敏度取决于电源。如果电机过热，请降低强度。",
    "Einfach": "简单",
    "Einstellungen": "设置",
    "Endpositionen kalibrieren": "校准终点位置",
    "Erkannt": "已识别",
    "Fahrenheit": "华氏度",
    "Fehler beim Kauf: %@": "购买失败：%@",
    "Fehler: Auto-Stopp!": "错误：自动停止!",
    "Fehler!": "错误!",
    "Fertig!": "完成!",
    "Filament": "耗材",
    "Filament Sensor nutzen": "使用耗材传感器",
    "Firmware aktualisieren": "更新固件",
    "Firmware ist aktuell": "固件已是最新",
    "Firmware wird aktualisiert...": "正在更新固件...",
    "Funktion": "功能",
    "Für die WLAN-Verbindung hier nach verfügbaren Netzwerken suchen und das Passwort eingeben. Funktioniert nur mit 2,4 GHz Netzwerken.": "在此搜索可用的 WLAN 网络并输入密码。仅支持 2.4 GHz 网络。",
    "Gering": "低",
    "Gesamte Spule": "整个线轴",
    "Geschwindigkeit: %lld %%": "速度：%lld %%",
    "Gespeichertes Gerät entfernen": "移除已保存的设备",
    "Getrennt": "已断开",
    "Glissando": "滑音",
    "High-Speed": "高速",
    "Hinweise": "提示",
    "Hoch": "高",
    "Kalibrierung": "校准",
    "Keine WLAN-Verbindung": "无 WLAN 连接",
    "Konfiguration": "配置",
    "Konnte nicht geladen werden.": "无法加载。",
    "LED Helligkeit: %lld %%": "LED 亮度：%lld %%",
    "Linke Seite": "左侧",
    "Links": "左",
    "Live-Aktivitäten": "实时活动",
    "LTS Control": "LTS Control",
    "Lüfter": "风扇",
    "Lüfter immer an": "风扇常开",
    "Mehr": "更多",
    "Mittel": "中",
    "Motor": "电机",
    "Motorstärke": "电机强度",
    "Nach verfügbaren Netzwerken suchen": "搜索可用网络",
    "Netzwerk": "网络",
    "Netzwerk-Scan": "网络扫描",
    "Neues Control Board": "新控制面板",
    "Nicht erkannt": "未识别",
    "Nicht unterstützt": "不支持",
    "Nicht verbunden": "未连接",
    "OK": "确定",
    "Passe die Motorstärke an, wenn der Motor heiß wird oder zu wenig Kraft hat.": "如果电机过热或动力不足，请调整电机强度。",
    "Passwort": "密码",
    "Pause": "暂停",
    "Pausiert": "已暂停",
    "Rabatt Code": "折扣码",
    "Rechte Seite": "右侧",
    "Rechts": "右",
    "Respool-Menge": "倒带量",
    "Respooler fertig!": "Respooler 完成!",
    "Respooler pausieren": "暂停 Respooler",
    "Respooler starten": "启动 Respooler",
    "Respooler stoppen": "停止 Respooler",
    "Respooler verbinden": "连接 Respooler",
    "Richtung umkehren": "反转方向",
    "Schließen": "关闭",
    "Schrittweite: %@ mm": "步进：%@ 毫米",
    "Sende bei Fragen, Problemen oder Anregungen gerne eine E-Mail.": "如有任何问题、问题或建议，请发送电子邮件。",
    "Servo": "伺服",
    "Speichern": "保存",
    "Stärke: %lld %%": "强度：%lld %%",
    "Star Wars": "星球大战",
    "Start": "开始",
    "state.autoStop": "自动停止",
    "state.disconnected": "已断开",
    "state.done": "已完成",
    "state.idle": "空闲",
    "state.paused": "已暂停",
    "state.running": "运行中",
    "state.updating": "更新中",
    "Status": "状态",
    "Stelle die Endanschläge links und rechts so ein, dass das Filament sicher geführt wird.": "调整左右终点限位器，确保耗材安全引导。",
    "Stelle sicher, dass das Board eingeschaltet ist und die neueste Firmware installiert hast.": "请确保主板已开启并安装了最新固件。",
    "Steuert den LTS Respooler.": "控制 LTS Respooler。",
    "Steuerung": "控制",
    "Stopp": "停止",
    "Temperatur": "温度",
    "Ton bei Fertigstellung": "完成时播放提示音",
    "Trinkgeld": "打赏",
    "Trinkgeld senden": "发送打赏",
    "Um das Respooler Board mit der App zu steuern, müssen die Bluetooth-Berechtigungen erteilt werden.": "要使用应用控制 Respooler 主板，必须授予蓝牙权限。",
    "Unbekannter Fehler beim Kauf.": "购买时发生未知错误。",
    "Unterstützen": "支持",
    "Unterstützen %@": "支持 %@",
    "Update erfolgreich!": "更新成功!",
    "Update fehlgeschlagen!": "更新失败!",
    "Update verfügbar (%@ → % @)": "更新可用 (%@ → %@)",
    "Updates nicht unterstützt": "不支持更新",
    "Variante": "变体",
    "Variante wählen": "选择变体",
    "Verbinden": "连接",
    "Verbindung": "连接",
    "Verbindung erneut starten": "重新建立连接",
    "Verbindung herstellen": "建立连接",
    "Verbindungseinstellungen": "连接设置",
    "Verbunden": "已连接",
    "Versionsverlauf": "版本历史",
    "Vielen Dank für deine Unterstützung!": "非常感谢您的支持!",
    "Wähle aus, auf welcher Seite die Startposition der Kalibrierung sein soll.": "选择校准起始位置在哪一侧。",
    "Wähle die Variante deines Respoolers. Abhängig davon werden verschiedene Funktionen unterstützt.": "选择您的 Respooler 变体。根据不同变体会支持不同功能。",
    "Wenn der Sensor deaktiviert ist, wird nicht auf das Filament geachtet.": "如果传感器被禁用，将不会检测耗材。",
    "Wenn dir die App gefällt, kannst du hier eine kleine Spende dalassen.": "如果您喜欢这个应用，可以在这里留下小额打赏。",
    "Wenn du **kostenlos** das neue Control Board V4 erhalten möchtest, kannst du den folgenden Code dafür im Store anwenden, sobald es verfügbar ist.": "如果您想**免费**获得新的 V4 控制面板，一旦有货，您可以在商店中使用以下代码。",
    "Willkommen bei LTS Control": "欢迎使用 LTS Control",
    "Winkel: %lld°": "角度：%lld°",
    "WLAN": "WLAN",
    "x": "x",
    "Zahlung konnte nicht verifiziert werden.": "无法验证支付。",
    "Zahlung wird verarbeitet...": "正在处理支付...",
    "Zugangsdaten senden": "发送访问数据",
}

try:
    # 读取文件
    with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"成功加载文件，总字符串数：{len(data['strings'])}")
    
    # 统计
    added_count = 0
    skipped_count = 0
    
    # 遍历所有需要翻译的字符串
    for key, value in data['strings'].items():
        # 跳过不应该翻译的内容
        if value.get('shouldTranslate') == False:
            skipped_count += 1
            continue
        
        # 获取 localizations
        localizations = value.get('localizations', {})
        
        # 如果已经有中文翻译，跳过
        if 'zh-Hans' in localizations:
            skipped_count += 1
            continue
        
        # 查找匹配的翻译
        if key in zh_translations:
            localizations['zh-Hans'] = {
                "stringUnit": {
                    "state": "translated",
                    "value": zh_translations[key]
                }
            }
            value['localizations'] = localizations
            added_count += 1
            print(f"✓ 已翻译：{key[:50]} -> {zh_translations[key][:30]}")
    
    # 保存修改后的文件
    with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n完成!")
    print(f"新增翻译：{added_count} 条")
    print(f"跳过：{skipped_count} 条")
    
    # 统计总数
    total_zh = sum(1 for v in data['strings'].values() 
                   if 'localizations' in v and 'zh-Hans' in v['localizations'])
    total_strings = len([k for k,v in data['strings'].items() if v.get('shouldTranslate') != False])
    print(f"中文翻译总数：{total_zh}/{total_strings}")
    print(f"完成率：{total_zh/total_strings*100:.1f}%")
    
except Exception as e:
    print(f"错误：{e}")
    import traceback
    traceback.print_exc()
