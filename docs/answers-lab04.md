# Trả lời câu hỏi thảo luận Lab 04

## 1. Vì sao release/* không merge ngược vào master?

release/* là baseline đóng băng, chỉ chứa những gì cần cho bản phát hành.
Mọi thay đổi đi theo chiều master -> release (tạo nhánh từ master). Nếu merge
ngược, các commit chuẩn bị riêng cho release (như nâng phiên bản hotfix 1.0.1)
sẽ lẫn vào master và xung đột với phiên bản đang phát triển (1.1.0). Bản sửa
lỗi cần lên master thì cherry-pick riêng (cherry-pick -x).

So sánh với GitFlow: GitFlow có nhánh develop và release/* merge ngược về
main và develop, nên có nhiều nhánh dài hạn, merge hai chiều, dễ lệch. Release
Flow của học phần chỉ có master làm trục chính, release/* là nhánh bảo trì một
chiều, ít nhánh dài hạn hơn và lịch sử gọn hơn.

## 2. Vì sao lên 1.0.0 mà không phải 0.4.0?

Theo Semantic Versioning, 0.y.z là giai đoạn đầu, API chưa ổn định. 1.0.0 đánh
dấu bản phát hành chính thức đầu tiên, sau khi đã có đủ tính năng cốt lõi
(giỏ hàng, tìm kiếm, giảm giá), có test, quy trình review và kiểm soát phát
hành. Từ 1.0.0, MAJOR chỉ tăng khi phá vỡ tương thích, MINOR khi thêm tính
năng, PATCH khi chỉ sửa lỗi.
