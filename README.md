Cải tiến thuật toán Whale Optimization Algorithm (WOA)
1. Giới thiệu
Thuật toán Whale Optimization Algorithm (WOA) là một phương pháp metaheuristic dựa trên hành vi săn mồi của loài cá voi. Tuy nhiên, thuật toán gốc có một số hạn chế trong khả năng khai thác và tìm kiếm không gian lời giải. Do đó, chúng tôi đề xuất một số cải tiến để nâng cao hiệu suất của WOA, tập trung vào cơ chế cập nhật vị trí, vận tốc và tìm kiếm cục bộ.
2. Các cải tiến đề xuất
2.1 Cơ chế mới và thay đổi
Bỏ cơ chế tìm kiếm ngẫu nhiên, thay bằng tìm kiếm cục bộ: Giảm phạm vi tìm kiếm, tập trung vào khai thác lời giải tiềm năng. (1)
Lưu trữ cá thể tốt nhất cục bộ và toàn cục: Lưu trữ cá thể tốt nhất từng vòng lặp để giúp điều chỉnh phạm vi tìm kiếm và tăng khả năng khai thác các lời giải tiềm năng. (2)
Khởi tạo và tính toán vận tốc cho mỗi cá thể mỗi vòng lặp: Giúp điều chỉnh linh hoạt quỹ đạo di chuyển của cá thể. (3)
Thay đổi công thức cập nhật cá thể mới bằng vận tốc: Tận dụng quán tính của hạt để cập nhật vị trí, tương tự cơ chế của thuật toán PSO. (4)
2.2 Công thức mới được sử dụng
(1) Khởi tạo cá thể trong phạm vi hẹp quanh cá thể tốt nhất
	
Trong đó:
minbs và maxbs là giá trị cận dưới và cận trên của cá thể tốt nhất tại vòng lặp hiện tại.
Giúp thuật toán khai thác tốt hơn những vùng tiềm năng.
(3) Cập nhật vận tốc
Trong đó:
C1 giảm tuyến tính từ 1 - 0 , giúp giảm sự lệ thuộc vào cục bộ.
C2 tăng từ 0.1 - 1 , giúp tăng khả năng khai thác vùng tốt nhất.
W giảm từ 2 - 0 , điều chỉnh mức độ tìm kiếm từ rộng sang hẹp.
(4) Cập nhật vị trí cá thể
Công thức này giúp cá thể dao động xung quanh , tạo sự cân bằng giữa khai thác và tìm kiếm.

3. Mã giả
Khởi tạo ma trận V
Các tham số w, c1, c2
While t < T do
	For I to N
		Giảm dần c1, tăng dần c2
		Tính w, Vi
		Random p
		If(p < 0.5):
  			Tính A
  			If(|A| < 1):
  				Sử dụng encircling cũ của cá voi
  			Else:
         Sử dụng cơ chế Khởi tạo cá thể trong phạm vi hẹp quanh cá thể tốt nhất (1) 
  			End if
		Else:
			Sử dụng cơ chế attacking mới sử dụng V (4)
		End if
		So sánh và cập nhật tốt nhất cục bộ của từng cá thể
	End for
	So sánh và cập nhật cá thể tốt nhất toàn cục dựa trên cá thể cục bộ
End while
	
	
	
		
3. Kết luận
Các cải tiến trên giúp thuật toán WOA:
Tăng khả năng khai thác cục bộ bằng cách thu hẹp phạm vi tìm kiếm.
Điều chỉnh linh hoạt vận tốc giúp kiểm soát quỹ đạo di chuyển của cá thể.
Giảm sự ngẫu nhiên trong cập nhật vị trí, giúp hội tụ ổn định hơn.

