import json

# 读取文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 完整中文翻译表
zh_translations = {
    # 重量单位
    "0,5 kg": "0.5 千克",
    "0,25 kg": "0.25 千克",
    "1,0 kg": "1.0 千克",
    
    # 温度
    "Celsius": "摄氏度",
    "Fahrenheit": "华氏度",
    "Temperature": "温度",
    
    # 连接状态
    "Board nicht verbunden": "主板未连接",
    "Getrennt": "已断开",
    "Nicht verbunden": "未连接",
    "Verbunden": "已连接",
    "Verbindung": "连接",
    "Verbinden": "连接",
    "Verbindung herstellen": "建立连接",
    "Verbindungseinstellungen": "连接设置",
    
    # 设置
    "Einstellungen": "设置",
    "Änderungen anzeigen": "显示更改",
    "Aus": "关闭",
    "An: %lld %%": "开启：%lld %%",
    "Auswählen (%lld)": "选择 (%lld)",
    
    # 通知和提示
    "Benachrichtigungen": "通知",
    "Hinweise": "提示",
    "Warnung": "警告",
    "Fehler!": "错误!",
    "Fertig!": "完成!",
    "Erfolg": "成功",
    
    # 固件更新
    "Firmware aktualisieren": "更新固件",
    "Firmware ist aktuell": "固件已是最新",
    "Firmware wird aktualisiert...": "正在更新固件...",
    
    # 功能
    "Funktion": "功能",
    "Mehr": "更多",
    "Weniger": "更少",
    
    # 耗材和线轴
    "Gesamte Spule": "整个线轴",
    "Spool": "线轴",
    "Filament": "耗材",
    
    # 速度和电机
    "Geschwindigkeit: %lld %%": "速度：%lld %%",
    "Motorstärke": "电机强度",
    "Stärke: %lld %%": "强度：%lld %%",
    
    # 设备和识别
    "Erkannt": "已识别",
    "Nicht erkannt": "未识别",
    "Gerät": "设备",
    "Gespeichertes Gerät entfernen": "移除已保存的设备",
    
    # 校准和配置
    "Endpositionen kalibrieren": "校准终点位置",
    "Kalibrierung": "校准",
    "Konfiguration": "配置",
    "Steuerung": "控制",
    
    # 网络和 WiFi
    "Keine WLAN-Verbindung": "无 WLAN 连接",
    "Netzwerk": "网络",
    "Netzwerk-Scan": "网络扫描",
    "Nach verfügbaren Netzwerken suchen": "搜索可用网络",
    "WLAN": "WLAN",
    
    # LED 和灯光
    "LED Helligkeit: %lld %%": "LED 亮度：%lld %%",
    
    # 方向
    "Linke Seite": "左侧",
    "Rechte Seite": "右侧",
    "Links": "左",
    "Rechts": "右",
    "Richtung umkehren": "反转方向",
    
    # 风扇
    "Lüfter": "风扇",
    "Lüfter immer an": "风扇常开",
    
    # 活动和实时
    "Live-Aktivitäten": "实时活动",
    
    # 应用名称
    "LTS Control": "LTS Control",
    
    # 升级码
    "Upgrade Code": "升级码",
    "Rabatt Code": "折扣码",
    
    # 暂停和继续
    "Pausiert": "已暂停",
    "Fortsetzen": "继续",
    
    # 状态
    "state.running": "运行中",
    "state.updating": "更新中",
    
    # 声音
    "Ton bei Fertigstellung": "完成时播放提示音",
    
    # 支持和感谢
    "Unterstützen": "支持",
    "Unterstützen %@": "支持 %@",
    "Trinkgeld": "打赏",
    "Trinkgeld senden": "发送打赏",
    "Vielen Dank für deine Unterstützung!": "非常感谢您的支持!",
    
    # 变体选择
    "Variante": "变体",
    "Variante wählen": "选择变体",
    
    # 欢迎信息
    "Willkommen bei LTS Control...": "欢迎使用 LTS Control...",
    
    # 角度
    "Winkel: %lld°": "角度：%lld°",
    
    # 持续时间
    "Dauer: %lldm %llds": "时长：%lld分%lld秒",
    
    # 芯片信息
    "Chip: %@": "芯片：%@",
    
    # 错误信息
    "Fehler beim Kauf: %@": "购买失败：%@",
    "Unbekannter Fehler beim Kauf.": "购买时发生未知错误。",
    "Zahlung konnte nicht verifiziert werden.": "无法验证支付。",
    "Zahlung wird verarbeitet...": "正在处理支付...",
    
    # 不支持
    "Nicht unterstützt": "不支持",
    "Updates nicht unterstützt": "不支持更新",
    
    # 连接问题
    "Bei Verbindungsproblemen das gespeicherte Gerät entfernen und die Verbindung neu aufbauen.": "如果遇到连接问题，请移除已保存的设备并重新建立连接。",
    
    # 电机控制说明
    "Der Respooler hat automatisch angehalten. Überprüfe das Filament und starte den Motor erneut.": "Respooler 已自动停止。请检查耗材并重新启动电机。",
    
    # 操作按钮
    "Schließen": "关闭",
    "Speichern": "保存",
    "Abbrechen": "取消",
    "Bestätigen": "确认",
    "Löschen": "删除",
    "Entfernen": "移除",
    
    # 其他
    "Glissando": "滑音",
    "Star Wars": "星球大战",
    "Einfach": "简单",
    "Gering": "低",
    "Mittel": "中",
    "Hoch": "高",
    "Passwort": "密码",
    "Servo": "伺服",
    "x": "x",
    
    # 新版本
    "Neues Control Board": "新控制面板",
    
    # 免费获取
    "Wenn du **kostenlos** das neue Control Board V4 erhalten möchtest, registriere dich jetzt!": "如果您想**免费**获得新的 V4 控制面板，请立即注册!",
    
    # WiFi 连接说明
    "Für die WLAN-Verbindung hier nach verfügbaren Netzwerken suchen und verbinden.": "在此处搜索并连接到可用的 WLAN 网络。",
}

# 统计
updated_count = 0

# 遍历所有需要翻译的字符串
for key, value in data['strings'].items():
    # 跳过不应该翻译的内容
    if value.get('shouldTranslate') == False:
        continue
    
    # 获取 localizations
    localizations = value.get('localizations', {})
    
    # 如果已经有中文翻译，跳过
    if 'zh-Hans' in localizations:
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
        updated_count += 1
        print(f"✓ 已翻译：{key[:60]} -> {zh_translations[key][:40]}")

# 保存修改后的文件
with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成!")
print(f"新增翻译：{updated_count} 条")

# 统计总数
total_zh = sum(1 for v in data['strings'].values() 
               if 'localizations' in v and 'zh-Hans' in v['localizations'])
print(f"中文翻译总数：{total_zh}")
