"""
    **Kiến thức:**

- Linked List là cấu trúc dữ liệu gồm các node liên kết với nhau
- Mỗi node chứa data và pointer đến node tiếp theo
- Types: Singly, Doubly, Circular
- Time complexity:
  - Access: O(n) - Phải duyệt từ đầu đến vị trí cần
  - Search: O(n) - Phải duyệt từng node
  - Insert: O(1) - Nếu đã có pointer đến vị trí chèn
  - Delete: O(1) - Nếu đã có pointer đến node cần xóa

**Giải thích chi tiết:**

1. **Cách hoạt động:**

   - Mỗi node chứa data và pointer (next) đến node tiếp theo
   - Head pointer trỏ đến node đầu tiên
   - Node cuối có next = None
   - Không cần bộ nhớ liên tiếp như Array
2. **Khi nào dùng Linked List:**

   - Cần insert/delete thường xuyên ở giữa danh sách
   - Kích thước không biết trước
   - Không cần truy cập ngẫu nhiên qua index
   - Cần implement Stack/Queue
3. **Ưu điểm:**

   - Insert/Delete nhanh O(1) nếu có pointer
   - Kích thước động, không lãng phí bộ nhớ
   - Dễ thêm/xóa phần tử
4. **Nhược điểm:**

   - Truy cập chậm O(n)
   - Tốn thêm bộ nhớ cho pointers
   - Không cache-friendly
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.size = 0
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next.next
            
    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)