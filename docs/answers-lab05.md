## Câu hỏi thảo luận Lab 05

**1. Ưu, nhược điểm của upstream first so với release first?**
- **Release first (sửa trên release trước):** Ưu điểm là cung cấp bản vá lỗi cực nhanh cho người dùng đang gặp sự cố ở bản release hiện tại. Nhược điểm là lập trình viên rất dễ quên thao tác lan truyền (cherry-pick) bản vá đó về nhánh `master`, khiến lỗi này lại xuất hiện trong các phiên bản cập nhật tương lai.
- **Upstream first (sửa trên master trước):** Ưu điểm là đảm bảo nhánh `master` (và mọi phiên bản sinh ra sau này) luôn có chứa mã sửa lỗi. Nhược điểm là thời gian phát hành bản vá cho người dùng hiện tại có thể bị chậm lại nếu nhánh `master` lúc đó đang bất ổn hoặc pipeline CI đang bị lỗi.

**2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?**
- Lệnh kiểm tra sự tương đương của commit: `git cherry -v origin/master origin/release/lab05`. Nếu quên cherry-pick, kết quả trả về sẽ không có dấu trừ `-` (dấu trừ báo hiệu nhánh kia đã có commit tương đương).
- Hoặc dùng vòng lặp kiểm tra vòng đời của commit: `git tag --contains <FIX_SHA>`. Nếu quên, lệnh sẽ không liệt kê tag tương ứng với lab05.
