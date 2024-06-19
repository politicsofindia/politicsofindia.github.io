<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indian Politics Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            background: url('https://i.ibb.co/nfgVLDX/illustrated-map-of-india-daria-i.jpg') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(5px);
            z-index: -1;
        }

        .container {
            width: 300px;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: rgba(128, 128, 128, 0.8);
            border-radius: 10px;
            border: 2px solid orange;
            position: relative;
        }

        .container h1 {
            color: white;
            margin-bottom: 20px;
        }

        .start-button button {
            padding: 10px 20px;
            font-size: 16px;
            color: orange;
            background-color: transparent;
            border: 2px solid orange;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .start-button button:hover {
            background-color: orange;
            color: white;
        }
    </style>
</head>
<body>
    <div class="overlay"></div>
    <div class="container">
        <h1>Politics of India</h1>
        <section class="start-button">
            <button onclick="startGame()">Start Game</button>
        </section>
    </div>
    <script>
        function startGame() {
            window.location.href = 'game.html'; // Adjust the path to your game page
        }
    </script>
</body>
</html>
