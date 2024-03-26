# Define the candidates and initialize their vote counts
candidates = {
    "Ogal": 0,
    "Steve": 0,
    "June": 0
}

def cast_vote():
    # Ask the user to cast their vote
    vote = input("Cast your vote (Alice, Bob, Charlie): ").capitalize()
    if vote in candidates:
        candidates[vote] += 1
        print(f"Thank you for voting for {vote}!")
    else:
        print("Error: Candidate not found. Please vote for a valid candidate.")

def display_results():
    print("\nVoting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

def main():
    while True:
        action = input("Do you want to vote or see results? (vote/results/exit): ").lower()
        if action == "vote":
            cast_vote()
        elif action == "results":
            display_results()
        elif action == "exit":
            print("Exiting the voting system. Final results:")
            display_results()
            break
        else:
            print("Invalid action. Please choose 'vote', 'results', or 'exit'.")

if __name__ == '__main__':
    main()