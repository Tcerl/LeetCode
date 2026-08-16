# 04. Chiến Lược Deploy — Từ "Chạy Script" Đến "Không Ai Nhận Ra Đã Deploy"

> Cấu hình GitHub Actions cụ thể đã có ở [`CI_CD_Automation_GithubActions.md`](../../10-DevOps-Architect/CI_CD_Automation_GithubActions.md). File này tập trung vào **chiến lược release** — thứ quyết định deploy có an toàn hay không, độc lập với công cụ CI/CD nào đang dùng.

---

## 1. Các chiến lược deploy — chọn theo mức độ chấp nhận rủi ro

| Chiến lược | Cách hoạt động | Rollback | Phù hợp |
|---|---|---|---|
| **Recreate** | Tắt hết instance cũ, bật instance mới | Chậm, có downtime | Môi trường dev/staging, không quan trọng uptime |
| **Rolling Update** | Thay dần từng phần instance cũ bằng mới | Vừa phải | Đa số ứng dụng web thông thường (mặc định K8s) |
| **Blue-Green** | Dựng hẳn 1 môi trường mới (Green) song song, chuyển traffic tức thì khi sẵn sàng | **Tức thì** — chuyển traffic ngược lại Blue | Hệ thống cần rollback cực nhanh, chấp nhận tốn gấp đôi tài nguyên trong lúc deploy |
| **Canary** | Chuyển dần % nhỏ traffic (VD: 5%) sang bản mới, tăng dần nếu ổn | Nhanh, chỉ ảnh hưởng % nhỏ user | Hệ thống traffic lớn, muốn phát hiện bug thật trước khi ảnh hưởng toàn bộ user |

### 🔥 Case thật: Vì sao Canary phát hiện được bug mà staging không phát hiện được

Staging test với dữ liệu giả, traffic giả, quy mô nhỏ. Nhiều bug **chỉ xuất hiện ở quy mô thật** (race condition khi có hàng nghìn user đồng thời, edge case dữ liệu thật mà môi trường test không có). Canary giải quyết đúng vấn đề này: cho 5% traffic THẬT chạy qua bản mới, theo dõi error rate/latency, nếu bất thường thì tự động rollback trước khi ảnh hưởng 100% user — đây là kỹ thuật các công ty lớn (Google, Netflix, Amazon) dùng thường xuyên cho mọi thay đổi quan trọng.

---

## 2. Feature Flag — tách "deploy code" khỏi "bật tính năng"

Đây là kỹ thuật senior dùng để giảm rủi ro deploy xuống gần 0, độc lập với chiến lược deploy ở trên:

```python
# Deploy code MỚI lên production nhưng tính năng VẪN TẮT — an toàn tuyệt đối
if feature_flags.is_enabled("new_checkout_flow", user_id=current_user.id):
    return new_checkout_flow()
return legacy_checkout_flow()
```

**Lợi ích thật:** code mới có thể nằm im trên production hàng ngày/hàng tuần trước khi bật cho user thật — tách rời hoàn toàn "rủi ro deploy" (code có lỗi cú pháp/crash) khỏi "rủi ro tính năng" (logic nghiệp vụ sai). Khi có vấn đề, **tắt flag tức thì** (không cần deploy lại/rollback code) — nhanh hơn rollback truyền thống rất nhiều, và có thể bật riêng cho từng nhóm user để test dần (kết hợp trực tiếp với Canary).

---

## 3. Database Migration trong CI/CD — nơi dễ gây sự cố nhất

**Sai lầm kinh điển:** migration đổi schema (VD: đổi tên cột, xóa cột) chạy **đồng thời** với deploy code mới — nếu rollback code do bug, code CŨ giờ chạy với schema MỚI → crash toàn bộ. Nguyên tắc senior — **migration phải tương thích ngược (backward-compatible) qua từng bước nhỏ**:

```
Bước 1: Thêm cột mới (KHÔNG xóa cột cũ) — deploy, code cũ vẫn chạy bình thường
Bước 2: Deploy code MỚI, ghi vào CẢ 2 cột (cũ + mới), đọc từ cột mới
Bước 3: Chạy backfill dữ liệu cũ sang cột mới
Bước 4: Deploy code, ngừng ghi vào cột cũ
Bước 5: (Sau khi chắc chắn ổn định) Migration riêng để xóa cột cũ
```

Đây gọi là **expand-contract pattern** — tốn nhiều bước hơn "đổi 1 phát", nhưng đảm bảo ở BẤT KỲ thời điểm nào trong quá trình rollout, cả code cũ và code mới đều chạy được với schema hiện tại — cho phép rollback an toàn ở mọi bước.

---

## 4. Pipeline gates — không phải mọi merge đều nên tự động deploy production

```yaml
# Pipeline thật cần các "cổng chặn" trước khi tới production, không chỉ chạy test rồi deploy luôn
Build → Unit Test → Integration Test → Security Scan (SAST/dependency check)
      → Deploy Staging → Smoke Test tự động → [Manual Approval nếu cần] → Deploy Production (Canary)
      → Theo dõi metric tự động → Auto rollback nếu error rate tăng bất thường
```

**Nguyên tắc senior:** mức độ tự động hóa tăng dần theo độ tin cậy đã chứng minh của team/hệ thống — team mới/hệ thống quan trọng nên có bước approval thủ công trước khi vào production; team trưởng thành với đủ test coverage + canary + auto-rollback có thể tự động hóa hoàn toàn (continuous deployment thật sự).

---

## 🎯 Câu hỏi senior hay hỏi khi review

1. "Nếu deploy này lỗi, bạn rollback trong bao lâu — và có tự động không hay phải người can thiệp thủ công?"
2. "Migration này có tương thích ngược không? Nếu phải rollback code sau khi đã chạy migration, hệ thống có crash không?"
3. "Tính năng rủi ro này có nằm sau feature flag không, hay phụ thuộc hoàn toàn vào việc code không có bug?"

## 🔗 Liên kết module khác
- Rolling update ở tầng container là nền tảng kỹ thuật cho các chiến lược này → [`03-Container-Orchestration-In-Practice`](../03-Container-Orchestration-In-Practice/README.md)
- Theo dõi metric để quyết định rollback tự động → [`05-Observability-Incident-Response`](../05-Observability-Incident-Response/README.md)
