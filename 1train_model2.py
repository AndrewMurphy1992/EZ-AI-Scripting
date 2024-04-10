import numpy as np
import tensorflow as tf
from nltk.tokenize import word_tokenize
import os
import tkinter as tk
from tkinter import filedialog
from itertools import combinations
#add function for estimating beam dependability/stability/cohesion/mutability/pervasiveness
#use function to estimate relative safety of autonomy


def main():
    # Initialize Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialogue to select text file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        print("No file selected!")
        return

    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Create word to index and index to word mappings
    vocab = set(words)
    word2idx = {word: idx for idx, word in enumerate(vocab)}
    idx2word = {idx: word for word, idx in word2idx.items()}

    # Convert words to indices
    indexed_words = [word2idx[word] for word in words]

    # Generate skip-grams
    window_size = 1
    skip_grams = []
    for i, word in enumerate(indexed_words):
        for j in range(max(i - window_size, 0), min(i + window_size + 1, len(indexed_words))):
            if i != j:
                skip_grams.append((word, indexed_words[j]))

    # Define the Word2Vec model (embedding_dim is how many elements a vector has) 
    embedding_dim = 300
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=len(vocab), output_dim=embedding_dim),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(units=len(vocab), activation='softmax')
    ])

    # Compile the model with increased learning rate
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss='sparse_categorical_crossentropy')

    # Unpack skip-grams
    X, y = zip(*skip_grams)
    X = np.array(X)
    y = np.array(y)

    # Reshape input for compatibility with GlobalAveragePooling1D layer
    X = np.expand_dims(X, axis=-1)

    # Train the model
    model.fit(X, y, epochs=30, batch_size=1)

    # Get word embeddings
    embeddings = model.layers[0].get_weights()[0]

    # Write word embeddings to file
    output_file_path = "wordembeddings.txt"
    with open(output_file_path, "w", encoding="utf-8") as f:
        for word, idx in word2idx.items():
            embedding_str = " ".join(str(val) for val in embeddings[idx])
            f.write(f"{word} {embedding_str}\n")

    print(f"Word embeddings saved to {output_file_path}")

if __name__ == "__main__":
    main()

