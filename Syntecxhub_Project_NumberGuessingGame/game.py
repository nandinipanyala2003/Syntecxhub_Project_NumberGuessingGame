import random
import time
import os

# Global best score
best_attempts = float('inf')
leaderboard_file = 'scores.txt'

def load_leaderboard():
    """Top 5 scores load cheyyi"""
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r') as f:
            scores = f.readlines()
        return [line.strip() for line in scores[-5:]]  # Last 5
    return []

def save_score(name, attempts, game_time):
    """Score file ki save"""
    score_line = f"{name}: {attempts} attempts, {game_time:.1f}s\n"
    with open(leaderboard_file, 'a') as f:
        f.write(score_line)

def show_leaderboard():
    """Leaderboard display"""
    scores = load_leaderboard()
    if scores:
        print("\n🏆 TOP SCORES:")
        for i, score in enumerate(scores, 1):
            print(f"{i}. {score}")
    else:
        print("\nNo scores yet!")

def play_game():
    global best_attempts
    
    print("\n🎯 === ADVANCED NUMBER GUESSING GAME ===")
    print("1. Easy (1-50, 15 tries)  2. Medium (1-100, 10 tries)  3. Hard (1-200, 7 tries)")
    
    # Difficulty with max tries
    while True:
        try:
            level = int(input("\nLevel (1/2/3): "))
            if level == 1:
                max_num, max_tries = 50, 15
                print("🥉 Easy mode!")
                break
            elif level == 2:
                max_num, max_tries = 100, 10
                print("🥈 Medium mode!")
                break
            elif level == 3:
                max_num, max_tries = 200, 7
                print("🥇 Hard mode!")
                break
            else:
                print("❌ 1-3 enter cheyyi!")
        except ValueError:
            print("❌ Number raa!")
    
    secret_num = random.randint(1, max_num)
    attempts = 0
    start_time = time.time()  # Timer start
    
    print(f"\n🎲 Secret: 1-{max_num} | Max tries: {max_tries}")
    print("Hints: Hot=close, Cold=far")
    
    # Main game loop
    while attempts < max_tries:
        try:
            guess = int(input(f"\nTry {attempts+1}/{max_tries} - Guess: "))
            attempts += 1
            diff = abs(guess - secret_num)
            
            if guess < 1 or guess > max_num:
                print("❌ Range lo!")
            elif guess == secret_num:
                game_time = time.time() - start_time
                print(f"\n🎉 WIN! Secret: {secret_num}")
                print(f"⭐ {attempts}/{max_tries} attempts | ⏱️ {game_time:.1f}s")
                
                # Best update
                if attempts < best_attempts:
                    best_attempts = attempts
                    print("🏆 PERSONAL BEST!")
                
                # Leaderboard save
                name = input("Name enter (for leaderboard): ").strip() or "Anonymous"
                save_score(name, attempts, game_time)
                show_leaderboard()
                break
                
            elif diff <= 5:
                print("🔥 HOT! Very close!")
            elif diff <= 15:
                print("🌡️ Warm!")
            elif diff <= max_num//4:
                print("❄️ Cold!")
            else:
                print("🧊 Freezing!")
                
            if guess < secret_num:
                print("📈 HIGHER")
            else:
                print("📉 LOWER")
                
        except ValueError:
            print("❌ Integer enter!")
            attempts -= 1  # Try waste kadu
    
    else:
        game_time = time.time() - start_time
        print(f"\n💥 GAME OVER! Secret was {secret_num} | ⏱️ {game_time:.1f}s")
    
    # Replay
    print("\n" + "="*50)
    while True:
        replay = input("Again? (y/n): ").lower().strip()
        if replay == 'y':
            play_game()
            return
        elif replay == 'n':
            print(f"\n👋 Bunny best: {best_attempts} attempts | Check scores.txt")
            return
        else:
            print("y/n raa!")

# Start with leaderboard
print("Syntecxhub Project 2 - Advanced Number Guessing Game")
show_leaderboard()
play_game()
