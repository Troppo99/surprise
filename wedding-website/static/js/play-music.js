const tracks = [
        "music/Naruto - Homecoming.mp3",
        "music/Naruto - Gentle Hands.mp3",
        "music/Naruto - Samidare.mp3",
        "music/Naruto - Nindo.mp3",
        "music/Naruto - Companions.mp3"
      ];

      let idx = 0;
      const player = document.getElementById("player");

      function play(index) {
        player.src = tracks[index];
        player.play();
      }

      player.addEventListener("ended", () => {
        idx = (idx + 1) % tracks.length; // maju, lalu balik ke 0
        play(idx);
      });

      play(idx); // mulai otomatis