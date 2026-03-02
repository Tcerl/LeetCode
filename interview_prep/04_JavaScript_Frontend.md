# ⚡ JAVASCRIPT & FRONTEND - ÔN THI PHỎNG VẤN

---

## 1. JAVASCRIPT CORE

### 1.1 var vs let vs const
```javascript
// var: function scoped, hoisted (đẩy lên đầu function), có thể re-declare
function example() {
    console.log(x); // undefined (hoisted, không error!)
    var x = 5;
    console.log(x); // 5
    
    if (true) {
        var y = 10;  // accessible outside if block!
    }
    console.log(y); // 10 - var không có block scope
}

// let: block scoped, không hoisted (Temporal Dead Zone)
{
    // console.log(a); // ReferenceError: TDZ!
    let a = 1;
    console.log(a); // 1
}
// console.log(a); // ReferenceError: out of scope

// const: block scoped, phải khởi tạo, không thể reassign
const PI = 3.14159;
// PI = 3; // TypeError!

// Nhưng: object/array const có thể thay đổi content!
const arr = [1, 2, 3];
arr.push(4); // OK - thay đổi content
// arr = []; // TypeError - thay đổi reference
```

> **🎯 Best practice:** Luôn dùng `const`, khi cần re-assign thì dùng `let`. **Không dùng `var`.**

---

### 1.2 Closures và Scope
```javascript
// Practical closure: counter
function createCounter(initial = 0) {
    let count = initial;  // private
    
    return {
        increment() { return ++count; },
        decrement() { return --count; },
        reset() { count = initial; },
        value() { return count; }
    };
}

const counter = createCounter(10);
console.log(counter.increment()); // 11
console.log(counter.value());     // 11

// Classic closure bug với var!
const funcs = [];
for (var i = 0; i < 3; i++) {
    funcs.push(() => console.log(i)); // tất cả capture cùng 'i'
}
funcs[0](); // 3 (bug!)
funcs[1](); // 3 (bug!)

// Fix với let (block scope per iteration)
const funcs2 = [];
for (let i = 0; i < 3; i++) {
    funcs2.push(() => console.log(i));
}
funcs2[0](); // 0 ✓
funcs2[1](); // 1 ✓
```

---

### 1.3 Prototype và this
```javascript
// Prototype chain
function Animal(name) {
    this.name = name;
}
Animal.prototype.speak = function() {
    return `${this.name} makes a sound`;
};

// ES6 Class (syntax sugar cho prototype)
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
    
    speak() {
        return `${this.name} barks!`;
    }
}

// 'this' context
const obj = {
    name: "Tin",
    greet() {
        console.log(`Hello, ${this.name}`); // 'this' = obj
    },
    greetArrow: () => {
        console.log(`Hello, ${this.name}`); // 'this' = outer (window/undefined!)
    }
};

// bind, call, apply
function introduce(greeting, punctuation) {
    console.log(`${greeting}, I'm ${this.name}${punctuation}`);
}

const person = { name: "Tin" };
introduce.call(person, "Hi", "!");     // Hi, I'm Tin! (immediate call)
introduce.apply(person, ["Hi", "!"]); // same, args as array
const boundIntro = introduce.bind(person, "Hello"); // returns new function
boundIntro(".");  // Hello, I'm Tin.
```

> **🎯 Arrow function và this:**
> - Arrow function **không có own `this`**, inherit từ outer scope
> - Dùng arrow function trong class methods: `this` luôn là class instance
> - Không dùng arrow function làm object methods (mất `this`)

---

### 1.4 Promises và Async/Await
```javascript
// Promise chain
fetch('/api/users')
    .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
    })
    .then(users => {
        return Promise.all(users.map(u => fetch(`/api/users/${u.id}/posts`)));
    })
    .then(responses => Promise.all(responses.map(r => r.json())))
    .catch(err => console.error('Failed:', err))
    .finally(() => setLoading(false));

// Async/Await (dễ đọc hơn)
async function loadUserPosts(userId) {
    try {
        const res = await fetch(`/api/users/${userId}`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const user = await res.json();
        
        const postsRes = await fetch(`/api/users/${userId}/posts`);
        const posts = await postsRes.json();
        
        return { user, posts };
    } catch (error) {
        console.error('Failed to load:', error);
        throw error; // re-throw để caller xử lý
    }
}

// Parallel vs Sequential
// Sequential (chậm hơn - chờ lần lượt)
const user = await fetchUser(id);
const posts = await fetchPosts(id); // chờ user xong

// Parallel (nhanh hơn - chạy đồng thời)
const [user, posts] = await Promise.all([
    fetchUser(id),
    fetchPosts(id)
]);

// Promise.allSettled - khi muốn tất cả complete dù có fail
const results = await Promise.allSettled([api1(), api2(), api3()]);
results.forEach(result => {
    if (result.status === 'fulfilled') console.log(result.value);
    else console.error(result.reason);
});
```

---

### 1.5 Destructuring, Spread, Rest
```javascript
// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

// Object destructuring với rename và default
const { name: fullName = "Anonymous", age = 0, address: { city } = {} } = user;

// Spread operator
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1,2,3,4,5]

