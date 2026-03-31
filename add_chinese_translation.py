import json
import re

# 读取原始文件
with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 中文翻译词典 (基于英语/德语关键词的常用翻译)
translations = {
    # UI 通用词汇
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
    "Yes": "是",
    "No": "否",
    "Confirm": "确认",
    "Reset": "重置",
    "Clear": "清除",
    "Search": "搜索",
    "Filter": "筛选",
    "Sort": "排序",
    "Refresh": "刷新",
    "More": "更多",
    "Less": "更少",
    "Help": "帮助",
    "Info": "信息",
    "Information": "信息",
    
    # 设备相关
    "Device": "设备",
    "Devices": "设备",
    "Select Device": "选择设备",
    "No devices found": "未找到设备",
    "Scanning for devices...": "正在扫描设备...",
    "Connection failed": "连接失败",
    "Connection lost": "连接丢失",
    "Reconnecting...": "正在重新连接...",
    
    # 电机控制
    "Motor": "电机",
    "Motor Control": "电机控制",
    "Start Motor": "启动电机",
    "Stop Motor": "停止电机",
    "Pause Motor": "暂停电机",
    "Speed": "速度",
    "Direction": "方向",
    "Forward": "前进",
    "Reverse": "反转",
    "Clockwise": "顺时针",
    "Counter-clockwise": "逆时针",
    
    # 耗材管理
    "Spool": "线轴",
    "Material": "材料",
    "Filament": "耗材",
    "PLA": "PLA",
    "ABS": "ABS",
    "PETG": "PETG",
    "TPU": "TPU",
    "Weight": "重量",
    "Remaining": "剩余",
    "Used": "已用",
    "Empty": "空",
    "Full": "满",
    
    # 进度和状态
    "Progress": "进度",
    "Status": "状态",
    "Active": "活跃",
    "Inactive": "不活跃",
    "Busy": "忙碌",
    "Idle": "空闲",
    "Ready": "就绪",
    "Waiting": "等待中",
    
    # 电池和电源
    "Battery": "电池",
    "Power": "电源",
    "Charging": "充电中",
    "Low Battery": "电量低",
    "Battery Level": "电量",
    
    # 时间和日期
    "Time": "时间",
    "Date": "日期",
    "Duration": "持续时间",
    "Elapsed": "已过",
    "Remaining Time": "剩余时间",
    
    # 文件和存储
    "File": "文件",
    "Files": "文件",
    "Storage": "存储",
    "Memory": "内存",
    "Disk": "磁盘",
    
    # 网络和通信
    "Network": "网络",
    "WiFi": "无线网络",
    "Signal": "信号",
    "Online": "在线",
    "Offline": "离线",
    
    # 用户界面
    "Menu": "菜单",
    "Home": "主页",
    "Profile": "个人资料",
    "Account": "账户",
    "Language": "语言",
    "Theme": "主题",
    "Dark Mode": "深色模式",
    "Light Mode": "浅色模式",
    "Appearance": "外观",
    
    # 操作提示
    "Make sure the Respooler Board is turned on and the latest firmware is installed.": "请确保 Respooler 主板已开启并安装了最新的固件。",
    "If you encounter connectivity issues, please remove the saved device and initialize a new connection.": "如果遇到连接问题，请移除已保存的设备并重新建立连接。",
    "Stopping works based on the dynamically calculated progress. Accuracy may vary by material.": "自动停止功能基于动态计算的进度。精度可能因材料而异。",
    
    # 版权信息
    "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, Germany, info@lts-design.com": "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, 德国，info@lts-design.com",
}

# 特殊格式处理
def translate_string(key, en_value):
    """根据关键词生成中文翻译"""
    # 直接匹配
    if key in translations:
        return translations[key]
    
    # 模糊匹配 - 检查是否包含已知关键词
    for en, zh in translations.items():
        if en.lower() in key.lower():
            return zh
    
    # 如果没有找到翻译，返回英文原文（需要手动翻译）
    return None

# 统计
translated_count = 0
skipped_count = 0

# 遍历所有字符串
for key, value in data['strings'].items():
    # 跳过不应该翻译的内容
    if value.get('shouldTranslate') == False:
        skipped_count += 1
        continue
    
    # 获取 localizations 或者创建新的
    localizations = value.get('localizations', {})
    
    # 检查是否已经有中文翻译
    if 'zh-Hans' in localizations:
        skipped_count += 1
        continue
    
    # 获取英语值作为参考
    en_value = None
    if 'en' in localizations:
        en_value = localizations['en'].get('stringUnit', {}).get('value', '')
    elif key.strip():  # 如果 key 不是空的，使用 key 本身
        en_value = key
    
    if en_value:
        # 尝试翻译
        zh_translation = translate_string(key, en_value)
        
        if zh_translation:
            # 添加简体中文翻译
            localizations['zh-Hans'] = {
                "stringUnit": {
                    "state": "translated",
                    "value": zh_translation
                }
            }
            value['localizations'] = localizations
            translated_count += 1
            print(f"✓ 已翻译：{key[:50]}... -> {zh_translation[:50]}...")
        else:
            # 标记为需要手动翻译
            print(f"⚠ 需要手动翻译：{key[:60]}...")

# 更新数据
data['strings'] = data['strings']

# 保存修改后的文件
with open('Localizable.xcstrings', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成!")
print(f"已翻译：{translated_count} 条")
print(f"跳过：{skipped_count} 条")
print(f"\n注意：部分字符串需要手动翻译，请在 Xcode 中完善。")
