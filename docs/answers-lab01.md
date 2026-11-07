## Câu hỏi thảo luận Lab 01

**1. Vì sao dùng git mv?**
Thay vì dùng lệnh `mv` thông thường của hệ điều hành, lệnh `git mv` giúp Git lập tức hiểu và ghi nhận đây là hành động đổi tên hoặc di chuyển file. Việc này giúp bảo toàn được toàn bộ lịch sử commit trước đây của file đó, thay vì hiểu nhầm là bạn vừa xóa một file cũ và tạo một file mới tinh.

**2. release/lab01 có phải baseline không?**
Có. Nhánh này đóng vai trò là một baseline vì nó đánh dấu một trạng thái mã nguồn đã được chốt (đóng băng) tại một thời điểm cụ thể để nộp bài. Ta không phát triển thêm các tính năng mới trực tiếp trên nhánh này nữa.

**3. Vì sao không commit thẳng master dù làm một mình?**
Để rèn luyện thói quen tuân thủ quy trình kiểm soát thay đổi (Change Control). Việc tách nhánh và đi qua quy trình Pull Request giúp mã nguồn luôn được kiểm thử và review cẩn thận trước khi hợp nhất. Điều này bảo vệ nhánh `master` luôn sạch và trong trạng thái ổn định nhất.
