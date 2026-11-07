# Trả lời câu hỏi thảo luận Lab 03

## 1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh, tức điểm chúng
bắt đầu tách ra (xem bằng git merge-base A B). Git merge theo ba chiều: so
sánh merge base với đầu nhánh A và đầu nhánh B. Nếu chỉ một bên đổi một đoạn
thì lấy bên đó. Nếu cả hai bên cùng đổi cùng một đoạn theo cách khác nhau thì
sinh conflict.

Trong bài: feature/show-added-title và master cùng tách từ một commit cũ, cả
hai đều sửa dòng print so với commit đó nên xảy ra conflict.

## 2. Vì sao master/release/* phải dùng revert?

master và release/* là lịch sử chung, mọi người đã pull và dựa vào. Reset
hoặc rebase viết lại lịch sử, đổi SHA, làm lịch sử của đồng đội lệch với
remote và có thể mất công việc. Revert không sửa lịch sử cũ mà thêm một
commit mới đảo ngược thay đổi, nên an toàn, vẫn truy vết được (đổi gì, vì
sao hoàn tác), và đi qua PR để được review. reset chỉ dùng cho commit chưa
push.
