# 🗄️ DATABASE - ÔN THI PHỎNG VẤN

---

## 1. SQL CƠ BẢN & NÂNG CAO

### 1.1 JOINs - Loại và khi nào dùng
```sql
-- INNER JOIN: Chỉ lấy records có match ở CẢ HAI bảng
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: Lấy TẤT CẢ từ bảng trái, NULL nếu không có match
-- Ví dụ: Lấy tất cả users, kể cả chưa có đơn hàng
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

-- RIGHT JOIN: Ngược lại LEFT JOIN (ít dùng)

-- FULL OUTER JOIN: Tất cả từ cả hai bảng
-- PostgreSQL hỗ trợ, MySQL dùng UNION của LEFT + RIGHT

-- CROSS JOIN: Tích Descartes (mọi cặp kết hợp)
SELECT * FROM colors CROSS JOIN sizes;  -- 3 colors × 4 sizes = 12 rows
```

> **🎯 Dùng khi nào?**
> - **INNER**: Data analysis, lọc chỉ records có quan hệ
> - **LEFT**: Báo cáo (users + orders kể cả chưa mua hàng)
> - **FULL OUTER**: So sánh 2 nguồn dữ liệu (migration verification!)

---

### 1.2 Subquery vs CTE vs JOIN
```sql
-- Subquery: Khó đọc, có thể chậm
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 1000);

-- CTE (Common Table Expression) - dễ đọc hơn, tái sử dụng
WITH high_value_orders AS (
    SELECT user_id, SUM(total) as total_spent
    FROM orders
    GROUP BY user_id
    HAVING SUM(total) > 1000
),
loyal_customers AS (
    SELECT user_id FROM orders
    GROUP BY user_id
    HAVING COUNT(*) > 5
)
SELECT u.name, hvo.total_spent
FROM users u
JOIN high_value_orders hvo ON u.id = hvo.user_id
JOIN loyal_customers lc ON u.id = lc.user_id;

-- Recursive CTE: Cho hierarchical data (category tree, org chart)
WITH RECURSIVE category_tree AS (
    -- Base case
    SELECT id, name, parent_id, 0 as level
    FROM categories WHERE parent_id IS NULL

    UNION ALL

    -- Recursive case
    SELECT c.id, c.name, c.parent_id, ct.level + 1
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level;
```

> **🎯 Dùng khi nào?**
> - **CTE**: Query phức tạp nhiều bước, hierarchical data
> - **JOIN**: Hiệu quả nhất với proper indexes
> - **Subquery**: Chỉ dùng khi không thể JOIN

---

### 1.3 Window Functions
```sql
-- ROW_NUMBER, RANK, DENSE_RANK
SELECT
    name,
    salary,
    department,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank_in_dept,
    RANK() OVER (ORDER BY salary DESC) as overall_rank,
    LAG(salary) OVER (ORDER BY salary) as prev_salary,
    LEAD(salary) OVER (ORDER BY salary) as next_salary
FROM employees;

-- Running total
SELECT
    date,
    amount,
    SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) as running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg_7d
FROM sales;

-- Lấy top N per group (ví dụ: top 3 sản phẩm bán chạy mỗi category)
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY sales DESC) as rn
    FROM products
)
SELECT * FROM ranked WHERE rn <= 3;
```

> **🎯 Dùng khi nào?**
> - **ROW_NUMBER**: Pagination, deduplication, top-N per group
> - **LAG/LEAD**: So sánh với record trước/sau (growth rate)
> - **Running total**: Dashboard metrics, financial reports

---

### 1.4 Indexes và Performance
```sql
-- Tạo index
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at DESC);
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Partial index (PostgreSQL) - index chỉ một phần data
CREATE INDEX idx_active_users ON users(email) WHERE is_active = true;

-- Full-text search index
CREATE INDEX idx_posts_content_fts ON posts USING GIN(to_tsvector('english', content));

-- Xem query plan
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123 AND status = 'pending';
-- Tìm: "Seq Scan" → thiếu index, "Index Scan" → có index
```

