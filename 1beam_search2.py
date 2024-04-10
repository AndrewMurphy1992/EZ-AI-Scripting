import random
import tkinter as tk
from tkinter import filedialog

def read_embeddings(file_path):
    embeddings = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split()
            word = line[0]
            embedding = [float(val) for val in line[1:]]
            embeddings.append((word, embedding))
    return embeddings

def sample_words(embeddings, num_words):
    return random.choices(embeddings, k=num_words)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        embeddings = read_embeddings(file_path)
        generated_string = []
        for _ in range(46):
            sampled_words = sample_words(embeddings, 5)
            generated_string.append(" ".join(word[0] for word in sampled_words))
        print("Generated strings:")
        for idx, string in enumerate(generated_string):
            print(f"Beam {idx+1}: {string}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    select_file()

