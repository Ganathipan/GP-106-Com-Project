<h1>Rock Paper Scissors Lizard Spock Game</h1>
  <h4>A GP106 Computing Project</h3>
  <p><em>Department of Computer Engineering, Faculty of Engineering, University of Peradeniya</em><br>
  <strong>Batch:</strong> E/21</p>


<h2>Project Overview</h2>
  <p>This project is an extension of the classic Rock Paper Scissors game, adding two new gestures, Lizard and Spock, to increase complexity. The game is implemented using an Arduino and includes hardware components like LEDs, push buttons, and a piezo buzzer.</p>

<h3>The Game Rules:</h3>
    <ul>
        <li>Rock crushes Scissors</li>
        <li>Scissors cuts Paper</li>
        <li>Paper covers Rock</li>
        <li>Rock crushes Lizard</li>
        <li>Lizard poisons Spock</li>
        <li>Spock smashes Scissors</li>
        <li>Scissors decapitates Lizard</li>
        <li>Lizard eats Paper</li>
        <li>Paper disproves Spock</li>
        <li>Spock vaporizes Rock</li>
    </ul>
    <p>You will compete against the computer for seven rounds. The game tracks your choices and the computer’s, using LEDs to display the scores.</p>

<h2>Hardware Components</h2>
    <ul>
        <li><strong>Arduino UNO</strong></li>
        <li><strong>10 LEDs</strong> (for displaying scores and the computer’s choices)</li>
        <li><strong>Piezo buzzer</strong> (for signaling game events)</li>
        <li><strong>6 Push buttons</strong> (for player input and starting/ending the game)</li>
        <li>Breadboard, resistors, jumper wires for circuit construction</li>
    </ul>

    
<h2>Project Features</h2>
    <ul>
        <li><strong>Real-Time Player vs. Computer Rounds:</strong> You play against the computer in seven rounds.</li>
        <li><strong>Score Display with LEDs:</strong> Both player and computer scores are shown with LEDs in binary form.</li>
        <li><strong>Timed Input Selection:</strong> A 3-second window is provided for the player to input their gesture using push buttons.</li>
        <li><strong>Buzzer Notifications:</strong> Different tones to indicate the start, end, and round results.</li>
        <li><strong>Serial Monitor:</strong> The game summary and current round details are displayed via the Arduino serial monitor.</li>
        <li><strong>Game End Indication:</strong> After 7 rounds, all LEDs blink, and a distinct buzzer sound plays to indicate the game’s end.</li>
    </ul>


<h2>Circuit Diagram</h2>
    <p>You can find the circuit diagram in the <code>schematics/</code> folder or view it online <a href="Circuite_Image.jfif">here</a>.</p>

 <h2>How to Play</h2>
    <ol>
        <li><strong>Start the Game:</strong> Press the "Start" button to begin the game.</li>
        <li><strong>Choose a Gesture:</strong> Use one of the five buttons to choose Rock, Paper, Scissors, Lizard, or Spock.</li>
        <li><strong>Computer Chooses:</strong> After you make your selection, the computer will randomly choose one of the five gestures, and the result will be displayed using LEDs.</li>
        <li><strong>Track the Score:</strong> The scores will update after each round and can be viewed on the LED displays.</li>
        <li><strong>End the Game:</strong> After 7 rounds, the game ends automatically, or you can end it manually by pressing the "End" button.</li>
    </ol>

<h2>Installation Instructions</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
        <pre><code>git clone [https://github.com/yourusername/rock-paper-scissors-lizard-spock.git](https://github.com/Ganathipan/GP-106-Com-Project)</code></pre></li>
        <li><strong>Upload Code to Arduino:</strong> Open the <code>.ino</code> file in Arduino IDE and upload it to your Arduino UNO board.</li>
        <li><strong>Build the Circuit:</strong> Follow the provided circuit diagram to set up the hardware.</li>
        <li><strong>Start Playing:</strong> Press the "Start" button to begin playing the game.</li>
    </ol>
