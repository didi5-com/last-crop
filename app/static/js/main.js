document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const analyzeBtn = document.getElementById('analyze-btn');
    const uploadContainer = document.getElementById('upload-container');
    const scannerOverlay = document.getElementById('scanner-overlay');
    const scanningImg = document.getElementById('scanning-img');
    const statusText = document.getElementById('status-text');
    const progressBar = document.getElementById('progress-bar');
    const cameraBtn = document.getElementById('camera-btn');
    const cameraContainer = document.getElementById('camera-container');
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture-btn');
    const closeCameraBtn = document.getElementById('close-camera');
    const themeToggle = document.getElementById('theme-toggle');

    // Theme Toggle Logic
    const currentTheme = localStorage.getItem('theme') || 'dark';
    document.body.className = currentTheme === 'dark' ? 'bg-slate-900 text-white min-h-screen font-sans' : 'bg-slate-50 text-slate-900 min-h-screen font-sans';
    updateThemeIcon(currentTheme);

    themeToggle.addEventListener('click', () => {
        const theme = document.body.classList.contains('bg-slate-900') ? 'light' : 'dark';
        document.body.className = theme === 'dark' ? 'bg-slate-900 text-white min-h-screen font-sans' : 'bg-slate-50 text-slate-900 min-h-screen font-sans';
        localStorage.setItem('theme', theme);
        updateThemeIcon(theme);
    });

    function updateThemeIcon(theme) {
        const icon = themeToggle.querySelector('i');
        icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }

    // Camera Logic
    let stream = null;

    cameraBtn.addEventListener('click', async (e) => {
        e.stopPropagation(); // Prevent dropZone click
        try {
            stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
            video.srcObject = stream;
            cameraContainer.classList.remove('hidden');
            dropZone.classList.add('hidden');
            gsap.from(cameraContainer, { opacity: 0, scale: 0.9, duration: 0.5 });
        } catch (err) {
            alert("Camera access denied or not available.");
        }
    });

    closeCameraBtn.addEventListener('click', () => {
        stopCamera();
        cameraContainer.classList.add('hidden');
        dropZone.classList.remove('hidden');
    });

    captureBtn.addEventListener('click', () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0);
        
        canvas.toBlob((blob) => {
            const file = new File([blob], "camera_capture.jpg", { type: "image/jpeg" });
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            fileInput.files = dataTransfer.files;
            handleFile(file);
            stopCamera();
            cameraContainer.classList.add('hidden');
        }, 'image/jpeg');
    });

    function stopCamera() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            stream = null;
        }
    }

    // Animations with GSAP
    gsap.from('#hero-title', { opacity: 0, y: 30, duration: 1, ease: 'power3.out' });
    gsap.from('#hero-sub', { opacity: 0, y: 20, duration: 1, delay: 0.3, ease: 'power3.out' });
    gsap.from('#upload-container', { opacity: 0, scale: 0.9, duration: 1, delay: 0.6, ease: 'back.out(1.7)' });

    // Drag and Drop Logic
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('border-green-500', 'bg-slate-700/50');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('border-green-500', 'bg-slate-700/50');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('border-green-500', 'bg-slate-700/50');
        const file = e.dataTransfer.files[0];
        handleFile(file);
    });

    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        handleFile(file);
    });

    function handleFile(file) {
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                scanningImg.src = e.target.result;
                previewContainer.classList.remove('hidden');
                dropZone.classList.add('hidden');
                gsap.from(previewContainer, { opacity: 0, y: 20, duration: 0.5 });
            };
            reader.readAsDataURL(file);
        }
    }

    function showError(message) {
        // Create toast or notification
        const toast = document.createElement('div');
        toast.className = 'fixed bottom-8 left-1/2 transform -translate-x-1/2 bg-red-600 text-white px-6 py-3 rounded-xl shadow-2xl z-[100] flex items-center space-x-3 animate-bounce';
        toast.innerHTML = `
            <i class="fas fa-exclamation-circle"></i>
            <span>${message}</span>
        `;
        document.body.appendChild(toast);
        setTimeout(() => {
            gsap.to(toast, { opacity: 0, y: 20, duration: 0.5, onComplete: () => toast.remove() });
        }, 4000);
    }

    // Analysis Logic
    analyzeBtn.addEventListener('click', async () => {
        const file = fileInput.files[0] || null;
        if (!file) {
            showError("Please select an image first.");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        // Show Scanner
        scannerOverlay.classList.remove('hidden');
        document.body.style.overflow = 'hidden';

        const stages = [
            { text: "Validating Image Quality...", progress: 20 },
            { text: "Checking for Plant Structures...", progress: 40 },
            { text: "Identifying Crop Type...", progress: 60 },
            { text: "Analyzing Disease Patterns...", progress: 80 },
            { text: "Generating Treatment Plan...", progress: 100 }
        ];

        // Simulate progress while waiting for API
        let stageIdx = 0;
        const interval = setInterval(() => {
            if (stageIdx < stages.length) {
                statusText.innerText = stages[stageIdx].text;
                progressBar.style.width = `${stages[stageIdx].progress}%`;
                stageIdx++;
            }
        }, 800);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            clearInterval(interval);

            if (data.success) {
                // Smooth transition to result page
                progressBar.style.width = '100%';
                statusText.innerText = "Finalizing Report...";
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 1000);
            } else {
                showError(data.error || "Analysis failed.");
                scannerOverlay.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }
        } catch (error) {
            clearInterval(interval);
            showError("Network error. Please check your connection.");
            scannerOverlay.classList.add('hidden');
            document.body.style.overflow = 'auto';
        }
    });
});
