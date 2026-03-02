# 📁 CÁC DỰ ÁN THỰC TẾ - PHÂN TÍCH & CÁC CÂU HỎI KHẢ NĂNG

---

## DỰ ÁN 1: TRADITIONAL MEDICINE TRADE PROMOTION PLATFORM
**Thời gian:** 02/2023 - 12/2023  
**Role:** Full Stack  
**Tech:** Python (Flask), HTML, CSS, PostgreSQL, MongoDB

---

### 🏗️ Architecture Overview
```
Frontend (HTML/CSS/JS)
        ↓ HTTP
Flask Backend (Python)
    ↓           ↓
PostgreSQL    MongoDB
(Users, Orders)  (Products, Categories)
```

### ❓ Câu hỏi có thể bị hỏi

**"Tại sao dùng cả PostgreSQL lẫn MongoDB?"**
> "PostgreSQL cho dữ liệu có quan hệ chặt chẽ: users, orders, transactions.
> MongoDB cho product catalog vì mỗi loại dược liệu có attributes khác nhau
> (cây → có lá/thân/rễ; động vật → các bộ phận khác nhau). 
> JSONB/flexible schema của MongoDB phù hợp hơn."

**"Làm sao connect practitioners, businesses, researchers, consumers?"**
> "Role-based system với 4 user types, permissions khác nhau.
> - Practitioner: đăng thông tin thuốc, case studies
> - Business: list products, manage orders  
> - Researcher: access research data
> - Consumer: browse, order"

**"Scale platform thế nào nếu user tăng 10x?"**
> "1. Add Redis cache cho frequently accessed products
> 2. PostgreSQL read replicas cho queries
> 3. CDN cho static assets (product images)
> 4. Background jobs (Celery) cho emails, reports"

---

### 💻 Code Pattern bạn cần nhớ
```python
# Multi-role authentication
from enum import Enum

class UserRole(Enum):
    PRACTITIONER = "practitioner"
    BUSINESS = "business"
    RESEARCHER = "researcher"
    CONSUMER = "consumer"

def require_roles(*roles):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_user = get_current_user()
            if current_user.role not in roles:
                return jsonify({"error": "Access denied"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@product_bp.route("/", methods=["POST"])
@require_roles(UserRole.BUSINESS, UserRole.PRACTITIONER)
def create_product():
    pass
```

---

## DỰ ÁN 2: eCOMMERCE MIGRATION SERVICES
**Thời gian:** 05/2023 - 12/2024  
**Role:** Backend  
**Tech:** Python 3.8, Docker, MySQL, MariaDB

---

### 🏗️ Architecture Overview
```
Source Platform APIs          Target Platform APIs
(Shopify/Magento/WooCommerce) (PrestaShop/Wix/etc.)
         ↓                              ↑
    Source Adapter              Target Adapter
         ↓                              ↑
    Extract Data  →  Transform  →  Load Data
         ↓
    Migration Engine (Python)
         ↓
    Job Queue (Celery + Redis)
         ↓
    Progress WebSocket → Frontend
```

### ❓ Câu hỏi có thể bị hỏi

**"Làm sao handle data inconsistency khi migrate?"**
```python
class MigrationValidator:
    def validate_product(self, product: dict) -> ValidationResult:
        errors = []
        
        # Required fields
        if not product.get("sku"):
            errors.append("SKU is required")
        
        # Business rules
        if product.get("price", 0) < 0:
            errors.append("Price cannot be negative")
        
        # Reference integrity
        if product.get("category_id"):
            if not self.category_exists(product["category_id"]):
                errors.append(f"Category {product['category_id']} not found")
        
        return ValidationResult(is_valid=len(errors) == 0, errors=errors)
```

**"Làm sao đảm bảo migration không mất data?"**
> 1. **Pre-migration**: Count source records, checksum data
> 2. **During**: Transaction per batch, log mọi record
> 3. **Post-migration**: Count target records, spot-check samples
> 4. **Rollback**: Keep source unchanged, drop target nếu fail

**"Tại sao dùng Docker trong dự án này?"**
> "Mỗi eCommerce source cần different API client libraries.
> Shopify SDK, Magento 2 API, WooCommerce REST client - có thể conflict.
> Docker isolates dependencies per service.
> Cũng đảm bảo dev environment = production environment."

**"PrestaShop connection error - bạn debug thế nào?"**
> "Dùng logging verbose, test từng step riêng lẻ.
> Phát hiện driver version incompatibility với MariaDB.
> Solution: Pin specific driver version, document cho team.
> Thêm integration test để catch sớm."

---