const defaults = { theme: 'dark', lang: 'en' };
const userPrefs = { lang: 'vi', notifications: true };
const merged = { ...defaults, ...userPrefs }; // { theme: 'dark', lang: 'vi', notifications: true }

// Practical: Clone và update (immutable pattern)
const updatedUser = { ...user, name: "New Name", updatedAt: Date.now() };
```

---

## 2. NEXT.JS (Framework trong CV)

### 2.1 Rendering Strategies
```javascript
// 1. SSG - Static Site Generation (build time)
// pages/blog/[slug].js
export async function getStaticPaths() {
    const posts = await fetchAllPosts();
    return {
        paths: posts.map(p => ({ params: { slug: p.slug } })),
        fallback: 'blocking' // ISR cho new posts
    };
}

export async function getStaticProps({ params }) {
    const post = await fetchPost(params.slug);
    return {
        props: { post },
        revalidate: 3600 // ISR: regenerate sau 1 giờ
    };
}

// 2. SSR - Server-side Rendering (per request)
export async function getServerSideProps({ req, params }) {
    const session = await getSession(req);
    if (!session) return { redirect: { destination: '/login' } };
    
    const data = await fetchUserDashboard(session.user.id);
    return { props: { data } };
}

// 3. App Router (Next.js 13+)
// app/dashboard/page.tsx
async function DashboardPage() {
    const data = await fetch('https://api.example.com/data', {
        cache: 'no-store'  // SSR
        // cache: 'force-cache' // SSG
        // next: { revalidate: 3600 } // ISR
    });
    const json = await data.json();
    return <Dashboard data={json} />;
}
```

### 2.2 API Routes
```javascript
// pages/api/users/[id].js
export default async function handler(req, res) {
    const { id } = req.query;
    
    if (req.method === 'GET') {
        const user = await db.users.findById(id);
        if (!user) return res.status(404).json({ error: 'Not found' });
        return res.status(200).json(user);
    }
    
    if (req.method === 'PUT') {
        const updated = await db.users.update(id, req.body);
        return res.status(200).json(updated);
    }
    
    res.setHeader('Allow', ['GET', 'PUT']);
    res.status(405).json({ error: `Method ${req.method} not allowed` });
}
```

---

## 3. REACT HOOKS

### 3.1 useState, useEffect, useCallback, useMemo
```javascript
import { useState, useEffect, useCallback, useMemo } from 'react';

function KioskQueue() {
    const [queue, setQueue] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // useEffect: Side effects (fetch, subscriptions, DOM manipulation)
    useEffect(() => {
        let isMounted = true; // prevent state update on unmounted component
        
        async function loadQueue() {
            try {
                const data = await fetchQueue();
                if (isMounted) setQueue(data);
            } catch (err) {
                if (isMounted) setError(err.message);
            } finally {
                if (isMounted) setLoading(false);
            }
        }
        
        loadQueue();
        const interval = setInterval(loadQueue, 5000); // refresh mỗi 5s
        
        return () => {
            isMounted = false;
            clearInterval(interval); // cleanup
        };
    }, []); // [] = chỉ chạy 1 lần khi mount

    // useCallback: Memoize function (tránh re-create mỗi render)
    const handleCallPatient = useCallback((patientId) => {
        callPatient(patientId);
        setQueue(prev => prev.filter(p => p.id !== patientId));
    }, []); // dependencies

    // useMemo: Memoize computed value (expensive calculation)
    const statistics = useMemo(() => ({
        total: queue.length,
        waiting: queue.filter(p => p.status === 'waiting').length,
        avgWaitTime: calculateAvgWait(queue)
    }), [queue]); // recalculate chỉ khi queue thay đổi

    if (loading) return <Spinner />;
    if (error) return <ErrorMessage message={error} />;
    
    return (
        <div>
            <Stats data={statistics} />
            <QueueList items={queue} onCall={handleCallPatient} />
        </div>
    );
}
```

### 3.2 Custom Hooks
```javascript
// Reusable WebSocket hook
function useWebSocket(url) {
    const [connected, setConnected] = useState(false);
    const [lastMessage, setLastMessage] = useState(null);
    const wsRef = useRef(null);

    useEffect(() => {
        const ws = new WebSocket(url);
        wsRef.current = ws;

        ws.onopen = () => setConnected(true);
        ws.onmessage = (e) => setLastMessage(JSON.parse(e.data));
        ws.onclose = () => setConnected(false);

        return () => ws.close();
    }, [url]);

    const sendMessage = useCallback((data) => {
        if (wsRef.current?.readyState === WebSocket.OPEN) {
            wsRef.current.send(JSON.stringify(data));
        }
    }, []);

    return { connected, lastMessage, sendMessage };
}

