"""
场景 10：特性开关（Feature Flags）

应用：根据用户等级、A/B 测试分组等因素，动态合并特性配置
"""

# 默认特性配置（所有用户）
DEFAULT_FEATURES = {
    "dark_mode": True,
    "notifications": True,
    "basic_analytics": True,
    "file_upload_limit_mb": 10,
    "api_rate_limit": 100
}

# VIP 用户特性
VIP_FEATURES = {
    "file_upload_limit_mb": 100,  # 覆盖默认值
    "api_rate_limit": 1000,
    "priority_support": True,
    "advanced_analytics": True
}

# 企业用户特性
ENTERPRISE_FEATURES = {
    "file_upload_limit_mb": 1000,
    "api_rate_limit": 10000,
    "priority_support": True,
    "advanced_analytics": True,
    "custom_branding": True,
    "sso": True
}

# A/B 测试组特性
AB_TEST_GROUP_A = {
    "new_ui": True,
    "ai_suggestions": True
}

AB_TEST_GROUP_B = {
    "new_ui": False,
    "ai_suggestions": False
}

def get_user_features_old(user_tier, ab_group=None, custom_features=None):
    """传统方式：逐步构建特性配置"""
    features = DEFAULT_FEATURES.copy()
    
    if user_tier == "vip":
        features.update(VIP_FEATURES)
    elif user_tier == "enterprise":
        features.update(ENTERPRISE_FEATURES)
    
    if ab_group == "A":
        features.update(AB_TEST_GROUP_A)
    elif ab_group == "B":
        features.update(AB_TEST_GROUP_B)
    
    if custom_features:
        features.update(custom_features)
    
    return features

def get_user_features_new(user_tier, ab_group=None, custom_features=None):
    """Python 3.9+ 方式：使用 | 运算符"""
    tier_features = {
        "vip": VIP_FEATURES,
        "enterprise": ENTERPRISE_FEATURES
    }.get(user_tier, {})
    
    ab_features = {
        "A": AB_TEST_GROUP_A,
        "B": AB_TEST_GROUP_B
    }.get(ab_group, {})
    
    return (
        DEFAULT_FEATURES
        | tier_features
        | ab_features
        | (custom_features or {})
    )

print("=" * 60)
print("场景 10：特性开关（Feature Flags）")
print("=" * 60)

# 测试用例 1：普通用户
print("\n[测试用例 1] 普通用户（无 A/B 测试）：\n")
basic_features = get_user_features_new("basic")
print(f"文件上传限制: {basic_features['file_upload_limit_mb']} MB")
print(f"API 请求限制: {basic_features['api_rate_limit']}")
print(f"优先支持: {basic_features.get('priority_support', False)}")

# 测试用例 2：VIP 用户 + A/B 测试 A 组
print("\n[测试用例 2] VIP 用户（A/B 测试 A 组）：\n")
vip_features_a = get_user_features_new("vip", ab_group="A")
print(f"文件上传限制: {vip_features_a['file_upload_limit_mb']} MB")
print(f"API 请求限制: {vip_features_a['api_rate_limit']}")
print(f"优先支持: {vip_features_a.get('priority_support', False)}")
print(f"AI 建议: {vip_features_a.get('ai_suggestions', False)}")
print(f"新 UI: {vip_features_a.get('new_ui', False)}")

# 测试用例 3：企业用户 + 自定义特性
print("\n[测试用例 3] 企业用户 + 自定义特性：\n")
enterprise_features = get_user_features_new(
    "enterprise",
    custom_features={"custom_domain": True, "white_label": True}
)
print(f"文件上传限制: {enterprise_features['file_upload_limit_mb']} MB")
print(f"API 请求限制: {enterprise_features['api_rate_limit']}")
print(f"SSO: {enterprise_features.get('sso', False)}")
print(f"自定义域名: {enterprise_features.get('custom_domain', False)}")
print(f"白标: {enterprise_features.get('white_label', False)}")

# 对比不同用户等级
print("\n[不同用户等级对比]")

tiers = ["basic", "vip", "enterprise"]
for tier in tiers:
    features = get_user_features_new(tier)
    print(f"\n{tier.upper()} 用户:")
    print(f"  文件上传限制: {features['file_upload_limit_mb']} MB")
    print(f"  API 请求限制: {features['api_rate_limit']}")
    print(f"  优先支持: {features.get('priority_support', False)}")
    print(f"  高级分析: {features.get('advanced_analytics', False)}")

# A/B 测试对比
print("\n[A/B 测试对比]")

for group in ["A", "B"]:
    features = get_user_features_new("basic", ab_group=group)
    print(f"\nA/B 测试组 {group}:")
    print(f"  新 UI: {features.get('new_ui', False)}")
    print(f"  AI 建议: {features.get('ai_suggestions', False)}")

# 验证两种实现结果一致
print("\n[验证结果一致性]")

test_params = [
    ("basic", None, None),
    ("vip", "A", None),
    ("enterprise", "B", {"custom_feature": True})
]

for tier, ab, custom in test_params:
    old_result = get_user_features_old(tier, ab, custom)
    new_result = get_user_features_new(tier, ab, custom)
    match = old_result == new_result
    print(f"  tier={tier}, ab={ab}, custom={custom}: {match}")

# 代码对比
print("\n[代码对比]")
print("传统方式需要多个 if-else 分支：")
print("  features = DEFAULT_FEATURES.copy()")
print("  if user_tier == 'vip':")
print("      features.update(VIP_FEATURES)")
print("  elif user_tier == 'enterprise':")
print("      features.update(ENTERPRISE_FEATURES)")
print("  # ... 更多条件")
print()
print("新方式使用声明式合并：")
print("  return (")
print("      DEFAULT_FEATURES")
print("      | tier_features")
print("      | ab_features")
print("      | (custom_features or {})")
print("  )")

print("\n💡 总结：| 运算符让特性分层清晰，便于管理复杂的特性开关系统")