### 💻 Code Pattern bạn cần nhớ
```python
# Adapter Pattern cho multiple platforms
from abc import ABC, abstractmethod

class ECommerceAdapter(ABC):
    @abstractmethod
    def get_products(self, page: int, page_size: int) -> list:
        pass
    
    @abstractmethod
    def get_orders(self, since: datetime) -> list:
        pass
    
    @abstractmethod
    def get_customers(self) -> list:
        pass

class ShopifyAdapter(ECommerceAdapter):
    def __init__(self, shop_url: str, api_key: str, password: str):
        self.client = ShopifyClient(shop_url, api_key, password)
    
    def get_products(self, page: int, page_size: int) -> list:
        return self.client.Product.find(page=page, limit=page_size)
    
    def get_orders(self, since: datetime) -> list:
        return self.client.Order.find(created_at_min=since.isoformat())
    
    def get_customers(self) -> list:
        return self.client.Customer.find()

class WooCommerceAdapter(ECommerceAdapter):
    def __init__(self, url: str, consumer_key: str, consumer_secret: str):
        self.api = WooCommerceAPI(url=url, consumer_key=consumer_key, 
                                   consumer_secret=consumer_secret)
    
    def get_products(self, page: int, page_size: int) -> list:
        return self.api.get("products", params={"page": page, "per_page": page_size}).json()
    
    def get_orders(self, since: datetime) -> list:
        return self.api.get("orders", params={"after": since.isoformat()}).json()
    
    def get_customers(self) -> list:
        return self.api.get("customers").json()


# Factory
def create_adapter(platform: str, credentials: dict) -> ECommerceAdapter:
    adapters = {
        "shopify": ShopifyAdapter,
        "woocommerce": WooCommerceAdapter,
        "magento": MagentoAdapter,
        "prestashop": PrestaShopAdapter,
    }
    adapter_class = adapters.get(platform)
    if not adapter_class:
        raise ValueError(f"Unsupported platform: {platform}")
    return adapter_class(**credentials)
```

---

## DỰ ÁN 3: VIET KIOSK - HOSPITAL & BANKING
**Thời gian:** 03/2024 - 12/2024  
**Role:** Full Stack / Front-end Developer  
**Tech:** Next.js, RESTful APIs, WebSockets

---

### 🏗️ Architecture Overview
```
Kiosk Terminal (Next.js)
    ↓ HTTPS          ↓ WebSocket
Backend (Viettel)   Real-time Updates
    ↓
BIDV Payment Gateway
```

### ❓ Câu hỏi có thể bị hỏi

**"WebSocket trong dự án này dùng thế nào?"**
> "Real-time cập nhật số thứ tự khám bệnh.
> Server push ngay khi bác sĩ gọi bệnh nhân, kiosk hiển thị ngay.
> Giúp bệnh nhân không cần reload, UX tốt hơn."

**"BIDV Banking integration - security considerations?"**
> "1. HTTPS/TLS cho mọi communication
> 2. Signature verification (HMAC) cho webhook từ BIDV
> 3. Idempotency key để tránh duplicate charges
> 4. Audit log mọi transaction
> 5. Timeout và retry với circuit breaker"

**"Kiosk bị offline thì xử lý thế nào?"**
> "Offline-first design:
> - LocalStorage cache patient data
> - Background sync khi reconnect
> - Clear UI messaging khi offline
> - Critical features phải hoạt động offline (in biên lai)"

---

### 💻 Code Pattern bạn cần nhớ
```javascript
// Next.js WebSocket với reconnection
import { useEffect, useRef, useState } from 'react';

function useWebSocket(url) {
    const [status, setStatus] = useState('connecting');
    const [data, setData] = useState(null);
    const wsRef = useRef(null);
    const reconnectTimeout = useRef(null);

    const connect = () => {
        wsRef.current = new WebSocket(url);
        
        wsRef.current.onopen = () => setStatus('connected');
        
        wsRef.current.onmessage = (event) => {
            const payload = JSON.parse(event.data);
            setData(payload);
        };
        
        wsRef.current.onclose = () => {
            setStatus('disconnected');
            // Auto-reconnect sau 3 giây
            reconnectTimeout.current = setTimeout(connect, 3000);
        };
    };

    useEffect(() => {
        connect();
        return () => {
            clearTimeout(reconnectTimeout.current);
            wsRef.current?.close();
        };
    }, [url]);

    return { status, data };
}

// Sử dụng
function KioskDisplay() {
    const { status, data } = useWebSocket('wss://viettel-api.vn/queue');
    
    return (
        <div>
            {status === 'disconnected' && <Alert>Mất kết nối, đang kết nối lại...</Alert>}
            {data && <PatientDisplay queue={data} />}
        </div>
    );
}
```

---

## DỰ ÁN 4: AI-POWERED RECRUITMENT ECOSYSTEM (MBW SUITE)
**Thời gian:** 01/2025 - 02/2026  
**Role:** Full Stack Web Developer  
**Tech:** Python, Frappe Framework, Vue 3, MySQL, LLMs, MATLAB MCR, React (Vite)