// Sử dụng
function RealtimeDisplay() {
    const { connected, lastMessage } = useWebSocket('wss://api.hospital.vn/queue');
    
    return (
        <div>
            <ConnectionBadge connected={connected} />
            {lastMessage && <QueueUpdate data={lastMessage} />}
        </div>
    );
}
```

---

## 4. VUE 3 (COMPOSITION API)

### 4.1 Reactivity System
```javascript
import { ref, reactive, computed, watch, watchEffect, onMounted, onUnmounted } from 'vue';

export default {
    setup() {
        // ref: cho primitives (number, string, boolean)
        const count = ref(0);
        // reactive: cho objects
        const candidate = reactive({
            name: '',
            skills: [],
            score: null
        });

        // computed: derived state (auto-update khi dependencies thay đổi)
        const matchingSkills = computed(() =>
            candidate.skills.filter(s => requiredSkills.includes(s))
        );

        // watch: side effects khi data thay đổi
        watch(count, (newVal, oldVal) => {
            console.log(`count: ${oldVal} → ${newVal}`);
        });

        // watchEffect: auto-track dependencies
        watchEffect(() => {
            document.title = `Score: ${candidate.score}`;
        });

        // Lifecycle hooks
        onMounted(async () => {
            const data = await fetchCandidates();
            // populate data
        });

        onUnmounted(() => {
            // cleanup
        });

        return { count, candidate, matchingSkills };
    }
};
```

---

## 5. HTML & CSS CẦN BIẾT

### 5.1 Semantic HTML
```html
<!-- BAD: Div soup -->
<div class="header">
    <div class="nav">...</div>
</div>
<div class="main-content">
    <div class="article">...</div>
</div>

<!-- GOOD: Semantic -->
<header>
    <nav aria-label="Main navigation">
        <ul role="list">
            <li><a href="/">Home</a></li>
        </ul>
    </nav>
</header>
<main>
    <article>
        <h1>Article Title</h1>
        <section>...</section>
    </article>
    <aside aria-label="Related content">...</aside>
</main>
<footer>...</footer>
```

### 5.2 CSS Flexbox vs Grid
```css
/* Flexbox: 1 chiều (row hoặc column) */
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: space-between;
    align-items: stretch;
}

.card {
    flex: 1 1 300px; /* grow, shrink, basis */
}

/* Grid: 2 chiều (rows và columns) */
.dashboard {
    display: grid;
    grid-template-columns: 250px 1fr;  /* sidebar + content */
    grid-template-rows: 60px 1fr auto; /* header + main + footer */
    grid-template-areas:
        "sidebar header"
        "sidebar main"
        "sidebar footer";
    height: 100vh;
}

.sidebar { grid-area: sidebar; }
.header  { grid-area: header; }
.main    { grid-area: main; }
```

### 5.3 CSS Variables
```css
:root {
    --color-primary: #2563eb;
    --color-success: #16a34a;
    --spacing-base: 8px;
    --border-radius: 8px;
    --shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.btn-primary {
    background: var(--color-primary);
    padding: calc(var(--spacing-base) * 1.5) calc(var(--spacing-base) * 3);
    border-radius: var(--border-radius);
}
```

### 5.4 TailwindCSS (trong CV)
```html
<!-- Responsive card -->
<div class="
    bg-white rounded-xl shadow-md
    p-6 m-4
    hover:shadow-lg transition-shadow duration-200
    md:flex md:items-center md:gap-6
    dark:bg-gray-800 dark:text-white
">
    <img class="w-16 h-16 rounded-full object-cover mx-auto md:mx-0" src="...">
    <div>
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Phạm Duy Tín</h3>
        <p class="text-sm text-gray-500 dark:text-gray-400">Junior Python Developer</p>
    </div>
</div>
```

---

## ✅ CHECKLIST JAVASCRIPT & FRONTEND

- [ ] `var` vs `let` vs `const` và hoisting
- [ ] Closure - ứng dụng và bug thường gặp
- [ ] `this` context - arrow function vs regular
- [ ] Promise.all vs Promise.allSettled
- [ ] async/await error handling
- [ ] Next.js SSG vs SSR vs ISR - khi nào dùng
- [ ] React hooks: useEffect cleanup, useCallback, useMemo
- [ ] Vue 3 Composition API: ref vs reactive
- [ ] Flexbox vs Grid - khi nào dùng
