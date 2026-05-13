import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.defense_power = 5

    def attack(self, enemy):
        damage = max(0, self.attack_power - enemy.defense_power)
        enemy.health -= damage
        print(f"{self.name} は {enemy.name} に {damage} のダメージを与えた！")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, player):
        damage = max(0, self.attack_power - player.defense_power)
        player.health -= damage
        print(f"{self.name} は {player.name} に {damage} のダメージを与えた！")

    def is_alive(self):
        return self.health > 0

def main():
    player_name = input("名前を入力してください: ")
    player = Player(player_name)
    enemies = [
        Enemy("ゴブリン", 50, 8, 2),
        Enemy("オーク", 80, 12, 5),
        Enemy("ドラゴン", 200, 20, 10)
    ]

    while player.is_alive():
        enemy = random.choice(enemies)
        print(f"\n野生の {enemy.name} が現れた！")
        while enemy.is_alive() and player.is_alive():
            print(f"\n{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")
            action = input("どうする？ (攻撃[a]/逃げる[r]): ").lower()
            if action in ["attack", "a", "攻撃"]:
                player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(player)
            elif action in ["run", "r", "逃げる"]:
                print("戦いから逃げ出した。")
                break
            else:
                print("無効なコマンドです。もう一度入力してください。")

        if not player.is_alive():
            print("\nゲームオーバー。あなたは死んでしまった。")
            break
        elif not enemy.is_alive():
            print(f"{enemy.name} を倒した！")
            # 敵を再生成
            if enemy.name == "ゴブリン":
                enemies.remove(enemy)
                enemies.append(Enemy("ゴブリン", 50, 8, 2))
            elif enemy.name == "オーク":
                enemies.remove(enemy)
                enemies.append(Enemy("オーク", 80, 12, 5))
            elif enemy.name == "ドラゴン":
                enemies.remove(enemy)
                enemies.append(Enemy("ドラゴン", 200, 20, 10))

if __name__ == "__main__":
    main()
