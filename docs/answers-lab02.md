# Trả lời câu hỏi thảo luận Lab 02

## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Khi tôi tạo nhánh, master có thể đã tiến lên nhờ các PR khác được merge.
Nếu không đồng bộ, nhánh của tôi dựa trên một trạng thái cũ và có thể
xung đột hoặc lỗi tích hợp với mã mới trên master mà tôi chưa hề biết.

Đồng bộ trước (git fetch rồi git merge origin/master) cho phép:

- Phát hiện xung đột và giải quyết ngay trên nhánh của mình, không làm
  hỏng master.
- Chạy lại chương trình và test trên mã đã tích hợp, nên thứ được review
  sát với thứ sẽ thực sự nằm trên master.
- Giữ nhánh sống ngắn và gần master, tránh "merge hell" khi nhánh lệch xa.

Ví dụ trong bài: nhánh feature/search-by-title của Dev 2 được tạo khi
master chưa có print_cart. Sau khi merge origin/master và chạy main.py,
tôi xác nhận hai tính năng chạy được cùng nhau trước khi mở PR.

## 2. Khi nào không được rebase?

Không được rebase khi các commit đã được chia sẻ, tức đã push và có người
khác dựa vào (checkout, tạo nhánh từ đó, hoặc review). Rebase viết lại
lịch sử: các commit cũ bị thay bằng commit mới có SHA khác. Người khác
vẫn giữ commit cũ nên lịch sử của họ lệch với remote, dễ gây xung đột,
trùng lặp commit hoặc mất công việc.

Cụ thể:

- Không rebase master hoặc release/*.
- Không rebase nhánh mà đồng đội đang dùng chung.
- Chỉ rebase nhánh riêng của mình, và nếu đã push thì phải dùng
  git push --force-with-lease thay vì --force.

Quy tắc của Release Flow: amend, reset, rebase chỉ dùng cho commit chưa
chia sẻ. Với lịch sử chung thì dùng merge hoặc revert.

## 3. feature/* khác topic/* ra sao?

Cả hai đều tạo từ master và merge lại vào master, khác nhau ở mục đích:

| | feature/* | topic/* |
|---|---|---|
| Nội dung | Thay đổi chức năng của sản phẩm | Chủ đề không đổi chức năng |
| Ví dụ trong bài | feature/cart-print, feature/search-by-title | topic/pr-template, topic/use-case-diagram |
| Ảnh hưởng | Thêm hoặc đổi hành vi chương trình | Tài liệu, cấu hình, quy trình |

Tên nhánh nói lên mục đích (một nhánh, một mục đích), giúp người review
biết cần kiểm tra điều gì: với feature thì kiểm tra hành vi và test, với
topic thì kiểm tra nội dung tài liệu hoặc cấu hình.
