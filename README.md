<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Python - Repository</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #3776ab;
            --secondary: #ffd43b;
            --accent: #a855f7;
            --dark: #1a1a2e;
            --light: #f8f9fa;
            --success: #10b981;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--dark) 0%, #2d3561 100%);
            color: #e0e0e0;
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #3776ab 0%, #a855f7 100%);
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(20px); }
        }

        .hero-content {
            position: relative;
            z-index: 2;
            text-align: center;
            animation: slideInUp 1s ease-out;
        }

        .hero h1 {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 20px;
            color: #fff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: fadeInScale 1s ease-out;
        }

        .snake-icon {
            display: inline-block;
            font-size: 3rem;
            animation: bounce 2s ease-in-out infinite;
            margin-right: 15px;
        }

        .subtitle {
            font-size: 1.5rem;
            color: #f0f0f0;
            margin-bottom: 30px;
            animation: fadeIn 1.2s ease-out;
        }

        .cta-button {
            display: inline-block;
            padding: 15px 40px;
            background: #fff;
            color: var(--primary);
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            transition: all 0.3s ease;
            animation: fadeIn 1.4s ease-out;
        }

        .cta-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        /* Main Content */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 30px;
        }

        section {
            margin-bottom: 80px;
            animation: fadeInUp 0.8s ease-out;
        }

        h2 {
            font-size: 2.5rem;
            margin-bottom: 40px;
            position: relative;
            display: inline-block;
            color: #fff;
        }

        h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, var(--secondary), var(--accent));
            border-radius: 2px;
            animation: expandWidth 0.6s ease-out;
        }

        /* Grid Layout */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 50px;
        }

        .card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            animation: fadeInUp 0.8s ease-out;
        }

        .card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.1);
            border-color: var(--accent);
            box-shadow: 0 20px 40px rgba(168, 85, 247, 0.2);
        }

        .card h3 {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: var(--secondary);
        }

        .card ul {
            list-style: none;
        }

        .card li {
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
            color: #b0b0b0;
            transition: all 0.3s ease;
        }

        .card li::before {
            content: '→';
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: bold;
        }

        .card:hover li {
            color: #e0e0e0;
            transform: translateX(5px);
        }

        /* Structure Section */
        .structure {
            background: rgba(255, 255, 255, 0.03);
            padding: 40px;
            border-radius: 15px;
            border-left: 4px solid var(--accent);
            font-family: 'Courier New', monospace;
            font-size: 1rem;
            line-height: 2;
            color: #90ee90;
            animation: slideInRight 0.8s ease-out;
            overflow-x: auto;
        }

        /* Goals Section */
        .goals {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }

        .goal-item {
            display: flex;
            align-items: center;
            padding: 20px;
            background: rgba(16, 185, 129, 0.1);
            border-radius: 10px;
            border-left: 4px solid var(--success);
            animation: fadeInLeft 0.8s ease-out;
        }

        .goal-icon {
            font-size: 2rem;
            margin-right: 20px;
        }

        .goal-text {
            font-size: 1.1rem;
        }

        /* Tech Stack */
        .tech-stack {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }

        .tech-item {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 25px;
            background: linear-gradient(135deg, rgba(55, 118, 171, 0.2), rgba(168, 85, 247, 0.2));
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            animation: fadeInUp 0.8s ease-out;
        }

        .tech-item:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, rgba(55, 118, 171, 0.4), rgba(168, 85, 247, 0.4));
            border-color: var(--accent);
        }

        .tech-item span {
            font-size: 1.5rem;
            margin-right: 10px;
        }

        /* Progress Timeline */
        .progress-timeline {
            position: relative;
            padding: 20px 0;
        }

        .progress-item {
            padding: 20px 0 20px 50px;
            position: relative;
            animation: fadeInLeft 0.8s ease-out;
        }

        .progress-item::before {
            content: '';
            position: absolute;
            left: 12px;
            top: 25px;
            width: 20px;
            height: 20px;
            background: var(--success);
            border-radius: 50%;
            border: 3px solid var(--dark);
            transition: all 0.3s ease;
        }

        .progress-item.in-progress::before {
            background: var(--secondary);
            animation: pulse 2s ease-in-out infinite;
        }

        .progress-item.pending::before {
            background: #6b7280;
        }

        .progress-item::after {
            content: '';
            position: absolute;
            left: 21px;
            top: 40px;
            width: 2px;
            height: 60px;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.2), transparent);
        }

        .progress-item:last-child::after {
            display: none;
        }

        .progress-label {
            font-size: 1.1rem;
            color: #e0e0e0;
        }

        /* Animations */
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes fadeInLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInScale {
            from {
                opacity: 0;
                transform: scale(0.8);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        @keyframes expandWidth {
            from { width: 0; }
            to { width: 60px; }
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }

        /* Code Block */
        .code-block {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
            color: #90ee90;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 40px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #6b7280;
            margin-top: 60px;
        }

        .footer-text {
            font-size: 1.2rem;
            animation: fadeIn 1s ease-out;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }

            .subtitle {
                font-size: 1.2rem;
            }

            h2 {
                font-size: 1.8rem;
            }

            .container {
                padding: 40px 20px;
            }
        }
    </style>
</head>
<body>
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1><span class="snake-icon">🐍</span>Learning Python</h1>
            <p class="subtitle">Master Python from Beginner to Advanced</p>
            <a href="#topics" class="cta-button">Explore Repository</a>
        </div>
    </section>

    <!-- Main Content -->
    <div class="container">
        <!-- About Section -->
        <section>
            <h2>📚 Welcome</h2>
            <p style="font-size: 1.1rem; color: #b0b0b0; margin-top: 30px;">
                This repository contains comprehensive practice programs, detailed notes, and mini-projects for learning Python from beginner to advanced concepts. Perfect for anyone looking to build a strong foundation in data analysis and scientific computing.
            </p>
        </section>

        <!-- Topics Section -->
        <section id="topics">
            <h2>🎯 Topics Covered</h2>
            <div class="grid">
                <div class="card">
                    <h3>🔢 NumPy</h3>
                    <ul>
                        <li>Arrays & Operations</li>
                        <li>Indexing & Slicing</li>
                        <li>Mathematical Functions</li>
                        <li>Statistics</li>
                        <li>Random Module</li>
                    </ul>
                </div>

                <div class="card">
                    <h3>📊 Matplotlib</h3>
                    <ul>
                        <li>Line Plots</li>
                        <li>Bar Charts</li>
                        <li>Scatter Plots</li>
                        <li>Pie Charts & Histograms</li>
                        <li>Advanced Customization</li>
                    </ul>
                </div>

                <div class="card">
                    <h3>🐼 Pandas</h3>
                    <ul>
                        <li>Series & DataFrame</li>
                        <li>CSV File Operations</li>
                        <li>Data Cleaning</li>
                        <li>Filtering & Sorting</li>
                        <li>Data Analysis</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Structure Section -->
        <section>
            <h2>📁 Repository Structure</h2>
            <div class="structure">
                📦 learning-python<br>
                &nbsp;&nbsp;├── 📂 numpy<br>
                &nbsp;&nbsp;├── 📂 matplotlib<br>
                &nbsp;&nbsp;├── 📂 pandas<br>
                &nbsp;&nbsp;└── README.md
            </div>
        </section>

        <!-- Goals Section -->
        <section>
            <h2>🎯 Learning Goals</h2>
            <div class="goals">
                <div class="goal-item">
                    <div class="goal-icon">✅</div>
                    <div class="goal-text">Learn Python Fundamentals</div>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">✅</div>
                    <div class="goal-text">Master Data Analysis Libraries</div>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">✅</div>
                    <div class="goal-text">Improve Problem-Solving</div>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">✅</div>
                    <div class="goal-text">Build ML Foundation</div>
                </div>
            </div>
        </section>

        <!-- Tech Stack -->
        <section>
            <h2>🛠️ Technologies</h2>
            <div class="tech-stack">
                <div class="tech-item">
                    <span>🐍</span>
                    <strong>Python 3</strong>
                </div>
                <div class="tech-item">
                    <span>🔢</span>
                    <strong>NumPy</strong>
                </div>
                <div class="tech-item">
                    <span>📊</span>
                    <strong>Matplotlib</strong>
                </div>
                <div class="tech-item">
                    <span>🐼</span>
                    <strong>Pandas</strong>
                </div>
                <div class="tech-item">
                    <span>💻</span>
                    <strong>VS Code</strong>
                </div>
            </div>
        </section>

        <!-- Setup Section -->
        <section>
            <h2>🚀 Quick Start</h2>
            <div class="code-block">
                # Clone repository<br>
                git clone https://github.com/sumittiruwa/learning_Python_from_apna_college.git<br><br>
                
                # Navigate to project<br>
                cd learning_Python_from_apna_college<br><br>
                
                # Install dependencies<br>
                pip install numpy matplotlib pandas<br><br>
                
                # Run any file<br>
                python filename.py
            </div>
        </section>

        <!-- Progress Section -->
        <section>
            <h2>📈 Learning Progress</h2>
            <div class="progress-timeline">
                <div class="progress-item">
                    <span class="progress-label">✅ Python Basics - Completed</span>
                </div>
                <div class="progress-item">
                    <span class="progress-label">✅ NumPy - Completed</span>
                </div>
                <div class="progress-item">
                    <span class="progress-label">✅ Matplotlib - Completed</span>
                </div>
                <div class="progress-item in-progress">
                    <span class="progress-label">🔄 Pandas - In Progress</span>
                </div>
                <div class="progress-item pending">
                    <span class="progress-label">⏳ More Libraries - Coming Soon</span>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer>
            <p class="footer-text">⭐ If you found this helpful, consider starring the repo on GitHub!</p>
            <p style="margin-top: 20px; color: #4b5563;">Happy Coding! 🚀</p>
        </footer>
    </div>
</body>
</html>