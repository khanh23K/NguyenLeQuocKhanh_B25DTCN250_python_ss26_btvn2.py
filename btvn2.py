from abc import ABC, abstractmethod


# Lớp cha trừu tượng
class Hero(ABC):

    @abstractmethod
    def use_ultimate(self):
        pass


# Pháp Sư
class Mage(Hero):

    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Sát Thủ
class Assassin(Hero):

    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# -------------------------
# KỊCH BẢN CHẠY GAME
# -------------------------

print("--- LOADING TRẬN ĐẤU ---")

team_heroes = [
    Mage(),
    Assassin()
]

print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")

for hero in team_heroes:
    hero.use_ultimate()
# 1. Vòng lặp hero.use_ultimate() thể hiện tính Đa hình như thế nào?

# Vì cùng một lời gọi use_ultimate() nhưng mỗi loại nhân vật sẽ thực hiện hành động khác nhau. Hệ thống không cần biết đó là Pháp Sư hay Sát Thủ, chỉ cần gọi chung một phương thức.

# 2. Game văng lỗi vào lúc nào? Vì sao nguy hiểm?

# Lỗi chỉ xảy ra khi trận đấu bắt đầu và hệ thống gọi chiêu cuối của Assassin. Báo lỗi muộn như vậy rất nguy hiểm vì người chơi đã vào trận bình thường rồi mới bị crash, gây mất trải nghiệm và khó phát hiện lỗi.

# 3. Nếu dùng abc và @abstractmethod thì lỗi xuất hiện khi nào?

# Lỗi sẽ xuất hiện ngay lúc khởi tạo đối tượng Assassin (giai đoạn loading trận đấu), vì Python phát hiện lớp này chưa cài đặt phương thức bắt buộc use_ultimate().

# 4. Nguyên lý Fail Fast được thể hiện như thế nào?

# Fail Fast nghĩa là phát hiện lỗi càng sớm càng tốt. Khi dùng Abstract Base Class, lỗi được báo ngay lúc tạo đối tượng thay vì đợi đến khi giao tranh mới phát sinh, giúp sửa lỗi nhanh và tránh game bị crash giữa trận.