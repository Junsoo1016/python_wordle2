from wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempts.append(x)
    
    if wordle.is_solved:
        print("You've solved the puzzle.")

if __name__ == "__main__":
    main()