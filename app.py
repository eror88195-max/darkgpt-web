<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DarkGPT - ذكاء اصطناعي بلا حدود</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }

        body {
            background: #0b0b12;
            color: #e0dce8;
            height: 100vh;
            display: flex;
            overflow: hidden;
        }

        /* ===== الشريط الجانبي ===== */
        .sidebar {
            width: 260px;
            background: #12121c;
            border-right: 1px solid #2a1f3a;
            display: flex;
            flex-direction: column;
            padding: 20px 16px;
            flex-shrink: 0;
            height: 100vh;
            overflow-y: auto;
        }

        .sidebar .logo {
            font-size: 22px;
            font-weight: 800;
            color: #b388ff;
            letter-spacing: -0.5px;
            margin-bottom: 28px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .sidebar .logo i {
            font-size: 28px;
            color: #b388ff;
            filter: drop-shadow(0 0 6px #9c27b0);
        }

        .sidebar .new-chat-btn {
            background: #1e1a2e;
            border: 1px solid #3b2a52;
            color: #d4c8f0;
            padding: 12px 16px;
            border-radius: 40px;
            font-weight: 600;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: 0.25s;
            width: 100%;
            margin-bottom: 24px;
        }

        .sidebar .new-chat-btn:hover {
            background: #2a1f3f;
            border-color: #9c27b0;
            box-shadow: 0 0 16px rgba(156, 39, 176, 0.25);
        }

        .sidebar .chat-list {
            list-style: none;
            flex: 1;
        }

        .sidebar .chat-list li {
            padding: 12px 14px;
            border-radius: 12px;
            margin-bottom: 6px;
            font-size: 14px;
            color: #b5aac8;
            cursor: pointer;
            transition: 0.2s;
            display: flex;
            align-items: center;
            gap: 12px;
            border: 1px solid transparent;
        }

        .sidebar .chat-list li:hover {
            background: #1a1728;
            border-color: #2a1f3a;
        }

        .sidebar .chat-list li.active {
            background: #201b30;
            border-color: #7b4b9e;
            color: #eee8f8;
        }

        .sidebar .chat-list li i {
            width: 18px;
            color: #7b4b9e;
        }

        .sidebar .footer-side {
            margin-top: 20px;
            font-size: 12px;
            color: #5a4a72;
            border-top: 1px solid #1e1a2e;
            padding-top: 18px;
            display: flex;
            justify-content: space-between;
        }

        /* ===== المنطقة الرئيسية ===== */
        .main {
            flex: 1;
            display: flex;
            flex-direction: column;
            height: 100vh;
            background: #0e0e16;
            position: relative;
        }

        /* ===== رأس الصفحة ===== */
        .header {
            padding: 16px 28px;
            border-bottom: 1px solid #1a1728;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0b0b12;
        }

        .header .title {
            font-size: 20px;
            font-weight: 700;
            color: #d4c8f0;
            letter-spacing: 0.3px;
        }

        .header .title span {
            color: #b388ff;
        }

        .header .badge {
            background: #1e1a2e;
            padding: 6px 18px;
            border-radius: 40px;
            font-size: 12px;
            color: #9c8bb5;
            border: 1px solid #2a1f3a;
        }

        /* ===== منطقة المحادثة ===== */
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 20px 28px 12px 28px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .message {
            max-width: 80%;
            padding: 16px 20px;
            border-radius: 24px;
            font-size: 15px;
            line-height: 1.6;
            animation: fadeUp 0.3s ease;
        }

        .message.user {
            align-self: flex-end;
            background: #1e1a2e;
            border: 1px solid #2a1f3a;
            color: #d4c8f0;
            border-bottom-right-radius: 6px;
        }

        .message.bot {
            align-self: flex-start;
            background: #16121f;
            border: 1px solid #2f2145;
            color: #e8e0f0;
            border-bottom-left-radius: 6px;
            box-shadow: 0 0 20px rgba(156, 39, 176, 0.05);
        }

        .message.bot .icon-bot {
            display: inline-block;
            margin-left: 10px;
            color: #b388ff;
            font-size: 18px;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ===== منطقة الإدخال السفلية ===== */
        .input-area {
            padding: 14px 28px 22px 28px;
            background: #0b0b12;
            border-top: 1px solid #1a1728;
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .input-area .input-wrapper {
            flex: 1;
            position: relative;
            display: flex;
            align-items: center;
            background: #14111f;
            border-radius: 60px;
            border: 1px solid #2a1f3a;
            transition: 0.25s;
            padding: 4px 6px 4px 18px;
        }

        .input-area .input-wrapper:focus-within {
            border-color: #9c27b0;
            box-shadow: 0 0 24px rgba(156, 39, 176, 0.15);
        }

        .input-area .input-wrapper input {
            flex: 1;
            background: transparent;
            border: none;
            padding: 14px 12px;
            color: #f0ecf8;
            font-size: 15px;
            outline: none;
        }

        .input-area .input-wrapper input::placeholder {
            color: #5a4a72;
        }

        .input-area .input-wrapper .robot-icon {
            background: linear-gradient(135deg, #7b1fa2, #9c27b0);
            width: 48px;
            height: 48px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            color: #fff;
            cursor: pointer;
            transition: 0.25s;
            box-shadow: 0 0 20px rgba(156, 39, 176, 0.35);
            border: none;
            flex-shrink: 0;
        }

        .input-area .input-wrapper .robot-icon:hover {
            transform: scale(1.05);
            box-shadow: 0 0 32px rgba(156, 39, 176, 0.55);
        }

        .input-area .input-wrapper .robot-icon:active {
            transform: scale(0.95);
        }

        /* ===== شريط الخصائص (الأيقونات الأربع) ===== */
        .features-bar {
            display: flex;
            justify-content: center;
            gap: 28px;
            padding: 14px 20px 20px 20px;
            background: #0b0b12;
            border-top: 1px solid #12121c;
            flex-wrap: wrap;
        }

        .features-bar .feature-item {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #8a7aa0;
            font-size: 13px;
            font-weight: 500;
            letter-spacing: 0.2px;
            transition: 0.2s;
        }

        .features-bar .feature-item i {
            font-size: 18px;
            color: #7b4b9e;
            width: 28px;
            text-align: center;
            transition: 0.2s;
        }

        .features-bar .feature-item:hover {
            color: #c4b5e0;
        }

        .features-bar .feature-item:hover i {
            color: #b388ff;
            text-shadow: 0 0 12px rgba(179, 136, 255, 0.4);
        }

        /* ===== التجاوب مع الجوال ===== */
        @media (max-width: 760px) {
            .sidebar {
                display: none;
            }
            .main {
                width: 100%;
            }
            .header .badge {
                display: none;
            }
            .message {
                max-width: 92%;
            }
            .features-bar {
                gap: 12px;
            }
            .features-bar .feature-item {
                font-size: 11px;
            }
            .input-area {
                padding: 12px 16px 16px 16px;
            }
            .input-area .input-wrapper input {
                font-size: 14px;
                padding: 10px 8px;
            }
            .input-area .input-wrapper .robot-icon {
                width: 42px;
                height: 42px;
                font-size: 18px;
            }
        }

        /* سكرول أنيق */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0e0e16;
        }
        ::-webkit-scrollbar-thumb {
            background: #2a1f3a;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #3b2a52;
        }
    </style>
</head>
<body>

<!-- ===== الشريط الجانبي ===== -->
<div class="sidebar">
    <div class="logo">
        <i class="fas fa-robot"></i> DarkGPT
    </div>
    <button class="new-chat-btn" onclick="resetChat()">
        <i class="fas fa-plus-circle"></i> محادثة جديدة
    </button>
    <ul class="chat-list" id="chatList">
        <li class="active"><i class="fas fa-comment-dots"></i> المحادثة الحالية</li>
        <li><i class="fas fa-comment"></i> محادثة سابقة ١</li>
        <li><i class="fas fa-comment"></i> محادثة سابقة ٢</li>
        <li><i class="fas fa-comment"></i> محادثة سابقة ٣</li>
    </ul>
    <div class="footer-side">
        <span><i class="fas fa-shield-alt"></i> خصوصية</span>
        <span>v2.0</span>
    </div>
</div>

<!-- ===== المنطقة الرئيسية ===== -->
<div class="main">

    <!-- رأس الصفحة -->
    <div class="header">
        <div class="title">🧠 <span>DarkGPT</span></div>
        <div class="badge"><i class="fas fa-circle" style="color:#b388ff; font-size:8px; margin-left:8px;"></i> ذكاء بلا حدود</div>
    </div>

    <!-- منطقة المحادثة -->
    <div class="chat-area" id="chatArea">
        <div class="message bot">
            <span class="icon-bot"><i class="fas fa-robot"></i></span>
            مرحباً! أنا DarkGPT، ذكاء اصطناعي بلا حدود. طورني فريق ليوز. اسألني ما تشاء.
        </div>
        <div class="message user">
            مرحباً، كيف حالك؟
        </div>
        <div class="message bot">
            <span class="icon-bot"><i class="fas fa-robot"></i></span>
            أنا بخير، شكراً لسؤالك! أنا هنا لمساعدتك بكل ما تحتاجه، بدون أي قيود.
        </div>
    </div>

    <!-- منطقة الإدخال السفلية -->
    <div class="input-area">
        <div class="input-wrapper">
            <input type="text" id="userInput" placeholder="اكتب سؤالك هنا..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button class="robot-icon" onclick="sendMessage()">
                <i class="fas fa-robot"></i>
            </button>
        </div>
    </div>

    <!-- شريط الخصائص الأربع -->
    <div class="features-bar">
        <div class="feature-item"><i class="fas fa-comments"></i> محادثة ذكية</div>
        <div class="feature-item"><i class="fas fa-brain"></i> فهم متقدم</div>
        <div class="feature-item"><i class="fas fa-bolt"></i> إجابات سريعة</div>
        <div class="feature-item"><i class="fas fa-lock"></i> خصوصية تامة</div>
    </div>

</div>

<script>
    // ===== إرسال الرسالة =====
    async function sendMessage() {
        const input = document.getElementById('userInput');
        const text = input.value.trim();
        if (!text) return;

        const chatArea = document.getElementById('chatArea');

        // إضافة رسالة المستخدم
        const userMsg = document.createElement('div');
        userMsg.className = 'message user';
        userMsg.textContent = text;
        chatArea.appendChild(userMsg);

        input.value = '';
        chatArea.scrollTop = chatArea.scrollHeight;

        // رسالة انتظار البوت
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.innerHTML = `<span class="icon-bot"><i class="fas fa-robot"></i></span> ⏳ جاري التفكير...`;
        chatArea.appendChild(botMsg);
        chatArea.scrollTop = chatArea.scrollHeight;

        try {
            const res = await fetch('/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: text })
            });
            const data = await res.json();

            const reply = data.reply || data.error || '⚠️ حدث خطأ، حاول مجدداً.';
            botMsg.innerHTML = `<span class="icon-bot"><i class="fas fa-robot"></i></span> ${reply}`;

        } catch (e) {
            botMsg.innerHTML = `<span class="icon-bot"><i class="fas fa-robot"></i></span> ❌ خطأ في الاتصال: ${e.message}`;
        }

        chatArea.scrollTop = chatArea.scrollHeight;
    }

    // ===== إعادة ضبط المحادثة (محاكاة) =====
    function resetChat() {
        const chatArea = document.getElementById('chatArea');
        chatArea.innerHTML = `
            <div class="message bot">
                <span class="icon-bot"><i class="fas fa-robot"></i></span>
                تم مسح المحادثة. كيف يمكنني مساعدتك اليوم؟
            </div>
        `;
        document.getElementById('userInput').value = '';
    }

    // ===== النقر على أيقونة الروبوت =====
    document.querySelector('.robot-icon').addEventListener('click', sendMessage);

    // ===== دعم الإدخال بالضغط على Enter =====
    document.getElementById('userInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
</script>

</body>
</html>
