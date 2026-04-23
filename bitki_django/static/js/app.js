// Akıllı Bahçe Ana JavaScript Dosyası

document.addEventListener('DOMContentLoaded', () => {
    // 1. Tema Ayarları (Dark Mode)
    const savedTheme = localStorage.getItem('theme');
    const htmlRoot = document.getElementById('html-root');
    const themeIcons = document.querySelectorAll('#themeIcon, #themeIcon2');
    const themeLabel = document.getElementById('themeLabel');

    if (savedTheme === 'dark') {
        htmlRoot.classList.add('dark');
        themeIcons.forEach(icon => icon.textContent = 'light_mode');
        if(themeLabel) themeLabel.textContent = 'Gündüz Modu';
    }

    window.toggleDark = function() {
        htmlRoot.classList.toggle('dark');
        const isDark = htmlRoot.classList.contains('dark');
        
        if (isDark) {
            localStorage.setItem('theme', 'dark');
            themeIcons.forEach(icon => icon.textContent = 'light_mode');
            if(themeLabel) themeLabel.textContent = 'Gündüz Modu';
        } else {
            localStorage.setItem('theme', 'light');
            themeIcons.forEach(icon => icon.textContent = 'dark_mode');
            if(themeLabel) themeLabel.textContent = 'Gece Modu';
        }
    };

    // 2. Dropdown Menüler (Bildirim & Kullanıcı)
    const notifPanel = document.getElementById('notifPanel');
    const userPanel = document.getElementById('userPanel');

    window.toggleNotif = function() {
        if(notifPanel.style.display === 'none' || notifPanel.style.display === '') {
            notifPanel.style.display = 'block';
            if(userPanel) userPanel.style.display = 'none';
        } else {
            notifPanel.style.display = 'none';
        }
    };

    window.toggleUserMenu = function() {
        if(userPanel.style.display === 'none' || userPanel.style.display === '') {
            userPanel.style.display = 'block';
            if(notifPanel) notifPanel.style.display = 'none';
        } else {
            userPanel.style.display = 'none';
        }
    };

    // Dışarı Tıklanınca Kapatma
    window.addEventListener('click', function(e) {
        const notifWrap = document.getElementById('notifWrap');
        const userWrap = document.getElementById('userWrap');
        
        if (notifPanel && notifWrap && !notifWrap.contains(e.target)) {
            notifPanel.style.display = 'none';
        }
        if (userPanel && userWrap && !userWrap.contains(e.target)) {
            userPanel.style.display = 'none';
        }
    });

    window.markAllRead = function() {
        const unreadItems = document.querySelectorAll('.notif-item.unread');
        unreadItems.forEach(item => {
            item.classList.remove('unread');
        });
        const badge = document.getElementById('notifBadge');
        if(badge) badge.style.display = 'none';
    };

    // 3. Saat / Tarih Gösterimi
    const timeEl = document.getElementById('currentTime');
    const dateEl = document.getElementById('currentDate');

    function updateTime() {
        if(!timeEl || !dateEl) return;
        const now = new Date();
        timeEl.textContent = now.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' });
        dateEl.textContent = now.toLocaleDateString('tr-TR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    }
    
    if(timeEl && dateEl) {
        updateTime();
        setInterval(updateTime, 60000); // Her dakika güncelle
    }

    // 4. Panel İçi Fonksiyonlar (Thirsty Filter)
    window.filterThirsty = function(val) {
        const list = document.getElementById('thirstyList');
        if(!list) return;
        const items = list.getElementsByClassName('plant-item');
        const lowerVal = val.toLowerCase();
        
        for (let item of items) {
            const text = item.textContent.toLowerCase();
            if (text.includes(lowerVal)) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        }
    };

    // 5. Not Yönetimi (AJAX Simülasyonu / Gerçekte Fetch API kullanılabilir)
    const noteDisplay = document.getElementById('noteDisplay');
    const noteEdit = document.getElementById('noteEdit');
    const noteText = document.getElementById('noteText');

    window.editNote = function() {
        if(!noteDisplay || !noteEdit) return;
        noteDisplay.style.display = 'none';
        noteEdit.style.display = 'block';
    };

    window.cancelNote = function() {
        if(!noteDisplay || !noteEdit) return;
        noteDisplay.style.display = 'block';
        noteEdit.style.display = 'none';
    };

    window.saveNote = async function(plantId) {
        if(!noteText) return;
        const content = noteText.value;
        const csrfToken = typeof CSRF !== 'undefined' ? CSRF : '';

        // Eğer backend hazır değilse simüle et:
        /*
        try {
            const response = await fetch('/api/note/save/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ plant_id: plantId, content: content })
            });
            if(response.ok) {
                // UI Güncelle
            }
        } catch(e) { console.error(e); }
        */

        // Basit UI Güncellemesi (Backend entegrasyonu tamamlanana kadar)
        noteDisplay.innerHTML = `<span class="material-symbols-outlined quote-icon">format_quote</span><p>"${content}"</p>`;
        noteDisplay.classList.remove('empty');
        cancelNote();
    };

    // 6. Sulama Butonu (AJAX)
    window.waterPlant = async function(plantId) {
        const btn = document.getElementById('waterBtn');
        const btnText = document.getElementById('waterBtnText');
        const csrfToken = typeof CSRF !== 'undefined' ? CSRF : '';

        if(btn) {
            btn.classList.add('loading'); // CSS'te loading state tanımlanabilir
            btnText.textContent = 'Sulanıyor...';
            btn.disabled = true;
        }

        // Backend entegrasyonu simülasyonu
        setTimeout(() => {
            if(btn) {
                btn.classList.remove('loading');
                btn.classList.replace('btn-primary', 'btn-secondary');
                btnText.textContent = 'Bugün Sulandı';
                const icon = btn.querySelector('.material-symbols-outlined');
                if(icon) icon.style.color = 'var(--primary)';
            }
        }, 1000);
    };

    // 7. AI Teşhis Animasyonu
    window.simulateDiagnosis = function() {
        const uploadArea = document.getElementById('uploadArea');
        const progressArea = document.getElementById('progressArea');
        const resultArea = document.getElementById('resultArea');

        if(uploadArea && progressArea) {
            uploadArea.style.display = 'none';
            progressArea.style.display = 'block';

            let progress = 0;
            const bar = document.getElementById('progressBar');
            const percent = document.getElementById('progressText');

            const interval = setInterval(() => {
                progress += Math.floor(Math.random() * 15) + 5;
                if(progress > 100) progress = 100;
                
                if(bar) bar.style.width = progress + '%';
                if(percent) percent.textContent = progress + '%';

                if(progress === 100) {
                    clearInterval(interval);
                    setTimeout(() => {
                        progressArea.style.display = 'none';
                        if(resultArea) resultArea.style.display = 'block';
                    }, 500);
                }
            }, 300);
        }
    };
});