> **🎯 Khi nào cần index?**
> - Cột dùng trong WHERE, JOIN ON, ORDER BY
> - **Composite index**: `(user_id, created_at)` - thứ tự quan trọng!
> - **Không index**: Cột ít distinct values (boolean, status với 3 giá trị)
> - **Trade-off**: Index tốn storage và làm chậm INSERT/UPDATE

> **❓ Câu hỏi phỏng vấn hay:** "Tại sao query vẫn chậm dù có index?"
> → Có thể query không dùng index (function trên cột, implicit cast), hoặc data skew

---

### 1.5 Transactions và ACID
```sql
-- Transactions
BEGIN;
    UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
    UPDATE accounts SET balance = balance + 1000 WHERE id = 2;
    -- Nếu lỗi ở đây, ROLLBACK hoàn tác cả 2
COMMIT;

-- Isolation levels
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;  -- Default PostgreSQL
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;     -- Strictest

-- Deadlock prevention
-- Luôn lock theo thứ tự nhất quán
-- Ex: luôn lock id nhỏ trước: UPDATE WHERE id = MIN(id1, id2)
```

> **🎯 ACID:**
> - **A**tomicity: Tất cả hoặc không gì cả
> - **C**onsistency: Không vi phạm constraints
> - **I**solation: Transactions không ảnh hưởng nhau
> - **D**urability: Commit rồi thì không mất dù crash

---

## 2. POSTGRESQL CỤ THỂ

### 2.1 JSON/JSONB
```sql
-- JSONB: lưu binary JSON, có thể index và query
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    attributes JSONB  -- thay vì nhiều cột optional
);

INSERT INTO products VALUES (1, 'Laptop', '{"RAM": "16GB", "CPU": "i7", "tags": ["tech", "sale"]}');

-- Query JSONB
SELECT * FROM products WHERE attributes->>'RAM' = '16GB';
SELECT * FROM products WHERE attributes @> '{"tags": ["sale"]}';

-- Index JSONB
CREATE INDEX idx_products_attrs ON products USING GIN(attributes);
```

### 2.2 Array Types
```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    tags TEXT[]  -- array column
);

INSERT INTO posts VALUES (1, 'Python Tips', ARRAY['python', 'tutorial', 'flask']);

-- Query arrays
SELECT * FROM posts WHERE 'python' = ANY(tags);
SELECT * FROM posts WHERE tags @> ARRAY['python', 'flask'];  -- contains
```

> **🎯 Dùng JSONB khi nào?**
> - Schema linh hoạt (product attributes khác nhau mỗi loại)
> - Lưu config, metadata
> - Trong dự án eCommerce của bạn: Product variants, custom fields

---

## 3. MONGODB

### 3.1 CRUD Operations
```javascript
// Insert
db.users.insertOne({
    name: "Tin",
    email: "tin@example.com",
    skills: ["Python", "Flask"],
    createdAt: new Date()
});

// Find với query operators
db.users.find({
    age: { $gte: 18, $lte: 30 },
    skills: { $in: ["Python", "JavaScript"] },
    "address.city": "Hanoi"  // nested field
});

// Update
db.users.updateOne(
    { _id: ObjectId("...") },
    {
        $set: { name: "New Name" },
        $push: { skills: "Vue.js" },
        $inc: { loginCount: 1 }
    }
);

// Delete
db.users.deleteMany({ isActive: false, lastLogin: { $lt: new Date("2024-01-01") } });
```

### 3.2 Aggregation Pipeline
```javascript
// Pipeline: [ stage1, stage2, stage3, ... ]
db.orders.aggregate([
    // Stage 1: Filter
    { $match: { status: "completed", createdAt: { $gte: new Date("2024-01-01") } } },

    // Stage 2: Join với users collection
    { $lookup: {
        from: "users",
        localField: "userId",
        foreignField: "_id",
        as: "user"
    }},

    // Stage 3: Unwind array
    { $unwind: "$user" },

    // Stage 4: Group và aggregate
    { $group: {
        _id: "$user.country",
        totalRevenue: { $sum: "$total" },
        orderCount: { $sum: 1 },
        avgOrderValue: { $avg: "$total" }
    }},

    // Stage 5: Sort
    { $sort: { totalRevenue: -1 } },

    // Stage 6: Limit
    { $limit: 10 }
]);
```

