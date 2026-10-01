# train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

# Load dataset
df = pd.read_csv("train.csv")

# Features and target
X = df.drop("fake", axis=1)
y = df["fake"]

# Train-test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numeric columns (optional but recommended)
X_train = X_train / X_train.max()
X_val = X_val / X_val.max()

# Build model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, validation_data=(X_val, y_val),
          epochs=50, batch_size=32,
          callbacks=[EarlyStopping(patience=5, restore_best_weights=True)])

# Save model
model.save("model.h5")
print("✅ model.h5 saved.")
