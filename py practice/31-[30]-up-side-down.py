is_it = False
try:
    n = int(input('enter the value '))
    is_it = True
except:
    print('error value, pls replay') 
if is_it:
    if n<0 or n >9:
        print('pls from 1 to 9')
    else:
        for i in range (n): #đi ngược (star, end, step)
            for j in range(n-i, 0, -1):
                print(j, end=' ')
            print('')


#vd và giải thích nếu n = 4
#Chắc chắn! Để hiểu rõ hơn về cách hoạt động của đoạn mã khi giá trị `n = 4`, chúng ta sẽ mô tả từng vòng lặp chi tiết.

#Khi `n = 4`, mã sẽ thực hiện như sau:

#1. **Kiểm tra điều kiện nhập liệu hợp lệ:**
#    - Giả sử người dùng nhập `4`, mã sẽ xác định đây là giá trị hợp lệ và chuyển đến bước tiếp theo.

#2. **Vòng lặp ngoài chạy từ `i = 0` đến `i = n-1` (tức `i = 3`):**
#    ```python
#    for i in range(n):
#    ```

#3. **Mô tả từng vòng lặp:**

#    - **Vòng lặp thứ nhất (`i = 0`):**
#        ```python
 #       for j in range(n-i, 0, -1):
#        ```
 #       - `range(4-0, 0, -1)` sẽ là `range(4, 0, -1)`.
  #      - Điều này có nghĩa là vòng lặp `j` sẽ chạy từ `4` đến `1`:
   #         - `j = 4`, in `4`
    #        - `j = 3`, in `3`
     #       - `j = 2`, in `2`
      #      - `j = 1`, in `1`
      #  - Dòng kết quả: `4 3 2 1`

#    - **Vòng lặp thứ hai (`i = 1`):**
#        ```python
 #       for j in range(n-i, 0, -1):
  #      ```
   #     - `range(4-1, 0, -1)` sẽ là `range(3, 0, -1)`.
    #    - Điều này có nghĩa là vòng lặp `j` sẽ chạy từ `3` đến `1`:
     #       - `j = 3`, in `3`
      #      - `j = 2`, in `2`
       #     - `j = 1`, in `1`
#        - Dòng kết quả: `3 2 1`

 #   - **Vòng lặp thứ ba (`i = 2`):**
  #      ```python
   #     for j in range(n-i, 0, -1):
    #    ```
     #   - `range(4-2, 0, -1)` sẽ là `range(2, 0, -1)`.
      #  - Điều này có nghĩa là vòng lặp `j` sẽ chạy từ `2` đến `1`:
#            - `j = 2`, in `2`
 #           - `j = 1`, in `1`
  #      - Dòng kết quả: `2 1`
#
 #   - **Vòng lặp thứ tư (`i = 3`):**
  #      ```python
   #     for j in range(n-i, 0, -1):
    #    ```
     #   - `range(4-3, 0, -1)` sẽ là `range(1, 0, -1)`.
      #  - Điều này có nghĩa là vòng lặp `j` sẽ chạy từ `1` đến `1`:
#            - `j = 1`, in `1`
 #       - Dòng kết quả: `1`