> **🎯 Aggregation pipeline - quan trọng!**
> - Thay thế cho SQL GROUP BY + JOIN
> - Xử lý data transformation trong DB
> - Trong dự án MBW của bạn: Phân tích candidate data

### 3.3 Indexes trong MongoDB
```javascript
// Single field index
db.users.createIndex({ email: 1 }, { unique: true });

// Compound index
db.orders.createIndex({ userId: 1, createdAt: -1 });

// Text index cho full-text search
db.products.createIndex({ name: "text", description: "text" });
db.products.find({ $text: { $search: "laptop gaming" } });

// TTL index - tự động xóa expired documents
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });
```

---

## 4. DATABASE DESIGN PATTERNS

### 4.1 Normalization
```
1NF: Không có repeating groups, mỗi cell là atomic value
2NF: 1NF + Không có partial dependency (với composite PK)
3NF: 2NF + Không có transitive dependency (A→B→C thì tách ra)

Ví dụ denormalize hợp lý:
- Orders table lưu user_name dù có FK tới users
  (Vì tên user có thể thay đổi, order cần lịch sử)
```

### 4.2 Migration Pattern
```python
# Alembic migration (Python)
# Tạo migration
# flask db migrate -m "Add user role column"

def upgrade():
    op.add_column("users",
        sa.Column("role", sa.String(50), nullable=False, server_default="user")
    )
    op.create_index("idx_users_role", "users", ["role"])

def downgrade():
    op.drop_index("idx_users_role", "users")
    op.drop_column("users", "role")
```

> **🎯 Quy tắc migration:**
> - Luôn có cả `upgrade()` và `downgrade()`
> - Không xóa column trong cùng release với code dùng nó
> - Thêm column với default value, KHÔNG nullable
> - Trong dự án eCommerce Migration của bạn: Migrate data từ Shopify → PrestaShop

---

## 5. CONNECTION POOLING

```python
# SQLAlchemy connection pool
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # Số kết nối trong pool
    max_overflow=20,       # Kết nối thêm khi pool đầy
    pool_timeout=30,       # Chờ tối đa 30s cho connection
    pool_recycle=3600,     # Recycle connection sau 1h
    pool_pre_ping=True     # Test connection trước khi dùng
)
```

> **🎯 Tại sao cần connection pooling?**
> - Tạo DB connection tốn ~50-300ms
> - Pool tái sử dụng connection → giảm latency
> - Giới hạn concurrent connections tránh quá tải DB

---

## 6. SQL vs NoSQL - KHI NÀO CHỌN CÁI NÀO?

| Tiêu chí | SQL (PostgreSQL, MySQL) | NoSQL (MongoDB) |
|----------|------------------------|-----------------|
| **Schema** | Fixed, structured | Flexible, dynamic |
| **ACID** | Đầy đủ | Eventual consistency (tunable) |
| **Query** | Phức tạp với JOINs | Đơn giản, denormalized |
| **Scale** | Vertical (mạnh hơn) | Horizontal (thêm node) |
| **Use case** | Financial, ERP, eCommerce | Content, IoT, real-time analytics |
| **Relationships** | Many-to-many dễ | Phải embed hoặc reference |

> **🎯 Trong dự án của bạn:**
> - **PostgreSQL**: Users, orders (cần ACID)
> - **MongoDB**: Traditional medicine products (schema linh hoạt), candidate profiles (MBW)
> - **MariaDB/MySQL**: eCommerce migration (tương thích với Shopify, Magento)

---

## ✅ CHECKLIST DATABASE

- [ ] Giải thích các loại JOIN và ví dụ thực tế
- [ ] N+1 problem và giải pháp (eager loading, JOIN)
- [ ] Index: khi nào cần, composite index ordering
- [ ] ACID properties với ví dụ thực tế
- [ ] MongoDB aggregation pipeline
- [ ] SQL vs NoSQL - khi nào chọn cái nào
- [ ] Connection pooling tại sao cần
- [ ] CTE và window functions
