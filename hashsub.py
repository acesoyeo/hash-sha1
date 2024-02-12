import subprocess

def run_hashcat(hash_file, wordlist):
    # Command to run Hashcat
    command = ["hashcat", "-m", "0", "-a", "0", hash_file, wordlist]  # Example parameters, adjust as needed

    # Run Hashcat using subprocess
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Hashcat failed with error:", e)
    except FileNotFoundError:
        print("Hashcat not found. Make sure it is installed and in the system PATH.")

if __name__ == "__main__":
    hash_file = "path/to/hash/file"
    wordlist = "path/to/wordlist/file"

    run_hashcat(hash_file, wordlist)
