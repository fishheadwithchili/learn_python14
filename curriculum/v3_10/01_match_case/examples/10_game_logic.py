"""
场景 10：游戏逻辑

应用：游戏中的碰撞检测、物品交互、技能系统等
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 10：游戏逻辑")
print("=" * 60)

# 示例 1：物品使用逻辑
print("\n[示例 1] 物品使用逻辑：\n")

def use_item(item, player_state):
    """使用游戏物品"""
    match (item, player_state):
        # 生命药水
        case ({"type": "potion", "effect": "heal", "amount": amt}, {"hp": hp, "max_hp": max_hp}) \
                if hp < max_hp:
            new_hp = min(hp + amt, max_hp)
            healed = new_hp - hp
            return f"❤️  恢复 {healed} HP（{hp} -> {new_hp}）"
        case ({"type": "potion", "effect": "heal"}, {"hp": hp, "max_hp": max_hp}) \
                if hp >= max_hp:
            return "⚠️  HP 已满，无法使用"
        
        # 魔法药水
        case ({"type": "potion", "effect": "mana", "amount": amt}, {"mp": mp, "max_mp": max_mp}) \
                if mp < max_mp:
            new_mp = min(mp + amt, max_mp)
            restored = new_mp - mp
            return f"💙 恢复 {restored} MP（{mp} -> {new_mp}）"
        
        # 攻击增益
        case ({"type": "buff", "stat": "attack", "duration": dur}, _):
            return f"⚔️  攻击力提升（持续 {dur} 秒）"
        
        # 防御增益
        case ({"type": "buff", "stat": "defense", "duration": dur}, _):
            return f"🛡️  防御力提升（持续 {dur} 秒）"
        
        # 钥匙
        case ({"type": "key", "color": color}, {"has_door": door_color}) \
                if color == door_color:
            return f"🔑 使用 {color} 钥匙打开门"
        case ({"type": "key", "color": color}, _):
            return f"⚠️  没有匹配的 {color} 门"
        
        case _:
            return "❌ 无法使用此物品"

# 测试物品使用
player = {"hp": 50, "max_hp": 100, "mp": 30, "max_mp": 50, "has_door": "red"}

items = [
    {"type": "potion", "effect": "heal", "amount": 30},
    {"type": "potion", "effect": "mana", "amount": 20},
    {"type": "buff", "stat": "attack", "duration": 60},
    {"type": "buff", "stat": "defense", "duration": 30},
    {"type": "key", "color": "red"},
    {"type": "key", "color": "blue"}
]

for item in items:
    result = use_item(item, player)
    print(f"{str(item):55s} -> {result}")

# 示例 2：技能释放逻辑
print("\n[示例 2] 技能释放逻辑：\n")

def cast_skill(skill, caster, target):
    """释放技能"""
    match (skill, caster, target):
        # 火球术（单体攻击）
        case (
            {"name": "fireball", "damage": dmg, "mp_cost": cost},
            {"mp": mp} as c,
            {"hp": hp} as t
        ) if mp >= cost:
            return f"🔥 火球术命中！造成 {dmg} 伤害（消耗 {cost} MP）"
        case ({"mp_cost": cost}, {"mp": mp}, _) if mp < cost:
            return f"❌ MP 不足（需要 {cost}, 当前 {mp}）"
        
        # 治疗术
        case (
            {"name": "heal", "amount": heal_amt, "mp_cost": cost},
            {"mp": mp},
            {"hp": hp, "max_hp": max_hp}
        ) if mp >= cost and hp < max_hp:
            return f"💚 治疗成功！恢复 {heal_amt} HP"
        
        # 群体攻击
        case (
            {"name": "meteor", "damage": dmg, "mp_cost": cost, "aoe": True},
            {"mp": mp, "level": level},
            _
        ) if mp >= cost and level >= 10:
            return f"☄️  流星术！对所有敌人造成 {dmg} 伤害"
        case ({"name": "meteor"}, {"level": level}, _) if level < 10:
            return f"❌ 等级不足（需要 10 级，当前 {level} 级）"
        
        # 复活术
        case (
            {"name": "resurrect"},
            {"class": "priest"},
            {"hp": 0}
        ):
            return "✨ 复活成功！"
        case ({"name": "resurrect"}, {"class": player_class}, _):
            return f"❌ 只有牧师可以使用复活术（当前职业: {player_class}）"
        
        case _:
            return "❌ 无法释放技能"

# 测试技能释放
caster_mage = {"mp": 100, "max_mp": 100, "level": 15, "class": "mage"}
caster_priest = {"mp": 80, "max_mp": 100, "level": 12, "class": "priest"}
target_enemy = {"hp": 50, "max_hp": 100}
target_ally = {"hp": 30, "max_hp": 80}
target_dead = {"hp": 0, "max_hp": 100}

test_cases = [
    ({"name": "fireball", "damage": 40, "mp_cost": 20}, caster_mage, target_enemy),
    ({"name": "heal", "amount": 30, "mp_cost": 15}, caster_priest, target_ally),
    ({"name": "meteor", "damage": 60, "mp_cost": 50, "aoe": True}, caster_mage, target_enemy),
    ({"name": "resurrect"}, caster_priest, target_dead),
    ({"name": "resurrect"}, caster_mage, target_dead)
]

for skill, caster, target in test_cases:
    result = cast_skill(skill, caster, target)
    print(f"{skill['name']:12s} -> {result}")

# 示例 3：碰撞检测
print("\n[示例 3] 碰撞检测：\n")

def check_collision(obj1, obj2):
    """检查碰撞并返回结果"""
    match (obj1, obj2):
        # 玩家拾取金币
        case ({"type": "player"}, {"type": "coin", "value": val}):
            return f"💰 获得 {val} 金币"
        
        # 玩家碰到敌人
        case ({"type": "player", "invincible": False}, {"type": "enemy", "damage": dmg}):
            return f"💥 受到 {dmg} 点伤害"
        case ({"type": "player", "invincible": True}, {"type": "enemy"}):
            return "✨ 无敌状态，免疫伤害"
        
        # 玩家拾取道具
        case ({"type": "player"}, {"type": "powerup", "effect": effect}):
            return f"⭐ 获得强化: {effect}"
        
        # 子弹击中敌人
        case ({"type": "bullet", "damage": dmg}, {"type": "enemy", "hp": hp}):
            return f"🎯 击中敌人！造成 {dmg} 伤害"
        
        # 玩家到达终点
        case ({"type": "player"}, {"type": "goal"}):
            return "🎉 关卡完成！"
        
        # 玩家碰到陷阱
        case ({"type": "player"}, {"type": "trap", "damage": dmg}):
            return f"⚠️  触发陷阱！受到 {dmg} 点伤害"
        
        # 无碰撞
        case _:
            return None

# 测试碰撞
player_normal = {"type": "player", "invincible": False}
player_invincible = {"type": "player", "invincible": True}

objects = [
    {"type": "coin", "value": 10},
    {"type": "enemy", "damage": 15},
    {"type": "powerup", "effect": "speed_boost"},
    {"type": "goal"},
    {"type": "trap", "damage": 10}
]

print("普通状态的玩家：")
for obj in objects:
    result = check_collision(player_normal, obj)
    if result:
        print(f"  {str(obj):50s} -> {result}")

print("\n无敌状态的玩家：")
result = check_collision(player_invincible, {"type": "enemy", "damage": 15})
print(f"  碰到敌人 -> {result}")

# 测试子弹碰撞
bullet = {"type": "bullet", "damage": 25}
enemy = {"type": "enemy", "hp": 100}
print(f"\n子弹碰撞：")
print(f"  {check_collision(bullet, enemy)}")

# 示例 4：装备系统
print("\n[示例 4] 装备系统：\n")

def equip_item(item, slot, character):
    """装备物品"""
    match (item, slot, character):
        # 武器
        case (
            {"type": "weapon", "subtype": wtype, "attack": atk},
            "weapon",
            {"class": cclass}
        ) if can_use_weapon(wtype, cclass):
            return f"⚔️  装备 {wtype}（+{atk} 攻击力）"
        case ({"type": "weapon", "subtype": wtype}, "weapon", {"class": cclass}):
            return f"❌ {cclass} 不能使用 {wtype}"
        
        # 护甲
        case (
            {"type": "armor", "subtype": atype, "defense": def_val},
            slot,
            _
        ) if atype == slot:
            return f"🛡️  装备 {atype}（+{def_val} 防御力）"
        
        # 饰品
        case ({"type": "accessory", "effect": effect}, "accessory", _):
            return f"✨ 装备饰品（效果: {effect}）"
        
        # 插槽不匹配
        case ({"type": item_type}, slot, _):
            return f"❌ {item_type} 不能装备在 {slot} 插槽"
        
        case _:
            return "❌ 无法装备"

def can_use_weapon(weapon_type, character_class):
    """检查职业是否可以使用武器"""
    weapon_classes = {
        "sword": ["warrior", "knight"],
        "staff": ["mage", "priest"],
        "bow": ["archer", "ranger"],
        "dagger": ["rogue", "assassin"]
    }
    return character_class in weapon_classes.get(weapon_type, [])

# 测试装备
warrior = {"class": "warrior", "level": 10}
mage = {"class": "mage", "level": 8}

equipment = [
    ({"type": "weapon", "subtype": "sword", "attack": 50}, "weapon", warrior),
    ({"type": "weapon", "subtype": "staff", "attack": 30}, "weapon", mage),
    ({"type": "weapon", "subtype": "sword", "attack": 50}, "weapon", mage),
    ({"type": "armor", "subtype": "helmet", "defense": 20}, "helmet", warrior),
    ({"type": "armor", "subtype": "chest", "defense": 40}, "chest", warrior),
    ({"type": "accessory", "effect": "fire_resistance"}, "accessory", warrior)
]

for item, slot, char in equipment:
    result = equip_item(item, slot, char)
    print(f"{char['class']:10s} 装备 {item['subtype'] if 'subtype' in item else item['type']:12s} -> {result}")

# 示例 5：任务系统
print("\n[示例 5] 任务系统：\n")

def check_quest_completion(quest, player_progress):
    """检查任务完成情况"""
    match (quest, player_progress):
        # 击杀任务
        case (
            {"type": "kill", "target": enemy, "count": required},
            {"killed": {target: killed}} as progress
        ) if enemy == target and killed >= required:
            return f"✅ 任务完成！击杀了 {killed}/{required} 个 {enemy}"
        case ({"type": "kill", "target": enemy, "count": required}, {"killed": killed_dict}):
            current = killed_dict.get(enemy, 0)
            return f"⏳ 进度: {current}/{required} 个 {enemy}"
        
        # 收集任务
        case (
            {"type": "collect", "item": item_name, "count": required},
            {"collected": {item: count}}
        ) if item_name == item and count >= required:
            return f"✅ 任务完成！收集了 {count}/{required} 个 {item_name}"
        case ({"type": "collect", "item": item_name, "count": required}, {"collected": collected}):
            current = collected.get(item_name, 0)
            return f"⏳ 进度: {current}/{required} 个 {item_name}"
        
        # 探索任务
        case (
            {"type": "explore", "locations": required_locs},
            {"visited": visited_locs}
        ):
            missing = set(required_locs) - set(visited_locs)
            if not missing:
                return f"✅ 任务完成！探索了所有地点"
            else:
                return f"⏳ 还需探索: {', '.join(missing)}"
        
        # 对话任务
        case (
            {"type": "talk", "npc": npc_name},
            {"talked_to": npcs}
        ) if npc_name in npcs:
            return f"✅ 任务完成！已与 {npc_name} 对话"
        case ({"type": "talk", "npc": npc_name}, _):
            return f"⏳ 需要与 {npc_name} 对话"
        
        case _:
            return "❓ 未知任务类型"

# 测试任务系统
quests = [
    ({"type": "kill", "target": "goblin", "count": 10}, {"killed": {"goblin": 10}}),
    ({"type": "kill", "target": "goblin", "count": 10}, {"killed": {"goblin": 7}}),
    ({"type": "collect", "item": "herb", "count": 5}, {"collected": {"herb": 5}}),
    ({"type": "collect", "item": "herb", "count": 5}, {"collected": {"herb": 3}}),
    ({"type": "explore", "locations": ["forest", "cave", "mountain"]}, 
     {"visited": ["forest", "cave", "mountain"]}),
    ({"type": "explore", "locations": ["forest", "cave", "mountain"]}, 
     {"visited": ["forest", "cave"]}),
    ({"type": "talk", "npc": "village_elder"}, {"talked_to": ["village_elder", "merchant"]}),
    ({"type": "talk", "npc": "village_elder"}, {"talked_to": ["merchant"]})
]

for quest, progress in quests:
    result = check_quest_completion(quest, progress)
    print(f"[{quest['type']:8s}] {result}")

print("\n💡 总结：match/case 让游戏逻辑更清晰、更易维护")

