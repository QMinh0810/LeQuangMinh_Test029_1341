import math


class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Tính số cột và số hàng của ma trận
        num_of_columns = key
        num_of_rows = math.ceil(len(text) / key)
        
        # Số ô trống không có ký tự ở hàng cuối cùng
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)
        
        # Tạo mảng để chứa các ký tự được khôi phục theo từng hàng
        decrypted_text = [''] * num_of_rows
        
        col = 0
        row = 0
        
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1 # Di chuyển xuống hàng tiếp theo trong cùng một cột
            
            # Nếu đi hết hàng hoặc chạm vào ô trống ở hàng cuối cùng của cột đó
            if (row == num_of_rows) or (row == num_of_rows - 1 and col >= num_of_columns - num_of_shaded_boxes):
                row = 0
                col += 1
                
        return ''.join(decrypted_text)