---

### 🏗️ Architecture Overview
```
                    MBW Suite
    ┌─────────────────────────────────────────┐
    │  MBW_Press  │  MBW_Admin  │  MBW_ATS   │
    │  MBW_MIRA   │  MBW_MIA   │  MBW_CMS   │
    │                 MBW_MJOB               │
    └─────────────────────────────────────────┘
              ↓
    Python Flask/Frappe Backend
         ↓          ↓         ↓
    MySQL DB    LLM APIs   MATLAB MCR
                            ↓
                   Candidate Scoring Algorithm
```

### ❓ Câu hỏi có thể bị hỏi

**"Làm sao integrate 6+ microservices trong một platform?"**
> "Dùng Frappe Framework như application server chính.
> Frappe có built-in: authentication, permissions, REST APIs, real-time.
> Mỗi MBW app là Frappe app riêng, share database và authentication.
> Communication qua Frappe's event system và REST APIs nội bộ."

**"LLM integration - làm sao tránh hallucination trong CV generation?"**
> "1. **Structured output**: Yêu cầu LLM trả JSON schema cụ thể
> 2. **Few-shot prompting**: Provide 3-5 examples của CV đẹp
> 3. **Validation layer**: Verify output matches schema, reject nếu không
> 4. **Human review**: Flag CV cần review trước khi send
> 5. **Fallback**: Template-based nếu LLM fail"

**"MATLAB scoring - làm sao ensure accuracy?"**
> "1. Unit tests với known inputs/outputs (validate từ MATLAB IDE)
> 2. Cross-validation: Run cả Python fallback và MATLAB, compare
> 3. Monitoring: Log difference nếu > threshold
> 4. Regression testing mỗi deployment
> 5. A/B test với sample candidates trước khi production"

**"6 out of 8 apps - tại sao không làm tất cả?"**
> "Honest về scope: Timeline giới hạn, 6 apps core đã cover full hiring lifecycle.
> MBW_Press (tin tuyển dụng), MBW_Admin (quản trị), MBW_ATS (applicant tracking),
> MBW_account (tài khoản), MBW_MIRA (AI resume), MBW_MIA (AI interview),
> MBW_CMS (content), MBW_MJOB (job matching).
> 2 apps còn lại là v2 features, planned cho next phase."

---

### 💻 Code Pattern bạn cần nhớ
```python
# LLM CV Generation với validation
import openai
from pydantic import BaseModel, Field
from typing import List, Optional

class CVSection(BaseModel):
    title: str
    content: str
    
class GeneratedCV(BaseModel):
    summary: str = Field(..., min_length=50, max_length=500)
    experience: List[CVSection]
    education: List[CVSection]
    skills: List[str] = Field(..., min_items=3)
    
class CVGenerationService:
    def __init__(self, openai_client: openai.OpenAI):
        self.client = openai_client
        
    def generate_cv(self, candidate_info: dict) -> GeneratedCV:
        prompt = self._build_prompt(candidate_info)
        
        for attempt in range(3):  # retry 3 lần
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4-turbo-preview",
                    messages=[
                        {"role": "system", "content": "You are a professional CV writer. Always respond with valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.7
                )
                
                raw = response.choices[0].message.content
                # Validate với Pydantic
                cv = GeneratedCV.model_validate_json(raw)
                return cv
                
            except Exception as e:
                if attempt == 2:
                    # Fallback to template
                    return self._template_cv(candidate_info)
                continue
    
    def _build_prompt(self, info: dict) -> str:
        return f"""
        Generate a professional CV based on:
        Name: {info['name']}
        Experience: {info['experience']}
        Skills: {', '.join(info['skills'])}
        
        Return JSON matching: {GeneratedCV.model_json_schema()}
        """
```

---

## 📝 TEMPLATE TRẢ LỜI VỀ DỰ ÁN (STAR METHOD)

```
Khi được hỏi về bất kỳ dự án nào, dùng cấu trúc:

S - Situation: Bối cảnh, vấn đề cần giải quyết
T - Task: Nhiệm vụ cụ thể của bạn
A - Action: Hành động cụ thể BẠN đã làm (dùng "tôi", không "chúng tôi")
R - Result: Kết quả định lượng được

Ví dụ cho eCommerce Migration:
S: "Client cần migrate 50,000 products từ Shopify sang PrestaShop mà không downtime"
T: "Tôi responsible for backend migration engine và PrestaShop integration"
A: "Tôi thiết kế adapter pattern để abstract multipe source/target platforms,
    implement batch processing với checkpoint/resume,
    debug driver incompatibility với MariaDB"
R: "Migration hoàn thành trong 8 tiếng, 0 data loss,
    platform reusable cho nhiều clients khác"
```
