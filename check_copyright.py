import json

with open('Localizable.xcstrings', 'r', encoding='utf-8') as f:
    data = json.load(f)

key = "© 2025, LTS Design, Heiligenbornstraße 23, 01219 Dresden, Deutschland, info@lts-design.com"

print("各语言版本:")
print("=" * 80)
print(f"德文：{data['strings'][key]['localizations']['de']['stringUnit']['value']}")
print(f"英文：{data['strings'][key]['localizations']['en']['stringUnit']['value']}")
print(f"中文：{data['strings'][key]['localizations']['zh-Hans']['stringUnit']['value']}")
print("=" * 80)
