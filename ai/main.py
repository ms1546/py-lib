from janome.tokenizer import Tokenizer as JanomeTokenizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

janome_tokenizer = JanomeTokenizer()

text_data = ["ここはAIに関する記事です。", "AIは人工知能を意味します。", "多くの分野でAIが使われています。"]

text_data_tokenized = [" ".join([token.surface for token in janome_tokenizer.tokenize(text)]) for text in text_data]

keras_tokenizer = Tokenizer()
keras_tokenizer.fit_on_texts(text_data_tokenized)
total_words = len(keras_tokenizer.word_index) + 1

input_sequences = []
for line in text_data_tokenized:
    token_list = keras_tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

X, labels = input_sequences[:,:-1], input_sequences[:,-1]
y = tensorflow.keras.utils.to_categorical(labels, num_classes=total_words)

model = Sequential([
    Embedding(total_words, 100, input_length=max_sequence_len-1),
    LSTM(150, return_sequences=True),
    LSTM(100),
    Dense(total_words, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
history = model.fit(X, y, epochs=100, verbose=1)
